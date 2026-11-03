# 장소 그림

- ‘바뀐 소풍 가방’ 기획안은 사용자 제공 넓은 소풍 대화 배경 `picnic-storyboard/picnic-wide.png`, 서류 증거 확대 `picnic-documents.png`, 낮 카페 `cafe-day.png`, 벤의 집 `ben-home.png`, 기존 정원 `garden.webp`를 사용한다. 게임에는 아직 연결하지 않았다. 출처·용도는 [소풍 배경 README](picnic-storyboard/README.md).

## 파출소 조사실

- 적용 파일: `station-interview-room.png` (1254×1254, 불투명 PNG). Codex가 기본 내장 `image_gen` 도구로 생성했으며 Higgsfield·CLI는 사용하지 않았다. 원본 출력 `exec-775099ed-d51e-4f18-aad7-1536ec5e74d1.png`를 후처리·크롭 없이 복사했다.
- `library-higgsfield-v2.png`와 `bakery-higgsfield.png`는 화풍 참조다. 크림색 벽·목재 바닥·황토색 램프·청록색 창틀·밤 숲과 달·빈 메모 코르크판·별 배지로 기존 색연필/과슈 그림책 분위기를 맞췄다. 인물·글자·사건 증거는 없다.
- 지목한 모든 인물과 오소리 경사가 공통으로 사용하는 대화 전용 방이다. 지도 탐색 장소에 추가하지 않는다. 배경과 캐릭터·말풍선·증거 UI는 분리돼 있다.
- SVG 논리 좌표는 1536×1536으로 정규화한다(원본은 정사각형이므로 비율 유지). 바닥이 그림 안에 포함돼 `ART_FLOOR` 조각이 필요 없다. 임시 전신 좌표는 오소리 x25%, 지목한 인물 x64%, 발82%, 키44%. 조사실 카메라는 전신이 장면 높이 약52%, 머리가 약35%에 오도록 잡아 말풍선 아래 얼굴을 보여 준다.
- 최종 생성 프롬프트(참조 순서: 도서관·빵집, `transparent_background:false`):

```text
Use case: illustration-story. Create ONE empty background illustration for the woodland detective game in the attached references. Both input images are STYLE REFERENCES ONLY, not edit targets: match their warm hand-drawn gouache and colored-pencil texture, soft uneven dark brown contours, gentle storybook proportions and muted teal / ochre / cream / terracotta palette. Subject: the small interview room of a friendly forest village police station at night. It should feel cozy, quiet and serious enough for a conversation, never bleak or threatening. Square 1:1 composition, 1536x1536 canvas. Straight-on view into the room, modest room-depth perspective. Honey-colored wooden floor fills the bottom 45 percent all the way to the bottom edge; warm cream plaster and lower wood panel walls fill the upper half. Keep the central broad standing area, from x 15 percent to x 85 percent, clear of furniture, with a plain softly lit wall behind it: full-body animal characters will be added separately by code at x 25 percent and 64 percent, with feet at y 82 percent and heads around y 38 percent. No furniture in front of those standing areas. A small wooden filing cabinet and a cork board with a few blank cream papers are tucked to the far left wall. A teal-framed window on the upper right shows a quiet dark blue woodland and a small moon, without bars. A warm amber hanging lamp and a little desk lamp on a narrow side shelf at the far right create gentle pools of light. A simple small wooden plaque bearing a star badge silhouette suggests a village police station; no lettering. Slightly worn natural materials, warm paper grain, charming asymmetry, flat illustrative shading matching the references. All objects are fixed in the room, no foreground overlay. The room must continue fully behind the characters, including all floor; no separate floor extension needed. Absolutely no people, no animals, no silhouettes of characters, no chairs or central table blocking the standing characters, no prison bars, no restraints, no interrogation mirror, no weapons, no crime evidence, no photographs of suspects, no readable text, no UI, no frame, no border, no watermark. Do not copy the references' bakery oven, library crime clues, clock or green door. Return the completed room background alone.
```

# 도서관 배경

- 적용 파일: `library-higgsfield-v2.png` (1376×768)
- 사용자 제작: Higgsfield / Nano Banana
- 공유 출처: https://higgsfield.ai/s/s2Ajq1IuOdk (2026-10-15 교체)
- 2026-10-27 큰 시계에 부딪힌 흔적(사용자 결정): 이 그림을 참조로 Nano Banana 2.1(16:9, 1K, thinking high)로 시계만 고친 4장을 차례로 만들었다(흔적 → 숫자 → 바늘 두 개 → 7·8 숫자, job `8fd70d91-…`·`20f2b7e0-…`·`e6459e33-…`·`5af42d02-…`, 약 6크레딧). 마지막 판(job `5af42d02-7245-4f52-bec3-251e60f26c13`, `library-clock-higgsfield-original.png`)에서 시계·유리 조각 부분(x 964–1172, y 84–572, 가장자리 5px 흐림)만 원래 그림에 붙였다. 바늘은 그림 안에 있어 SVG로 덧그리지 않는다.
- 앱의 SVG 레이어에서는 피해자 윤곽선(`library-chalk-owl.png`)만 얹는다.
- `library-chalk-owl.png`: Hoot 교수(부엉이)의 분필 윤곽선. Claude 제작, Higgsfield Nano Banana 2.1(job `418fefc0-4d1f-4393-82b8-8ceec2c1115c`), 원본 `library-chalk-owl-original.png`(1376×768, 검은 배경). 밝기를 투명도로 바꾸고 선을 5px 굵힌 뒤 잘라 2/3로 줄였다(640×450). 위에서 본 모양이라 SVG에서 세로 0.56배·-10도로 바닥에 눕힌다. 프롬프트 요지: 날개를 양옆으로 편 통통한 부엉이가 누운 실루엣, 귀깃·작은 발·짧은 꼬리, 흰 분필 크레용의 거친 한 줄, 그림책 화풍, 순수 검은 배경, 얼굴·채움·피 없음.
- 도서관 대화 배경·현장 조사·사건 카드에서 공통으로 사용한다.
- 새 창문 잼·시계판·문 오른쪽 털 위치에 맞춰 핫스팟과 4:3 증거 촬영 범위를 조정했다.

# 빵집·카페·언덕 배경

- 모두 1376×768 PNG이며 현장 조사·인물 대화 배경·증거 사진에서 공통으로 사용한다.
- `bakery-higgsfield.png`: 사용자 제작, Higgsfield / Nano Banana.
- `cafe-higgsfield.png`, `hill-higgsfield.png`: Claude Code 제작, Nano Banana 2.1 · 16:9 · 1K · thinking high. 빵집 그림을 스타일 참고 이미지로 사용했다.
- 출처와 적용 좌표는 2026-10-15 `CLAUDE_REQUEST.md`의 인계 내용에 따른다.
- 2026-10-27 언덕 벤치에 즉석카메라 추가(사용자 결정, 증거 `hill-5`): 지금 그림을 참조로 Nano Banana 2.1(16:9, 1K, thinking high, 1장 약 1.5크레딧)로 카메라만 그려 넣게 한 판(job `21f906f2-cb54-48ee-985d-ccaec6058da5`, `hill-camera-higgsfield-original.png`)에서 카메라 부분(x 1016–1150, y 370–502, 가장자리 4px 흐림)만 원래 그림에 옮겨 붙였다. 나머지 화면·바닥 확장은 그대로다.
- 빵집 안내판 `CLOSED / at 7 PM`은 그림 안의 손글씨다(2026-10-27, 사용자 요청: SVG 글씨가 인위적): 이 그림을 참조로 Nano Banana 2.1 1장(job `cf013a4e-4155-4f34-81c7-889885e3c160`, `bakery-sign-higgsfield-original.png`, 약 1.5크레딧)에서 안내판 부분(x 96–212, y 200–292)만 붙였다.
- 카페 포스터 `LIVE / MUSIC / Ray Raccoon / 8:00 - 9:30 PM`(기타·음표 낙서 포함)도 그림 안의 손글씨다(2026-10-28, 사용자 요청): 포스터 주변(x 522–1002, y 90–360)을 3배로 키워 Nano Banana 2.1 1장(job `335f4194-15f0-4e2b-985b-8d86452715d0`, `cafe-poster-higgsfield-original.png`, 약 1.5크레딧)으로 글씨를 그려 넣게 한 뒤 포스터 부분(x 702–832, y 132–296, 가장자리 4px 흐림)만 붙였다. 앱의 SVG 글씨는 없다.
- 새 그림에 맞춘 핫스팟은 비율 좌표, 증거 촬영 영역은 원본 픽셀 좌표(4:3)로 `PLACES`에 지정한다.

# 대화용 바닥 확장 (`<id>-floor.jpg`)

- 대화 화면이 질문 버튼 뒤까지 그림으로 채워지도록 원본 아래 바닥을 이어 그린 조각이다. 대화 카메라에서만 원본 바로 아래(`ART_FLOOR`)에 붙는다.
- Claude Code 제작(2026-10-16): Higgsfield `outpaint_image`, 3:4 캔버스로 원본을 확장한 뒤 원본 위치를 찾아 그 아래만 잘라 원본 폭 1376에 맞췄다. 확장 전체 원본은 `<id>-outpaint-original.png`(1792×2400)로 보관한다.
- 크기: library 1376×506, bakery 1376×518, cafe 1376×725, hill 1376×370.
- 원본 배경을 교체하면 이 조각도 다시 만들어야 이음새가 맞는다.
- 도서관 이음새 보정(2026-10-28, 사용자 요청: 대화 화면에서 잘린 줄이 보임): outpaint가 원본 아래 끝에 흐릿한 가로 띠를 남겼다. 그림+바닥을 이은 1376×1274에서 y 400–1174를 Nano Banana 2.1 1장(job `52afa19f-b165-4efc-b08a-218cd6a49301`, `library-seam-higgsfield-original.png`, 약 1.5크레딧)으로 띠만 다시 그리게 하고, 3px 위로 맞춘 결과의 y 700–852(가장자리 5px 흐림)만 붙인 뒤 다시 `library-higgsfield-v2.png`(y 0–768)와 `library-floor.jpg`(y 768–1274)로 나눴다. 핫스팟·크레용 증거 좌표는 그대로다.

# 마을 지도 (`village-map-higgsfield.png`)

- 768×1376(9:16), Claude Code 제작(2026-10-16): Nano Banana 2.1, 1K, thinking high, 빵집 그림을 화풍 참조로 사용. 해 질 녘 숲 마을을 위에서 내려다본 그림책 지도이며 글자는 없다.
- 위치(그림 %): 달빛 언덕(망원경·벤치) ~(64–75, 14), 도서관 ~(27, 37), 호수 카페 ~(83, 46)·호수 ~(71, 57), 빵집 ~(28, 69). 위 12%는 하늘, 아래 20%는 풀밭으로 비워 제목과 버튼을 올린다.
- 지도 화면은 이 그림을 9:16 비율 그대로 화면 전체에 꽉 채우고(좌우가 조금 잘림), `PLACES[].x/y`(그림 %)에 핀을 놓는다.

# 카페 배경에서 오리 지우기 (2026-10-16)

- 오리 아저씨를 NPC로 세우려고 카운터 뒤에 그려져 있던 오리를 지웠다. Nano Banana 2.1 편집(job `354bb7cb-245c-43da-b41f-3c27bbe0634c`).
- 원본과 어긋나지 않도록 **오리 주변 상자(345,182)–(515,398)만** 편집본에서 가져와 흐리게 섞고 나머지는 원본 픽셀을 그대로 썼다. 핫스팟·증거 좌표와 `cafe-floor.jpg` 이음새는 바뀌지 않는다.

# 탐정 사무소 (Claude 제작)

- 플레이어 탐정의 참나무 구멍 속 사무소. 첫 실행 사무소 화면·탐정 이름 짓기·홈 사무소에 쓴다.
- **게임에 쓰는 그림 `detective-office-wide.jpg` (1843×1376, 4:3)**: 사용자 요청(홈 사무소를 옆으로 밀어 둘러보기). 아래 세로 원본을 Higgsfield `outpaint_image`(4:3, 2크레딧, job `8061e105-90ad-465c-b0ca-26cd1aa9ae82`)로 양옆을 넓힌 2400×1792를 높이 1376으로 줄여 JPEG(품질 90)로 저장했다. 바깥 확장이 그림 전체를 다시 그려서, 세로 원본과 물건 크기·위치가 조금 다르다(왼쪽 둥근 창 전체, 오른쪽 끝 문이 새로 생김). 확장 원본은 `detective-office-outpaint-original.png`.
- 그림 기준 위치(%): 깔개 가운데 x 50.2·y 72.3, 코르크 게시판 x 47.8–63.4·y 28.8–44.1, 책장 x 64.8–80·y 52.5–77.
- 세로 원본(768×1376, 9:16, 파일은 지움. 넓힌 전체는 `detective-office-outpaint-original.png`): Nano Banana 2.1(1K, thinking high, 1.5크레딧), 화풍 참조 카페 편집본(job `354bb7cb-…`). job `0b35855d-efca-4847-8d9c-ad46af85aae4`. 인물 없음, 글자 없음. 아래 3분의 1은 탐정이 설 빈 바닥(가운데 둥근 깔개).
- 프롬프트 요지: cozy detective office inside the hollow of a big old oak tree, evening; round window to the forest village at dusk, hanging lamp, desk with open notebook, pencil, magnifying glass, jar of acorns, desk lamp; cork board with blank pinned photos and red string; coat hook with scarf, small bookshelf, cup of tea; lower third empty wooden floor with a round woven rug; no characters, no text.

# 곰 베티의 집 (`betty-home-higgsfield.png`, `betty-home-floor.jpg`)

- Claude 제작(2026-10-28, 사용자 결정: 바닥 확장을 따로 하지 않고 처음부터 바닥까지 한 장으로): Nano Banana 2.1 · 3:4 · 2K · thinking high(약 2크레딧), 빵집 그림을 화풍 참조로(업로드 media `39e83b77-…`). job `5a023938-5be9-49d1-86c8-9385ba7c4481`, 원본 `betty-home-higgsfield-original.png`(1792×2400).
- 원본을 1376×1843으로 줄여 위 768을 장소 그림, 아래 1075를 대화 바닥(`ART_FLOOR.bettyhome`)으로 나눴다. 한 그림이라 이음새가 없다.
- 물건 핫스팟: 빈 빵 바구니 (213,367)–(360,500), 꿀단지 (1200,253)–(1347,327), 털실 바구니 (927,580)–(1087,707).

# 마을 지도에 곰 베티의 집 (2026-10-28)

- 사용자 요청. 지도 (448,780)–(768,1100)을 3배로 키워 Nano Banana 2.1(1:1, 1K, job `bea993c0-0b10-403f-af25-08958b491590`, 원본 `map-betty-higgsfield-original.png`, 약 1.5크레딧)로 울타리 안 덤불 자리에 작은 통나무집을 그리게 한 뒤, 집과 길 부분(지도 (548,908)–(700,1063), 가장자리 4px 흐림)만 붙였다. 핀은 `PLACES` `bettyhome` x 82, y 78.

# 빵집 고침 (2026-10-28, 사용자 결정: 이야기 고침)

- 계산대: (220,300)–(920,600)을 2배로 키워 Nano Banana 2.1(21:9, 1K, job `39a1956e-6808-4885-8e88-eea4e14adc69`, 원본 `bakery-counter-higgsfield-original.png`)로 쪽지를 지우고 계산대 앞 칠판 "TODAY'S ORDERS / Mrs. Bear - 1 loaf - 8:30 PM / Mr. Duck - 12 muffins - 7 AM"과 왼쪽 쓰레기통 속 구겨진 신문을 그리게 한 뒤 (228,308)–(912,592)만 붙였다(가장자리 5px 흐림).
- 오븐: (1040,120)–(1376,456)을 3배로 키워 Nano Banana 2.1(1:1, 1K, job `879e3094-9cc4-4135-a8df-b31aee6649d3`, 원본 `bakery-oven-higgsfield-original.png`)로 오븐 안 쟁반 위 까맣게 탄 블루베리 파이 세 개와 연기를 그리게 한 뒤 (1099,150)–(1302,378)만 붙였다.
- 각 약 1.5크레딧. 핫스팟: 주문 보드 x 43.2 y 54.8, 쓰레기통 x 23.1 y 59.

# 우산 사건 장소 (`umbrella/`, Claude 제작, 2026-11-03)

- 사용자 결정(그림 계획): 베티의 집처럼 바닥까지 세로 한 장. Nano Banana 2.1 · 3:4 · 2K · thinking high, 베티의 집(job `5a023938-…`)을 화풍 참조로. 장당 2크레딧.
  - 회관 `a1d92bb6-30e1-4827-8bc3-37844a57c8c6`: 빈 우산꽂이·코르크 게시판·빈 안내문 종이·벽시계·햇빛 드는 창문·빈 의자, 바닥에 글자 없는 현수막.
  - 토이 네스트 `ec6369d3-828a-49c8-997e-143f6ef45fdb`: 장난감 선반·계산대 위 곰 인형과 종·빈 나무 간판·둥근 창.
  - 풍차 언덕 `07a632f5-8d4d-485e-8aac-d52ae1a6502f`: 맑은 하늘·언덕 위 풍차·풀밭의 작은 바람개비.
  - 원본 `<id>-higgsfield-original.jpg`(1792×2400).
- `scripts/cut-umbrella-places.py`: 1376×1843로 줄여 회관 100·가게 60·언덕 50부터 768 띠를 장소 그림(`<id>.webp`), 그 아래를 바닥(`<id>-floor.jpg`, 975·1015·1025)으로. 회관은 바닥의 현수막이 그림 안에 들도록 띠를 내렸다. 한 그림이라 이음새가 없다.
- 덧그림(`ART`): 현수막·안내문·게시판 사진 글자, 토이 네스트 간판 글자. 게시판의 큰 사진 자리에 실내 바자회 사진(`bazaar-photo.webp` 720×538, job `cc6471b9-62ab-4ae6-8f79-a30d3c9a525d`, 4:3 1K 1.5크레딧, 원본 `bazaar-photo-higgsfield-original.jpg`)을 폴라로이드로 얹는다. 우산꽂이에는 `umbrella-folded.png`를 위아래로 뒤집어(손잡이 위) 4° 기울여 꽂고, 꽂이 앞면(`stand-front.png`, 그림 (204,517)–(304,690))을 다시 덮는다.
- 접힌 우산 `umbrella-folded.png`: 아랫단(y 455–530)의 금빛 안감을 남색으로 칠함(크레딧 없음, 접었을 때 안감이 보이지 않게).
- 핫스팟(장소 그림 px): 현수막 (305,657)–(1035,750), 안내문 (722,213)–(852,387), 게시판 사진 (324,196)–(464,314), 시계 (708,18)–(852,162), 의자 (1143,405)–(1357,738), 창문 (905,65)–(1192,457). 가게 선반 (0,120)–(520,620), 곰 인형 (1010,368)–(1100,485). 풍차 (895,45)–(1240,450), 바람개비 (448,468)–(497,555).

# 마을 지도에 우산 사건 장소 (2026-11-03)

- 사용자 요청. 지도 그림 전체를 편집하게 한 뒤 바뀐 부분만 지금 지도에 붙였다(베티의 집 때와 같은 방식, 다른 핀은 그대로). Nano Banana 2.1 · 9:16 · 1K · thinking high, 장당 1.5크레딧.
  - 1차(job `487057cf-9078-42ce-80c2-254cbf3ce5b5`, 원본 `map-umbrella-higgsfield-original.jpg`): 처음 낮 지도 job `627775f2-…`을 참조로 풍차·마을회관·장난감 가게를 더하게 함. 풍차(왼쪽 위 언덕)와 회관(오른쪽 위, 덤불 자리, 길이 회관 앞으로 이어짐)만 썼다. 참조에 베티의 집이 없어서 가게를 베티의 집 자리에 그렸기 때문에 가게는 버림.
  - 2차(job `96f44e4b-bd97-48f1-ac56-3dcb055bf0f5`, 원본 `map-toynest-higgsfield-original.jpg`): 1차를 붙인 지도를 올려(media `6187f858-…`) 호수 아래 오른쪽 끝 소나무 자리에 장난감 가게(민트색 정면·곰 인형 그림 간판)만 더하게 함.
- 붙이기: 지도와 편집본이 픽셀 단위로 맞아(어긋남 0) 상자 안에서 다른 곳(밝기 차 45 초과)만 넓혀 흐린 가장자리로 붙였다. 풍차 (215,110)–(375,340), 회관 (540,200)–(768,450), 가게 (590,720)–(768,1000)(베티의 집 (560,940)–(690,1000)은 붙이지 않음).
- 핀: 풍차 언덕 x 38 y 17, 마을회관 x 84 y 28, 토이 네스트 x 91 y 65.
- 우산 가장자리(2026-11-03, 사용자 요청: 우산 조사 화면에서 배경 없이 우산만): `umbrella-folded.png`·`umbrella-open.png`에 남아 있던 크림색 종이 테두리를 바깥 투명에서부터 8px 안까지, 밝고 채도 낮은 픽셀만 지움(파이썬 한 번, 크레딧 없음). 조사 화면 바탕은 크림색 면 대신 회관 그림을 흐리고 어둡게 깐다(`ART.umbrella`).
