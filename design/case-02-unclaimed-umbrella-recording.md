# 주인 없는 우산 — 녹음 대본

`scripts/umbrella-recording-script.js`가 게임 데이터(`index.html`의 `UMBRELLA_CASE`)에서 뽑은 목록이다. 대사를 고치면 이 파일도 다시 뽑는다. 파일 이름은 게임이 재생하는 녹음 파일이다(Higgsfield MiniMax). **녹음 필요**는 v2 쉬운 판에서 새로 생겼거나 바뀐 줄이다(그전까지 인물 줄은 브라우저 음성, 탐정 줄은 소리 없음).

- 목소리(사용자 결정): 엘라 Petra, 테스 Callan, 루비 Gracie, 핀 Dylan, 모두 감정 행복(Higgsfield 웹에서 만듦). 탐정은 소풍·도서관 사건과 같은 Grady, 감정 중립(감정 값 없음).
- 읽기용 문장이 따로 있는 줄은 **읽기**에 적었다(화면 글은 그대로).
- 같은 화자의 같은 문장은 한 번만 녹음하고 파일을 함께 쓴다(**같은 녹음**에 처음 나온 번호).

| 화자 | 줄 수 | 녹음할 문장 |
|---|---|---|
| 엘라 | 5 | 5 |
| 테스 | 6 | 6 |
| 루비 | 7 | 7 |
| 핀 | 5 | 5 |
| 탐정 | 25 | 16 |
| **합계** | **48** | **39** |

## 엘라 (5줄)

| # | 파일 | 장면 | 영어 | 해석 |
|---|---|---|---|---|
| 1 | `ella-hello.mp3` | 첫 인사 | Hello. I'm Ella. I help at the village hall. | 안녕. 난 엘라야. 마을회관 일을 돕고 있어. |
| 2 | `ella-e0.mp3` | 대답 e0 | Someone left an umbrella here. Can you help me? | 누가 우산을 여기 두고 갔어. 좀 도와줄래? |
| 3 | `ella-e1.mp3` | 대답 e1 | Three friends came here. They said they lost their umbrellas. | 친구 세 명이 우산을 잃어버렸다고 찾아왔어. |
| 4 | `ella-inspect.mp3` | 행동의 대답 | Of course. Here you go. | 물론이지. 여기 있어. |
| 5 | `ella-end3.mp3` | 결말 2 (엘라) | Wonderful! Thank you for your help, Detective. | 잘됐다! 도와줘서 고마워, 탐정. |

## 테스 (6줄)

| # | 파일 | 장면 | 영어 | 해석 |
|---|---|---|---|---|
| 1 | `tess-hello-v3.mp3` | 첫 인사 | Hi! I'm Tess. Have you seen my umbrella? | 안녕! 난 테스야. 내 우산 봤니? |
| 2 | `tess-hello3.mp3` | 첫 인사 | Maybe! I can't find mine. | 그럴지도! 내 우산을 못 찾고 있거든. |
| 3 | `tess-t1.mp3` | 대답 t1 | Mine is dark blue. It has a blue handle. | 내 거는 남색이야. 파란 손잡이가 있어. |
| 4 | `tess-t2.mp3` | 대답 t2 | Mine has gold stars. | 내 거에는 금빛 별무늬가 있어. |
| 5 | `tess-t3.mp3` | 대답 t3 | Mine is dark blue inside. | 내 거는 안쪽이 남색이야. |
| 6 | `tess-give.mp3` | 행동의 대답 | No, it's not mine. Mine is dark blue inside. | 아니, 내 거 아니야. 내 건 안쪽이 남색이야. |

## 루비 (7줄)

| # | 파일 | 장면 | 영어 | 해석 |
|---|---|---|---|---|
| 1 | `ruby-hello-v2.mp3` | 첫 인사 | Hi, I'm Ruby. Have you seen my umbrella? | 안녕, 난 루비야. 내 우산 봤니? |
| 2 | `ruby-hello2-v2.mp3` | 첫 인사 | Maybe! I don't know where I left it. | 그럴지도! 어디에 두고 왔는지 모르겠어. |
| 3 | `ruby-r1.mp3` | 대답 r1 | Mine is dark blue. It has a blue handle. | 내 거는 남색이야. 파란 손잡이가 있어. |
| 4 | `ruby-r2.mp3` | 대답 r2 | Mine has gold stars. | 내 거에는 금빛 별무늬가 있어. |
| 5 | `ruby-r3.mp3` | 대답 r3 | Mine is gold inside. | 내 거는 안쪽이 금빛이야. |
| 6 | `ruby-end1.mp3` | 행동의 대답 | Yes, it's mine! Gold stars, and it's gold inside too. | 응, 내 거야! 금빛 별에 안쪽도 금빛이야. |
| 7 | `ruby-end2h.mp3` | 결말 1 (루비) | So I left it here! Thank you, Detective. | 여기 두고 왔구나! 고마워, 탐정. |

## 핀 (5줄)

| # | 파일 | 장면 | 영어 | 해석 |
|---|---|---|---|---|
| 1 | `finn-hello-v2.mp3` | 첫 인사 | Hi! I'm Finn. Have you seen my umbrella? I lost it. | 안녕! 난 핀이야. 내 우산 봤니? 잃어버렸어. |
| 2 | `finn-hello2.mp3` | 첫 인사 | Maybe! I'm still looking for mine. | 그럴지도! 아직 내 우산을 찾고 있거든. |
| 3 | `finn-f1.mp3` | 대답 f1 | Mine is a small folding umbrella. It's dark blue. | 내 거는 작은 접이식 우산이야. 남색이야. |
| 4 | `finn-f2.mp3` | 대답 f2 | Mine has no pattern. It's plain. | 내 거는 무늬가 없어. 민무늬야. |
| 5 | `finn-give.mp3` | 행동의 대답 | No, it's not mine. Mine is a folding umbrella. | 아니, 내 거 아니야. 내 건 접이식 우산이야. |

## 탐정 (25줄)

| # | 파일 | 장면 | 영어 | 해석 |
|---|---|---|---|---|
| 1 | `detective-ella-e0.mp3` | 엘라에게 질문 e0 | Hello. How can I help? | 안녕. 무슨 일이야? |
| 2 | `detective-ella-e1.mp3` | 엘라에게 질문 e1 | Did anyone come for it? | 누가 이 우산 찾으러 왔어? |
| 3 | `detective-ella-act-inspect.mp3` | 엘라에게 행동(우산 조사) | Can I take a closer look at the umbrella? | 그 우산 좀 자세히 봐도 될까? |
| 4 | `detective-hello-found.mp3` | 테스 첫 인사 | I have an umbrella here. Is it yours? | 여기 우산이 하나 있어. 네 거야? |
| 5 | `detective-tess-t1.mp3` | 테스에게 질문 t1 | What is your umbrella like? | 네 우산은 어떻게 생겼어? |
| 6 | `detective-tess-t2.mp3` | 테스에게 질문 t2 | What pattern is on your umbrella? | 네 우산에는 어떤 무늬가 있어? |
| 7 | `detective-tess-t3.mp3` | 테스에게 질문 t3 | What color is your umbrella inside? | 네 우산 안쪽은 무슨 색이야? |
| 8 | `detective-tess-act-give.mp3` | 테스에게 행동(우산 건네기) | Is this umbrella yours? | 이 우산 네 거야? |
| 9 | `detective-hello-found.mp3` | 루비 첫 인사 | I have an umbrella here. Is it yours?<br>**같은 녹음**: 4번 | 여기 우산이 하나 있어. 네 거야? |
| 10 | `detective-ruby-r1.mp3` | 루비에게 질문 r1 | What is your umbrella like?<br>**같은 녹음**: 5번 | 네 우산은 어떻게 생겼어? |
| 11 | `detective-ruby-r2.mp3` | 루비에게 질문 r2 | What pattern is on your umbrella?<br>**같은 녹음**: 6번 | 네 우산에는 어떤 무늬가 있어? |
| 12 | `detective-ruby-r3.mp3` | 루비에게 질문 r3 | What color is your umbrella inside?<br>**같은 녹음**: 7번 | 네 우산 안쪽은 무슨 색이야? |
| 13 | `detective-ruby-act-give.mp3` | 루비에게 행동(우산 건네기) | Is this umbrella yours?<br>**같은 녹음**: 8번 | 이 우산 네 거야? |
| 14 | `detective-hello-found.mp3` | 핀 첫 인사 | I have an umbrella here. Is it yours?<br>**같은 녹음**: 4번 | 여기 우산이 하나 있어. 네 거야? |
| 15 | `detective-finn-f1.mp3` | 핀에게 질문 f1 | What is your umbrella like?<br>**같은 녹음**: 5번 | 네 우산은 어떻게 생겼어? |
| 16 | `detective-finn-f2.mp3` | 핀에게 질문 f2 | What pattern is on your umbrella?<br>**같은 녹음**: 6번 | 네 우산에는 어떤 무늬가 있어? |
| 17 | `detective-finn-act-give.mp3` | 핀에게 행동(우산 건네기) | Is this umbrella yours?<br>**같은 녹음**: 8번 | 이 우산 네 거야? |
| 18 | `detective-think-give.mp3` | 생각(조건이 맞을 때) | Let's give the umbrella back to its owner. | 우산을 주인에게 돌려주자. |
| 19 | `detective-umbrella-0.mp3` | Umbrella · Umbrella handle | This handle is blue. | 이 손잡이는 파란색이야. |
| 20 | `detective-umbrella-1.mp3` | Umbrella · Umbrella pattern | This umbrella has gold stars on dark blue fabric. | 이 우산은 남색 천에 금빛 별무늬가 있어. |
| 21 | `detective-umbrella-2.mp3` | Umbrella · Inside of the umbrella | This umbrella is gold inside. | 이 우산은 안쪽이 금빛이야. |
| 22 | `detective-item-umbrella.mp3` | 소지품 · Umbrella from Ella | The umbrella Ella gave me. | 엘라가 맡긴 우산. |
| 23 | `deduce/miss.mp3` | 추리 오답(공통) | Hmm… that doesn't fit. | 음… 그건 맞지 않아. |
| 24 | `detective-end-ruby2.mp3` | 결말 1 (루비) 시작 | Here you go. | 여기 있어. |
| 25 | `detective-end-ella3.mp3` | 결말 2 (엘라) 시작 | I gave the umbrella back to Ruby. | 루비에게 우산을 돌려줬어. |
