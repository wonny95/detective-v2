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
| 탐정 | 35 | 26 |
| **합계** | **58** | **49** |

## 엘라 (5줄)

| # | 파일 | 장면 | 영어 | 해석 |
|---|---|---|---|---|
| 1 | `ella-hello.mp3` | 첫 인사 | Hello. I'm Ella. I help at the village hall. | 안녕. 난 엘라야. 마을회관 일을 돕고 있어. |
| 2 | `ella-e0.mp3` | 대답 e0 | Someone left that umbrella here. Can you help me? | 누가 저 우산을 여기 두고 갔어. 좀 도와줄래? |
| 3 | `ella-e1.mp3` | 대답 e1 | I don't know. But Finn, Tess, and Ruby lost their umbrellas. | 몰라. 그런데 핀, 테스, 루비가 우산을 잃어버렸어. |
| 4 | `ella-inspect.mp3` | 행동의 대답 | Of course. Here you go. | 물론이지. 여기 있어. |
| 5 | `ella-end3.mp3` | 결말 2 (엘라) | Wonderful! Thank you for your help, Detective. | 잘됐다! 도와줘서 고마워, 탐정. |

## 테스 (6줄)

| # | 파일 | 장면 | 영어 | 해석 |
|---|---|---|---|---|
| 1 | `tess-hello.mp3` | 첫 인사 | Hi! Welcome to Toy Nest. I'm Tess. | 안녕! 토이 네스트에 온 걸 환영해. 난 테스야. |
| 2 | `tess-hello3.mp3` | 첫 인사 | Maybe! I can't find mine. | 그럴지도! 내 우산을 못 찾고 있거든. |
| 3 | `tess-t1.mp3` | 대답 t1 | Mine is dark blue. It has a blue handle. | 내 거는 남색이야. 파란 손잡이가 있어. |
| 4 | `tess-t2.mp3` | 대답 t2 | Mine has gold stars. | 내 거에는 금빛 별무늬가 있어. |
| 5 | `tess-t3.mp3` | 대답 t3 | Mine is dark blue inside. | 내 거는 안쪽이 남색이야. |
| 6 | `tess-give.mp3` | 행동의 대답 | No, it's not mine. Mine is dark blue inside. | 아니, 내 거 아니야. 내 건 안쪽이 남색이야. |

## 루비 (7줄)

| # | 파일 | 장면 | 영어 | 해석 |
|---|---|---|---|---|
| 1 | `ruby-hello.mp3` | 첫 인사 | Hi, I'm Ruby. Nice to meet you. | 안녕, 난 루비야. 만나서 반가워. |
| 2 | `ruby-hello2.mp3` | 첫 인사 | I can't find my umbrella. I don't know where I left it. Could it be mine? | 내 우산을 못 찾고 있어. 어디에 두고 왔는지 모르겠어. 혹시 내 거일까? |
| 3 | `ruby-r1.mp3` | 대답 r1 | Mine is dark blue. It has a blue handle. | 내 거는 남색이야. 파란 손잡이가 있어. |
| 4 | `ruby-r2.mp3` | 대답 r2 | Mine has gold stars. | 내 거에는 금빛 별무늬가 있어. |
| 5 | `ruby-r3.mp3` | 대답 r3 | Mine is gold inside. | 내 거는 안쪽이 금빛이야. |
| 6 | `ruby-end1.mp3` | 행동의 대답 | Yes, it's mine! Gold stars, and it's gold inside too. | 응, 내 거야! 금빛 별에 안쪽도 금빛이야. |
| 7 | `ruby-end2v.mp3` | 결말 1 (루비) | So I left it at the village hall! Thank you, Detective. | 회관에 두고 왔구나! 고마워, 탐정. |

## 핀 (5줄)

| # | 파일 | 장면 | 영어 | 해석 |
|---|---|---|---|---|
| 1 | `finn-hello.mp3` | 첫 인사 | Hi! I'm Finn. Can I help you? | 안녕! 난 핀이야. 무슨 일이야? |
| 2 | `finn-hello2.mp3` | 첫 인사 | Maybe! I'm still looking for mine. | 그럴지도! 아직 내 우산을 찾고 있거든. |
| 3 | `finn-f1.mp3` | 대답 f1 | Mine is a small folding umbrella. It's dark blue. | 내 거는 작은 접이식 우산이야. 남색이야. |
| 4 | `finn-f2.mp3` | 대답 f2 | Mine has no pattern. It's plain. | 내 거는 무늬가 없어. 민무늬야. |
| 5 | `finn-give.mp3` | 행동의 대답 | No, it's not mine. Mine is a folding umbrella. | 아니, 내 거 아니야. 내 건 접이식 우산이야. |

## 탐정 (35줄)

| # | 파일 | 장면 | 영어 | 해석 |
|---|---|---|---|---|
| 1 | `detective-ella-e0.mp3` | 엘라에게 질문 e0 | Hello. How can I help? | 안녕. 무슨 일이야? |
| 2 | `detective-ella-e1.mp3` | 엘라에게 질문 e1 | Whose umbrella is that? | 저건 누구 우산이야? |
| 3 | `detective-ella-act-inspect.mp3` | 엘라에게 행동(우산 조사) | Can I take a closer look at that umbrella? | 저 우산 좀 자세히 봐도 될까? |
| 4 | `detective-hello-tess.mp3` | 테스 첫 인사 | Hello. | 안녕. |
| 5 | `detective-hello-finn2.mp3` | 테스 첫 인사 | There's an umbrella at the village hall. Is it yours? | 회관에 우산이 하나 있어. 네 거야? |
| 6 | `detective-tess-t1.mp3` | 테스에게 질문 t1 | What is your umbrella like? | 네 우산은 어떻게 생겼어? |
| 7 | `detective-tess-t2.mp3` | 테스에게 질문 t2 | What pattern is on your umbrella? | 네 우산에는 어떤 무늬가 있어? |
| 8 | `detective-tess-t3.mp3` | 테스에게 질문 t3 | What color is your umbrella inside? | 네 우산 안쪽은 무슨 색이야? |
| 9 | `detective-tess-act-give.mp3` | 테스에게 행동(우산 건네기) | Is this umbrella yours? | 이 우산 네 거야? |
| 10 | `detective-hello-finn2.mp3` | 루비 첫 인사 | There's an umbrella at the village hall. Is it yours?<br>**같은 녹음**: 5번 | 회관에 우산이 하나 있어. 네 거야? |
| 11 | `detective-ruby-r1.mp3` | 루비에게 질문 r1 | What is your umbrella like?<br>**같은 녹음**: 6번 | 네 우산은 어떻게 생겼어? |
| 12 | `detective-ruby-r2.mp3` | 루비에게 질문 r2 | What pattern is on your umbrella?<br>**같은 녹음**: 7번 | 네 우산에는 어떤 무늬가 있어? |
| 13 | `detective-ruby-r3.mp3` | 루비에게 질문 r3 | What color is your umbrella inside?<br>**같은 녹음**: 8번 | 네 우산 안쪽은 무슨 색이야? |
| 14 | `detective-ruby-act-give.mp3` | 루비에게 행동(우산 건네기) | Is this umbrella yours?<br>**같은 녹음**: 9번 | 이 우산 네 거야? |
| 15 | `detective-hello-finn2.mp3` | 핀 첫 인사 | There's an umbrella at the village hall. Is it yours?<br>**같은 녹음**: 5번 | 회관에 우산이 하나 있어. 네 거야? |
| 16 | `detective-finn-f1.mp3` | 핀에게 질문 f1 | What is your umbrella like?<br>**같은 녹음**: 6번 | 네 우산은 어떻게 생겼어? |
| 17 | `detective-finn-f2.mp3` | 핀에게 질문 f2 | What pattern is on your umbrella?<br>**같은 녹음**: 7번 | 네 우산에는 어떤 무늬가 있어? |
| 18 | `detective-finn-act-give.mp3` | 핀에게 행동(우산 건네기) | Is this umbrella yours?<br>**같은 녹음**: 9번 | 이 우산 네 거야? |
| 19 | `detective-hall-0.mp3` | Village Hall · Toy bazaar banner (소품) | A toy bazaar banner. October 24. Hosted by Toy Nest.<br>**읽기**: A toy bazaar banner. October twenty-fourth. Hosted by Toy Nest. | 장난감 바자회 현수막이야. 10월 24일. 토이 네스트에서 열었네. |
| 20 | `detective-hall-1.mp3` | Village Hall · Venue change notice (소품) | A venue change notice. "The toy bazaar is indoors because of rain." | 장소 변경 안내문이야. "비가 와서 장난감 바자회를 실내에서 진행합니다." |
| 21 | `detective-hall-2.mp3` | Village Hall · Toy bazaar photo (소품) | A toy bazaar inside the village hall. October 24.<br>**읽기**: A toy bazaar inside the village hall. October twenty-fourth. | 마을회관 안에서 열린 장난감 바자회야. 10월 24일이네. |
| 22 | `detective-hall-3.mp3` | Village Hall · Clock (소품) | A clock on the wall. | 벽에 걸린 시계야. |
| 23 | `detective-hall-4.mp3` | Village Hall · Chair (소품) | An empty chair. | 빈 의자야. |
| 24 | `detective-hall-5.mp3` | Village Hall · Window (소품) | Sunlight through the window. | 창문으로 햇빛이 들어와. |
| 25 | `detective-toynest-0.mp3` | Toy Nest · Toy shelf (소품) | Toys on the shelf. | 선반 위의 장난감들이야. |
| 26 | `detective-toynest-1.mp3` | Toy Nest · Teddy bear (소품) | A teddy bear on the counter. | 계산대 위의 곰 인형이야. |
| 27 | `detective-windmill-0.mp3` | Windmill Hill · Windmill (소품) | A windmill on the hill. | 언덕 위의 풍차야. |
| 28 | `detective-windmill-1.mp3` | Windmill Hill · Pinwheel (소품) | A small pinwheel. | 작은 바람개비야. |
| 29 | `detective-umbrella-0.mp3` | Umbrella · Umbrella handle | This handle is blue. | 이 손잡이는 파란색이야. |
| 30 | `detective-umbrella-1.mp3` | Umbrella · Umbrella pattern | This umbrella has gold stars on dark blue fabric. | 이 우산은 남색 천에 금빛 별무늬가 있어. |
| 31 | `detective-umbrella-2.mp3` | Umbrella · Inside of the umbrella | This umbrella is gold inside. | 이 우산은 안쪽이 금빛이야. |
| 32 | `detective-item-umbrella.mp3` | 소지품 · Umbrella from Ella | The umbrella Ella gave me. | 엘라가 맡긴 우산. |
| 33 | `deduce/miss.mp3` | 추리 오답(공통) | Hmm… that doesn't fit. | 음… 그건 맞지 않아. |
| 34 | `detective-end-ruby2.mp3` | 결말 1 (루비) 시작 | Here you go. | 여기 있어. |
| 35 | `detective-end-ella3.mp3` | 결말 2 (엘라) 시작 | I gave the umbrella back to Ruby. | 루비에게 우산을 돌려줬어. |
