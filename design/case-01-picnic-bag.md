# Case 05 — 바뀐 소풍 가방 (게임 판, 2026-11-24)

교육용 L1-01 A의 **제작자용** 기획. 게임의 `PICNIC_CASE`(`?case=picnic`, 사건 목록 Case 05)와 같은 내용이다. 2026-10-30 개발 인계 뒤 점검·수정은 개발(Claude)이 사용자와 한다(`AGENTS.md` 사건 진행 순서).

- 2026-11-19에 쓴 v3 카페 판(카페 안에서 해결, 분실물 가방 3개)은 개발하지 않고 멈췄다. `design/backups/picnic-v3-cafe/`에 그대로 보관한다.
- 스토리보드 `case-01-picnic-bag.html`은 아직 v3 카페 판 그대로다. 기준은 이 문서다.

**방향(사용자 결정 2026-11-24)**
- 노라·회사 로비를 뺐다. 벤이 카페에서 로지의 가방을 잘못 가져갔다.
- 탐정이 벤의 가방을 열어 보지 않는다. 플레이어가 **로지에게 받은 가방 속 물건(망치·톱·못)**과 **벤의 직업(목수)**을 이어서 누구 가방인지 추리한다.
- 추리 보드는 없다. 가방을 **줄 사람을 플레이어가 고르는 것**이 풀이다(우산 사건의 "~에게 우산 주기"와 같은 방식). 틀린 사람에게 주면 그 사람이 자기 가방이 아니라고 말한다.

노트는 탐정이 들은 사실을 정리하는 짧은 메모다. NPC의 대답 전체를 따옴표로 옮기지 않는다.

## 사건의 진실

로지와 벤은 오늘 아침 호수 카페에 들렀다. 둘 다 겉모습이 똑같은 파란 가방을 들고 왔고, 나갈 때 서로의 가방을 들고 나왔다. 벤은 가방을 열어 보지 않고 집에 갔다. 미아와 올리도 카페에 들렀다가 정원으로 갔다. 미아의 가방도 파란색이지만 미아의 것이 맞다.

| 가방 | 겉모습 | 안에 든 것 | 주인 | 지금 있는 곳 |
|---|---|---|---|---|
| 로지가 들고 온 가방 | 파란 가방 | 망치, 톱, 못 | **벤** | 소풍 탁자 → 탐정의 소지품 |
| 벤이 가진 가방 | 파란 가방 | 빨간 도시락, 노란 물병 | **로지** | 벤의 집 |
| 미아의 가방 | 파란 가방 | 장갑, 씨앗 (꺼내서 벤치에 둠) | 미아 | 정원 |
| 올리의 가방 | 빨간 가방 | (나오지 않음) | 올리 | 정원 |

가방에는 이름표·글자가 없다. 주인은 사람의 말과 가방 속 물건으로만 알아낸다.

**추리의 길**: 로지의 가방에는 도시락과 물병이 들어 있다(로지 r2). 그런데 로지가 들고 온 가방에는 망치·톱·못이 있다(소지품 살펴보기). 카페에 온 사람은 로지·벤·미아·올리다(오리 v1). 올리의 가방은 빨갛고, 미아는 꽃을 심으려고 장갑과 씨앗을 가져왔다(미아 g1, 정원 벤치의 열린 가방). 벤은 목수이고 파란 가방을 매일 일하러 갈 때 가지고 다닌다(벤 b1). 그러니 공구가 든 가방은 벤의 것이고, 로지의 가방은 벤에게 있다. 이 결론은 플레이어가 "Ben에게 가방 주기"를 고르는 것으로 정한다.

## 학습과 등장인물

- 목표: `my/your/her`, `mine/yours`를 듣고 사람과 물건을 연결한다. 가방 속 물건과 들은 말을 대조한다.
- 열쇠 카드: 소유 표현(`ownership`).

| 인물 | 역할 | 장소 | 목소리(Higgsfield MiniMax) |
|---|---|---|---|
| 토끼 로지 Rosie Rabbit | 의뢰인 | 소풍 탁자 | Evie |
| 오리 아저씨 Mr. Duck | 카페 주인, 참고인 | 호수 카페 | Alden |
| 비버 벤 Ben Beaver | 목수, 참고인(가방이 바뀐 상대) | 벤의 집 | Benji |
| 미아와 올리 Mia & Ollie | 소풍 온 친구들, 참고인(한 사람으로 대화) | 정원 | Giselle / Emmett |
| 탐정 | 플레이어 | — | Grady |

## 장면과 해금

| # | 장면 | 하는 일 | 열리는 것 |
|---|---|---|---|
| 01 | 소풍 탁자 · 로지 | 인사 → r0 의뢰 → r1·r2·r4 | r4: 오리 아저씨(호수 카페) |
| 02 | 로지가 가방을 맡김 | 대화를 다 마치면 로지가 가방을 건넴 → 소지품에 들어가며 살펴보기(`baglook`)가 열림. `가방 열기`로 열면 망치·톱·못 | 소지품 `Blue bag from Rosie` |
| 03 | 호수 카페 · 오리 아저씨 | v2·v1 → v3 | v1: 벤·미아 이름, v3: 벤의 집·정원 |
| 04 | 벤의 집 · 벤 | 인사 → b1 | — |
| 05 | 정원 · 미아와 올리 | 인사 → g1. 벤치 위 열린 파란 가방과 장갑·씨앗, 옆의 닫힌 빨간 가방이 정원 그림에 보임. 벤치를 누르면 탐정: A blue bag is open on the bench. Gloves and seeds are next to it. | — |
| 06 | 가방 주기 (풀이) | 벤·미아 대화에 `Ben에게 가방 주기`·`Mia에게 가방 주기` 버튼(소지품에 가방이 있고 b1·g1을 들었을 때) | 맞으면 엔딩 |
| 07 | 벤과 가방 바꾸기 | Is this your bag? → 가방 건네주기 → 벤 "I took the wrong bag.", 로지의 가방을 받음 | 소지품 `Blue bag` |
| 08 | 받은 가방 확인 | 로지에게 가면(머리 위 !) 피크닉 테이블에서 살펴보기 `roselook`가 열림 → 가방 열기 → 도시락·물병 | 로지의 `Rosie에게 가방 주기` |
| 09 | 로지에게 돌려주기 | 로지 대화에서 버튼 → 가방 건네주기 → 로지 감사 | 복습 |

## 대본

### 로지 (소풍 탁자)

| 키 | 질문 | 대답 | 노트 |
|---|---|---|---|
| hello | — | Hi, I'm Rosie. Are you the detective? | — |
| r0 | Yes. How can I help you? | This isn't my bag. Can you help me find mine? | - this bag [isn't] Rosie's / - asked me to [find] her bag |
| r1 | Did your bag get mixed up with someone else's? | I'm not sure. My bag is blue, just like this one. | - Her bag is [blue]. |
| r2 | What is in your bag? | My bag has a red lunch box and a yellow bottle. | - Her bag has a [red] [lunch box] and a [yellow] [bottle]. |
| r4 | Where did you go today? | I went to the Lake Cafe before I came here. Maybe the bags got mixed up there. | - She went to the [Lake Cafe]. / - Maybe the bags got [mixed up] there. |
| give (대화 끝) | — | Please take this bag and find mine. → 탐정 I will. | — |

### 오리 아저씨 (호수 카페)

| 키 | 질문 | 대답 | 노트 |
|---|---|---|---|
| hello | — | Hello! Welcome to the Lake Cafe. What would you like? → 탐정 Hello! I'm Detective ○○. I'm looking for a blue bag. → Oh! I see. How can I help? | — |
| v2 | Did anyone leave a blue bag here? | No. Nobody left a bag here today. | - [Nobody] [left] a bag at the cafe. |
| v1 | Who came to the cafe today? | Rosie, Ben, Mia, and Ollie came today. | - Rosie, [Ben], Mia, and Ollie came to the cafe. |
| v3 | Where are they now? | They told me their plans. Ben went home. Mia and Ollie went to the garden. | - Ben went [home]. / - Mia and Ollie went to the [garden]. |

### 벤 (벤의 집)

| 키 | 질문 | 대답 | 노트 |
|---|---|---|---|
| hello | — | Hi there! What can I do for you? → 탐정 Hi, I'm Detective ○○. Are you Ben? → Yes, that's me! | — |
| b0 | You were at the Lake Cafe today, right? | Yes, I stopped there this morning. | - Ben [stopped] at the cafe this [morning]. |
| b1 | Do you have a blue bag? | Yes, I do. I'm a carpenter. I take it to work every day. | - Ben is a [carpenter]. / - Ben takes his blue bag to [work] [every day]. |

### 미아와 올리 (정원)

| 키 | 질문 | 대답 | 노트 |
|---|---|---|---|
| hello | — | 올리 Oh, hi! I'm Ollie. Nice to meet you. → 미아 I'm Mia. Want to join our picnic? → 탐정 Nice to meet you, Ollie and Mia! I'm Detective ○○. → 올리 A detective? That's cool! → 탐정 You were at the Lake Cafe today, right? → 미아 Yes. We stopped there before coming here. | — |
| g1 | Do either of you have a blue bag? | 올리 No. Mine is red. 미아 Mine is blue. I brought my gloves and seeds. We're planting flowers today. | - Ollie's bag is [red]. / - Mia's bag is [blue]. / - Mia brought her [gloves] and [seeds]. |

## 살펴보기 (확대 화면)

| 무엇 | 어디서 여나 | 열면 | 탐정의 말 |
|---|---|---|---|
| 벤이 돌려준 가방 `roselook` | 그 가방을 가지고 로지와 대화할 때(안을 볼 때까지 매번), 소지품에서 | 빨간 도시락, 노란 물병 | There is a red lunch box and a yellow bottle inside. |
| 로지가 들고 온 가방 `baglook` | 로지가 건넬 때, 소지품에서 | 망치, 톱, 못 | There is a hammer, a saw, and some nails inside. |

처음에는 닫혀 있고 `가방 열기`나 가방을 누르면 열린다. 안을 누르면 탐정이 안에 든 것을 말한다. 사진은 남기지 않는다(심문 증거가 아님).

## 가방 주기 (풀이)

- 벤과 미아의 대화에 `Ben에게 가방 주기`·`Mia에게 가방 주기` 버튼이 나온다. 조건은 소지품에 로지의 가방이 있고, 벤 b1·미아 g1을 들었을 때다. 모든 대화를 마쳐도 저절로 넘어가는 버튼은 없다.
- 탐정: Is this your bag?
  - 미아(틀림): No, it's not mine. Mine is right there, with my gloves and seeds. → 가방은 소지품에 그대로 있다. 벌점은 없다.
  - 벤(맞음): 바로 엔딩(가방 바꾸기)으로 넘어간다.
- 오리 아저씨·로지에게는 주기 버튼이 없다(파란 가방을 가진 사람이 아님).

## 엔딩

1. 벤의 대화에서 `Ben에게 가방 주기` → 탐정: Is this your bag? → 소지품에서 가방 건네주기.
2. 벤: Yes, it's mine! I took the wrong bag. 벤이 가진 가방(로지의 것)이 소지품에 들어온다.
3. 엔딩이 잠깐 멈추고 벤의 집으로 돌아온다(가방은 열리지 않고 탐정 생각도 없음). 로지 머리 위에 !가 뜬다.
4. 로지와 대화하면 피크닉 테이블에서 그 가방의 살펴보기(`roselook`)가 열린다. `가방 열기` → 안을 누르면 탐정: There is a red lunch box and a yellow bottle inside. 안을 보지 않고 〈를 누르면 피크닉 테이블로 나가고, 로지와 다시 대화하면 또 열린다. (소지품에서도 열어 볼 수 있음)
5. 〈로 로지의 대화에 돌아오면 `Rosie에게 가방 주기`(가방 안을 본 뒤) → 탐정: Rosie, I brought your bag back. → 가방 건네주기. 로지: My lunch box and bottle are here! Thank you, Detective!
6. 복습.

## 주변 물건 (음성만)

| 장소 | 물건 |
|---|---|
| 소풍 탁자 | 소풍 바구니, 식탁보, 호수 |
| 호수 카페 | 컵, 기타, 창문 |
| 벤의 집 | 선반, 통나무, 러그 |
| 정원 | 꽃, 돌길, 울타리, 벤치(열린 파란 가방과 장갑·씨앗, 탐정 관찰) |

## 자산

- 그림: 소풍 탁자·낮 카페·벤의 집·정원 배경(정원은 벤치 가방을 넣어 다시 그림 `garden-tools-higgsfield-original`, `scripts/cut-picnic-garden-tools.py`, 예전 그림은 `garden-plain`·`garden-floor-plain`), 로지(가방 든 모습 포함)·오리·벤·미아와 올리, 닫힌 파란 가방 `bag-blue`, 열린 가방 `bag-ben-open`(망치·톱·못), 로지의 가방 사진 `picnic-rosie-bag`.
- 녹음: `audio/picnic/`. 2026-11-24 새로 만든 것: 벤 b1 `ben-b1-carpenter`, 미아 `mia-g1-mia-gloves`·`mia-give-gloves`, 탐정 `detective-ben-act-give`·`detective-garden-bench`(`detective-mia-act-give`는 같은 파일을 복사).
- 쓰지 않게 된 것(지울지 사용자 결정): 노라 녹음 `nora-*`·`detective-hello-nora`·`detective-handoff1/2`·`detective-item-bag-nora`, 로비 그림·`detective-lobby-*`, 벤 가방 살펴보기 `ben-look`·`detective-ben-act-look`·`detective-item-bag-rosie-in`·`bag-rosie-open`, 미아 가방 살펴보기 `mia-sure`·`detective-mia-act-look`·`bag-blue-open*`, 예전 미아 `mia-g1-mia`·`mia-give`, 예전 `ben-b1-own`·`ben-b1`·`duck-v1-ben`·`duck-v4`.
