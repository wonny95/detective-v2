# 튜토리얼 그림

튜토리얼 7장의 그림(`tut-1.webp` … `tut-7.webp`, 900×720, 5:4)은 **실제 게임 화면을 잘라 만든 것**이다(사용자 결정). Claude가 만들었고 크레딧은 쓰지 않았다.

- 촬영: 헤드리스 Chrome에서 폰 화면 390×844 CSS px를 3배(1170×2532)로 찍는다. 게임의 미리보기 모드(`?preview=talk`·`place`·`deduce`)라 기기 기록은 바뀌지 않는다.
- 합성: 튜토리얼 종이색(`#F3ECDD`) 위에 자른 화면을 둥근 모서리·갈색 테두리 패널로 놓는다. 두 장면이면 가운데 화살표.
- **잘라 내는 기준**: 정답, 범인, 핵심 증거(시계·잼·털)가 보이지 않게 한다.
  - 1 질문하고 들어요: 질문 버튼 아래 오소리 경사 → 노트가 올라오고 대답이 나오는 중(빈칸은 비어 있음).
  - 2 빈칸을 채워요: 빈칸 세 줄과 단어 카드(채우지 않음).
  - 3 기록 완료로 확인해요: 틀리게 채우고 확인한 뒤(`다시 확인`, 틀린 칸 테두리). 남은 단어 카드는 답을 알려 주므로 잘라 냄.
  - 4 현장을 조사해요: 처음 열린 지도(Old Library 핀만) → 도서관 현장(시계·분필 윤곽선은 빠지게, 증거 수·`추리하기`·옆으로 밀기 안내는 숨기고 찍음).
  - 5 Note를 펼쳐 봐요: 인물 탭·얼굴·📌까지, 대답 줄 위에서 자름.
  - 6 추리해요: 추리 보드 첫 질문(용의자 사진은 아직 흐린 상태).
  - 7 심문해요(사용자 결정: 추리와 심문을 한 장씩): 게임의 심문은 범인이 보이므로 움직임 시안(`design/tutorial-motion.html`)의 예시 심문을 찍음. 게임의 심문 화면 구성(심문실, 서 있는 비버 벤, 말풍선, 증거 내밀기, 서랍) 그대로이고, 그림은 지어낸 주장에 램프 사진을 고른 순간의 화면 전체(진행 막대·말풍선·벤·서랍·내밀기, 양옆은 심문실 배경). `scripts/tutorial-shots/questioning.mjs` → `questioning.py`.

## 다시 만들기

화면이 바뀌면 다시 찍는다. 스크립트는 `scripts/tutorial-shots/`에 있다.

```bash
node server.js                      # 5173 (또는 PORT=5174)
"C:/Program Files/Google/Chrome/Application/chrome.exe" --headless=new --remote-debugging-port=9333 --user-data-dir=<임시 폴더> --autoplay-policy=no-user-gesture-required --mute-audio about:blank
node scripts/tutorial-shots/cdp.mjs scripts/tutorial-shots/steps.json   # shots/ 에 원본 화면
python scripts/tutorial-shots/compose.py                                 # 자르기·합성 → assets/ui/tutorial/
```

`steps.json`의 주소 포트는 띄운 서버에 맞춘다. 자르는 좌표(CSS px)는 `compose.py`에 장마다 있다.
