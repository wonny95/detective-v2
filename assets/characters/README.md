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
