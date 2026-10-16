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
