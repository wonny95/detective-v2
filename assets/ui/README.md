# UI 그림

## 적용 중

### 말풍선

- `speech-paper-frame.png` (1536×1024, 투명 바깥): 힌트·엔딩 공용 말풍선 본문. **Codex가 기본 내장 `image_gen` 도구로 생성**, Higgsfield·CLI 미사용. 기존 `buttons/cream-flat.png`는 재질 참조, `places/library-higgsfield-v2.png`는 화풍 참조로 사용했다. 따뜻한 아이보리 종이, 갈색 색연필선과 가는 황토색 안쪽 선, 장식 없는 읽기 영역이다. 생성 출력 `exec-19bb79b2-db66-495c-ad43-11e798066f23.png`를 알파 채널 그대로 복사했다(원본 보관 `speech-paper-frame-original.png`, 1536×1024).
  - 2026-10-22 Claude 다시 자름(사용자 제보: 말풍선이 크기에 따라 일그러짐): 원본은 위 52·아래 64·좌우 14px가 투명 여백이고 모서리 곡선이 가로 약 170·세로 약 125px인데, 9조각을 사방 100px로 잘라 모서리 곡선이 변 조각에 걸려 함께 늘어났다. 종이 외곽 (14,52)–(1522,960)으로 잘라 1508×908로 만들고, CSS 조각을 위·아래 150 · 좌우 190px(모서리를 다 담음), 화면 두께 33px·42px(예전과 같은 0.22배), `inset:0`으로 바꿨다(`.bubble::before`, `.office-say::before`·`.oh-say::before`).
  - 같은 날 꼬리 위치도 맞춤(사용자 요청): 종이가 상자 바닥까지 내려와 꼬리가 7px쯤 안으로 올라가 있었다. 꼬리 그림의 열린 윗변(48×30 상자에서 위 3.6px)이 말풍선 아래 테두리(마지막 약 5px)를 덮도록 `bottom:-21px`로 내렸다(설계 시안은 44×28이라 `-19px`).
  - `.bubble::before`의 `border-image`로 **9조각 확장**한다. slice `100`, 표시 테두리 `22px`, 원본 투명 여백을 고려해 `inset:-8px -3px`. 모서리와 선 두께를 유지하고 가운데만 늘린다. 본문 폭은 `min(88%,380px)`이며 화면 높이에 따라 내용만 스크롤한다.
  - 이미지의 반투명한 안쪽 조각 경계에 얇은 선이 드러나지 않도록 `background-clip:padding-box`인 불투명 종이색 바탕을 함께 쓴다(`--bubble-paper`, 기본 `#FFF8E9`). 바깥 투명 모서리는 채우지 않는다. 말풍선 안의 영어·한국어·버튼 영역에는 구분선을 넣지 않고 여백만 둔다.
- `speech-paper-tail-pencil.png` (1585×992, 투명): **현재 적용**. Codex가 내장 `image_gen`으로 편집. 원본 `exec-fe952193-7816-4263-b158-60420c65dc26.png`를 가공 없이 복사해 알파 유지. 직선 삼각형, 거친 갈색 연필 외곽·황토색 안쪽 선, 열린 윗변. 불투명 V 끝 아래 약 80px 여백이 있어 끝이 잘리지 않는다. `.bubble::after`의 48×30px 상자에서 `contain`, `bottom:-14px`로 배치한다. 본체는 그대로 9조각 확장, 꼬리 크기는 고정이다. 원본 색상 구간을 기준으로 축소 후 갈색 선 약 2.5–2.7px(본문 약 2.2px)로 확인했다. Higgsfield·CLI 미사용.
  - 본문과 꼬리 모두 글자·캐릭터·조작 요소가 없는 배경 부품이다. 이름·영어·한국어·버튼은 HTML이므로 콘텐츠를 추가하거나 문장이 길어져도 이미지를 다시 만들 필요가 없다.

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

기본 형태 편집(참조: 이전 곡선 꼬리(파일은 지움), 본체; `transparent_background:true`):

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

- `casefile-panel.webp` (728×2206): 노트 패널 배경(2026-10-19 교체). 남색 서류철 위에 크림색 서류 한 장, 오른쪽 위 클립. **사용자가 직접 누끼 딴 그림** `casefile-cutout-original.png`(762×1071)의 빈 여백을 잘라 내고(18,7–746,1071), 아래 y 560–1064 구간을 위아래로 뒤집어 가며 이어 붙여 예전 그림과 같은 세로 비율(가로의 3.03배)로 늘렸다. 서류 위치·머리줄(가로의 21.7%)이 예전 그림과 같아 CSS 수치는 그대로다.
  - 2026-10-23 클립 지움(사용자 요청: 노트 오른쪽 위 UI를 가림): 클립 자리(x 570–640, y 0–135)를 같은 줄의 75px 왼쪽(파란 테두리·종이)으로 덮고 가장자리를 3px 흐리게 섞었다(Pillow).
  - 남색은 나무 바닥·타일·풀밭 같은 따뜻한 배경과 대비되도록 고른 색이다.
  - CSS는 그림 폭 기준 %로 맞춘다: 서류 윗변 7.9%, 머리 띠 높이 13.6%, 서류 폭 6.5%–93.8%. 클립(약 81–86%)을 피해 탭은 오른쪽 22%까지만 놓는다.
- `tab-1.png` … `tab-3.png` (160×148): 인덱스 탭(2026-10-27 교체, 사용자 선택 A). Higgsfield Nano Banana 2.1(1K, thinking high), 노트 종이 윗부분(`casefile-cutout-original.png`의 왼쪽 위를 마젠타 위에 놓은 것)을 참조로 그 거친 연필선과 같은 선으로 탭 6개를 마젠타 위에 한 장 그렸다(job `13d92d57-fc24-4a03-addf-5d9011ae4521`, 원본 `tabs-pencil-a-higgsfield-original.png`, 같은 프롬프트 두 장 중 하나 → 약 3크레딧). `scripts/cut-note-tabs.py`로 윗줄 세 개를 잘랐다: 연필 알갱이 사이로 비친 마젠타는 모양을 메워 선 색으로 칠하고, 선을 조금 굵히고(화면 58px에서 종이 테두리와 비슷한 굵기), 진하기(초록 채널)만 남겨 흰 바탕 위 한 가지 잉크(`#342C2A`, 종이 테두리 색)로 다시 칠하고, 아래 외곽선을 잘라 냈다. 안쪽이 흰색이라 곱하기로 입힌 색이 그대로 보인다.
- `casefile-paper-edge.png` (728×44): 노트 탭(칸막이 종이)용 종이 위 테두리 조각. `casefile-panel.webp`의 y 40–84에서 열마다 종이와 그 바로 위 연필선 2줄만 남기고(그 위·종이 밖은 투명) 잘라 냈다(PIL, 크레딧 없음). 그림의 연필선은 5–7줄로 두꺼워서(폴더에 대고 그은 선) 그대로 얹으면 닫힌 탭 밑에 짙은 띠가 보였다(사용자: 아래 여백 없게). 게임에서 닫힌 탭의 발 위에 같은 크기로 겹쳐 얹는다(독 너비의 5.49%부터).
  - 탭은 서류철 그림(`.dock::before`) 뒤(`z-index:-1`)에 놓여 윗변 너머로 머리만 나온다. 아래 14px은 서류철에 가려지고, 선택된 탭은 더 높이 나온다.
  - 탭 버튼은 이 PNG로 마스크하고 `--tab-bg` 색 위에 곱하기로 겹쳐 색을 입힌다. 선택된 탭은 꿀색(`--honey`)이며 조금 더 높다. 순서대로 1–3번 모양을 돌려 쓴다.

- `corkboard-cork.webp` (512×512, 화면에서 320px 타일): 사건 수첩 코르크판 바탕. Higgsfield Nano Banana 2.1(1K, thinking high), 카페 배경 그림(job `354bb7cb-…`)을 화풍 참조로 한 손그림 코르크 2장 중 고른 것(job `b4aa7ed9-993b-4f17-8c5e-e42688cb7edf`, 원본 `corkboard-cork-higgsfield-original.png`). 반 칸 밀어 낸 사본과 가장자리만 섞어 이음매 없는 타일로 만들었다. 처음 뽑은 사진 같은 코르크(job `96438498-…`)는 사용자가 "너무 리얼하다"고 해 버렸다.
- `corkboard-frame.webp` (804×1093, 투명): 코르크판 나무 액자. 같은 모델, 카페 배경 그림(job `354bb7cb-…`) 화풍 참조로 손그림 나무 액자 2장 중 고른 것(job `60b9f138-bafa-4736-9dd5-53bca97a5ecd`, 원본 `corkboard-frame-higgsfield-original.png`). 마젠타 배경을 로컬에서 지우고 잘랐다. 나무 두께 네 변 약 86px → CSS `border-image` 조각 `86`, 화면 두께 18px, `stretch`. 액자 안쪽 가장자리는 반투명이라 코르크를 액자 밑까지 깐다(`background-clip:border-box`, 바깥 둥근 모서리는 `border-radius:9px`로 자름) — 안 그러면 뒤 종이색이 얇은 흰 선으로 비친다. 처음 액자(job `75a1eb0e-…`, 오리 그림 참조)는 일러스트 느낌이 약하다는 피드백으로 바꿨다.

- `tack-red.webp`, `tack-grey.webp` (116×160): 코르크판 압정. 한 장(`tacks-higgsfield-original.png`, job `4c2a85c0-84ff-490d-a1c2-f1a064906458`)에 빨강·회색을 그려 마젠타를 지우고 반씩 잘랐다. 바늘 끝은 그림 가로 36.3%, 맨 아래 → SVG에서 24×33px로, 그 점이 압정 자리에 오게 놓는다.
- `polaroid-card.webp` (414×528): 사진 카드(사진 칸 없는 빈 폴라로이드 종이). job `68f66e93-f8c8-49b2-9a6e-d0eb3a8a0694`, 원본 `polaroid-card-higgsfield-original.png`. `.polaroid` 배경으로 100%×100% 늘린다(사진 카드 비율이 0.7–0.8로 비슷해 9조각 없이 씀).
- 셋 다 Nano Banana 2.1(1K, thinking high), 카페 배경 그림(job `354bb7cb-…`) 화풍 참조, 마젠타 배경을 로컬에서 지움.

## 제작

- Nano Banana 2.1, 1K, thinking high, 오소리 경사 그림을 화풍 참조(`image_references`)로 사용. 수첩 4:5, 탭 시트 3:2.

## 버튼·아이콘 (2026-10-19)

- `icons-higgsfield-original.png` (1200×896, job `4104e401-…`): 아이콘 12개 시트. 아이콘 12개 중 게임이 쓰는 play, note, magnifier만 `icons/`에 남겼다.
- `buttons-higgsfield-original.png` (1264×848, job `3599eae3-…`): 빈 버튼 시트. 알약 6색(sage·berry·honey·cream·sky·peach, 각각 보통·눌림)과 둥근 버튼 4색을 그렸다. 게임이 쓰는 `*-flat.png` 5색과 `round-cream.png`만 `buttons/`에 남겼다.
  - 문제: 보통 상태 알약 6개는 오른쪽 위 모서리가 각지게 나왔다. 눌린 상태는 온전한 알약 모양이다.
- 제작: Nano Banana 2.1, 1K, thinking high, 오소리 경사 그림을 화풍 참조로 사용. 배경은 마젠타(#FF00FF) 단색으로 지정해 로컬에서 지웠다(마젠타 정도로 알파를 매기고 가장자리 색에서 마젠타를 빼냄). 색은 게임 CSS 토큰(--moss, --berry, --honey, --paper, --sky, --peach)에 맞췄다.
- 적용:
  - 아이콘: 한 번 적용했다가 사용자 판단("안 어울린다")으로 되돌렸다. 게임은 원래의 SVG 선 아이콘을 쓴다.
  - 버튼: `.pill`과 `.tab`에 `border-image`로 `*-flat.png`를 입힌다(조각 `60 62 62 62`, 둥근 끝은 늘이지 않음, 크기 `--bw`). `*-flat.png`는 보통 상태 그림의 왼쪽 절반을 좌우로 뒤집어 붙여 만든 평평한 알약이다(각진 오른쪽 위 모서리를 없앰, 279×125 안팎). 입체감 있는 눌린 상태는 사용자가 별로라고 해 쓰지 않는다. 색: 기본 cream, `.big` berry, `.green`·`기록 완료` sage, 힌트·열린 Note honey, 켜진 토글 sky. 둥근 버튼은 cream만 쓴다(사건의 열쇠 ▶).

## 손그림 아이콘 v2 (2026-10-20)

- `icons-v2-higgsfield-original.png` (1024×1024, job `782fc121-af0e-4cb5-ae70-245350d74452`): 3×3 시트 — 돋보기, 카메라, 도토리 / 오소리 경사, 두더지 부인, 여우 피오나 / 너구리 레이, 토끼 로지, 오리 아저씨.
- 사용자 요청: 이전 아이콘(위 `icons/`)은 외곽선이 얇아 잘 안 보였다 → 굵은 갈색 외곽선(1024px 기준 약 14px), 노트(서류철)와 어울리는 색연필 화풍.
- 제작: Nano Banana 2.1, 1K, thinking high, 1.5크레딧. 참조: `notebook-v2-nobg.png`(화풍, 지금은 지운 수첩 그림) + 여섯 인물 `characters/<id>-higgsfield.png`(생김새). 마젠타 배경.
- 자르기: 마젠타 정도로 알파를 매기고 가장자리 색에서 마젠타를 빼낸 뒤, 칸이 아니라 이어진 덩어리(8방향)별로 잘라 정사각형 여백 4px를 두고 160×160으로 줄였다 → `icons-v2/<이름>.png`. 토끼 귀가 윗줄 칸까지 올라가 있어 칸 자르기는 쓰지 않는다.
- 적용: 증거 탭 카메라(`cameraIcon`, 30px), 힌트 도토리(`acorns()`, 17px), 작은 얼굴 전부(`miniSVG()`의 `FACE_ICONS`; 둥근 `.mini` 틀 안에서는 아래로 8% 내리고 1.06배).

## COMPLETE 도장·별 (2026-10-20)

- `complete-stamp.png` (900×332, 투명): 사용자 요청으로 `수사완료` 한글 도장을 영문 `COMPLETE` 도장으로 교체. Nano Banana 2.1(1K, thinking high, 16:9), 참조: 이전 한글 도장 `investigation-complete-stamp.png`(모양, 지금은 지움) + `notebook-v2-nobg.png`(화풍, 지금은 지운 수첩 그림). job `f656df82-84d3-447a-a9f1-29b1bfe258de`, 원본 `complete-stamp-higgsfield-original.png`. 마젠타 배경을 지우고(테두리 중앙값을 배경색으로 잡아 알파·색 분리) 잉크 영역으로 잘라 가로 900px로 줄였다. 엔딩 도장 카드(`.cc-stamp`)와 복습 1단계 서류(`.rv-file img`)에 쓴다. 이전 `investigation-complete-stamp.png`는 미사용 보관.
- `star.png`, `star-empty.png` (160×155, 투명): 얻은 별 / 못 얻은 별. 같은 모델, 참조: 아이콘 v2 시트(job `782fc121-…`) + 노트 화풍. job `1d60cfdf-9737-437c-ac15-91b7f5f8aad5`, 원본 `stars-higgsfield-original.png`(왼쪽 금색, 오른쪽 베이지). 반씩 잘라 마젠타를 지웠다. 사건 목록 사진 카드(`.case-stars img`, 16px)와 복습 1단계(`.rv-stars img`, 50px)에 쓴다.
- 두 장 합계 3크레딧.

## 닫기 버튼 (2026-10-20)

- `close-button.png` (128×128, 투명): 지도·증거 서랍·문법 노트·홈에서 연 복습 창·범인 선택 창의 공용 닫기. 사용자 요청으로 Higgsfield 제작. Nano Banana 2.1(1K, thinking high, 1:1, 1.5크레딧), 참조: 아이콘 v2 시트(job `782fc121-…`) + 노트 화풍. job `4cb64d76-b816-4afd-8f7b-0b75a0e89e8d`, 원본 `close-button-higgsfield-original.png`. 둥근 크림 종이 + 굵은 갈색 테두리 + 갈색 X. 마젠타를 지우고 잘랐다. `.close-button` 배경(42px), 갈색 그림자·누를 때 1px 이동 공용. 문법 노트는 오른쪽 위에 배치하며 모두 화면별 접근성 이름을 둔다. 재사용 확장에는 추가 생성·크레딧 없음.

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

## 홈 메뉴 아이콘 (2026-10-23)

- `nav-icons-higgsfield-original.png` (1264×848, job `2ba9fd48-3269-4795-9c52-f945c8a0ea47`): 3×2 시트 — 동그란 나무 문, 돋보기, 펼친 책 / 다람쥐 탐정 얼굴, 탐정 모자, 나무 문 + 등불.
- 사용자 요청: 홈 메뉴 아이콘을 앱 일러스트와 같은 화풍으로, 지금 아이콘보다 더 단순하게. 사건 = 돋보기, 홈 = 동그란 나무 문(탐정사무소), 마이 = 다람쥐 탐정 얼굴 또는 탐정 모자.
- 제작: Nano Banana 2.1, 3:2, 1.5크레딧, 마젠타 배경. 참조 그림 없이 글로만 화풍을 지정했다(그래서 탐정 얼굴이 실제 탐정 그림과 조금 다르다).
- 자르기: `scripts/cut-nav-icons.py` — 마젠타 정도로 알파, 가장자리에서 마젠타를 빼고, 칸마다 그림만 잘라 정사각형 여백을 두고 160×160 → `nav/<이름>.png`.
- 사용처: 게임 메뉴(`.nav`, `.hn-ic`). 이 시트에서는 사건 돋보기·학습 책·마이 탐정 모자만 쓴다. 나무 문은 사용자가 직관적이지 않다고 해 집(아래 시트)으로 바꿨고, 다람쥐 얼굴·문 + 등불은 고르지 않았다(시트 원본에는 남아 있음).
- `nav-icons-2-higgsfield-original.png` (1264×848, job `cd4840ad-c696-42db-bb34-9b5829edc4f6`): 3×2 시트 — 집, 굴뚝 오두막, 나무 집 / 지도, 수첩 + 연필, 덮인 공책. 위 시트를 화풍 참조로 붙여 같은 결로 그렸다(Nano Banana 2.1, 1.5크레딧). 쓰는 것: 집 `home-house`(홈), `map`·`note`(사건 안 `지도`·`Note`).
- 자르기 문턱: 마젠타 정도 60–170 사이에서 알파가 줄고, 아이콘 범위는 알파 64 넘는 픽셀로 잡는다(시트 가장자리의 옅은 줄을 버리려고).

## 이번 사건의 열쇠 종이 (2026-10-26)

- 사용자 요청: 사건의 열쇠 화면(모눈 종이 + 열쇠 카드 + 색 쪽지)을 게임 일러스트 화풍으로. Claude 제작, Nano Banana 2.1, 크레딧 약 3(1.5 × 2장).
- `casekey-pieces-higgsfield-original.png` (1264×848, job `b824d795-353a-49b3-90a6-2e4dbd276eae`, 3:2): 마젠타 바탕에 빈 크림 카드, 노랑·하늘·분홍 긴 쪽지(오른쪽 끝 말린 귀퉁이), 마스킹 테이프 두 조각. 참조: 아이콘 v2 시트(job `782fc121-…`) + 폴라로이드 카드(job `68f66e93-…`).
- `graph-paper-higgsfield-original.png` (1024×1024, job `2ddbcb24-d472-41d4-a350-03f69bcc6108`, 1:1): 손그림 모눈 종이 한 장(마젠타 위, 칸 약 50px). 참조: 폴라로이드 카드.
- `scripts/cut-casekey-pieces.py`로 `casekey/`에 잘라 냄: `card.webp`(539×194, 절반 크기, 9조각 `border-image` 20 → 12px), `note-yellow/blue/pink.webp`(632×110, 조각 22 54 22 22 → 11 26 11 11px, 오른쪽은 말린 귀퉁이까지), `tape.webp`(405×122, 쪽지 위 58×18px, 위 조각 하나만 씀), `graph-paper.webp`(352×352 타일: 원본 x 238–635, y 286–688 = 가운데 8×8칸을 연필선 사이에서 잘라 이음매에서 선이 이어짐, 화면 176px 반복 + 옅은 크림 덧칠).

## 인물 부르는 표시 (2026-10-26)

- `nudge-bang.png` (182×200, 투명): 장소에서 오래 가만히 있을 때 물어볼 게 남은 인물 머리 위에 뜨는 크림 말풍선 속 빨간 느낌표(사용자 결정). Claude 제작, Nano Banana 2.1(3:2), 참조: 아이콘 v2 시트(job `782fc121-…`) + 메뉴 아이콘 2 시트(job `cd4840ad-…`).
- 원본 `nudge-bang-higgsfield-original.png` (job `ad920057-7b41-4812-bcb7-9fece326cb5c`): 3×2 느낌표 6종 중 위 가운데. `scripts/cut-nudge-marks.py`로 마젠타를 지우고 잘라 긴 변 200px. 함께 그린 화살표 6종(job `aeb76a38-…`)과 다른 느낌표는 고르지 않았다. 두 장 크레딧 약 3.

# 추리 보드 크레용 X (`crayon-x-1.png`, `crayon-x-2.png`)

- Claude Code 제작(2026-10-28, 사용자 요청: 크레용으로 그린 듯한 X, 1장만): Nano Banana 2.1 · 1:1 · 1K · thinking high, 흰 종이 위 벽돌색(#A4352C) 크레용 X 두 획(job `09da62d6-a999-49fe-9352-16ba2cc866e2`, 원본 `crayon-x-higgsfield-original.png`, 약 1.5크레딧).
- `scripts/cut-crayon-x.py`: 흰색에서 먼 정도로 투명도를 만들고(흰 기운을 뺀 색), 픽셀을 가까운 획에 나눈다. 첫 획(왼쪽 위 → 오른쪽 아래)은 교차점을 포함한 띠 전체를 가진다. 두 장을 같은 정사각 영역(원본 (70,66)–(962,958))에서 240×240으로 줄였다.
- 게임에서는 두 장을 겹쳐 두고 `clip-path` 삼각형을 각 획 방향으로 넓혀 한 획씩 그린다(`.ded-x`).

# 추리 보드 크레용 동그라미 (`crayon-o-1.png`, `crayon-o-2.png`)

- Claude Code 제작(2026-10-28, 사용자 요청: X처럼 크레용 느낌, 아래에서 시작하는 획): Nano Banana 2.1 · 3:4 · 1K · thinking high. 첫 판(job `d31582f9-772c-413e-8eb7-90a7e3656ce8`)은 위에 X처럼 겹친 획이 생겨 버리고, 아래 왼쪽에서 시작해 아래에서 끝이 겹치는 한 획으로 다시 그림(job `6f432f4d-1cda-496e-aa3f-8e293246bf42`, 원본 `crayon-o-higgsfield-original.png`). 두 장 약 3크레딧.
- `scripts/cut-crayon-o.py`: 흰색에서 먼 정도로 투명도를 만들고, 아래쪽 두 획 중 안쪽(끝 획, x 265–600, 따라 그린 경계선 위)을 `crayon-o-2.png`로, 나머지를 `crayon-o-1.png`로 나눈다. 원본 (121,79)–(780,1116)을 200×315로 줄였다. 고리 가운데가 잘라 낸 그림의 50%·50%다.
- 게임에서는 80×100 상자에 늘려 겹치고, 원뿔 마스크로 시작 각도(205°, 끝 획 211°)에서 시계 반대 방향으로 드러낸다(`.ded-o`).
