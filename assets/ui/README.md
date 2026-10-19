# UI 그림

## 적용 중

- `casefile-panel.webp` (728×2206): 노트 패널 배경(2026-10-19 교체). 남색 서류철 위에 크림색 서류 한 장, 오른쪽 위 클립. **사용자가 직접 누끼 딴 그림** `casefile-cutout-original.png`(762×1071)의 빈 여백을 잘라 내고(18,7–746,1071), 아래 y 560–1064 구간을 위아래로 뒤집어 가며 이어 붙여 예전 그림과 같은 세로 비율(가로의 3.03배)로 늘렸다. 서류 위치·머리줄(가로의 21.7%)·클립 위치가 예전 그림과 같아 CSS 수치는 그대로다. 예전 원본·누끼는 `casefile-higgsfield-original.png`, `casefile-nobg.png`.
  - 남색은 나무 바닥·타일·풀밭 같은 따뜻한 배경과 대비되도록 고른 색이다.
  - CSS는 그림 폭 기준 %로 맞춘다: 서류 윗변 7.9%, 머리 띠 높이 13.6%, 서류 폭 6.5%–93.8%. 클립(약 81–86%)을 피해 탭은 오른쪽 22%까지만 놓는다.
- 아래 `notebook-panel.webp`(스프링 수첩)는 사용자 피드백으로 교체되어 미사용이다.

- `notebook-panel.webp` (640×1731): 노트 패널 배경. `notebook-v2-higgsfield-original.png`의 배경을 Higgsfield `remove_background`로 지운 뒤(`notebook-v2-nobg.png`) 수첩만 잘라, 스프링 4칸 구간(원본 y 380–680)을 6번 이어 붙여 길게 만들었다. 패널 폭에 맞춰 위에서부터 그리며 아래는 화면 밖으로 잘린다.
  - CSS는 그림 폭 기준 %로 맞춘다: 종이 윗변 4.7%, 머리 띠 높이 12%(제목과 `기록 완료`), 스프링 영역 ~12.4%, 오른쪽 표지 ~9%.
- `tab-1.png` … `tab-6.png` (160×146): 인덱스 탭. 흰 종이 탭 6개를 한 장(`tabs-higgsfield-original.png`)에 그려 크레딧을 아끼고, 칸별로 잘라 아래 외곽선을 지우고 바깥을 투명하게 만들었다.
  - 탭은 서류철 그림(`.dock::before`) 뒤(`z-index:-1`)에 놓여 윗변 너머로 머리만 나온다. 아래 14px은 서류철에 가려지고, 선택된 탭은 더 높이 나온다.
  - 탭 버튼은 이 PNG로 마스크하고 `--tab-bg` 색 위에 곱하기로 겹쳐 색을 입힌다. 선택된 탭은 꿀색(`--honey`)이며 조금 더 높다. 순서대로 1–6번 모양을 돌려 쓴다.

- `corkboard-cork.webp` (512×512, 화면에서 320px 타일): 사건 수첩 코르크판 바탕. Higgsfield Nano Banana 2.1(1K, thinking high), 카페 배경 그림(job `354bb7cb-…`)을 화풍 참조로 한 손그림 코르크 2장 중 고른 것(job `b4aa7ed9-993b-4f17-8c5e-e42688cb7edf`, 원본 `corkboard-cork-higgsfield-original.png`). 반 칸 밀어 낸 사본과 가장자리만 섞어 이음매 없는 타일로 만들었다. 처음 뽑은 사진 같은 코르크(job `96438498-…`)는 사용자가 "너무 리얼하다"고 해 버렸다.
- `corkboard-frame.webp` (804×1093, 투명): 코르크판 나무 액자. 같은 모델, 카페 배경 그림(job `354bb7cb-…`) 화풍 참조로 손그림 나무 액자 2장 중 고른 것(job `60b9f138-bafa-4736-9dd5-53bca97a5ecd`, 원본 `corkboard-frame-higgsfield-original.png`). 마젠타 배경을 로컬에서 지우고 잘랐다. 나무 두께 네 변 약 86px → CSS `border-image` 조각 `89`, 화면 두께 18px, `stretch`. 처음 액자(job `75a1eb0e-…`, 오리 그림 참조)는 일러스트 느낌이 약하다는 피드백으로 바꿨다.

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
