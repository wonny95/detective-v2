# 장소 그림

- ‘바뀐 소풍 가방’ 기획안은 사용자 제공 넓은 소풍 대화 배경 `picnic-storyboard/picnic-wide.png`, 서류 증거 확대 `picnic-documents.png`, 낮 카페 `cafe-day.png`, 벤의 집 `ben-home.png`, 기존 정원 `garden.webp`를 사용한다. 게임에는 아직 연결하지 않았다. 출처·용도는 [소풍 배경 README](picnic-storyboard/README.md).

## 쌍둥이 사건 장소 (`twins/`)

- 수리점 앞 `outside-higgsfield-original.png`(1792×2400): 2026-11-25 Claude 제작(사용자 승인), Higgsfield nano_banana_2_1 3:4 2K, job `0d1888e3-313a-407a-a157-910d966f2d5d`, 2크레딧. 참고: 꿀 가게 거리 job `a9d09de1-0e98-481a-bc1a-c28a4b4642c6`(화풍·구도), 면담 그림 job `8f9b17b6-…`(밴). 요지: 세이지색 나무·크림색 벽의 작은 수리점(톱니바퀴·렌치 간판, 진열창의 시계·라디오·등), 오른쪽 연석에 앞이 찌그러지고 전조등이 깨진 파란 밴, 글자 없는 노랑·흰 통제선, 빈 자갈길, 글자·사람 없음. `scripts/cut-twins-places.py`가 1376 폭으로 줄여 1056 띠(`outside.webp`)와 바닥(`outside-floor.jpg`)으로 자름.

- 사고 현장 `road`(job `17e13cc8-d3b6-4e2f-95a8-2680a708e23b`), 병실 `hospital`(`c11c0ab8-5769-4adf-95e4-ef71b06e2ba5`), 수리점 안 `workshop`(`ab802042-8793-45f2-b0c6-7b054c742c81`): 2026-11-25 Claude 제작(사용자 승인), 같은 모델 3:4 2K, 장당 2크레딧, 참고는 수리점 앞 job. 원본 `<id>-higgsfield-original.png`. 사고 현장은 원본에 참고 그림의 자갈길이 아래에 남고 바퀴 자국이 U자로 돌아 `scripts/fix-twins-road.py`(0크레딧)가 흙길과 곧은 급정거 자국으로 고쳐 `road-fixed.png`를 만든다. 자르기는 `scripts/cut-twins-places.py`(띠 1056).
- **지금 게임의 수리점 안**은 `workshop-musicbox-higgsfield-original.png`(1792×2400, job `20226936-b45a-4d5e-8116-e920d19f504f`, 2크레딧, 참고: 위 수리점 job): 드라이버 둘 자리에 열린 오르골과 빈 이름표. 예전 원본은 `scripts/make-ada-clock.py`가 시계를 오려 쓰므로 남긴다.
- 밴 안 `van-inside-higgsfield-original.png`(2400×1792, 4:3, job `181e16c9-fbf4-434b-9773-d4b82da61eb7`, 2크레딧, 참고: 수리점 앞·에반 면담 job): 휜 핸들·쌍둥이 사진·선인장·사탕·빵·시계 장식. 크기만 줄여 `van-inside.webp`(1600×1195). 둘 다 2026-11-25 사용자 승인, 만든 그대로.

- 지도 `map-higgsfield-original.png`(2048×2048, 1:1 2K): 2026-11-25 Claude 제작(사용자 승인), nano_banana_2_1, job `f414056b-8cce-4aea-9e09-a4e834d15408`, 2크레딧, 참고는 수리점 앞 job(화풍·수리점·밴만). 요지: 위에서 비스듬히 본 새 마을, 왼쪽 위 병원·오른쪽 위 경찰서·가운데 분수 광장·냇물과 다리·굽은 길의 급정거 자국과 고깔·오른쪽 아래 수리점과 밴, 인물·글자 없음.

## 쌍둥이 면담 (`twins/`)

- 2026-11-24 Claude 제작(사용자 요청): `interview-evan-higgsfield-original.png`(896×1200, Higgsfield nano_banana_2_1 3:4, job `8f9b17b6-b7bc-42cd-b4d7-f99572dd8db1`, 1.5크레딧, 참고 그림 `station-interview-room`·`evan-talk`). 프롬프트 요지: 지금 조사실과 같은 방에서 책상을 사이에 두고 마주 본 1인칭, 미어캣이 의자에 앉아 두 손을 책상에 올림, 노트북·서류·길과 파란 밴 사진, 글자·다른 인물 없음.
- **지금 게임의 그림(2026-11-25)**: `interview-evan-v2-higgsfield-original.png`(1792×2400, nano_banana_2_1 3:4 2K, job `bde5cff8-efe6-4581-b679-f56ced087be5`, 2크레딧, 참고: 아래 첫 그림과 수리점 앞). 파란 셔츠·진한 갈색 멜빵 작업복·이마 거즈·책상 사진의 밴. 에반은 원본 그대로(사용자 요청, 책상 사진의 밴 색만 밝게). 마일로는 같은 그림에서 거즈를 지우고(첫 그림의 이마가 똑같이 겹침) 셔츠를 베이지로 바꾸고 손가락 붕대를 그린 것(0크레딧, `scripts/make-twins-rooms.py`). → `interview-evan-v2.png`·`interview-milo-v2.png`, 게임용 `interview.webp`(두 방)·`evan.webp`(복습 사진).
- 게임의 면담실은 `room-evan.webp`·`room-milo.webp`(1344×1800, 위 두 그림을 자르지 않고 크기만 줄임, 사용자 요청 2026-11-25). 벽을 사이에 둔 `interview.webp`는 쓰지 않음.
- `scripts/make-twins-interview.py`: 원본의 상처(반대쪽 팔)를 거울 복사로 지우고 `interview-evan.png`(오른쪽 손목)·`interview-milo.png`(왼손 검지)에 다시 그린다. WebP는 quality 90.

## 파출소 조사실

- **2026-11-13 교체(사용자 요청: 나무색 실내라 다른 장소와 구분이 안 됨, 3안 중 A 선택)**: 청회색 타일 벽·회색 바닥·형광등·왼쪽 어두운 유리창·벽시계·배지·오른쪽 철제 책상과 의자 둘. Higgsfield Nano Banana 2.1 1:1, 예전 그림을 구도 참조(media `237c7e94-…`), job `74fd7944-5b4b-41f2-9b27-eb216dd561ff`(1.5크레딧, 3안 합계 4.5) → 원본 `interview-room-higgsfield-original.png`(1024), 1536으로 키워 `station-interview-room.png`. 아래는 예전(나무색) 그림의 기록이다.

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

# 바이올린 사건 장소·물건 (`violin/`, Claude 제작, 2026-11-07, 원본만)

- 사용자 결정(그림 계획, 총 27.5크레딧). 아직 자르기·배경 제거·게임 연결을 하지 않은 원본이다. 받은 PNG를 품질 92 JPG로 저장했다(우산 원본과 같게, 크기 약 10분의 1). 인물 원본도 같다.
- 장소 4곳: 우산 사건처럼 바닥까지 세로 한 장. Nano Banana 2.1 · 3:4 · 2K · thinking high, 회관 원본(`umbrella/hall-higgsfield-original.jpg`, media `216af844-…`)을 화풍 참조로. 장당 2크레딧. 1792×2400.
  - 로비 `7b6d317d-1ae9-4f9d-bedb-dc835ef8f5b1` → `lobby-higgsfield-original.jpg`: 바이올린·음표 포스터, 그 아래 긴 벤치와 벤치 밑 안내지, 빈 안내판(이젤), 탁자 위 프로그램 묶음, 안쪽 복도 문.
  - 대기실 `e1ab2f17-86a3-4a76-8335-40b9b2d5720c` → `waiting-higgsfield-original.jpg`: 왼쪽 열린 문 너머 준비실 입구와 붉은 커튼, 의자 두 개(왼쪽 의자 옆 빈 바닥), 옷걸이, 전신거울, 탁자 위 물병. 니퍼는 그림에 없다(소지품 그림을 오른쪽 의자 아래에 얹는다).
  - 무대(다시 만듦, 2026-11-09, 사용자 요청: 무대답게; 첫 판 `8dbddf27-…`은 복도 옆방처럼 보였음) `db00b210-344d-41b3-8bed-936a47f1367b` → `stage-higgsfield-original.jpg`: 무대 위에서 객석을 보는 시점. 금색 무대 틀과 양옆으로 걷힌 붉은 막·술 달린 위 장식, 조명 봉의 스포트라이트, 무대 앞 각광, 어두운 붉은 객석과 2층, 비상구 등. 왼쪽 무대 옆 열린 문 너머 작업등 옆 사다리(이보 i4). 같은 날 문을 걷힌 검은 옆 가림막으로 고친 판(사용자 결정, 이보 i4를 side curtain으로) `58bc5c63-…`을 쓴다(이 판을 참조로 편집, 2크레딧), 오른쪽 악보대와 작은 의자. 참조 첫 판 무대·준비실 job, 3:4 2K thinking high, 2크레딧.
  - 준비실 `4c7728ea-0c9b-48b0-be61-0565a3a6eaf5` → `backstage-higgsfield-original.jpg`: 왼쪽 통로 문, 사다리와 켜진 작업등, 닫힌 긴 붉은 커튼, 오른쪽 무대 쪽 문.
  - 커튼을 연 준비실 `2e486cef-dbad-449d-9965-7f936977410b` → `backstage-open-higgsfield-original.jpg`(위 준비실을 참조로 편집, 2K라 2크레딧): 커튼을 오른쪽으로 걷어 선반 위 예비 전구들, 선반 아래 검은 공구함. 케이스·단추는 그림에 없다(소지품 그림을 얹는다).
- 소지품 시트 `1a72b2d8-fc85-4c82-acaf-4c7fe9885655` → `items-sheet-original.jpg`(16:9 2K, 2크레딧, 참조 `umbrella/umbrella-sheet-original.png`·타라와 오웬 시트): 닫힌 검은 케이스(노란 달), 연 케이스(현이 끊어진 바이올린·활), 금색 단추, 날에 은색 현 조각이 낀 빨간 손잡이 니퍼. 연 케이스의 달 스티커가 뚜껑 안쪽 안감에 그려졌다.
- 소매 확대 시트 `997b5f43-8664-4a83-a3cb-655ca3491c9f` → `sleeves-sheet-original.jpg`(16:9 2K, 2크레딧, 참조 세 인물 시트): 2×2 칸. 왼쪽 위 오웬(화면 왼쪽 소매는 빈 자리와 실, 오른쪽은 금색 단추, 사진 증거 sleeve-photo), 오른쪽 위 이보(어두운 단추), 왼쪽 아래 모모(은색 똑딱이 둘씩), 오른쪽 아래 빈 칸.
- 타라가 준 케이스 사진 `556e9eef-71bc-4676-9539-09cec339f321` → `tara-photo-higgsfield-original.jpg`(4:3 1K, 1.5크레딧, 참조 소지품 시트): 집 의자 위의 닫힌 케이스와 노란 달.
- 마을 지도에 음악회관 `e1f461aa-df1d-4a82-9f3e-d9b8e625a756` → `../map-violin-higgsfield-original.jpg`(9:16 1K, 1.5크레딧, 참조 지금 낮 지도 `village-map-day-higgsfield.webp`, media `6b7ce609-…`): 오른쪽 종탑 회관과 호수 오두막 사이 소나무 자리에 크림 벽·붉은 둥근 지붕·바이올린 그림 간판의 음악회관. 바뀐 부분만 지금 지도에 붙일 차례(우산 때와 같은 방식).
- 적용(2026-11-08, 앞 사건들처럼 Python으로 다시 자름): `scripts/cut-violin-places.py <배경 제거 폴더>`(Pillow). 장소는 1376×1843으로 줄여 띠 시작(로비 380: 벤치 밑 안내지가 들어가게·대기실 140·무대 300·준비실과 커튼을 연 판 250)부터 768을 `<id>.jpg`, 그 아래를 `<id>-floor.jpg`(로비 695·대기실 935·무대 775·준비실 825). 게임의 장소 id는 로비만 `foyer`(소풍 사건의 `lobby`와 겹치지 않게). 소지품은 배경 제거한 시트(`remove_background` `3f42bb9c-…`, 저장소에 넣지 않음)에서 남은 흰 스티커 테두리를 바깥에서 깎고(옅은 회백색만, 갈색 선에서 멈춤) 물건마다 잘라 `case-closed.png` 293×640·`case-open.png` 416×640·`gold-button.png` 240×240·`cutters.png` 302×460. 니퍼는 대기실 오른쪽 의자 아래, 케이스는 커튼을 연 준비실 선반 앞에 눕혀, 단추는 커튼 자락 아래에 `ART`로 얹는다. 소매는 시트의 세 칸에서 종이를 가장자리부터 지우고(사용자 요청: 종이 없이) 큰 조각만 남겨 높이 300 PNG로(`sleeves-owen.png` 442·`-ivo` 427·`-momo` 385 폭), 확대 조사에서는 방 그림을 흐리게 깐 위 가운데에 높이 260으로 놓는다(`closeLook()`). 타라의 사진은 1024×765 `tara-photo.jpg`.
- **사건 지도(2026-11-09, 사용자 요청: 대회장 안에서만 일어나는 사건이라 마을 전체가 필요 없음)**: 음악회관을 지붕을 걷고 위에서 본 그림책 지도 `cb7a0679-efeb-45be-84b5-8a4790b21ede` → `map-hall-higgsfield-original.jpg`(9:16 2K, 2크레딧, 참조 마을 지도 편집본·무대 그림). 아래 로비(포스터·프로그램 탁자·벤치·안내판), 가운데 객석, 위 무대, 왼쪽 대기실(의자 둘·거울·물병), 왼쪽 위 준비실(사다리·작업등·붉은 커튼·전구 선반·공구함). 글자 없음. 1080×1935 `map-hall.webp`(품질 86). 핀: 로비 50,78·대기실 22,46·무대 68,39·준비실 30,18.
- 마을 지도(처음 판): 편집본의 (540,410) 228×200에서 낮 지도와 달라진 곳만 가장자리를 흐려 `village-map-day-higgsfield.webp`에 붙였다(우산 사건 때와 같은 방식, 모든 사건의 지도). 핀: 로비 87,41·대기실 74,38·무대 91,33·준비실 76,29(한 건물의 네 방이라 둘레에 나눔).

- **음악 대회장답게 다시 그림(2026-11-17, Claude, 사용자 요청: 악기가 없고 창고 같았다)**: Nano Banana 2.1 1K 16:9 편집(장마다 1.5크레딧, 지금 그림을 참고로 같은 구도·배치, 바이올린 케이스·검은 케이스·금색 단추·사람 없음) → 원본 `<id>-restyle-higgsfield-original.png`: 로비(빨간 카펫·음표 현수막·벽지·오케스트라 사진·진열장의 트로피·트럼펫·하프·호른·게시판 이젤; 진열장의 바이올린 모양 악기는 호른으로 다시 편집), 대기실(조명 거울·나비넥타이와 목도리 걸린 고리·보면대와 트럼펫·구석의 첼로), 무대(무대 왼쪽 위 그랜드 피아노·현수막, 객석의 피아노는 지움), 준비실·커튼 연 판(코르크 게시판·문의 금색 별). 띠는 처음과 같은 자리에서 768로 잘라 `<id>.jpg`.
- **세로 한 장(사용자 결정: 짧은 그림에 예전 바닥을 붙이면 벽과 바닥이 겹쳐 보임)**: Nano Banana 2.1 3:4 2K(장마다 2크레딧), 지금 그림을 참고로 천장부터 아래 40%의 빈 바닥까지. 1376×1842(3)로 줄여 자름 — 옆 통로 `77d0da52-…` → `passage-tall-higgsfield-original.png`, y 260–1028을 `passage.jpg`, 아래를 `passage-floor.jpg`(814); 로비 `dd121020-…` → `lobby-tall-higgsfield-original.png`, y 160–1216을 `lobby.jpg`(1376×1056, 포스터부터 벤치 밑 안내지까지), 아래를 `lobby-floor.jpg`(627). 예전 `passage-floor.webp`·`passage-outpaint-original.jpg`는 안 씀(지우기 승인 대기).
- **사건 지도 다시(2026-11-17)**: 사용자와 정한 방 배치(왼쪽 위 준비실·그 아래 옆 통로·대기실, 오른쪽 위 무대·그 아래 객석, 아래 전체 로비, 문은 준비실–무대 왼쪽 날개·준비실–통로·통로–대기실·대기실–로비·객석–로비·정문만)를 색 평면도로 그려 GPT Image 2.6로 지도화한 뒤, 2K high로 아이소메트릭 다시 그림 → `map-hall-restyle-higgsfield-original.png` → `map-hall.webp`(1080×1920). 핀: 로비 52,72·대기실 24,48·무대 72,27·준비실 30,17.
- **로비 게시판 확대 `winners`(2026-11-17)**: 처음엔 메달판(GPT Image 2.6 `winners-higgsfield-original.png`, 안 씀), 사용자 요청으로 로비의 이젤을 잘라 참고로 같은 모양을 다시 그림 `78eab01d-…`(3:4 1K high, 약 1.5크레딧) → `winners-easel-higgsfield-original.png`, 양옆 벽지를 잘라 `winners-board.jpg`(774×1168), 확대 화면에 (483,50) 410×619. 손글씨 7줄: 1st Tara Ferret - Violin · 2nd Ivo Goat - Flute · 3rd Owen Dog - Cello · 4th Lily Duck - Piano · 5th Sam Otter - Trumpet · 6th Zoe Owl - Harp · 7th Leo Lion - Drum. `winners.jpg`는 안 씀.

# 크리스마스 별 사건 장소 (`christmas/`, Claude 제작, 2026-11-10)

- 사용자 결정(그림 계획 약 19크레딧, 실제 27크레딧: 천막 상자 수 수정·창고 저울 지우기·배경 제거 포함). Higgsfield Nano Banana 2(`nano_banana_2`), 장소는 3:4 2K 바닥까지 한 장(1792×2400), 화풍 참조는 바이올린 로비·준비실 job(`7b6d317d-…`·`4c7728ea-…`)과 첫 광장 그림.
  - 트리 광장 `5f133213-ab30-41c8-a659-5d77f85cddf0` → `tree-higgsfield-original.jpg`: 큰 트리(별 없음, 낮은 가지의 종·리본), 오른쪽 줄무늬 차양 안내소, 왼쪽 위로 올라가는 눈길.
  - 밤 광장: 위 그림을 어둡고 푸르게(Python, 크레딧 없음, `tree-night.jpg`). 불 켜진 트리는 그 어둡게 한 판을 참조로 편집 `0f4a3ae2-3b33-4029-96b5-ee11ee207a82` → `tree-lit-higgsfield-original.jpg`(전구·꼭대기 금별·창문 불빛, 2크레딧).
  - 창고 `848bb86b-5992-4051-8fb3-46d7d9ffe795` → `storeroom-higgsfield-original.jpg`: 왼쪽 앞 장식 작업대, 장식 상자 더미, 벽 화환·사다리, 접이식 의자 앞 양팔 저울, 전구 줄 상자·식탁보 바구니, 오른쪽 뒷문과 별 받침이 빈 보관함 선반·선반 아래 반짝이, 포장지 선반. 저울을 지운 판 `9bf23ead-3b69-4f33-9adb-21b58013cf52` → `storeroom-noscale-original.jpg`(2크레딧), 저울 자리만 섞어 `storeroom-noscale.jpg`(저울을 가져간 뒤의 창고).
  - 창고 모퉁이 사진 c-track-yard: 처음 그림 `c22d4912-0409-479f-88c7-2a578feca526` → `corner-higgsfield-original.jpg`(4:3 1K, 1.5크레딧, 이제 안 씀: 오른쪽 자국이 창고에서 시작하지 않고 손수레가 없었음). 지금 그림은 이것을 고친 `80cdd3ed-5fde-46bd-b596-c8953243afee` → `corner-cart-higgsfield-original.jpg`(nano_banana_2 편집, 1.5크레딧, 사용자 요청): 문 옆에 트리 장식(공 장식·갈랜드·화환·전구 줄·종)을 가득 실은 데이지의 손수레, 손수레에서 시작해 트리까지 굽는 바퀴 자국, 문에서 나와 나무 기둥 옆을 지나 왼쪽 아래로 가는 썰매 자국, 멀리 트리. 창고 뒷문을 누르면 열리는 확대 화면 `backyard`(창고 뒤 눈밭)의 그림이고, 거기서 찍는 `Marks outside` 증거 사진도 이 그림 전체다.
  - 천막 `6469c9fa-09d8-4963-aa2d-1f21f309fee1` → `tent-higgsfield-original.jpg`: 상자가 다섯이라(자동차와 별 장난감이 한 상자) 전체 편집 `597d611d-…`(실패, 2크레딧) 뒤 작업대 부분만 잘라 편집 `522fa594-eb33-4aac-b385-13b75464b6e0`(4:3 1K, 1.5크레딧)으로 여섯 상자(자동차 상자·별 장난감 상자 따로)를 만들어 붙임 → `tent-fixed-original.jpg`. 진행된 천막은 빨간 리본 상자를 오려(`tent-wrapped.png`) 자동차 상자 위에 덮고 클립보드 체크를 넷으로(`ART.tent`, `xmasList()`).
  - 썰매 `25c189bc-3204-4b7e-ac01-6832755e132a` → `sleigh-higgsfield-original.jpg`: 똑같은 빨간 상자 다섯(가운데가 조금 낮음), 옆의 빈 상자·선물 자루, 왼쪽 나무 기둥과 썰매 밑으로 드는 자국, 뒤 오른쪽 천막. (지금은 쓰지 않음: 아래 천막 옆 썰매로 바꿈.)
  - 천막 옆 썰매 `d2a69ace-01b9-4c8d-af3c-f353423d4c89` → `sleigh-side-higgsfield-original.jpg`(3:4, 896×1200, 1.5크레딧, 위 썰매 원본과 창고 모퉁이 사진을 참고로): 같은 썰매·상자·자루·기둥 자리, 오른쪽 천막의 열린 옆면과 작업대, 뒤쪽 마을 대신 나무, 왼쪽 멀리 창고와 그 문에서 기둥 옆을 지나 썰매 밑으로 드는 자국(사용자 요청: 천막 앞은 너무 눈에 띔, 창고에서 이어지는 자국). `scripts/cut-sleigh-side.py`가 위 1028을 장소 그림(이 장소만 더 김), 아래를 바닥으로 자르고 자국을 연하게 함(사용자: 너무 진함). 앞서 자국만 고친 Higgsfield 수정(1.5크레딧)은 자국이 더 흐려져 쓰지 않음.
  - 물건 시트 `7ff573b5-8062-4c09-a671-9e9f1afa154d` → `items-sheet-original.jpg`(16:9 2K, 2크레딧, 참조 바이올린 물건 시트·썰매), 배경 제거 `f80127de-…`: 별 장난감 뒷면 `toy-star-back.png`, 상자 속 금별 `box-star.png`, 금별 뒷면 잎사귀 `star-back.png`, 털장갑 상자 `box-mittens.png`, 닫힌 상자 `box-closed.png`, 저울 `scale.png`(배경 제거 그대로는 `scale-sticker-original.png`: 흰 스티커 테두리가 남아 `scripts/clean-christmas-scale.py`로 지움).
  - 저울 화면 배경 무늬 `1d707443-619e-4378-99ed-42ffbb3b5894`(gpt_image_2_6, 1:1, 약 0.25크레딧; 짙은 소나무색 바탕, 크림색 눈송이·별, 연두 호랑가시잎, 빨강·금색 없음) → `weigh-pattern-higgsfield-original.png`, `scripts/make-weigh-pattern.py`로 이음새 없는 `weigh-pattern.jpg`(640×640).
  - 열린 상자 뒤 썰매·빈 상자(Claude, 2026-11-16, gpt_image_2_6, 약 0.5크레딧): 썰매 그림 일부 (416, 388)-(992, 772)에서 앞 가운데 상자를 지운 편집 job `ea67f0e4-2a2c-4df8-9ec6-b930d8718f84` → `sleigh-nobox-higgsfield-original.png`, 상자 자리만 가장자리를 흐려 붙인 `sleigh-nobox.jpg`(상자가 열리면 배경). `box-star-higgsfield-original.png`에서 별을 지운 편집 job `00958f63-ddc4-4340-a1df-1a0044850798` → `box-empty-higgsfield-original.png`, 회색 바탕을 잘라 `box-star.png`와 같은 크기의 `box-empty.png`(별을 꺼낸 뒤). 둘 다 `scripts/fix-sleigh-open-box.py`.
  - 썰매 상자를 하나씩 그림(Claude, 2026-11-16, gpt_image_2_6 4장 약 1크레딧): 썰매 그림 일부 (380, 320)-(1100, 800)에서 상자 다섯을 모두 지운 편집 job `77d5e28f-9403-4b10-9fbe-6ea3690c3523` → `sleigh-empty-higgsfield-original.png`, 붙인 `sleigh-empty.jpg`(썰매 배경)와 그 위에 얹는 앞판 `sleigh-rail.png`. 같은 상자의 닫힌 모습 job `e9fb63cc-e376-4546-b20e-a4425f1d157d` → `box-shut-higgsfield-original.png` → `box-closed.png`(썰매·저울), 장갑이 든 모습 job `fdbc02bb-bed5-4c2f-b121-ac9e65526bb9` → `box-mittens-open-higgsfield-original.png` → `box-mittens.png`(예전 초록 리본 그림을 바꿈). 처음 해 본 좁은 빈 썰매 job `a48109fd-…`는 오른쪽 상자 끝이 잘려 쓰지 않음. `scripts/make-sleigh-boxes.py`. 게임은 원래 `sleigh.jpg`를 그대로 쓰고, 여는 상자 자리만 `scripts/make-sleigh-box-slots.py`가 자른 조각으로 바꿈: 빈 썰매 조각 `box-gap-0…4.png`, 앞에 선 상자 `box-cut-1…3.png`, 왼쪽 벽·앞판 `sleigh-front.png`. 쓰지 않는 그림: `sleigh-nobox.jpg`(셋째만 지운 썰매), `sleigh-rail.png`(빈 썰매 위에 새 상자를 그리던 때의 앞판; 사용자: 부자연스러움).
  - 소지품 금별(정면) `f72a6bd0-…` → `star-front-higgsfield-original.png`(gpt_image_2_6, 상자 속 금별을 참고로 별만), 마젠타를 빼 `star-front.png`(700×662): 소지품 칸·가방 그림.
  - 테스의 선물 목록 클립보드(정면) `5e46d6df-ed0c-4aec-a227-58c82aef1a73` → `gift-list-higgsfield-original.png`(gpt_image_2_6, 3:4, 0.25크레딧, 천막 그림의 클립보드를 참고로 빈 종이). `scripts/make-christmas-gift-list.py`가 마젠타를 빼고 손글씨 글꼴(Windows Ink Free)로 목록(Gifts for This Delivery · Toy gifts: 6 · 여섯 이름과 체크 칸)을 써 `gift-list-2.png`(체크 둘)·`gift-list-4.png`(체크 넷, 779×1138, 종이 64,172–716,1066)를 만듦.
  - 코코의 인수증: 바닥에 붙였던 빈 종이(`tent-slip-higgsfield-original.png`)를 `scripts/fix-christmas-tent-slip-table.py`가 예전 천막 그림(git e096264)의 바닥으로 덮음.
  - 탁자 위 접힌 종이(2026-11-16): `tent.jpg` 960,384–1376,768 조각에 Higgsfield(gpt_image_2_6, 약 0.25크레딧)가 접힌 종이를 그린 `coco-table-higgsfield-original.png`(1008×896). 조각이 원본과 어긋나 종이만 테두리째 다각형으로 잘라 82%로 줄여 오른쪽 6px·위 16px에 붙임: `scripts/add-christmas-coco-slip-table.py`(종이 없는 `tent.jpg`에서 한 번 돌림).
  - 펼친 인수증(확대 `cocoslip`, 2026-11-16): Higgsfield(gpt_image_2_6, 약 0.25크레딧) 빈 종이 `coco-slip-higgsfield-original.png`(마젠타 배경) → `scripts/make-christmas-coco-slip.py`가 마젠타를 빼고 글씨(Ink Free 연필, 서명은 Segoe Script 파란 잉크: Hand-over Slip · Mittens · wrapped by Coco · Ivy·Toby·Wren·Hugo 체크 · 4 boxes · Taken by: Nico)를 써 `coco-slip.png`.
  - 축제장 지도 `e40f2a1f-38aa-4585-904e-10ac1d0cfdd3` → `map-higgsfield-original.jpg`(9:16 1K, 1.5크레딧) → `map-festival.webp`. 핀: 광장 50,74·창고 26,20·천막 82,20·썰매 58,33.
- 적용: `scripts/cut-christmas-assets.py <받은 파일 폴더>`(Pillow). 장소는 1376×1843으로 줄여 띠 시작(광장 330·창고 380·천막 520·썰매 260)부터 768을 `<id>.jpg`, 그 아래를 `<id>-floor.jpg`(745·695·555·815).

## 화단 사건 옆집 마당 (Claude 제작, 2026-11-23)
- 사용자 제안(용의자들이 다른 배경에서 공놀이): Nano Banana 2.1 3:4 2K, job `97d6b7b4-3f6a-4837-b26b-7da31d48a96a`, 정원 그림 참조 → `flowerbed/yard-higgsfield-original.png`(1792×2400). `scripts/cut-flowerbed-yard.py`: 1376 폭으로 줄여 위 360부터 768을 `yard.webp`, 아래 잔디를 뒤집어 이은 `yard-floor.jpg`(900).

