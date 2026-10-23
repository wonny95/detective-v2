# 캐릭터 일러스트

## 적용 중: 사용자 제공 Sgt. Badger

- 출처: https://higgsfield.ai/s/VhySEcEzf5k (사용자 제작, Higgsfield / Nano Banana)
- 원본: `sgt-badger-higgsfield-original.png` (1376×768)
- 적용본: `sgt-badger-higgsfield.png` (1060×1484, 투명 배경)
- 내장 `image_gen` 도구로 배경을 제거했다. 전신과 작은 얼굴 아이콘에 사용한다.
- 최종 편집 프롬프트:

BACKGROUND REMOVAL ONLY. Return this exact existing badger policeman as a clean transparent alpha cutout. Keep the exact original pixels/appearance of the character as faithfully as possible, same drawing, pose, uniform, face, all proportions. Remove the cream paper background, ALL surrounding decorative stars dots and floor shadow. Absolutely no glow, no halo, no vignette, no gray or cream haze behind the subject. All pixels outside the character silhouette must be alpha=0, including between the legs. A tiny original paper rim touching the character is okay but there must not be any diffused light around it. Center the entire head-to-feet character on a portrait transparent canvas with small margin. Do not redesign, do not add lighting or effects. Plain isolated sprite ready for compositing over a dark library background.

## Sgt. Badger

- 파일: `sgt-badger.png`
- 제작: 2026-10-15, 내장 `image_gen` 도구, 투명 배경
- 상태: 미사용 시안으로 보관. 사용자 요청으로 앱의 동료 경찰 전신과 얼굴 아이콘은 기존 SVG로 복원했다.

### 생성 프롬프트

Use case: illustration-story. Asset type: transparent full-body NPC sprite for a cozy forest-animal detective web game. Primary request: Sgt. Badger, a friendly adult anthropomorphic European badger police sergeant, one single character. Subject: recognizable cream-white badger face with two broad charcoal vertical eye stripes, small round gray ears, small glossy brown-black nose, warm attentive eyes and a gentle closed-mouth smile. Wearing a muted dusty-blue police cap with a small simple gold badge, dusty-blue uniform jacket, cream shirt collar, simple gold star badge, brown belt, dark navy trousers and brown shoes. Empty relaxed paws at sides, standing still upright, both feet on same baseline, facing the viewer with a very slight three-quarter turn. Style/medium: polished storybook game character, warm hand-drawn dark-brown ink outlines, subtly irregular pencil contours, matte flat gouache fills with restrained paper-grain texture, soft pastel palette. Simple readable shapes to harmonize with existing lavender-and-beige storybook interiors; charming but mature and dependable, no realism or 3D. Composition/framing: portrait 1:2 canvas, complete body including cap and both shoes, horizontally centered, character nearly fills canvas with 3 percent transparent margins, face within top third of full image; moderately large rounded head and sturdy body, silhouette about 70 percent of canvas width. Scene/backdrop: genuinely transparent alpha background, isolated sprite, no ground shadow or scenery. Constraints: exactly one character, no text, lettering, watermark, speech bubbles, extra props, weapons, notebook, frame, or background.

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
- Claude가 투명 바깥에서부터 밝고 채도 낮은 픽셀만 깎아(갈색 잉크 외곽선에서 멈춤) 테두리를 지우고 다시 잘랐다. 이전 파일은 `<id>-higgsfield-sticker.png`로 보관한다.
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

## 플레이어 탐정 다람쥐 Pioo (Claude 제작, 2026-10-22, 적용 중)

- 사용자 요청: 플레이어인 탐정의 비주얼을 다람쥐로. 후보 3장 중 **A안**(사용자 선택, 털은 주황색 그대로).
- 적용본 `detective-higgsfield.png`(627×700, 투명): Higgsfield `remove_background`(job `93e2ad30-681e-4015-af3a-7d1be40dd9e6`) 후 알파 경계로 자르고 3% 여백. 원본 `detective-higgsfield-original.png`(= 후보 A).
- 도구: Higgsfield Nano Banana 2.1, 16:9, 1K, thinking high, 참조 오리 아저씨 원본(job `6f92a3f3-dcaa-471e-b35e-edfa9f3af87b`). 장당 1.5크레딧.
- 공통 프롬프트: 위 공통 프롬프트(기준 캐릭터 duck) + "Pioo, a clever young red squirrel detective, the hero of the game. Warm russet-orange fur with a cream belly and muzzle, small ear tufts, a big fluffy curled russet tail … no white sticker outline".

| 파일 | job | 차림 |
|---|---|---|
| `detective-candidate-a.png` | `a66500b9-6ed2-43e7-8118-3713c4d8efc5` | 체크무늬 탐정 모자, 베이지 트렌치코트, 돋보기 |
| `detective-candidate-b.png` | `5dd13d0d-644e-450b-ba92-9ff4800acacc` | 겨자색 헌팅캡, 꿀색 조끼(도토리 배지), 수첩·연필 |
| `detective-candidate-c.png` | `23f91937-62a2-4eb2-921b-63657e35e78a` | 올리브색 야전 코트, 목에 카메라, 도토리 장식 가방 |

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
- `smile.png`, `smile-open.png`, `nervous*.png`, `sad*.png`, `beak*.png`: 초록을 빼고 하나씩 잘라 낸 입.
- `<인물>-closed.png`, `<인물>-open.png`(badger, mole, fiona, ray, rosie, fiona-nervous, fiona-sad, duck, detective, detective-thinking·point·lens·wave): 게임에 쓰는 그림. 그려진 입을 찾아 주변 털색으로 덮고(코는 남김) 그 위에 새 입을 얹었다. 닫은 입 선은 각 그림의 원래 선 굵기에 맞춰 굵혔다. 오리는 생성한 부리로 부리 전체를 바꾼다.
- 만드는 법: `python -I scripts/make-npc-mouths.py`(Pillow만 사용). 출력된 `[x, y, w, h]`를 `index.html`의 `MOUTHS`에 넣는다. 같은 입력이면 같은 파일이 나온다.
