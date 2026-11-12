# 캐릭터 일러스트

## 적용 중: 사용자 제공 Sgt. Badger

- 출처: https://higgsfield.ai/s/VhySEcEzf5k (사용자 제작, Higgsfield / Nano Banana)
- 원본: `sgt-badger-higgsfield-original.png` (1376×768)
- 적용본: `sgt-badger-higgsfield.png` (1060×1484, 투명 배경)
- 내장 `image_gen` 도구로 배경을 제거했다. 전신과 작은 얼굴 아이콘에 사용한다.
- 최종 편집 프롬프트:

BACKGROUND REMOVAL ONLY. Return this exact existing badger policeman as a clean transparent alpha cutout. Keep the exact original pixels/appearance of the character as faithfully as possible, same drawing, pose, uniform, face, all proportions. Remove the cream paper background, ALL surrounding decorative stars dots and floor shadow. Absolutely no glow, no halo, no vignette, no gray or cream haze behind the subject. All pixels outside the character silhouette must be alpha=0, including between the legs. A tiny original paper rim touching the character is okay but there must not be any diffused light around it. Center the entire head-to-feet character on a portrait transparent canvas with small margin. Do not redesign, do not add lighting or effects. Plain isolated sprite ready for compositing over a dark library background.

## 적용 중: 두더지·여우·너구리·토끼 (Claude 제작, 2026-10-15)

- 도구: Higgsfield Nano Banana 2.1, 16:9, 1K, 사고 수준 높음. 참조 이미지로 `sgt-badger-higgsfield-original.png`를 넣어 화풍·비율을 맞췄다.
- 배경 제거: Higgsfield `remove_background`. 그다음 알파 경계로 자르고 3% 여백을 남겼다.
- 원본(크림 배경, 1376×768): `<id>-higgsfield-original.png`

| id | 적용본 | 크기 | 얼굴 아이콘 viewBox |
|---|---|---|---|
| mole | `mole-higgsfield.png` | 454×665 | `65 25 340 340` |
| fiona | `fiona-higgsfield.png` | 493×677 | `40 25 340 340` |
| ray | `ray-higgsfield.png` | 569×675 | `55 25 340 340` |
| rosie | `rosie-higgsfield.png` | 361×724 | `28 150 300 300` |

### 공통 프롬프트

Draw a NEW character in exactly the same art style, proportions, size and framing as the reference badger: same storybook crayon and colored-pencil texture, same soft dark outline, same thin white sticker-like rim around the character, same big round head and short chunky body, same tiny dot eyes and round red blush cheeks, standing straight and facing the viewer, arms relaxed at the sides, full body from head to feet centered on a plain flat cream paper background, the same height on the canvas as the reference. Character: {아래 설명}

### 인물별 설명

- mole: Mrs. Mole, a kind old mole librarian woman with grey-brown velvety fur, round glasses, a big pink nose, a lavender button cardigan, a green skirt and small brown shoes, a gentle worried smile. No stars, dots or decorations around her, no floor shadow, no text, exactly one character.
- fiona: Fiona Fox, a young orange fox woman baker with a white apron that has a small peach heart pocket, a peach blouse, a fluffy orange tail with a cream tip visible beside her, a slightly prim polite smile. No stars, dots or decorations around her, no floor shadow, no text, exactly one character.
- ray: Ray Raccoon, a young grey raccoon musician man with a dark mask around the eyes, a light blue shirt, a coral striped scarf, blue jeans and red sneakers, a striped ringed tail visible beside him, a slightly nervous smile. No guitar, no stars, dots or decorations around him, no floor shadow, no text, exactly one character.
- rosie: Rosie Rabbit, a shy young white rabbit girl stargazer with long ears with pink insides, round glasses, a honey yellow shirt, lavender overalls with a small yellow star patch, and a round fluffy tail, a shy worried look. No telescope, no stars, dots or decorations around her, no floor shadow, no text, exactly one character.

## 흰 스티커 테두리 제거 (2026-10-16)

- 두더지·여우·너구리·토끼 원본에는 캐릭터를 두른 흰 스티커 테두리가 함께 그려져 있었고, 배경 제거 후에도 남아 있었다.
- Claude가 투명 바깥에서부터 밝고 채도 낮은 픽셀만 깎아(갈색 잉크 외곽선에서 멈춤) 테두리를 지우고 다시 잘랐다.
- 새 크기: mole 408×620, fiona 439×621, ray 509×628, rosie 316×661. `SPRITES`의 얼굴 viewBox·`anchor`·`mouth` 좌표를 잘라 낸 만큼 옮겼다.

## 적용 중: 오리 아저씨 (Claude 제작, 2026-10-16)

- 카페 참고인 NPC. Higgsfield Nano Banana 2.1, 16:9, 1K, thinking high. 참조: `ray-higgsfield-original.png`(화풍·비율), 이전 카페 배경(오리 생김새·초록 앞치마). job `6f92a3f3-dcaa-471e-b35e-edfa9f3af87b`.
- 배경 제거: Higgsfield `remove_background`(job `b64889c1-…`). 알파 경계로 자르고 3% 여백. 스티커 테두리 없음.
- 원본 `duck-higgsfield-original.png`(1376×768), 적용본 `duck-higgsfield.png`(447×694). `SPRITES.duck`: face `52 0 340 340`, anchor .5, mouth `{x:218,y:224,w:46,h:16}`(부리 가운데 선).
- 프롬프트: 위 공통 프롬프트의 기준 캐릭터를 raccoon으로 바꾸고 "Mr. Duck, a cheerful plump middle-aged white duck cafe owner with an orange bill and orange webbed feet, wearing the same green apron as the duck in the second reference image over a cream shirt, a friendly proud smile … no white sticker outline".

## 적용 중: 피오나 표정 2종 (Claude 제작, 2026-10-16)

- 엔딩 대질·자백용. Nano Banana 2.1, 16:9, 1K, thinking high, 참조 `fiona-higgsfield-original.png`. 배경 제거 후 알파 경계 + 3% 여백.
- `fiona-nervous.png`(477×641, job `9789584a-…`): 눈을 옆으로 피하고 땀방울, 두 손을 모은 당황한 표정. mouth `{x:200,y:230,w:52,h:22}`, anchor .42.
- `fiona-sad.png`(569×624, job `390cc566-…`): 귀가 처지고 앞치마를 쥔 고개 숙인 표정. mouth `{x:236,y:215,w:36,h:16}`, anchor .415.
- 기본 그림과 같은 화면 배율이라고 보고 `height`를 스프라이트 높이 비(641/621, 624/621)로 둔다.

## 플레이어 탐정 다람쥐 (Claude 제작, 2026-10-22, 적용 중)

- 사용자 요청: 플레이어인 탐정의 비주얼을 다람쥐로. 후보 3장 중 **A안**(사용자 선택, 털은 주황색 그대로).
- 적용본 `detective-higgsfield.png`(627×700, 투명): Higgsfield `remove_background`(job `93e2ad30-681e-4015-af3a-7d1be40dd9e6`) 후 알파 경계로 자르고 3% 여백. 원본 `detective-higgsfield-original.png`(= 후보 A).
- 도구: Higgsfield Nano Banana 2.1, 16:9, 1K, thinking high, 참조 오리 아저씨 원본(job `6f92a3f3-dcaa-471e-b35e-edfa9f3af87b`). 장당 1.5크레딧.
- 공통 프롬프트: 위 공통 프롬프트(기준 캐릭터 duck) + "Pioo, a clever young red squirrel detective, the hero of the game. Warm russet-orange fur with a cream belly and muzzle, small ear tufts, a big fluffy curled russet tail … no white sticker outline".

- 후보 B(겨자색 헌팅캡, job `5dd13d0d-…`)·C(올리브색 야전 코트, job `23f91937-…`)는 고르지 않아 파일을 지웠다. A는 원본과 같다.

## 탐정 포즈 4종 (Claude 제작, 2026-10-23, 적용 중)

- 사용자 요청: 홈에서 탐정을 누를 때마다 포즈가 바뀌게. Higgsfield Nano Banana 2.1, 3:4, 1K, thinking high, 참조 `detective-higgsfield-original.png`(job `a66500b9-…`). 장당 1.5크레딧(모두 6크레딧).
- 배경 제거 Higgsfield `remove_background` 후 알파 경계 + 3% 여백으로 자르고 높이 700px로 맞췄다(기본 그림과 같은 키). 원본은 `detective-<포즈>-original.png`(896×1200).
- 프롬프트: "Redraw this exact same squirrel detective character from the reference image in a NEW POSE. Keep everything else identical: same face, … the same small closed w-shaped smile (mouth closed, clearly visible), … POSE: {아래} … plain flat cream paper background. No floor shadow, no text, no stars, dots or decorations, no white sticker outline, exactly one character."

| 파일 | 크기 | job | 포즈 |
|---|---|---|---|
| `detective-thinking.png` | 611×700 | `58376661-244d-43a4-8825-5e512a43536a` | 턱에 손, 위를 보며 생각 |
| `detective-point.png` | 614×700 | `7c0fdd81-efd4-4eae-9f93-ee0eaf546d33` | 앞을 손가락으로 가리킴 |
| `detective-lens.png` | 606×700 | `62fa87c7-51d3-4243-a57a-205966ca601a` | 돋보기를 얼굴 옆에 들고 들여다봄 |
| `detective-wave.png` | 614×700 | `52fb8489-d879-4471-8544-9986991169c9` | 한 손을 높이 들어 인사 |

## NPC 입 (`mouths/`)

- 사용자 요청: 말할 때 입 모양 개선. 그림의 입을 가리고 닫은 입·벌린 입을 번갈아. 크레딧을 아끼려고 **이미지 1장**에 모든 입을 모아 생성했다.
- `sheet-original.png`: Claude 제작, Higgsfield Nano Banana 2.1(job `bdd5aa63-00f7-4aa2-af64-3525b7a306bb`, 1.5크레딧), 1376×768. 순수 초록 배경 위 4×2: 미소 / 미소 벌림 / 당황(물결) / 당황 벌림(이) / 슬픔 / 슬픔 벌림 / 오리 부리 / 오리 부리 벌림. 프롬프트 요지: 그림책 동물 캐릭터의 말하기용 입 스프라이트, 진갈색 색연필 외곽선과 과슈 색, 칸마다 하나씩 같은 크기, 얼굴·코·글자 없음.
- 미소·당황·슬픔·오리 부리(각각 벌림 포함): 스크립트가 시트에서 초록을 빼고 하나씩 잘라 낸 입. 중간 단계라 파일로 남기지 않는다.
- `<인물>-closed.png`, `<인물>-open.png`(badger, mole, fiona, ray, rosie, fiona-nervous, fiona-sad, duck, detective, detective-thinking·point·lens·wave): 게임에 쓰는 그림. 그려진 입을 찾아 주변 털색으로 덮고(코는 남김) 그 위에 새 입을 얹었다. 닫은 입 선은 각 그림의 원래 선 굵기에 맞춰 굵혔다. 오리는 생성한 부리로 부리 전체를 바꾼다.
- 소풍 사건(Claude 제작, 2026-11-02, 크레딧 없음, 같은 시트): `nora`(입 상자 225,284,62,13), `mia`(638,328,72,22, 코에서 내려온 선은 남김), `mia-ollie`(322,205,143,45, 올리 코는 남김). 이 셋은 덮는 범위를 입 상자 둘레로 제한한다(`LIMIT`: 크레용 결이 입을 볼터치·수염과 이어 버림). 미아 흰 주둥이는 결이 짙어 어두운 선 기준을 50으로 올렸다(`DARK`). `ben`은 앞니가 미소선에 붙어 있어 닫은 입은 그림 그대로(236,222 160×70을 잘라 냄). 벌린 입은 Higgsfield 편집 한 장(사용자 요청, 2026-11-02, Nano Banana 2.1 1k 1.5크레딧, job `524c832a-8557-41fa-a4e7-174ffed2c2b0`): 스프라이트 얼굴 196..436 × 110..350을 1024로 키워 입만 벌리게 고친 것 → `mouths/ben-open-higgsfield-original.png`. 스크립트가 240으로 줄여 위쪽 얼굴로 색을 맞추고, 그림과 다른 곳(입과 조금 내려간 턱)만 번지게 잘라 `ben-open.png`(272,249 92×70)를 만든다(`ben_mouth()`).
- 만드는 법: `python -I scripts/make-npc-mouths.py [키…]`(Pillow만 사용, 키를 주면 그 입만). 출력된 `[x, y, w, h]`를 `index.html`의 `MOUTHS`에 넣는다(`mia-ollie` → `'mia:ollie'`). 같은 입력이면 같은 파일이 나온다.

## 곰 베티 (Claude 제작, 2026-10-28, 적용 중)

- 사용자 결정: 피오나의 예약 손님 Betty Bear(곰 베티), 필수 대화 참고인. Higgsfield Nano Banana 2.1, 16:9, 1K, thinking high, 참조 오리 아저씨 원본(job `6f92a3f3-dcaa-471e-b35e-edfa9f3af87b`), job `f733a908-6d1c-4c6e-8649-95e6faf98784`(약 1.5크레딧).
- 배경 제거 Higgsfield `remove_background`(job `fc620315-7242-491d-95e1-47c999ebea91`) 후 알파 경계 + 3% 여백. 원본 `betty-higgsfield-original.png`(1376×768), 적용본 `betty-higgsfield.png`(445×680). `SPRITES.betty`: face `52 -5 340 340`, anchor .5.
- 프롬프트: 위 공통 프롬프트(기준 캐릭터 duck) + "Betty Bear, a warm, kind, slightly plump middle-aged brown bear lady … chestnut-brown fur with a lighter tan muzzle … cozy knitted cream shawl over a dusty rose dress with tiny white flower dots, small brown slippers … no white sticker outline".
- 얼굴 아이콘 `assets/ui/icons-v2/betty.png`(160×160): 적용본에서 머리·어깨(22,0)–(422,400)를 잘라 줄였다.
- 입: `scripts/make-npc-mouths.py`의 `S`에 `betty`(입 상자 224,210,66,16, 미소, 선 2.6px) → `mouths/betty-closed/open.png`, `MOUTHS.betty`.

## 후트 교수 (Codex 제작, 적용 중)

- 피해자 Professor Hoot의 전신 그림. Higgsfield Nano Banana 2.1, 16:9, 1K, thinking high, 이미지 **한 장만 생성**(job `bc0e43f0-32f3-4e38-bbd3-700e3461c3bd`, 1.5크레딧). 참조: 오리 아저씨 원본(job `6f92a3f3-dcaa-471e-b35e-edfa9f3af87b`)의 화풍·비율만 사용.
- 프롬프트 요지: 기존 그림책 색연필·과슈 질감, 진갈색 연필 외곽선, 둥근 볼과 눈을 유지한 따뜻한 황갈색 노교수 부엉이. 둥근 안경·이끼색 트위드 조끼·버건디 나비넥타이·갈색 바지, 정면 전신, 팔을 내린 차분한 자세, 크림 단색 바탕, 소품·글자·스티커 테두리 없음.
- 원본 `hoot-higgsfield-original.png`(1376×768). 배경은 로컬에서 가장자리와 연결된 크림 영역만 투명하게 제거하고 캐릭터 바깥 경계(원본 x480–903, y96–727)에 약 3% 여백을 두어 `hoot-higgsfield.png`(461×669)로 잘랐다. 별도 이미지 생성·배경 제거 크레딧은 쓰지 않았다.
- 적용: 사건 완료 뒤 복습 첫 페이지의 사건 요약에 피해자 초상으로 표시한다(`CASES[0].victimPhoto`). 추리 인물 선택창에는 같은 적용본의 머리·어깨를 (28,0)–(433,405)로 잘라 160×160으로 줄인 `assets/ui/icons-v2/hoot.png`를 쓴다. 현장 분필 윤곽선은 유지한다.

## 적용 중: 소풍 사건 벤·노라·미아와 올리 (Claude 제작, 2026-10-30)

- 사용자 결정: 크레딧을 아끼려 **두 명씩 한 장**. Higgsfield Nano Banana 2.1, 16:9, **2K**, thinking high, 참조 `duck-higgsfield-original.png`·`rosie-higgsfield-original.png`. 장당 2크레딧.
  - 벤 비버 + 노라 고슴도치: job `0af39333-877b-4d1a-911f-52702b371c10` → `ben-nora-higgsfield-original.jpg`(2752×1536, 보관용 JPEG)
  - 수달 올리 + 생쥐 미아: job `54654c8f-bfc1-49a1-8a30-4845ad024a73` → `mia-ollie-higgsfield-original.jpg`
- 배경 제거: Higgsfield `remove_background`(벤·노라 `22f50dfb-…`, 미아·올리 `00e22088-…`) → `ben-nora-cutout.webp`, `mia-ollie-cutout.webp`.
- `scripts/cut-picnic-characters.py`: 벤(왼쪽)·노라(오른쪽)는 반으로 나누고, 미아와 올리는 게임에서 한 사람(`mia`, `Mia & Ollie`)이라 함께 자른다. 알파 경계 + 3% 여백, 높이 700px. 얼굴 아이콘(`assets/ui/icons-v2/ben·nora·mia.png`, 160px, 흰 테두리)도 같은 스크립트가 자른다(미아·올리는 두 얼굴을 겹쳐 한 장). 지도 핀용으로 한 얼굴씩 `mia-solo.png`·`ollie.png`도 자른다(`save(..., sprite=False)`).
- 적용본: `ben-higgsfield.png` 542×700, `nora-higgsfield.png` 475×700, `mia-higgsfield.png` 909×700. 말하는 입은 `mouths/`의 `ben`·`nora`·`mia`·`mia-ollie`(위 NPC 입 절).
- 프롬프트 요지: 참조 그림과 같은 크레용·색연필 화풍·비율로 두 인물을 나란히, 크림 종이 배경, 빈손. 벤 — 갈색 털, 옅은 주둥이, 앞니 두 개, 납작한 꼬리, 겨자색 니트 조끼·흰 셔츠·갈색 바지. 노라 — 갈색 가시, 크림 얼굴, 청록 재킷·흰 블라우스·남색 치마. 올리 — 갈색 털·크림 얼굴·긴 꼬리, 초록 티셔츠·황갈색 반바지. 미아 — 회색 생쥐, 분홍 귀·꼬리, 흰 점 하늘색 원피스, 노란 머리띠, 올리보다 머리 하나 작음.

## 적용 중: 우산 사건 엘라·핀·테스·루비 (Claude 제작, 2026-11-03)

- 소풍 사건처럼 **두 명씩 한 장**(한 화면에 함께 서는 테스와 루비를 한 장에). Higgsfield Nano Banana 2.1, 16:9, 2K, thinking high, 참조 벤·노라 시트(job `0af39333-…`)와 오리 아저씨 원본(job `6f92a3f3-…`). 장당 2크레딧.
  - 거북 테스 + 고양이 루비: job `a429340b-ad97-40d1-be9f-e20badd92fce`. 루비 옷은 사용자 요청("좀 세련된 옷으로")으로 같은 그림을 편집해 다시 그림(job `07d90f37-e824-4854-957f-d389a3ddfdb7`, 2크레딧, 테스는 그대로) → `tess-ruby-higgsfield-original.jpg`
  - 사슴 엘라 + 개구리 핀: job `af3a0080-e3d5-48bb-8e22-48589d3a5393` → `ella-finn-higgsfield-original.jpg`
- 배경 제거: Higgsfield `remove_background`(테스·루비 `d5fc2a32-…`, 엘라·핀 `d62816f2-…`) → `tess-ruby-cutout.webp`, `ella-finn-cutout.webp`. 배경 제거가 크림 종이와 비슷한 밝은 부분(테스의 소매, 루비의 스타킹, 엘라의 주둥이, 핀의 밑창)을 비우거나 반투명하게 만들어, `scripts/cut-umbrella-characters.py`가 윤곽 안쪽을 원본 시트 색으로 다시 채운다.
- 같은 스크립트가 반으로 나눠 알파 경계 + 3% 여백, 높이 700px로 맞추고 얼굴 아이콘(`assets/ui/icons-v2/<id>.png`, 160px, 흰 테두리)을 자른다. 적용본: `tess-higgsfield.png` 459×700, `ruby-higgsfield.png` 517×700, `ella-higgsfield.png` 472×700, `finn-higgsfield.png` 420×700. 화면 높이(`positions`)는 시트 안의 키 비율로(엘라·루비 46, 테스 43, 핀 37).
- 입: `scripts/make-npc-mouths.py`의 `tess`·`ruby`·`ella`·`finn`. 닫은 입은 그림 그대로(`AS_DRAWN`: 고양이·사슴의 코 밑 입 모양을 살림), 벌린 입만 시트의 미소 벌림.
- 프롬프트 요지: 참조와 같은 크레용·색연필 화풍·비율로 두 인물을 나란히, 크림 종이 배경, 빈손, 우산 없음, **남색·금색 없음**(우산 특징과 겹치지 않게, 설계서 3절). 테스 — 올리브색 피부, 갈색 등딱지, 크림 셔츠에 민트색 가게 앞치마. 루비 — 회색 줄무늬 고양이, 흰 둥근 깃의 루비색 원피스·검정 벨트·크림 스타킹·검정 메리제인. 엘라 — 황갈색 사슴(뿔 없음), 테라코타 니트 가디건·흰 블라우스·베이지 치마. 핀 — 연두색 개구리, 주황 줄무늬 티셔츠·황갈색 반바지·빨간 운동화.

## 바이올린 사건 타라·오웬·이보·모모·핍 (Claude 제작, 2026-11-07, 원본만)

- 사용자 결정(그림 계획). 우산 사건처럼 Higgsfield Nano Banana 2.1, 16:9, 2K, thinking high, 참조 `tess-ruby-higgsfield-original.jpg`·`ella-finn-higgsfield-original.jpg`(업로드 media `dfbb2e87-…`·`a129b601-…`). 장당 2크레딧. 아직 배경 제거·자르기·입을 하지 않은 원본이다.
  - 족제비 타라 + 여우 오웬: job `10d6669d-b559-4cd2-bbe0-bfce23d6d736` → `tara-owen-higgsfield-original.jpg`. 오웬 재킷의 민무늬 금색 단추, **화면 왼쪽(오웬의 오른쪽) 소매 단추가 빠지고 실이 나온 자리**, 화면 오른쪽 소매에는 금색 단추(설계서 8절).
  - 두더지 모모 + 참새 핍(같은 화면에 섬): job `9e3f5b63-83d8-4ce3-bbd2-11ea736d9146` → `momo-pip-higgsfield-original.jpg`. 모모는 도서관의 몰 부인과 구별되게 안경 없이 올리브색 작업 멜빵·줄무늬 셔츠, 소매마다 은색 똑딱이 단추 둘.
  - 염소 이보: job `aebc6daf-da25-45c6-9781-147d0b92f52c` → `ivo-higgsfield-original.jpg`. 남색 재킷, 소매마다 납작하고 어두운 단추.
- **오웬을 강아지로 바꿈(사용자 결정, 2026-11-09: 범인이 도서관과 같은 여우라서).** 지금 쓰는 오웬 세 장은 아래 강아지 판이고, 위의 여우 오웬 job은 기록으로만 남긴다(타라는 여전히 `tara-owen` 시트의 왼쪽).
  - 기본: Nano Banana 2.1, 3:4, 2K, thinking high, 참조 `10d6669d-…`(여우 오웬), 2크레딧. job `273bc0cd-ea5e-449d-addc-43a00da7260c` → `owen-higgsfield-original.jpg`. 갈색·크림색 처진 귀 강아지, 같은 초록 재킷·금색 단추·나비넥타이·회색 바지·갈색 구두, 화면 왼쪽 소매 단추 빠지고 실밥, 오른쪽 소매 금색 단추.
  - 당황: 1K, 참조 위 강아지 job과 여우 당황 `581e5172-…`, 1.5크레딧. job `a68ad591-3ba0-41a8-884d-30831619496e` → `owen-nervous-original.jpg`.
  - 고개 숙임: 1K, 참조 강아지 job과 여우 고개 숙임 `5b073cde-…`, 1.5크레딧. job `17267e35-ed72-4799-9b01-d05918f6239b` → `owen-sad-original.jpg`(한 마리만).
  - 배경 제거 `cf2d5d88-…`·`794a91fe-…`·`8a54745e-…` → `scripts/cut-violin-characters.py <폴더> owen owen-nervous owen-sad`. 그 뒤 바깥에 닿은 흰 테두리 조각(소매 실밥 옆·손과 재킷 사이·구두 옆)을 따로 지웠다. 적용본 `owen-higgsfield.png` 471×700(얼굴 `68 0 336 336`), `owen-nervous-higgsfield.png` 470×700, `owen-sad-higgsfield.png` 471×700. 입은 `scripts/make-npc-mouths.py owen owen-nervous owen-sad`(닫은 입은 그린 그대로).
  - 소매 사진 `places/violin/sleeves-owen.png`의 주황 여우 발을 강아지 털색으로 바꿨다(Python, 색상만).
- 오웬 표정 2종(심문용, 도서관 피오나처럼, 여우 판): 16:9, 1K, 참조 위 오웬 job. 장당 1.5크레딧.
  - 당황: job `581e5172-d478-45d9-aa35-6f3a3129d222` → `owen-nervous-original.jpg`(첫 판 `70a59d9f-…`는 다리·꼬리가 하나 더 그려져 버림).
  - 고개 숙임: job `5b073cde-e582-4779-bf6d-d10c53a9ec25` → `owen-sad-original.jpg`. 같은 오웬이 둘 그려졌다. 왼쪽(두 손을 모은 쪽)을 쓴다.
- 프롬프트 요지: 참조와 같은 크레용·색연필 화풍·비율, 흰 스티커 테두리, 크림 종이 배경, 빈손, 악기·케이스 없음. 타라 — 크림·세이블 털과 눈가 띠, 자두색 연주 원피스·흰 둥근 깃·검정 플랫. 오웬 — 붉은 주황 여우, 짙은 초록 연주 재킷·검정 나비넥타이·회색 바지. 모모 — 짙은 회색 두더지, 분홍 코, 안경 없음. 핍 — 갈색 참새, 하늘색 자원봉사 조끼와 글자 없는 흰 배지. 이보 — 흰 염소, 굽은 뿔, 남색 재킷, 금색 없음.
- 적용(2026-11-08): Higgsfield `remove_background`(타라·오웬 `60c41134-…`, 모모·핍 `b953d4e8-…`, 이보 `c27799c2-…`, 오웬 당황 `b0b16f89-…`, 오웬 고개 숙임 `ac464ae9-…`; 결과 PNG는 저장소에 넣지 않고 job에서 다시 받는다) → `scripts/cut-violin-characters.py <배경 제거 폴더>`(Python + Pillow, 우산 스크립트와 같은 3% 여백·높이 700·160px 얼굴 아이콘). 배경 제거 뒤에도 남은 흰 스티커 테두리는 바깥에서 깎는다(옅은 회백색만, 갈색 선에서 멈춤). 적용본: `tara-higgsfield.png` 470×700, `owen-higgsfield.png` 485×700, `ivo-higgsfield.png` 457×700, `momo-higgsfield.png` 420×700, `pip-higgsfield.png` 480×700, `owen-nervous-higgsfield.png` 486×700, `owen-sad-higgsfield.png` 566×700(시트 왼쪽 오웬), 얼굴 `assets/ui/icons-v2/tara·owen·ivo·momo·pip.png`. 입은 `scripts/make-npc-mouths.py`로 `mouths/<id>-closed·open.png`(오웬은 표정 셋 모두, 닫은 입은 그림 그대로, 핍은 부리가 벌어짐).
- 타라(`tara-higgsfield.png`): 원피스와 양팔 사이 빈틈 두 곳에 남은 흰 배경(왼쪽 x149–173·y448–500, 오른쪽 x382–401·y450–485 근처)을 스크립트 뒤에 따로 투명하게 지웠다(사용자 지적, 2026-11-09). 스크립트를 다시 돌리면 이 두 곳을 다시 지워야 한다.

# 크리스마스 별 사건 인물 (Claude 제작, 2026-11-10)

- 홀리(양)·메이(생쥐, 앉아서 가위질)·니코(펭귄) 한 장 `b7571dd2-ea5c-4ea3-86bd-4f79f863a91f` → `holly-mae-nico-higgsfield-original.jpg`(16:9 2K, 2크레딧, 참조 엘라·핀과 테스·루비 시트 업로드 media `5ed35ee6-…`·`37934cf2-…`), 배경 제거 `a2a05aec-…`. 니코 당황 `8e15f2a7-c1f5-4829-be44-973fab4497d3` → `nico-nervous-original.jpg`(1K, 1.5크레딧), 배경 제거 `45c2e2c2-…`.
- `scripts/cut-christmas-assets.py`로 인물마다 잘라 높이 700(`holly-`·`mae-`·`nico-`·`nico-nervous-higgsfield.png`). 말하는 입(`MOUTHS`)·얼굴 아이콘(`ui/icons-v2`)은 아직 만들지 않았다(얼굴은 `SPRITES[].face`로 그림에서 잘라 보임).
- 흰 스티커 테두리는 `scripts/remove-sticker-border.py`로 지웠다(홀리 `200 6`, 메이·니코·니코 당황은 기본값; 잘라 낸 그림을 덮어씀, 높이 700). 위 자르기 스크립트를 다시 돌리면 그 뒤에 이것도 다시 돌린다.
- **대화하는 모습**(사용자 요청: 일하다가 탐정을 보고 말하기): 홀리(리본을 늘어뜨리고 정면)·메이(의자에 앉은 채 가위·눈송이를 무릎에, 정면) 한 장 `c7030135-61c3-4009-8874-15aa5adb4b2f` → `holly-mae-talk-higgsfield-original.png`(16:9, 1.5크레딧, 참조 엘라 그림만, 마젠타 배경). `scripts/cut-christmas-talk.py` → `holly-talk.png`·`mae-talk.png`. 게임에서 이 그림이 기본(대화·얼굴·엔딩 방문), 자기 장소에서 대화하지 않을 때는 일하는 그림(`holly:work`·`mae:work`, `spriteKey`). 첫 시도 `47a3c1fd-…`(`holly-mae-talk-try1.png`)는 손일을 계속하는 자세라 쓰지 않고 지움(사용자 승인).
- **홀리 대화 모습 다시 그림**(사용자 요청: 말을 걸면 통통한 양털 몸이 너무 얄쌍해짐): 일하는 그림 `holly-higgsfield.png`를 참조로 올려(media `a7f387f6-…`) 같은 통통한 몸으로 정면·리본을 늘어뜨린 자세, Nano Banana 2.1 3:4 1K 마젠타 배경, job `5e30114d-7383-4472-9fb1-a9fb46f17e81`(1.5크레딧) → `holly-talk2-higgsfield-original.png`. `scripts/cut-holly-talk.py` → `holly-talk.png`(483×700). `cut-christmas-talk.py`는 이제 메이만 자른다.

## 크리스마스 점등: 뒷모습 넷

- 사용자 요청(점등 때 모두 트리를 보게, 뒷모습은 한 장에만). Higgsfield Nano Banana 2.1, 16:9, 1K, thinking high, 참조 `ella-finn-`·`holly-mae-nico-`·`tess-ruby-higgsfield-original.jpg`, job `b5ff3ce7-2534-4964-a7e6-e1c6bd91b4c9`(약 1.5크레딧) → `xmas-backs-higgsfield-original.png`(마젠타 배경, 왼쪽부터 홀리·메이(의자 위)·엘라·테스). `scripts/cut-christmas-backs.py`가 `holly|mae|ella|tess-back.png`(높이 700)로 자른다.
