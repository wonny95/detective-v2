# 바뀐 소풍 가방 · 기획 화면 그림

게임(`?case=picnic`)과 스토리보드(`design/case-01-picnic-bag.html`)가 함께 쓴다.

| 파일 | 용도·출처 |
|---|---|
| `picnic-wide.png` | 로지와 대화하는 호숫가의 넓은 배경. **사용자가 제공한 Higgsfield 이미지**(`https://higgsfield.ai/s/uuBTFpMza-I`의 화면 구도와 사용자 첨부 PNG). 탁자가 오른쪽에 작고 왼쪽에 인물이 설 공간이 있다. 1280×714. |
| `picnic-documents.png` | 서류 가방 촬영을 위한 확대 시안. Codex 이미지 편집 도구로 기존 `picnic.webp`를 참조해 초록 도시락·파란 물병을 초록 서류 폴더·파란 펜으로 바꿈. 가방의 파란 외형·탁자 구도는 유지. 1679×937. |
| `cafe-day.png` | 낮의 호수 카페. Codex 이미지 편집 도구로 도서관 사건의 `../cafe-higgsfield.png`를 참조해 낮빛과 호수 풍경으로 바꾸고 레이 라쿤 라이브 포스터와 벽·바닥 낙서를 지움. 1679×937. 도서관 사건용 밤 카페 원본은 유지. |
| `ben-home.png` | 벤의 집 내부. Codex 기본 이미지 생성 도구로 사용자 제공 소풍 배경의 화풍을 참조해 제작한 16:9 한 장(1672×941). 크림색 벽·둥근 강가 창·오른쪽 작은 탁자와 의자. 첫 결과의 과밀한 벽돌·난로·장식을 덜어낸 수정본만 보관한다. 캐릭터를 합성할 중앙은 비웠다. 그림 안에 가방·서류·펜은 없다. |
| `garden.webp` | 기존 Higgsfield 정원 배경. 미아·올리 장면에 사용. 원본 생성 job `ed423a34-161b-4c5a-885d-0aa17620a3ff`. |
| `picnic.webp` | 이전 소풍 탁자 그림. 초록 도시락·파란 물병이 들어 있어 현재 서류 가방 설정에는 사용하지 않음. 원본 job `a13b9d3f-5211-48fe-9e4f-fa2f1789428f`. |
| `cafe.webp` | 이전 카페 가방 소품 참고 그림. 현재 줄거리에는 카페에 남은 가방이 없어 사용하지 않음. 원본 job `b33d63ae-7e89-4da1-8c44-678173424197`. |

로지와 벤의 **두 파란 가방은 겉모습이 동일**하다. 소풍 탁자에서는 닫힌 가방을 넓은 화면으로 보고, 촬영할 때만 서류 가방 확대를 보여 준다. 미아가 받은 로지의 소풍 가방은 정원에 별도 소품으로 제작해야 한다. 이번 이미지 생성에는 Higgsfield 크레딧을 쓰지 않았다.

## 2026-10-30 추가 (Claude, 사용자와 정한 그림 계획)

| 파일 | 용도·출처 |
|---|---|
| `lobby-higgsfield.webp` | 노라의 회사 1층 로비. Nano Banana 2.1 1K 16:9(1.5크레딧), 참조 `ben-home.png`·`picnic-wide.png`, job `8239acb2-96ce-4612-8358-41de6d5806d1`. 가운데 바닥을 비움. |
| `picnic-rosie-bag.webp` | 노라에게서 돌려받은 로지의 가방(소지품 `bag-rosie`). `picnic.webp`의 초록 도시락·파란 물병을 빨강·노랑으로 직접 색 편집(`scripts/recolor-picnic-bag.py`, 크레딧 없음). |
| `backpack-blue.png`, `backpack-red.png` | 정원 벤치의 미아(파랑)·올리(빨강) 가방. `picnic-wide.png`의 배낭을 오려 색을 입힘(`scripts/cut-picnic-backpack.py`, 크레딧 없음). 정원 그림(`garden.webp`) 위에 겹쳐 그린다. |
| `bag-blue.png` (427×420) | 결말에서 노라·로지에게 건네는 파란 가방(두 가방 겉모습이 같아 한 장). Higgsfield Nano Banana 2.1 1k 한 장(사용자 요청, 2026-11-02, 1.5크레딧, job `4514fe11-d4ea-4c01-9e46-395525df8c15`, 소풍 탁자 배낭을 참조로 초록 단색 배경) → 원본 `bag-blue-higgsfield-original.png`. `scripts/cut-picnic-bag.py`가 초록을 빼고 가장자리 초록 번짐을 지운 뒤, 회녹색으로 나온 천을 소풍 탁자 배낭의 파랑 쪽으로 옮기고(끈·외곽선은 그대로) 높이 420px로 줄인다. |
| `picnic-nobag.png` (198×188) | 탐정이 가방을 들고 있는 동안 소풍 탁자 그림(`picnic-wide.png`) 위 939,272에 덮어 배낭을 지우는 조각. 탁자 둘레(890..1190 × 235..460)를 1024×768로 키워 Higgsfield Nano Banana 2.1 1k로 배낭만 지움(사용자 요청, 2026-11-02, 1.5크레딧, job `4ad63d5e-765a-43a4-bacd-a0348d7e7531`) → 원본 `picnic-nobag-higgsfield-original.png`. `scripts/cut-picnic-nobag.py`가 그림과 달라진 곳(배낭 자리)만 번지게 잘라 낸다. |

마을 지도는 `../village-map-day-higgsfield.webp`(두 사건 공용, 아래 HANDOFF 참고).

## 2026-10-30 대화 바닥 (Claude, 사용자 결정: 노트가 열리면 로지 얼굴이 가려짐)

- 다섯 장소 그림을 Higgsfield `outpaint_image` 3:4(1792×2400, 장당 2크레딧, 합계 10)로 넓혀 `<id>-outpaint-original.jpg`로 보관하고, `scripts/cut-picnic-floors.py`가 원본 위치를 찾아 그 아래만 잘라 원본 폭으로 줄인 `<id>-floor.jpg`를 만든다(이음새 위 260px는 원본 아래 색에 맞춰 물들임).
- job: picnic `7ac5bc59-52f8-4fa5-aac1-feb4c2ce023e`, daycafe `9f68fb08-e9ed-4896-9522-26e8481b6cf1`, benhome `7ef736a7-ef3d-4ff2-aeea-47d386066f34`, garden `9d9acc9c-d7a5-4b29-a14d-3f2272318ec1`, lobby `832e5bf3-3a01-4592-8dc1-e8fba40c2b1a`.
- 로비는 outpaint가 판자를 세로 원근으로 다시 그려 이음새에 선이 생겼다. 그래서 바닥을 원본 아래 110px 위에서 시작해 알파로 서서히 나타나게 한 `lobby-floor.webp`를 쓰고, 게임은 `ART_FLOOR.lobby.overlap`만큼 올려 붙인다.
- 장소 그림을 바꾸면 바닥도 다시 만들어야 이음새가 맞는다.

