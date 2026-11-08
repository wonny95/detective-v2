# Violin case art, cut from the Higgsfield originals (assets/characters/README.md, assets/places/README.md) with the C#
# helpers in scripts/ArtTools.cs (this computer had no Python; the steps match scripts/cut-umbrella-*.py).
#   people: the background-removed sheets (Higgsfield remove_background, kept outside the repo: -Cutouts <folder>, files
#           <sheet>-cutout.png) cut per person, trimmed with a 3% margin, 700 px tall -> assets/characters/<id>-higgsfield.png,
#           and a 160 px face icon -> assets/ui/icons-v2/<id>.png
#   places: each tall picture scaled to 1376 wide; a 1376x768 band from TOP is the place (<id>.jpg), the rest its floor
#   things: the background-removed item sheet cut per thing; the sleeves sheet's panels; Tara's photo
#   map:    the music hall from the edited map pasted onto the day map
# Run from the project folder: powershell -File scripts/cut-violin-art.ps1 -Cutouts <folder> [-Step people|places|things|map]
param([string]$Cutouts, [string]$Step = 'all')
$ErrorActionPreference = 'Stop'
Add-Type -ReferencedAssemblies System.Drawing -Path "$PSScriptRoot/ArtTools.cs"
$root = Split-Path $PSScriptRoot
$C = "$root/assets/characters"; $V = "$root/assets/places/violin"; $I = "$root/assets/ui/icons-v2"

function Sprite($sheet, $x0, $x1, $id, $face) {
  # $face: centre x, top, side as shares of the sprite's width/height (as the Python scripts' head)
  $src = [ArtTools]::Load("$Cutouts/$sheet-cutout.png")
  $half = [ArtTools]::Crop($src, [int]($src.Width * $x0), 0, [int]($src.Width * ($x1 - $x0)), $src.Height)
  $t = [ArtTools]::Trim($half, .03)
  $w = [int][Math]::Round($t.Width * 700 / $t.Height)
  $s = [ArtTools]::Resize($t, $w, 700)
  [ArtTools]::SavePng($s, "$C/$id-higgsfield.png")
  if ($face) {
    $side = [int][Math]::Round($face[2] * 700); $cx = [int][Math]::Round($face[0] * $w); $top = [int][Math]::Round($face[1] * 700)
    $fx = $cx - [int]($side / 2)
    [ArtTools]::SavePng([ArtTools]::Icon($s, $fx, $top, $side), "$I/$id.png")
    "$id ${w}x700 face:'$fx $top $side $side'"
  } else { "$id ${w}x700" }
}

if ($Step -in 'all', 'people') {
  Sprite 'tara-owen' 0 .5 'tara' @(.5, .02, .5)
  Sprite 'tara-owen' .5 1 'owen' @(.42, .0, .5)
  Sprite 'momo-pip' 0 .5 'momo' @(.5, .02, .5)
  Sprite 'momo-pip' .5 1 'pip' @(.5, .0, .62)
  Sprite 'ivo' 0 1 'ivo' @(.5, .0, .52)
  Sprite 'owen-nervous' 0 1 'owen-nervous' $null
  Sprite 'owen-sad' 0 .5 'owen-sad' $null
}

if ($Step -in 'all', 'places') {
  # the band's top in the 1376-wide picture: low enough that the clues (the lobby's bench, the stage's stool) are in it
  $BAND = @{ lobby = 200; waiting = 140; stage = 160; backstage = 250; 'backstage-open' = 250 }
  foreach ($id in $BAND.Keys) {
    $im = [ArtTools]::Resize([ArtTools]::Load("$V/$id-higgsfield-original.jpg"), 1376, 1843)
    $top = $BAND[$id]
    [ArtTools]::SaveJpg([ArtTools]::Crop($im, 0, $top, 1376, 768), "$V/$id.jpg", 88)
    $fh = 1843 - $top - 768
    if ($id -ne 'backstage-open') { [ArtTools]::SaveJpg([ArtTools]::Crop($im, 0, $top + 768, 1376, $fh), "$V/$id-floor.jpg", 85) }
    "$id floor h $fh"; $im.Dispose(); [GC]::Collect()
  }
}

if ($Step -in 'all', 'things') {
  # the item sheet (2752 wide): closed case, open case, button, cutters, side by side
  $sheet = [ArtTools]::Load("$Cutouts/items-cutout.png")
  foreach ($t in @(@('case-closed', 150, 684, 640), @('case-open', 790, 1581, 640), @('gold-button', 1624, 2051, 240), @('cutters', 2115, 2607, 460))) {
    $cut = [ArtTools]::Trim([ArtTools]::Crop($sheet, $t[1], 0, $t[2] - $t[1], $sheet.Height), .03)
    $h = $t[3]; $w = [int][Math]::Round($cut.Width * $h / $cut.Height)
    [ArtTools]::SavePng([ArtTools]::Resize($cut, $w, $h), "$V/$($t[0]).png"); "$($t[0]) ${w}x$h"
  }
  # the sleeves sheet's panels (inside their pencil frames), 4:3-ish photos of each pair of cuffs
  $sl = [ArtTools]::Load("$V/sleeves-sheet-original.jpg")
  foreach ($p in @(@('sleeves-owen', 100, 90), @('sleeves-ivo', 1446, 90), @('sleeves-momo', 100, 820))) {
    [ArtTools]::SaveJpg([ArtTools]::Resize([ArtTools]::Crop($sl, $p[1], $p[2], 1208, 626), 1024, 531), "$V/$($p[0]).jpg", 88); "$($p[0]) 1024x531"
  }
  [ArtTools]::SaveJpg([ArtTools]::Resize([ArtTools]::Load("$V/tara-photo-higgsfield-original.jpg"), 1024, 765), "$V/tara-photo.jpg", 88); 'tara-photo 1024x765'
}

if ($Step -in 'all', 'map') {
  # the day map read through Windows' WebP decoder (WPF), the music hall's part of the edit pasted on it
  Add-Type -AssemblyName PresentationCore
  $fs = [IO.File]::OpenRead("$root/assets/places/village-map-day-higgsfield.webp")
  $dec = [System.Windows.Media.Imaging.BitmapDecoder]::Create($fs, 'PreservePixelFormat', 'OnLoad'); $fs.Close()
  $tmp = [IO.Path]::GetTempFileName() + '.png'
  $enc = New-Object System.Windows.Media.Imaging.PngBitmapEncoder; $enc.Frames.Add($dec.Frames[0])
  $o = [IO.File]::Create($tmp); $enc.Save($o); $o.Close()
  $map = [ArtTools]::Load($tmp); Remove-Item $tmp
  $edit = [ArtTools]::Load("$root/assets/places/map-violin-higgsfield-original.jpg")
  [ArtTools]::PasteFeathered($map, [ArtTools]::Crop($edit, 540, 410, 228, 200), 540, 410, 10)
  [ArtTools]::SaveJpg($map, "$root/assets/places/village-map-day.jpg", 90); 'village-map-day 768x1376'
}
