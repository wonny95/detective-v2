# 파출소 조사실

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
- 이전 `library-higgsfield.png`는 미사용 원본으로 보관한다. 이전 출처: https://higgsfield.ai/s/tZfhIDZWdaQ
- 원본을 그대로 보관하고, 앱의 SVG 레이어에서 시계 바늘(8:40)과 피해자 위치 윤곽선을 표시한다.
- 도서관 대화 배경·현장 조사·사건 카드에서 공통으로 사용한다.
- 새 창문 잼·시계판·문 오른쪽 털 위치에 맞춰 핫스팟과 4:3 증거 촬영 범위를 조정했다.

# 빵집·카페·언덕 배경

- 모두 1376×768 PNG이며 현장 조사·인물 대화 배경·증거 사진에서 공통으로 사용한다.
- `bakery-higgsfield.png`: 사용자 제작, Higgsfield / Nano Banana.
- `cafe-higgsfield.png`, `hill-higgsfield.png`: Claude Code 제작, Nano Banana 2.1 · 16:9 · 1K · thinking high. 빵집 그림을 스타일 참고 이미지로 사용했다.
- 출처와 적용 좌표는 2026-10-15 `CLAUDE_REQUEST.md`의 인계 내용에 따른다.
- 원본은 그대로 보관하고 빵집 안내판의 `CLOSED / at 7 PM`, 카페 포스터의 공연 정보는 앱의 SVG 레이어로 표시한다.
- 새 그림에 맞춘 핫스팟은 비율 좌표, 증거 촬영 영역은 원본 픽셀 좌표(4:3)로 `PLACES`에 지정한다.

# 대화용 바닥 확장 (`<id>-floor.jpg`)

- 대화 화면이 질문 버튼 뒤까지 그림으로 채워지도록 원본 아래 바닥을 이어 그린 조각이다. 대화 카메라에서만 원본 바로 아래(`ART_FLOOR`)에 붙는다.
- Claude Code 제작(2026-10-16): Higgsfield `outpaint_image`, 3:4 캔버스로 원본을 확장한 뒤 원본 위치를 찾아 그 아래만 잘라 원본 폭 1376에 맞췄다. 확장 전체 원본은 `<id>-outpaint-original.png`(1792×2400)로 보관한다.
- 크기: library 1376×506, bakery 1376×518, cafe 1376×725, hill 1376×370.
- 원본 배경을 교체하면 이 조각도 다시 만들어야 이음새가 맞는다.

# 마을 지도 (`village-map-higgsfield.png`)

- 768×1376(9:16), Claude Code 제작(2026-10-16): Nano Banana 2.1, 1K, thinking high, 빵집 그림을 화풍 참조로 사용. 해 질 녘 숲 마을을 위에서 내려다본 그림책 지도이며 글자는 없다.
- 위치(그림 %): 달빛 언덕(망원경·벤치) ~(64–75, 14), 도서관 ~(27, 37), 호수 카페 ~(83, 46)·호수 ~(71, 57), 빵집 ~(28, 69). 위 12%는 하늘, 아래 20%는 풀밭으로 비워 제목과 버튼을 올린다.
- 지도 화면은 이 그림을 9:16 비율 그대로 화면 전체에 꽉 채우고(좌우가 조금 잘림), `PLACES[].x/y`(그림 %)에 핀을 놓는다.

# 카페 배경에서 오리 지우기 (2026-10-16)

- 오리 아저씨를 NPC로 세우려고 카운터 뒤에 그려져 있던 오리를 지웠다. Nano Banana 2.1 편집(job `354bb7cb-245c-43da-b41f-3c27bbe0634c`).
- 원본과 어긋나지 않도록 **오리 주변 상자(345,182)–(515,398)만** 편집본에서 가져와 흐리게 섞고 나머지는 원본 픽셀을 그대로 썼다. 핫스팟·증거 좌표와 `cafe-floor.jpg` 이음새는 바뀌지 않는다.
- 이전 판은 `cafe-higgsfield-with-duck.png`로 보관한다.
