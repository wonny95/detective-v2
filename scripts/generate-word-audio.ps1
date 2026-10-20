# Run with Windows PowerShell 5.1 from the project root. Requires Node and an installed English SAPI voice.
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Speech
$projectDir = Split-Path $PSScriptRoot -Parent
$entries = (& node -e @'
const fs=require('fs');
const h=fs.readFileSync(process.argv[1],'utf8');
const literal=h.match(/const WORDS = (\{[\s\S]*?\n\});/)[1];
const words=Function('return ('+literal+')')();
console.log(JSON.stringify(Object.entries(words).map(([key,value])=>({
  key, file:key.replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'')+'.wav',
  text:(value[2]||key).replace(/^sgt\./i,'Sergeant').replace(/^mrs\./i,'Missus').replace(/^mr\./i,'Mister')
}))));
'@ (Join-Path $projectDir 'index.html')) | ConvertFrom-Json
if ($LASTEXITCODE -ne 0) { throw 'Unable to read WORDS.' }
$outDir = Join-Path $projectDir 'audio/words'
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
    $synth.SetOutputToWaveFile((Join-Path $outDir $entry.file), $format)
    $synth.Speak($entry.text)
    $synth.SetOutputToNull()
  }
  Write-Output ('Generated {0} word clips with {1}.' -f $entries.Count,$voice.VoiceInfo.Name)
} finally {
  $synth.Dispose()
}
