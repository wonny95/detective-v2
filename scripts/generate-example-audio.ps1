# Run with Windows PowerShell 5.1 from the project root. Requires Node and an installed English SAPI voice.
# -Missing: only the files not made yet (another computer's voice may differ; existing clips stay as they are)
param([switch]$Missing)
# 이번 사건의 열쇠: each form (GRAMMAR[].examples[].head) -> audio/examples/<grammar>-<page>.wav,
# its example sentences (.lines) -> audio/examples/<grammar>-<page>-<line>.wav
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Speech
$projectDir = Split-Path $PSScriptRoot -Parent
$entries = (& node -e @'
const fs=require('fs');
const h=fs.readFileSync(process.argv[1],'utf8');
const literal=h.match(/const GRAMMAR = (\{[\s\S]*?\n\});/)[1];
const grammar=Function('return ('+literal+')')();
// the form itself (<grammar>-<page>.wav; the A and B of a pattern read as letters), then its example lines
console.log(JSON.stringify(Object.entries(grammar).flatMap(([g,v])=>(v.examples||[]).flatMap((ex,p)=>[
  { file:`${g}-${p+1}.wav`, text:ex.head.replace(/\bA\b/g,'ay').replace(/\bB\b/g,'bee').replace(/\s*[\/\u2192]\s*/g,', ') },
  ...ex.lines.map(([en],i)=>({ file:`${g}-${p+1}-${i+1}.wav`, text:en.replace(/[{}]/g,'') }))
]))));
'@ (Join-Path $projectDir 'index.html')) | ConvertFrom-Json
if ($LASTEXITCODE -ne 0) { throw 'Unable to read GRAMMAR.' }
$outDir = Join-Path $projectDir 'audio/examples'
New-Item -ItemType Directory -Path $outDir -Force | Out-Null
$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
try {
  $voice = $synth.GetInstalledVoices() | Where-Object { $_.Enabled -and $_.VoiceInfo.Culture.Name -eq 'en-US' } | Select-Object -First 1
  if (!$voice) { throw 'An enabled en-US SAPI voice is required.' }
  $synth.SelectVoice($voice.VoiceInfo.Name)
  $synth.Rate = -1
  $synth.Volume = 85
  $format = New-Object System.Speech.AudioFormat.SpeechAudioFormatInfo(22050, [System.Speech.AudioFormat.AudioBitsPerSample]::Sixteen, [System.Speech.AudioFormat.AudioChannel]::Mono)
  foreach ($entry in $entries) {
    if ($Missing -and (Test-Path (Join-Path $outDir $entry.file))) { continue }
    $synth.SetOutputToWaveFile((Join-Path $outDir $entry.file), $format)
    $synth.Speak($entry.text)
    $synth.SetOutputToNull()
  }
  Write-Output ('Generated {0} example clips with {1}.' -f $entries.Count,$voice.VoiceInfo.Name)
} finally {
  $synth.Dispose()
}
