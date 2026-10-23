# UI 그림

## 적용 중

### 수사완료 도장

- `investigation-complete-stamp.png` (1774×887, 투명 PNG): Codex가 기본 내장 `image_gen`으로 생성. Higgsfield·CLI 미사용. 프롬프트만으로 제작한 적갈색 잉크 자국이며 글자는 `수사완료` 네 글자. 원본 `exec-be163cb2-3e7e-4028-82d1-d600c6210822.png`를 가공 없이 복사해 알파 유지(바깥·글자 사이 투명 확인).
- 엔딩의 `.cc-stamp` 이미지로 표시. 사건명 아래 여백을 확보하고, 회전(-10도)·축소하며 찍히는 동작은 CSS로 처리한다. 원본은 수평이라 다른 크기·각도로 재사용 가능. 시작 시 미리 불러오며 대체 텍스트는 `수사완료`.

최종 프롬프트 (`transparent_background:true`):

```text
Use case: illustration-story
Asset type: a transparent PNG rubber-stamp imprint for the completion of a cozy woodland detective game.
Create one horizontal rounded rectangular double-outline stamp containing ONLY the exact Korean text "수사완료". Four syllables, left to right: 수 사 완 료. Bold, rounded, friendly hand-lettered Hangul, large and perfectly readable on a small mobile screen.
Warm gouache and colored-pencil sensibility with subtly irregular hand-drawn contours, consistent with a cream-paper illustrated storybook game. Single red-brown ink color #B8433F. Light ink bleed and scattered tiny worn gaps in the ink, but keep the characters and double outline strong and legible. Restrained vintage rubber-stamp texture.
Front-on, perfectly horizontal, no rotation, perspective, lighting, shadows, embossing, or 3D. Landscape 2:1 canvas; stamp occupies about 90% of width and 75% of height, with transparent safety margins on every side. The interior between text and outline is also transparent.
Actual transparent alpha background. ONLY the ink imprint. No paper sheet, white background, checkerboard pattern, stamp handle, icons, characters, stars, additional text or watermark. Ready-to-use game UI asset.
```

### 말풍선

- `speech-paper-frame.png` (1536×1024, 투명 바깥): 힌트·엔딩 공용 말풍선 본문. **Codex가 기본 내장 `image_gen` 도구로 생성**, Higgsfield·CLI 미사용. 기존 `buttons/cream-flat.png`는 재질 참조, `places/library-higgsfield-v2.png`는 화풍 참조로 사용했다. 따뜻한 아이보리 종이, 갈색 색연필선과 가는 황토색 안쪽 선, 장식 없는 읽기 영역이다. 생성 출력 `exec-19bb79b2-db66-495c-ad43-11e798066f23.png`를 알파 채널 그대로 복사했다(원본 보관 `speech-paper-frame-original.png`, 1536×1024).
  - 2026-10-22 Claude 다시 자름(사용자 제보: 말풍선이 크기에 따라 일그러짐): 원본은 위 52·아래 64·좌우 14px가 투명 여백이고 모서리 곡선이 가로 약 170·세로 약 125px인데, 9조각을 사방 100px로 잘라 모서리 곡선이 변 조각에 걸려 함께 늘어났다. 종이 외곽 (14,52)–(1522,960)으로 잘라 1508×908로 만들고, CSS 조각을 위·아래 150 · 좌우 190px(모서리를 다 담음), 화면 두께 33px·42px(예전과 같은 0.22배), `inset:0`으로 바꿨다(`.bubble::before`, `.office-say::before`·`.oh-say::before`).
  - 같은 날 꼬리 위치도 맞춤(사용자 요청): 종이가 상자 바닥까지 내려와 꼬리가 7px쯤 안으로 올라가 있었다. 꼬리 그림의 열린 윗변(48×30 상자에서 위 3.6px)이 말풍선 아래 테두리(마지막 약 5px)를 덮도록 `bottom:-21px`로 내렸다(설계 시안은 44×28이라 `-19px`).
  - `.bubble::before`의 `border-image`로 **9조각 확장**한다. slice `100`, 표시 테두리 `22px`, 원본 투명 여백을 고려해 `inset:-8px -3px`. 모서리와 선 두께를 유지하고 가운데만 늘린다. 본문 폭은 `min(88%,380px)`이며 화면 높이에 따라 내용만 스크롤한다.
  - 이미지의 반투명한 안쪽 조각 경계에 얇은 선이 드러나지 않도록 `background-clip:padding-box`인 불투명 종이색 바탕을 함께 쓴다(`--bubble-paper`, 기본 `#FFF8E9`). 바깥 투명 모서리는 채우지 않는다. 말풍선 안의 영어·한국어·버튼 영역에는 구분선을 넣지 않고 여백만 둔다.
- `speech-paper-tail-pencil.png` (1585×992, 투명): **현재 적용**. Codex가 내장 `image_gen`으로 편집. 원본 `exec-fe952193-7816-4263-b158-60420c65dc26.png`를 가공 없이 복사해 알파 유지. 직선 삼각형, 거친 갈색 연필 외곽·황토색 안쪽 선, 열린 윗변. 불투명 V 끝 아래 약 80px 여백이 있어 끝이 잘리지 않는다. `.bubble::after`의 48×30px 상자에서 `contain`, `bottom:-14px`로 배치한다. 본체는 그대로 9조각 확장, 꼬리 크기는 고정이다. 원본 색상 구간을 기준으로 축소 후 갈색 선 약 2.5–2.7px(본문 약 2.2px)로 확인했다. Higgsfield·CLI 미사용.
- `speech-paper-tail-flat.png` (1774×887, 투명): 미사용 이전 직선 꼬리 보관. 생성 출력 `exec-2ab58def-170a-4c49-a180-d8841a44b768.png`.
- `speech-paper-tail.png` (1792×896, 투명): 미사용 곡선 꼬리 보관. 생성 출력 `exec-9e79024f-9613-455f-b0d6-e19a5b57a5f6.png`.
  - 두 이미지 모두 글자·캐릭터·조작 요소가 없는 배경 부품이다. 이름·영어·한국어·버튼은 HTML이므로 콘텐츠를 추가하거나 문장이 길어져도 이미지를 다시 만들 필요가 없다.

### 말풍선 생성 프롬프트

본문(참조 순서: 기존 크림 버튼, 도서관 배경; `transparent_background:true`):

```text
Use case: illustration-story. Create ONE production-ready raster UI asset: an empty expandable speech-panel body for a cozy woodland detective listening game. Reference image 1 is the existing cream paper button material and brown outline. Reference image 2 is STYLE REFERENCE ONLY: warm colored pencil, gouache, subtle paper grain, slightly imperfect ink contours. Draw a single large warm ivory paper speech panel, viewed perfectly flat front-on, landscape 3:2 composition, nearly filling the canvas with only 8px transparent safety margin. Rounded softly irregular rectangle, slightly wavering dark warm brown pencil outline, a fine golden ochre inner rim and gentle warm paper grain. Rounded corners are modest, NOT pill-shaped. Mostly plain very light cream center (#FFF8E9) to read black text over it. Restrained handmade tactile appearance, neither glossy nor photoreal. Outline thin but clear, approximately 7 pixels on a 1024px wide asset. Very subtle shading near edge ONLY, no directional cast shadow. No speech tail on this body asset: the tail is a separate component to be positioned by code. The straight middle parts of all four edges must stay straight enough to stretch, with corner details confined to the outer 80px; this is a nine-slice UI frame. Fully opaque interior, truly transparent outside panel. Absolutely no text, no letters, no buttons, no icons, no ornaments, no scene, no characters, no watermark. Return the asset alone, never a mockup or sheet.
```

꼬리(참조: 생성된 본문; `transparent_background:true`):

```text
Use case: illustration-story. Generate ONE standalone UI speech-bubble TAIL asset that matches the attached cream paper frame exactly. The attachment is only a material/style reference; do NOT reproduce its rectangular frame. This output is only a single small downward-pointing speech tail, isolated on true transparent alpha. Front-on flat view. Shape is a broad gently curving downward triangular paper tongue, slightly leaning to the right, width about twice its height. The upper edge is a straight horizontal OPEN CONNECTION to the speech panel: there must be NO brown outline, NO gold outline and NO shadow across that top edge; just solid warm ivory #FFF8E9 paper all the way to its flat top. The left and right slanted edges and bottom tip have the same dark warm brown colored-pencil contour and fine golden ochre rim as the reference. Cream interior with barely perceptible paper grain, NO gradients to dark brown, no thick shadow. Tail fills almost the whole canvas, with only 8px transparent safety padding; landscape 2:1 canvas. Make it broad enough to read as a speech tail rather than a long spike. No rectangle body, no sheet, no labels, no text, no decorations, no characters, no mockup, no background.
```

### 플랫 삼각형 꼬리 프롬프트

기본 형태 편집(참조: 보관 곡선 꼬리, 본체; `transparent_background:true`):

```text
Use case: precise-object-edit
Asset type: transparent PNG speech bubble tail, replacement for a woodland detective game's illustrated paper dialog.
Image 1 is the existing tail to replace. Image 2 is ONLY the color, paper grain, brown pencil outline and gold inner rim reference.
User specifically requests a FLAT TRIANGLE: a simple downward-pointing isosceles triangle with perfectly straight left and right diagonal sides meeting at a sharp point. Absolutely NO curved sides, rounded shoulders, rounded tip, bulge, swoosh or droplet. Flat 2D shape, no bevel or shadow.
Opaque pale warm ivory #FFF8E9 interior with very faint paper grain matching the reference body. Thin warm dark brown colored-pencil outer outline and restrained ochre inner rim ONLY along the TWO diagonal sides and bottom point. Top horizontal base must be OPEN, with no visible outline or colored rim across it, so it seamlessly overlaps the body. At mobile display size 40px wide, brown outline should read about 1.2px thick and gold about .8px. Keep the outline geometrically straight while its material has fine colored-pencil grain.
One standalone triangle only on a landscape 2:1 canvas. Top base nearly fills canvas width, begins at 2% canvas height; sharp bottom point at 97% height. Minimal transparent safety padding around silhouette. Preserve true transparent alpha outside triangle, no white halo or stray detached pixels. No bubble rectangle, sheet, text, icons, buttons, background, checkerboard, drop shadow or additional shapes.
```

최종 굵기 편집(참조: 삼각형 꼬리 시안 `exec-f4c5b3fb-e6fa-4e13-b385-b3a5874589b8.png`; `transparent_background:true`):

```text
Precise image edit of the attached flat triangular speech tail.
The ONLY requested change is to TRIPLE the thickness of BOTH colored outline bands. Keep the same straight-sided triangle, sharp point, cream paper color, open top base and transparent background.
IMPORTANT: the current image has only about 43 pixels of brown and 44 pixels of gold along a horizontal scanline through a diagonal side. The result MUST instead have about 130 pixels of BROWN followed by about 125 pixels of GOLD at each side on that horizontal scanline. This means about 90 pixels thickness perpendicular to each diagonal for each color. Make the outline three times bolder than the attached image. NOT a subtle adjustment.
The combined brown and gold contour should take up roughly 30% of the triangle's vertical height at its bottom point, with a much smaller inset cream triangle remaining inside. It may look unusually thick at this large asset scale; that is intentional, since it is displayed at only 40px wide in the UI. Final rendered band widths should each be about 2px, a visible 4px total double border.
Warm dark brown outer band, golden ochre inner band, both strong opaque textured colored pencil. Straight geometry, flat 2D, no rounded edges, shadows, bevel or glossy effects. Do NOT put any horizontal colored line across the open upper base. Triangle nearly fills a landscape 2:1 canvas. Preserve genuine transparent alpha outside the triangle and opaque pale ivory paper inside, with no extra objects, specks, text or background.
```

### 수첩·공용 부품

- `casefile-panel.webp` (728×2206): 노트 패널 배경(2026-10-19 교체). 남색 서류철 위에 크림색 서류 한 장, 오른쪽 위 클립. **사용자가 직접 누끼 딴 그림** `casefile-cutout-original.png`(762×1071)의 빈 여백을 잘라 내고(18,7–746,1071), 아래 y 560–1064 구간을 위아래로 뒤집어 가며 이어 붙여 예전 그림과 같은 세로 비율(가로의 3.03배)로 늘렸다. 서류 위치·머리줄(가로의 21.7%)이 예전 그림과 같아 CSS 수치는 그대로다. 예전 원본·누끼는 `casefile-higgsfield-original.png`, `casefile-nobg.png`.
  - 2026-10-23 클립 지움(사용자 요청: 노트 오른쪽 위 UI를 가림): 클립 자리(x 570–640, y 0–135)를 같은 줄의 75px 왼쪽(파란 테두리·종이)으로 덮고 가장자리를 3px 흐리게 섞었다(Pillow). 클립이 있던 그림은 `casefile-panel-with-clip.webp`.
  - 남색은 나무 바닥·타일·풀밭 같은 따뜻한 배경과 대비되도록 고른 색이다.
  - CSS는 그림 폭 기준 %로 맞춘다: 서류 윗변 7.9%, 머리 띠 높이 13.6%, 서류 폭 6.5%–93.8%. 클립(약 81–86%)을 피해 탭은 오른쪽 22%까지만 놓는다.
- 아래 `notebook-panel.webp`(스프링 수첩)는 사용자 피드백으로 교체되어 미사용이다.

- `notebook-panel.webp` (640×1731): 노트 패널 배경. `notebook-v2-higgsfield-original.png`의 배경을 Higgsfield `remove_background`로 지운 뒤(`notebook-v2-nobg.png`) 수첩만 잘라, 스프링 4칸 구간(원본 y 380–680)을 6번 이어 붙여 길게 만들었다. 패널 폭에 맞춰 위에서부터 그리며 아래는 화면 밖으로 잘린다.
  - CSS는 그림 폭 기준 %로 맞춘다: 종이 윗변 4.7%, 머리 띠 높이 12%(제목과 `기록 완료`), 스프링 영역 ~12.4%, 오른쪽 표지 ~9%.
- `tab-1.png` … `tab-6.png` (160×146): 인덱스 탭. 흰 종이 탭 6개를 한 장(`tabs-higgsfield-original.png`)에 그려 크레딧을 아끼고, 칸별로 잘라 아래 외곽선을 지우고 바깥을 투명하게 만들었다.
- `tab-1-closed.png` … `tab-3-closed.png` (160×146): 노트 탭(폴더 앞에 붙인 견출지). `tab-1…3.png`의 위쪽 42%를 위아래로 뒤집어 아래에 붙여 테두리를 닫았다(PIL, 크레딧 없음).
  - 탭은 서류철 그림(`.dock::before`) 뒤(`z-index:-1`)에 놓여 윗변 너머로 머리만 나온다. 아래 14px은 서류철에 가려지고, 선택된 탭은 더 높이 나온다.
  - 탭 버튼은 이 PNG로 마스크하고 `--tab-bg` 색 위에 곱하기로 겹쳐 색을 입힌다. 선택된 탭은 꿀색(`--honey`)이며 조금 더 높다. 순서대로 1–6번 모양을 돌려 쓴다.

- `corkboard-cork.webp` (512×512, 화면에서 320px 타일): 사건 수첩 코르크판 바탕. Higgsfield Nano Banana 2.1(1K, thinking high), 카페 배경 그림(job `354bb7cb-…`)을 화풍 참조로 한 손그림 코르크 2장 중 고른 것(job `b4aa7ed9-993b-4f17-8c5e-e42688cb7edf`, 원본 `corkboard-cork-higgsfield-original.png`). 반 칸 밀어 낸 사본과 가장자리만 섞어 이음매 없는 타일로 만들었다. 처음 뽑은 사진 같은 코르크(job `96438498-…`)는 사용자가 "너무 리얼하다"고 해 버렸다.
- `corkboard-frame.webp` (804×1093, 투명): 코르크판 나무 액자. 같은 모델, 카페 배경 그림(job `354bb7cb-…`) 화풍 참조로 손그림 나무 액자 2장 중 고른 것(job `60b9f138-bafa-4736-9dd5-53bca97a5ecd`, 원본 `corkboard-frame-higgsfield-original.png`). 마젠타 배경을 로컬에서 지우고 잘랐다. 나무 두께 네 변 약 86px → CSS `border-image` 조각 `86`, 화면 두께 18px, `stretch`. 액자 안쪽 가장자리는 반투명이라 코르크를 액자 밑까지 깐다(`background-clip:border-box`, 바깥 둥근 모서리는 `border-radius:9px`로 자름) — 안 그러면 뒤 종이색이 얇은 흰 선으로 비친다. 처음 액자(job `75a1eb0e-…`, 오리 그림 참조)는 일러스트 느낌이 약하다는 피드백으로 바꿨다.

- `tack-red.webp`, `tack-grey.webp` (116×160): 코르크판 압정. 한 장(`tacks-higgsfield-original.png`, job `4c2a85c0-84ff-490d-a1c2-f1a064906458`)에 빨강·회색을 그려 마젠타를 지우고 반씩 잘랐다. 바늘 끝은 그림 가로 36.3%, 맨 아래 → SVG에서 24×33px로, 그 점이 압정 자리에 오게 놓는다.
- `polaroid-card.webp` (414×528): 사진 카드(사진 칸 없는 빈 폴라로이드 종이). job `68f66e93-f8c8-49b2-9a6e-d0eb3a8a0694`, 원본 `polaroid-card-higgsfield-original.png`. `.polaroid` 배경으로 100%×100% 늘린다(사진 카드 비율이 0.7–0.8로 비슷해 9조각 없이 씀).
- 셋 다 Nano Banana 2.1(1K, thinking high), 카페 배경 그림(job `354bb7cb-…`) 화풍 참조, 마젠타 배경을 로컬에서 지움.

## 제작

- Nano Banana 2.1, 1K, thinking high, 오소리 경사 그림을 화풍 참조(`image_references`)로 사용. 수첩 4:5, 탭 시트 3:2.
- `notebook-higgsfield-original.png`: 1차 시안(참조 없음, 줄 있음). 매끈해서 미사용.

## 버튼·아이콘 (2026-10-19)

- `icons-higgsfield-original.png` (1200×896, job `4104e401-…`): 아이콘 12개 시트. 잘라 낸 투명 PNG는 `icons/`에 있다: map, note, camera, folder, acorn, play, turtle, lock, close, check, magnifier, speaker.
- `buttons-higgsfield-original.png` (1264×848, job `3599eae3-…`): 빈 버튼 시트. 잘라 낸 PNG는 `buttons/`에 있다: 알약 버튼 sage·berry·honey·cream·sky·peach(각각 보통·`-pressed`), 둥근 버튼 `round-cream`·`round-honey`·`round-sage`·`round-berry`.
  - 문제: 보통 상태 알약 6개는 오른쪽 위 모서리가 각지게 나왔다. 눌린 상태(`-pressed`)는 온전한 알약 모양이다.
- 제작: Nano Banana 2.1, 1K, thinking high, 오소리 경사 그림을 화풍 참조로 사용. 배경은 마젠타(#FF00FF) 단색으로 지정해 로컬에서 지웠다(마젠타 정도로 알파를 매기고 가장자리 색에서 마젠타를 빼냄). 색은 게임 CSS 토큰(--moss, --berry, --honey, --paper, --sky, --peach)에 맞췄다.
- 적용:
  - 아이콘: 한 번 적용했다가 사용자 판단("안 어울린다")으로 되돌렸다. 게임은 원래의 SVG 선 아이콘을 쓴다. `icons/` 파일은 남겨 두었다.
  - 버튼: `.pill`과 `.tab`에 `border-image`로 `*-flat.png`를 입힌다(조각 `60 62 62 62`, 둥근 끝은 늘이지 않음, 크기 `--bw`). `*-flat.png`는 보통 상태 그림의 왼쪽 절반을 좌우로 뒤집어 붙여 만든 평평한 알약이다(각진 오른쪽 위 모서리를 없앰, 279×125 안팎). 입체감 있는 `-pressed`는 사용자가 별로라고 해 쓰지 않는다. 색: 기본 cream, `.big` berry, `.green`·`기록 완료` sage, 힌트·열린 Note honey, 켜진 토글 sky. peach와 둥근 버튼은 미사용.

## 손그림 아이콘 v2 (2026-10-20)

- `icons-v2-higgsfield-original.png` (1024×1024, job `782fc121-af0e-4cb5-ae70-245350d74452`): 3×3 시트 — 돋보기, 카메라, 도토리 / 오소리 경사, 두더지 부인, 여우 피오나 / 너구리 레이, 토끼 로지, 오리 아저씨.
- 사용자 요청: 이전 아이콘(위 `icons/`)은 외곽선이 얇아 잘 안 보였다 → 굵은 갈색 외곽선(1024px 기준 약 14px), 노트(서류철)와 어울리는 색연필 화풍.
- 제작: Nano Banana 2.1, 1K, thinking high, 1.5크레딧. 참조: `notebook-v2-nobg.png`(화풍) + 여섯 인물 `characters/<id>-higgsfield.png`(생김새). 마젠타 배경.
- 자르기: 마젠타 정도로 알파를 매기고 가장자리 색에서 마젠타를 빼낸 뒤, 칸이 아니라 이어진 덩어리(8방향)별로 잘라 정사각형 여백 4px를 두고 160×160으로 줄였다 → `icons-v2/<이름>.png`. 토끼 귀가 윗줄 칸까지 올라가 있어 칸 자르기는 쓰지 않는다.
- 적용: 증거 탭 카메라(`cameraIcon`, 30px), 힌트 도토리(`acorns()`, 17px), 작은 얼굴 전부(`miniSVG()`의 `FACE_ICONS`; 둥근 `.mini` 틀 안에서는 아래로 8% 내리고 1.06배).

## COMPLETE 도장·별 (2026-10-20)

- `complete-stamp.png` (900×332, 투명): 사용자 요청으로 `수사완료` 한글 도장을 영문 `COMPLETE` 도장으로 교체. Nano Banana 2.1(1K, thinking high, 16:9), 참조: 기존 `investigation-complete-stamp.png`(모양) + `notebook-v2-nobg.png`(화풍). job `f656df82-84d3-447a-a9f1-29b1bfe258de`, 원본 `complete-stamp-higgsfield-original.png`. 마젠타 배경을 지우고(테두리 중앙값을 배경색으로 잡아 알파·색 분리) 잉크 영역으로 잘라 가로 900px로 줄였다. 엔딩 도장 카드(`.cc-stamp`)와 복습 1단계 서류(`.rv-file img`)에 쓴다. 이전 `investigation-complete-stamp.png`는 미사용 보관.
- `star.png`, `star-empty.png` (160×155, 투명): 얻은 별 / 못 얻은 별. 같은 모델, 참조: 아이콘 v2 시트(job `782fc121-…`) + 노트 화풍. job `1d60cfdf-9737-437c-ac15-91b7f5f8aad5`, 원본 `stars-higgsfield-original.png`(왼쪽 금색, 오른쪽 베이지). 반씩 잘라 마젠타를 지웠다. 사건 목록 사진 카드(`.case-stars img`, 16px)와 복습 1단계(`.rv-stars img`, 50px)에 쓴다.
- 두 장 합계 3크레딧.

## 닫기 버튼 (2026-10-20)

- `close-button.png` (128×128, 투명): 지도·증거 서랍·문법 노트·홈에서 연 복습 창·범인 선택 창의 공용 닫기. 사용자 요청으로 Higgsfield 제작. Nano Banana 2.1(1K, thinking high, 1:1, 1.5크레딧), 참조: 아이콘 v2 시트(job `782fc121-…`) + 노트 화풍. job `4cb64d76-b816-4afd-8f7b-0b75a0e89e8d`, 원본 `close-button-higgsfield-original.png`. 둥근 크림 종이 + 굵은 갈색 테두리 + 갈색 X. 마젠타를 지우고 잘랐다. `.close-button` 배경(42px), 갈색 그림자·누를 때 1px 이동 공용. 문법 노트는 오른쪽 위에 배치하며 모두 화면별 접근성 이름을 둔다. 재사용 확장에는 추가 생성·크레딧 없음.

## 보관된 심문 게이지 (미사용)

- `gauge-empty.png`, `gauge-full.png` (각 651×185, 투명): 사용자 요청으로 돋보기와 막대를 한 덩어리로 그린 손그림 게이지. Nano Banana 2.1(1K, thinking high, 16:9, 1.5크레딧), 참조: 첫 게이지 시안(job `cea84c82-…`) + 아이콘 v2 시트. job `d3e797e1-afa4-424a-8ee2-4b5fcc0b30a6`, 원본 `gauge-magnifier-higgsfield-original.png`(위 빈 게이지, 아래 꿀색 꽉 찬 게이지). 위 게이지의 손잡이가 아래 게이지와 몇 줄 겹쳐 이어진 덩어리별로 나눠 마젠타를 지웠다. 아래 그림이 11px 높게 그려져 막대 위치에 맞춰 내린 뒤 같은 캔버스(1302×370)에서 반으로 줄였다.
- 첫 시안(돋보기 없는 막대만, job `cea84c82-…`, 원본 `gauge-higgsfield-original.png`)은 돋보기와 따로 논다는 피드백으로 교체.

## 튜토리얼 그림

- `index.html`의 `TUT` 6장에 쓰는 인라인 SVG 조합. Codex가 현재 플레이 방식에 맞춰 구성했다. 새 비트맵 생성·기존 이미지 가공·추가 크레딧 사용 없음.
- 공용 `buttons/*-flat.png`, `casefile-panel.webp`, `icons-v2/camera.png`·`acorn.png`, `magnifier-paper.png`와 기존 인물·장소 그림을 그대로 참조한다. 심문 게이지는 크림/갈색 종이 외곽과 꿀색 채움으로 그린다. 노트의 네 버튼 배치, 단어 터치 후 빈칸으로 이동, 증거 획득 장소·듣기·해석, 파출소 심문을 안내한다.
- 정답·범인·핵심 증거를 보여 주지 않는다. 빈칸 예문은 사건과 무관한 문장이며 증거 사진은 카메라 아이콘으로 대신한다. 원본 이미지의 출처는 각 그림 항목을 따른다.

### 연필선 삼각형 꼬리 편집 프롬프트

내장 `image_gen`, `transparent_background:true`. 1차 편집은 이전 직선 꼬리 + 본체를 참조해 끝 아래 투명 여백과 온전한 V 끝을 생성했다(`exec-e51ecd10-8f3f-4313-bae5-d83a2d072c99.png`). 최종 편집의 참조 순서는 1차 꼬리(수정 대상), 본체(재질 참조)다.

```text
EDIT IMAGE 1 ONLY. Keep its complete triangular V point, exact overall triangle dimensions and open unoutlined top edge, transparent canvas and generous transparent safety space beneath its pointed tip. Image 2 is only the material reference. The most important change is dramatic THICKENING of the DARK BROWN OUTER CONTOUR on both diagonal sides: make the dark brown band THREE TIMES its existing normal perpendicular thickness, roughly 110-130 pixels thick at the source image's current width around 1600 pixels. It will be displayed only 44px wide, so without this extreme source thickness it becomes a thin hairline. This is a deliberately very bold chunky hand-drawn dark brown pencil/crayon V stroke, NOT a slender elegant outline. Grow the dark stroke inward into the cream area, so the exterior triangle size and the fully intact pointed tip do not change. Also thicken the muted golden ochre inner rim to 1.5 times its current width but keep dark brown dominant, not orange. Make the outline visibly imperfect and coarse: broad pencil marks, irregular pressure, small wavers around the straight underlying triangular geometry, slightly rough ragged pencil edges; NOT parallel ruler-cut vector bands. Cream interior remains warm pale #FFF8E9. No horizontal line at top. No curve in overall triangular silhouette, no round droplet, no flat cutoff at the V tip. Keep at least 100 pixels of transparent margin below the V point, no cropping. Do not add any object, any rectangle, any whole speech bubble, text, icon or cast shadow. One isolated transparent TAIL asset. The large brown band is essential; change it substantially, not subtly.
```

## 종이 심문 게이지

- 사용자 요청으로 같은 페이지의 종이 버튼·말풍선과 맞춘 디자인. 외곽은 CSS 2px 갈색 선·비대칭 둥근 모서리, 바탕과 진행 채움은 기존 `buttons/cream-flat.png`·`honey-flat.png`의 가운데 질감을 확대해 쓴다. 높이 36px로 뒤로 버튼과 맞추고, 내부 16px 채널의 꿀색만 진행률에 따라 표시한다. 숫자·칸 구분·바깥 그림자는 없다.
- `magnifier-paper.png` (1254×1254, 투명): Codex가 내장 `image_gen`으로 제작. 출력 `exec-dd3a8872-2ceb-4d40-9677-55cf2c687ab2.png`를 가공 없이 복사해 알파 유지. 크림 종이 렌즈·차분한 손잡이·갈색 연필선, 무광. 실제 표시 상자는 34px. Higgsfield·CLI 미사용, 추가 Higgsfield 크레딧 없음. 참조: `close-button.png`(갈색 손그림 선), `speech-paper-frame.png`(종이 재질).
- UI 구조는 `.gauge-track` → 아이콘 + `.gauge-meter` → `.gauge-fill`이고, 종이 외곽·아이콘은 고정한 채 채움만 clip-path로 표시한다. 튜토리얼 마지막 그림도 같은 아이콘/색으로 구성한다.

생성 프롬프트(`transparent_background:true`):

```text
Use case: illustration-story. Asset: ONE small magnifying-glass UI ICON on true transparent alpha for the progress gauge of a cozy paper storybook detective game. Images 1 and 2 are STYLE references only (dark brown hand-drawn X on cream paper and the speech paper frame). Do not reproduce their circular button or rectangular panel. Draw a simple magnifying glass, round lens at upper left, short diagonal handle to lower right, front-on flat paper-cut illustration. Warm DARK BROWN #4A3628 broad rough colored-pencil contours with slight pressure variation and paper grain, clear at just 26px displayed size. Source contour should be approximately 70-90px wide in a 1024px image so it remains around 2px at final small size. Lens is matte IVORY #FBF4E6 paper, not blue glass, no glass shine, no white reflection dots. Handle is a flat muted tan/cream with brown sketch contours, NOT glossy wood. Very simple restrained two-tone cream and brown appearance, matching the existing hand-drawn close/back paper buttons. NO gold metallic rim, NO blue, NO highlights, NO bevel, NO gradients, NO cast shadow, NO circular badge background, NO extra ring framing the entire icon, NO text, NO other objects. Keep lens and handle complete with at least 8 percent truly transparent margin on all sides, use about 80 percent of the square canvas for the icon. Coarse pencil edge irregularity should survive reduction; underlying circular lens geometry remains easy to recognize. Output this single isolated icon only, not a whole gauge, not a mockup, not a sprite sheet.
```

## 탐정 신분증·얼굴 (Claude 제작, 2026-10-22, 게임에는 아직 미적용)

- `detective-id-card.png` (1143×747, 투명): 탐정 이름 짓기 화면의 빈 신분증(왼쪽 위 도토리, 왼쪽 사진 칸, 오른쪽 빈 줄 세 개, 오른쪽 아래 도장 동그라미). Nano Banana 2.1(1K, thinking high, 3:2, 1.5크레딧), 화풍 참조 아이콘 v2 시트(job `782fc121-…`). job `ff14130a-afef-447c-bded-ba767b186f49`, 원본 `detective-id-card-higgsfield-original.png`. 마젠타를 로컬에서 지우고(가장자리 색 분리) 잘랐다.
  - 칸 위치(그림 대비 %): 사진 칸 left 11.3 · top 24.9 · w 29.6 · h 50.6 / 줄 x 47.5–90, 바닥선 y 37.1·49.8·62.5 / 도장 동그라미 중심 (85.1, 77.5), 지름 w 12.6.
- `icons-v2/detective.png` (160×160): 탐정 얼굴 아이콘. `characters/detective-higgsfield.png`에서 (95,15)–(465,385)를 잘라 줄였고, 왼쪽 아래 돋보기 테두리는 지웠다(크레딧 없음).
