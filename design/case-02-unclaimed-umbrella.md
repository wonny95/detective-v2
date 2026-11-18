# 주인 없는 우산 — L1-01 B 상세 기획

**1차 기획 완료 · 2026-11-02 사용자 결정으로 Claude Code에 개발 인계 · 2026-11-03 개발 점검 뒤 사용자와 2차 수정 · 2026-11-18 v2 쉬운 판(아래).** v1에서는 교육 순서 Case 02, v2에서는 Case 01의 사건이다. 현재 앱의 Case 02 도서관과 번호를 혼동하지 않는다. 사건 식별 이름 제안은 `unclaimed-umbrella`이며 실제 앱 표시 번호·선택 주소는 개발에서 정한다. [장면별 기획 화면](case-02-unclaimed-umbrella.html)을 함께 본다.

**v2 쉬운 판 — 2026-11-18 사용자 결정 (아래 1–9절보다 우선)**

피드백: 다섯 사건 모두 너무 길고, 첫 사건부터 난도가 높다. v2에서는 **한 사건에 풀이 방식 하나**만 쓴다. 우산 사건은 **Case 01**(맨 앞)이 되고 풀이 방식은 **듣고 비교해서 맞는 사람에게 우산을 건네주기**다. 아래 1–9절은 v1 기록으로 남기며, 이 절과 다르면 이 절을 따른다.

- **흐름**: 의뢰(엘라 e0) → 우산 확대 조사(접기·펴기, 손잡이·겉무늬·안감 사진 3장, 조사하면 우산이 소지품에 들어옴) → 엘라 e1로 우산을 잃어버린 세 사람을 알게 됨 → 핀·테스·루비에게 각자 우산 특징 듣기 → 아무에게나 "Is this umbrella yours?"(행동 선택지)로 우산 건네기 → 루비에게 반환 → 엘라에게 보고 → 복습.
- **뺀 것**: 현수막·장소 변경 안내문 촬영과 두 장 해금(날씨 단서, 탐정 생각 together1), 테스 t0·t4·t5(소개 단계), 엘라 e2, 테스의 이름 숨김, 추리 보드 5문항(맞장구·힌트 포함), 결말 1차례(엘라가 주인을 묻고 우산을 줌), 테스의 결말 질문. 회관의 현수막·안내문·게시판 사진은 그림에 남기고 **살펴보기**(관찰 한 줄, 사진 없음)로만 둔다.
- **엘라 e1 대답(바뀜)**: I don't know. But Finn, Tess, and Ruby lost their umbrellas. / 몰라. 그런데 핀, 테스, 루비가 우산을 잃어버렸어. 노트: Finn, Tess, and Ruby [lost] their umbrellas(사용자 결정: "Ella does not know the owner"·e0의 "Ella asked for my help"처럼 단서가 아닌 줄은 노트에 적지 않음). 바르게 적으면 핀·테스·루비와 토이 네스트·풍차 언덕이 열린다.
- **첫인사(바뀜)**: 세 사람 모두 탐정이 "There's an umbrella at the village hall. Is it yours?"(기존 녹음)로 온 이유를 말한다. 테스: Hello. → Hi! Welcome to Toy Nest. I'm Tess. → (탐정) → **Maybe! I can't find mine.** / 그럴지도! 내 우산을 못 찾고 있거든. 루비·핀은 기존 대답 그대로. "Tess said…"로 시작하던 탐정 줄은 뺐다.
- **질문**: 엘라 e0·e1, 핀 f1·f2, 테스 t1·t2·t3, 루비 r1·r2·r3 — 받아쓰기 10개·빈칸 21칸(대사·빈칸은 5절 그대로, 엘라 노트는 위처럼 줄이고 핀 f2의 겹치는 [plain] 줄은 뺌).
- **우산 건네기(풀이)**: 세 사람의 특징 질문을 모두 적고 우산을 가지고 있으면 세 사람에게 행동 "Is this umbrella yours? / 이 우산 네 거야?"가 나온다(받아쓰지 않음, 몇 번이고 고를 수 있음). 탐정은 결론을 말하지 않고 인물이 답한다.
  - 핀: No, it's not mine. Mine is plain. / 아니, 내 거 아니야. 내 건 민무늬야.
  - 테스: No, it's not mine. Mine is dark blue inside. / 아니, 내 거 아니야. 내 건 안쪽이 남색이야.
  - 루비: Yes, it's mine! Gold stars, and it's gold inside too. (기존 녹음) → 결말 시작.
- **결말**: (토이 네스트) 탐정 Here you go. → `우산 건네주기` → 루비 **So I left it at the village hall! Thank you, Detective.** / 회관에 두고 왔구나! 고마워, 탐정. → 생각 "엘라에게 알려 주자." · `Village Hall로 가기` → 탐정 I gave the umbrella back to Ruby. → 엘라 Wonderful! Thank you for your help, Detective. → 복습.
- **우산 건네받기(2026-11-18 사용자 요청)**: 엘라의 "Of course. Here you go."와 함께 엘라가 접힌 우산을 양손에 들고 내미는 그림(`ella-give.png`)으로 바뀌고, 엘라 손 위의 우산을 눌러야 소지품에 들어온다(그때까지 질문은 숨음). 누르면 원래 모습으로 돌아오고 우산 확대 조사가 열린다. 회관 우산꽂이의 우산은 엘라가 들고 있는 동안 비어 보인다.
- **핀의 우산은 접이식(2026-11-18 사용자 결정: 세 우산이 다 비슷함)**: f1 대답 **Mine is a small folding umbrella. It's dark blue.** / 내 거는 작은 접이식 우산이야. 남색이야. 노트: Finn's umbrella: a small [folding] umbrella · [dark blue]. 건네기 거절 **No, it's not mine. Mine is a folding umbrella.** / 아니, 내 거 아니야. 내 건 접이식 우산이야. f2(무늬 없음)는 그대로. 테스·루비는 그대로라 안감 색으로 가르는 단서는 유지된다.
- **건네기 알림과 버튼(2026-11-18 사용자 요청)**: 세 사람의 특징 질문을 모두 적고 우산을 가지고 있으면 탐정 생각 **Let's give the umbrella back to its owner.** / 우산을 주인에게 돌려주자. (어디로 갈지만 말하고 주인은 말하지 않음). 세 사람에게 다시 말을 걸면 질문 대신 초록 버튼 **Finn에게 우산 주기 · Tess에게 우산 주기 · Ruby에게 우산 주기**가 나오고, 누르면 탐정이 "Is this umbrella yours?"라고 묻는다(그 뒤는 위와 같음). 탐정 생각 녹음(`detective-think-give.mp3`)은 아직 없음.
- **새 녹음 5줄**(감정 happy, Higgsfield 웹): ella-e1, tess-hello3, tess-give, finn-give, ruby-end2v. 목록은 `case-02-unclaimed-umbrella-recording.md`의 **녹음 필요**. 탐정의 "Is this umbrella yours?"는 기존 녹음(`detective-end-ruby1-yours.mp3`)을 복사해 쓴다.
- **튜토리얼**: 소풍 그림 그대로 둔다(사용자 결정: 튜토리얼 팝업은 나중에 다시 정함).
- **장소 한 곳 — 마을회관(2026-11-18 사용자 결정: 장소가 너무 많음)**: 우산을 잃어버린 세 친구가 회관에 찾아와 있다. 토이 네스트·풍차 언덕은 사건에서 뺐다(그림 파일은 남김). 위 항목과 다르면 이 항목을 따른다.
  - **엘라 e1**: 탐정 **Did anyone come for it?** / 누가 이 우산 찾으러 왔어? → 엘라 **Three friends came here. They said they lost their umbrellas.** / 친구 세 명이 우산을 잃어버렸다고 찾아왔어. 노트: three friends [lost] their umbrellas. 엘라는 세 사람의 이름을 말하지 않는다(사용자 결정).
  - **이름**: 세 친구는 각자 인사하기 전까지 Frog · Tortoise · Cat으로 보이고(발견 알림도 같음), 첫 인사에서 이름을 말하면 이름으로 바뀐다.
  - **첫 인사**: 탐정 **I have an umbrella here. Is it yours?** / 여기 우산이 하나 있어. 네 거야?(세 사람 공통) → 대답은 그대로(Maybe! …). 테스 인사는 **Hi! I'm Tess.** / 안녕! 난 테스야.(기존 녹음에서 Welcome to Toy Nest를 잘라 씀)
  - **배치**: 회관 그림 안에 왼쪽부터 테스·핀·루비·엘라. 입구 우산꽂이는 가리지 않는다.
  - **결말**: 루비 **So I left it here! Thank you, Detective.** / 여기 두고 왔구나! 고마워, 탐정. → 이동 없이 `다음` → 엘라에게 보고(대사 그대로).
  - **회관 소품**: 바자회 현수막 하나만 살펴볼 수 있다(장소 변경 안내문·바자회 사진·시계·의자·창문은 그림으로만 남음).
  - **새 녹음 4줄**: ella-e1, ruby-end2h, detective-ella-e1, detective-hello-found. 녹음 전까지 엘라·루비 줄은 브라우저 음성, 탐정 줄은 소리 없음.
- **이번 사건의 열쇠 — 한 장(2026-11-18 사용자 결정)**: v2 대사에서 Whose…?는 탐정의 e1 질문 한 번뿐이고, 실제로 계속 들리는 표현은 세 친구의 **Mine is… / Mine has…**와 **Is it yours? / Is this umbrella yours?**, **No, it's not mine. / Yes, it's mine!**이다. 그래서 열쇠(예습)를 세 장(Whose is this? · Is this yours? · my/mine)에서 **mine / yours 한 장**으로 줄였다. 예문: This pencil is mine. / 이 연필은 내 거야. · Is this ruler yours? / 이 자 네 거야? · This book is not mine. / 이 책은 내 거 아니야.(기존 녹음 재사용) 복습의 핵심 문법도 이 한 장이며, 사건 대사 예문은 Mine is dark blue.가 붙는다. Whose…?는 e1 질문으로만 들리고 열쇠·핵심 문법에서 뺀다. 2절·10절의 열쇠 설명은 v1 기록이다.

**2차 수정 요약 — 2026-11-03 사용자 결정**

- 바람개비 만들기 행사(재료 바구니·설명서·기념사진)를 뺐다. 행사는 장난감 바자회 하나다. 헷갈리게 하는 역할은 겉모습이 비슷한 세 후보가 맡는다.
- 엘라에게 “Whose umbrella is that?” 질문을 더하고, 우산은 회관 입구 우산꽂이에 둔다(멀리 있을 때 that, 조사로 건네받으면 this).
- 사건의 열쇠 표현 Whose…? · Is this/that … yours? · that이 대사에서 자주 들리도록 엘라 질문, 우산 조사 나레이션, 추리 질문, 결말을 고쳤다(2절 표). that은 우산이 실제로 보이는 장면에서만 쓴다.
- 핀에게도 테스·루비와 같은 무늬 질문을 한다.
- 테스가 바자회 날 우산을 가져왔는지는 인사말이 아니라 첫 질문 t0으로 묻고 노트에 적는다(사용자 결정). 인사말은 다른 인물처럼 인사 → 온 이유 → 짧은 반응으로 끝난다.
- 대사 다듬기: 테스의 가게 인사, 루비에게 하는 “with her”, 루비의 “I don't know where I left it.”, 추리 Q2(손잡이)를 고쳤다.
- 결말을 다듬었다: 엘라가 주인을 묻고 → 우산을 받아 → 토이 네스트에서 테스가 묻고 루비가 확인 → 엘라에게 보고.
- 한국어 해석은 모두 반말이다(소풍 사건과 같은 규칙: 숲속 이웃끼리의 그림책 말투, 영어에 없는 높임 차이를 해석에 만들지 않음).
- 엘라의 “Hello. How can I help?”는 자동으로 넘어가는 인사말이 아니라 인사 뒤 혼자 나오는 첫 질문 e0이다. 엘라의 의뢰가 그 대답이고 노트에 받아 적는다. e1·e2·조사 선택지는 e0 뒤에 나온다(2026-11-04 사용자 결정).

노트는 탐정이 들은 사실을 정리하는 짧은 메모다. NPC의 대답 전체를 따옴표로 옮기지 않는다. 빈칸의 ID·정답·순서는 유지하며, 대명사·장소 표현의 원형이 빈칸인 경우에만 화자를 명시하고 해당 표현을 짧게 인용한다. 실제 대답과 음성은 지문 보기에서 그대로 확인한다.

## 1. 사건의 뼈대와 진실 — 제작자용

- **의뢰인**: 마을회관 일을 돕는 사슴 엘라. 일주일째 아무도 찾아가지 않는 비싼 우산을 보관하다가 주인을 찾아 달라고 부탁한다. 엘라는 행사와 우산의 연결·행사 때 날씨·후보 이름·행선지를 알려 주지 않는다(사용자 결정).
- **의문**: 일주일째 회관에 남아 있는 비싼 우산 한 자루는 누구 것인가? 바자회를 연 가게의 테스에게 묻고, 소개받은 행사 참석자 루비와 우산을 찾는 핀의 설명까지 대조한다.
- **단서**: 엘라에게 우산을 잠시 건네받아 손잡이·겉무늬·안감 부분 사진 3장을 찍는다. 회관 바닥의 장난감 바자회 현수막과 장소 변경 안내문을 촬영해 바자회 날 비가 와서 행사를 회관 안으로 옮겼음을 알고, 바자회를 연 토이 네스트를 발견한다. 게시판의 실내 바자회 사진은 선택 관찰·촬영 대상이다. 테스 t4 진술을 기록하면 함께 행사에 참여한 루비를, t5 진술을 기록하면 우산을 찾는 핀과 풍차 언덕을 알게 된다. 펼쳐 확인한 금빛 안감으로 루비와 테스를 구별한다.
- **해결**: 루비·테스의 겉모습은 같다. 루비는 안쪽도 금빛이라고, 테스는 안쪽이 남색이라고 설명한다. 실물의 금빛 안감과 일치하는 루비가 주인이다. 핀은 무늬가 없어 먼저 제외한다. 추리 뒤 엘라에게 주인을 알리고 우산을 받아 루비에게 반환한 다음 의뢰인에게 보고한다.

모두 남색 겉감과 파란 손잡이를 말한다. 루비와 테스는 금빛 별무늬까지 같고 안쪽 색만 다르다. 별무늬는 접힌 상태에서도 보이며, 안감 색은 우산을 펼쳐야 확인한다. 누구도 탐정을 만나기 전에 남은 우산을 자기 것이라고 주장하지 않는다. 탐문 중 우산이나 정답 사진을 먼저 보여 주어 따라 말하게 하지 않는다. 조사할 때 잠시 건네받지만 소지품에는 등록하지 않고, 후보를 찾아갈 때는 엘라가 회관 우산꽂이에 보관한다.

### 바자회와 일주일의 시간 관계

**날짜 초안 — 게임 속 시간:** 2026년 10월 24일(토) 장난감 바자회·비, 10월 31일(토) 탐정 조사·맑음.

- **사용자 결정**: 장난감 바자회 뒤 우산을 일주일 내내 찾아가지 않아 엘라가 의뢰했다. 우산은 비싼 물건이다. 구체적인 가격·브랜드는 정하지 않는다.
- **사용자 결정 — 엘라가 가게에 묻지 않은 이유(제작자용 배경)**: 바자회에는 참여한 동물이 많아 엘라는 누구에게 물어야 할지 몰랐다. 대사로는 넣지 않는다(엘라가 행사와 우산을 연결하지 않는다는 결정과 맞춤).
- 2차 수정에서 바람개비 만들기 행사는 뺐다(사용자 결정). 회관의 행사 단서는 장난감 바자회 하나다.
- 장난감 바자회 현수막에는 행사명·날짜와 주관 가게 명칭 Toy Nest만 적혀 있다. 개인 이름은 없다. 토이 네스트에 찾아가 서로 인사를 나눈 뒤 테스의 자기소개를 듣고 이름을 알게 된다. 핀과 연락 장소 Windmill Hill은 테스 t5의 진술을 바르게 기록한 뒤 알게 된다. 루비는 테스 t4의 진술을 바르게 기록했을 때 처음 알게 된다.
- **날씨 단서 — 사용자 결정:** 장소 변경 안내문은 10월 24일 장난감 바자회를 가리킨다. 현수막과 같은 날짜, Courtyard → Village Hall(마당 → 마을회관 안), “The toy bazaar is indoors because of rain.”(비가 와서 장난감 바자회를 실내에서 진행합니다.)가 보인다. 날씨를 엘라에게 묻지 않으며 오늘 햇빛·물웅덩이를 과거 날씨의 근거로 쓰지 않는다.
- 우산이 비싼 물건이라는 설정은 제작자용 배경으로만 두고, 엘라가 가격이나 가치에 관해 말하는 대사는 넣지 않는다. 비싼 물건이라는 이유로 특정 후보를 의심하거나 사진에 가격·주인 표식을 넣지 않는다.

| 대상 | 겉감·손잡이 | 겉무늬 | 안쪽 | 판단 |
|---|---|---|---|---|
| 실제 우산 | 남색·파란색 | 금빛 별 | 금빛 | 펼쳐서 안감 확인 |
| 루비의 설명 | 남색·파란색 | 금빛 별 | 금빛 | 모든 특징 일치 |
| 테스의 설명 | 남색·파란색 | 금빛 별 | 남색 | 겉은 같고 안쪽이 다름 |
| 핀의 설명 | 남색·파란색 | 무늬 없음 | 미확인 | 무늬 불일치 |

**닫힌 우산의 정보만으로는 루비·테스 두 명이 남는다. 펼쳐서 얻는 금빛 안감 사진과 두 사람의 inside 진술을 함께 사용해야 주인이 한 명으로 좁혀진다.** 금빛은 색 표현이며 실제 금 소재나 브랜드로 정답을 알려 주지 않는다.

## 2. 학습 목표와 이번 사건의 열쇠

L1-01 A의 소유 표현을 우산이라는 다른 상황에 적용한다. 주인이 한 말을 듣고 mine이 누구의 우산을 가리키는지 이해하고, 특징 하나와 전체 일치를 구분한다. 신규 초점은 Whose…?와 this/that, 재사용 표현은 my/your·mine/yours·his/her이다. 각 소유 대명사의 뜻을 맞혔다고 추리를 자동으로 정답 처리하지 않는다.

| 열쇠 묶음 | 뜻·맥락 | 사건 밖 예문 |
|---|---|---|
| Whose + 물건 + is this/that? | 누구의 물건인지 묻는다. this는 가까이 가리키는 것, that은 멀리 가리키는 것. 사진·실물을 가리키는 대사 맥락을 분명히 한다. | Whose book is this? / 이 책은 누구 거야?<br>Whose hat is that? / 저 모자는 누구 거야?<br>Whose pencil is this? / 이 연필은 누구 거야? |
| Is this/that … yours? | 물건을 가리키며 듣는 사람의 것인지 확인한다. | Is this ruler yours? / 이 자 네 거야?<br>Is that coat yours? / 저 외투 네 거야?<br>Is this cup yours? / 이 컵 네 거야? |
| my + 물건 / mine | A에서 익힌 소유 표현을 새 물건에 적용한다. mine은 물건 이름 없이 쓴다. | My notebook is green. / 내 공책은 초록색이야.<br>This toy is mine. / 이 장난감은 내 거야.<br>That scarf is not mine. / 저 목도리는 내 거 아니야. |

예습 카드는 이 세 묶음이다. 실제 게임의 예문 해석은 버튼을 눌러야 보인다. hers·이름 뒤 소유격은 결말·추리의 고정 설명으로 지원하고 별도 새 받아쓰기 목표로 늘리지 않는다. 후보 진술의 노트는 발화자를 바꾸지 않는 직접 인용이다. **빈칸은 대답에서 실제로 들리는 말만 사용한다.**

### 열쇠 표현이 들리는 대사 — 사용자 결정

**사건의 열쇠 표현은 사건 대사에서 실제로 들리게 한다.** my/mine은 후보의 대답마다 이미 충분히 나오므로, 이번 사건에 새로 나오는 Whose…?·Is this/that … yours?·that을 늘렸다. that은 우산이 실제로 멀리 보이는 장면(회관 우산꽂이, 결말에서 탐정이 펼쳐 든 우산)에서만 쓰고, 손에 든 우산은 this로 가리킨다. 눈앞에 없는 우산을 that으로 묻지 않는다(사용자 지적: 테스 인사에서 부자연스러움). 의뢰인에게는 “네 거야?”라고 묻지 않는다.

| 표현 | 대사 | 화자 · 장면 |
|---|---|---|
| Whose…? | Whose umbrella is that? | 탐정 → 엘라 · e1 질문 |
| | Whose umbrella is this? | 탐정 · 추리 Q5 |
| | So, whose umbrella is that? | 엘라 · 결말 보고 |
| | Oh! Whose umbrella is that? Is it mine? | 테스 · 결말 반환 |
| Is this/that … yours? (…'s?) | Is this umbrella Finn's? / Is this umbrella Tess's? | 탐정 · 추리 Q3·Q4 |
| | Is this umbrella yours? | 탐정 → 루비 · 결말 반환 |
| | Is it yours? | 탐정 → 핀 · 첫인사 (yours) |
| that | Someone left that umbrella here. / Can I take a closer look at that umbrella? / That umbrella is Ruby's. | 엘라 의뢰 · 조사 질문 · 결말 보고 |
| this | This handle is blue. / This umbrella has gold stars… / This umbrella is gold inside. / This one is gold inside. | 우산 조사 나레이션 · 추리 · 결말 |
| my / mine (재사용) | Mine is… / Mine has… (후보 대답 8개), I can't find my umbrella. Could it be mine?, I often lend mine to friends., I'm still looking for mine., Yes, it's mine! | 핀·테스·루비 |

주목표는 소유자와 물건의 특징을 연결하는 것이다. 날씨는 탐문 방향을 잡는 맥락이며 because of·brought를 새 받아쓰기·문법 숙달 목표로 추가하지 않는다. 실제로 소유 표현을 이해했는지와 음성 난도는 학생 플레이 검증이 필요하다.

## 3. 인물·장소와 공개 순서

**가게 이름 — 사용자 결정:** Toy Nest / 토이 네스트. 동물 마을의 장난감가게이며, nest는 둥지라는 뜻이다. 현수막·간판·지도·장소 목록·대사에서 같은 이름을 쓴다.

**사용자 결정:** 장소도 소풍과 겹치지 않게 새로 구성한다. 회관·토이 네스트·풍차 언덕을 사용하며, 소풍 탁자·호수 카페·벤의 집·정원·회사 로비는 이 사건의 방문 장소로 쓰지 않는다. 장소를 재활용하지 않고 공통 엔진·화면만 그대로 사용한다.

**사용자 결정:** 소풍 사건과 혼동하지 않도록 등장인물 네 명을 모두 새 동물 친구로 구성한다. 아래 이름·종은 그 결정에 따른 기획 제안이며, 소풍 사건의 인물·대본은 바꾸지 않는다. 탐정이 다람쥐이므로 이 사건의 새 NPC에는 다람쥐를 쓰지 않는다(사용자 지적 반영).

| 인물 | 장소 | 제작자용 역할 |
|---|---|---|
| Ella Deer / 사슴 엘라 | 마을회관 | 의뢰인 · 일주일째 남은 비싼 우산을 보관한 사슴 |
| Finn Frog / 개구리 핀 | 풍차 언덕 | 개구리 · 테스가 소개한 우산 분실자 · 겉무늬가 다른 후보 |
| Tess Tortoise / 거북 테스 | 토이 네스트 | 거북 · 바자회를 연 가게의 담당자 · 겉은 같고 안감이 다른 후보 |
| Ruby Cat / 고양이 루비 | 토이 네스트 | 고양이 · 토이 네스트 직원이자 바자회 참석자 · 겉과 안쪽이 모두 일치하는 후보 |

엘라는 차분하고 친절한 회관 도우미, 루비는 산책을 좋아하는 고양이, 핀은 짧고 명랑하게 말하는 개구리, 테스는 차분하게 자기 물건을 설명하는 거북으로 잡는다. 이 성격은 대사를 읽는 느낌을 위한 참고이며 정답·거짓말의 단서가 아니다. 동물의 외형·색·성격을 우산 특징과 연결하지 않는다.

### 세 친구와 우산의 사연

- **핀 — 사용자 결정**: 핀도 자기 우산을 잃어버렸다. 테스에게 우산을 잃어버린 친구가 있는지 물으면 핀과 풍차 언덕을 소개한다. 탐정은 t5 진술을 기록한 뒤 찾아간다. 핀은 자신의 우산일 수도 있다고 생각해 특징을 설명한다. 분실 날짜·장소는 미정이다. 결말에서 핀의 우산은 찾지 않는다(사용자 결정: 그대로 둠).
- **테스 — 사용자 결정**: 바자회를 연 가게의 담당자. 가게 인사와 자기소개 뒤 탐정의 방문 목적을 듣고 그날 바자회에서 일했다고 답한다. 첫 질문 t0에서 바자회 날 우산을 가져왔지만 친구들에게 자주 빌려줘서 지금 어디 있는지 잘 모른다고 답한다. 다른 행사 참석자를 묻는 질문에는 같은 가게 직원 루비도 함께 참여했으니 물어보라고 소개한다. 우산을 잃어버린 친구를 묻는 별도 질문에는 핀과 풍차 언덕을 알려 준다. 루비의 우산 색·무늬·안감이나 회관 우산의 주인은 말하지 않는다. 테스의 우산이 지금 어디 있는지는 밝히지 않는다(사용자 결정: 그대로 둠).
- **루비 — 사용자 결정**: 토이 네스트 직원이며 바자회에 우산을 가져갔다. 테스의 진술을 기록한 뒤 가게에서 만난다. 자기 우산을 잃어버린 것은 알지만 어디에 두고 왔는지는 모른다. 탐정의 방문 목적을 듣고 “내 우산을 못 찾고 있어. 혹시 내 거일까?”라고 반응한다. 특징은 기억대로 답하며 반환 때 실물을 보고 자기 우산임을 확인하고, 바자회에 두고 왔다는 것을 그때 알게 된다. 집에 확인하러 가는 과정은 넣지 않는다.
- 세 사연은 첫인사에서 탐정이 조사 목적을 설명한 뒤 자연스럽게 나온다. 각자의 분실 경험·사용 습관·기억을 말하되, 행사 날의 날씨·현재 우산 위치·발견 우산의 주인을 확정하지 않는다. 테스의 t0 대답은 우산을 자주 빌려준다는 습관일 뿐, 회관 우산을 누구에게 빌려줬다는 확인 진술이 아니다. 루비와 핀도 회관의 우산이 자기 것일 수 있다고 추측할 뿐, 특징을 비교하기 전에는 소유를 확정하지 않는다.

| 장소 | 조사 내용 | 필요한 자산 |
|---|---|---|
| 마을회관 | 엘라 의뢰·우산 확대 조사·바자회 현수막·장소 변경 안내·게시판·최종 보고 | 입구 우산꽂이에 꽂힌 접힌 우산(현장에서 멀리 보임). 조사 때는 별도 손 그래픽 없이 우산만 크게 보여 줌 |
| 토이 네스트 | 테스·루비를 각각 탐문. 결말에서 테스가 묻고 루비에게 반환 | 장난감 진열대·계산대가 있는 새 가게 배경. 서로 별개의 대화 상대 |
| 풍차 언덕 | 핀 탐문 | 언덕과 풍차가 보이는 새 장소 그림. 다른 우산·소유자 표식은 배치하지 않음 |

첫 방문에는 회관과 엘라만 안다. 현수막과 장소 변경 안내문을 모두 촬영 → 같은 날짜의 바자회가 비 때문에 실내로 옮겨졌음을 연결 → 토이 네스트만 방문 대상으로 발견. 가게에 있는 이름 모르는 거북에게 말을 걸어 서로 인사하고 자기소개를 들은 뒤 테스의 이름을 알게 된다. 테스 t5 진술의 노트 채점 통과 → 핀·풍차 언덕 발견. 테스 t4 진술의 노트 채점 통과 → 루비 발견(이미 열린 토이 네스트에 새 대화 상대 추가). 루비는 그전까지 대화 대상으로 표시하지 않는다. 핀과 루비는 각각 테스의 소개를 기록한 뒤에 만나며, 두 사람의 방문 순서는 자유다. t4·t5의 선택 순서도 자유다. 나머지 사진은 인물·장소를 해금하지 않는다. 세 명이 전체 방문객이라는 뜻은 아니다. 발견 알림은 이름만 보여 주며 자동 이동하지 않는다.

## 4. 첫인사와 의뢰 대사

아래는 순서대로 주고받는 대사다. 이를 NPC 한 줄로 요약하거나 합치지 않는다. 탐정의 별도 자기소개에 플레이어 이름을 넣을 필요는 없다. 제작자용 문서에만 한영을 함께 적고 실제 플레이의 번역은 해석 버튼 뒤에 둔다. 해석은 모두 반말이다.

### 엘라 · 마을회관

| 화자 | 영어 | 한국어 |
|---|---|---|
| 엘라 | Hello. I'm Ella. I help at the village hall. | 안녕. 난 엘라야. 마을회관 일을 돕고 있어. |

인사 뒤에는 선택지가 하나만 나온다(사용자 결정): 탐정의 “Hello. How can I help?”(ella:e0). 엘라의 “Someone left that umbrella here. Can you help me?”가 그 대답이고 노트에 받아 적는다(5절). 엘라는 입구의 우산꽂이를 가리킨다. 우산은 현장에서 멀리 보인다(that).

### 테스 · 토이 네스트

테스는 제작자용 화자 이름이다. 실제 플레이에서는 자기소개를 듣기 전 이름표·인물 목록·발견 알림에 이름을 노출하지 않는다. 가게에 있는 거북에게 이름 없이 말을 걸 수 있고, 인사를 나눈 뒤 “I'm Tess”를 들으면 이름을 표시한다. 별도의 받아쓰기는 추가하지 않는다(사용자 결정).

| 화자 | 영어 | 한국어 |
|---|---|---|
| 탐정 | Hello. | 안녕. |
| 테스 | Hi! Welcome to Toy Nest. I'm Tess. | 안녕! 토이 네스트에 온 걸 환영해. 난 테스야. |
| 탐정 | I saw Toy Nest on the bazaar banner. I'm looking for the owner of an umbrella at the village hall. | 바자회 현수막에서 토이 네스트를 봤어. 회관에 있는 우산의 주인을 찾고 있어. |
| 테스 | Oh, the toy bazaar! I worked there that day. | 아, 장난감 바자회! 그날 내가 거기서 일했어. |

인사말은 다른 인물처럼 인사 → 탐정이 온 이유 → 짧은 반응으로 끝난다. 테스가 그날 우산을 가져왔는지는 첫 질문 t0으로 묻고 노트에 적는다(사용자 결정: 조사 정보는 인사말이 아니라 질문으로). 이후 질문 선택지에서 우산 특징과 다른 참석자를 확인한다.

### 핀 · 풍차 언덕

| 화자 | 영어 | 한국어 |
|---|---|---|
| 핀 | Hi! I'm Finn. Can I help you? | 안녕! 난 핀이야. 무슨 일이야? |
| 탐정 | Tess said you were looking for your umbrella. | 테스가 네가 우산을 찾고 있다고 했어. |
| 탐정 | There's an umbrella at the village hall. Is it yours? | 회관에 우산이 하나 있어. 네 거야? |
| 핀 | Maybe! I'm still looking for mine. | 그럴지도! 아직 내 우산을 찾고 있거든. |

### 루비 · 토이 네스트

| 화자 | 영어 | 한국어 |
|---|---|---|
| 루비 | Hi, I'm Ruby. Nice to meet you. | 안녕, 난 루비야. 만나서 반가워. |
| 탐정 | Tess said you were at the bazaar with him. I'm looking for the owner of an umbrella at the village hall. | 테스가 너도 바자회에 같이 있었다고 했어. 회관에 있는 우산의 주인을 찾고 있어. |
| 루비 | I can't find my umbrella. I don't know where I left it. Could it be mine? | 내 우산을 못 찾고 있어. 어디에 두고 왔는지 모르겠어. 혹시 내 거일까? |

루비가 먼저 자기 것일 수 있다고 말하므로 탐정은 따로 묻지 않는다. “I don't know where I left it.”은 결말의 “So I left it at the bazaar!”로 이어진다.

### 엘라 대화 뒤 · 질문 선택으로 우산 조사

| 화자 | 영어 | 한국어 |
|---|---|---|
| 탐정 | Can I take a closer look at that umbrella? | 저 우산 좀 자세히 봐도 될까? |
| 엘라 | Of course. Here you go. | 물론이지. 여기 있어. |

사용자 결정: “Can I take a closer look at that umbrella?”는 엘라의 질문 목록에 표시하는 선택지(ella:inspect)다. 첫 질문 e0 뒤 e1·e2 질문과 함께 표시하며 선택 순서는 자유다. 선택하면 질문 음성과 엘라의 “Of course. Here you go.”를 듣고, 엘라가 우산꽂이에서 우산을 가져와 건넨 뒤 우산 확대 조사를 시작한다. 자동 전환 대화로 재생하지 않는다. 이 선택지는 받아쓰기·단어 카드·채점 없이 조사를 여는 질문이다. 우산만 화면 가운데 크게 나타난다. 손이나 손에 든 인물 그래픽은 필요 없다. 접기·펴기를 자유롭게 바꾸며 부분 촬영한다. 이때 소지품에는 등록하지 않는다. 조사를 마치면 사진은 증거 노트에 남고 우산은 다시 우산꽂이에 꽂혀 엘라가 보관한다.

우산 확대 화면은 접힌 상태·펼친 상태 모두 가운데에 고정하며 좌우로 밀리지 않는다. 드래그를 끝내도 조사 화면이 닫히거나 물건을 누른 것으로 처리하지 않는다. 겉무늬 사진은 아래쪽 별무늬가 잘리지 않도록 촬영 시점을 조금 낮춘다. 손잡이·안감 사진은 같은 구도를 유지한다.

**우산 일러스트 — 사용자 확정 (2026-10-30)**

![접힌 우산과 펼친 우산 한 장: 남색 겉감·금빛 별·파란 손잡이·금빛 안감](https://d8j0ntlcm91z4.cloudfront.net/user_3GQcP8akZKK6UYHE3DZOw7Yns30/hf_20261030_075043_0e9a6716-5dcf-4000-b20d-dcbdab288f26.png)

- [기획 화면의 우산 조사 장면](case-02-unclaimed-umbrella.html#scene-1a)에 원본 한 장을 내장했다. 접힌 모습과 펼친 모습을 따로 생성하지 않았다.
- 제작: Higgsfield Nano Banana 2.1 · 16:9 · 1K · thinking high · 한 장. 생성 전 안내 비용 1.5크레딧. 작업 ID: `0e9a6716-5dcf-4000-b20d-dcbdab288f26`.
- 화풍 참조: 기존 후트 교수 원본의 그림책 크레용·색연필 질감과 부드러운 윤곽선만 사용했다. 남색 겉감·금빛 별·파란 손잡이·전체 금빛 안감의 기준 그림이다. 게임에서는 접힌 모습과 펼친 모습을 나눠 써야 한다(개발 제작 대상).

## 5. 전체 탐문 대본·노트·단어 카드

질문 선택지는 **15개**(받아쓰기 **14개** + 조사 시작 **1개**), 노트 빈칸은 **32칸**이다. 아래 수치는 제작용이며 게임 화면에서 질문·증거 개수를 알려 주지 않는다. 이름과 장소 철자는 고정한다. 노트는 탐정 시점의 메모이며 NPC의 대답 전체를 인용하지 않는다. 토이 네스트는 현수막과 장소 변경 안내문을 함께 살핀 뒤, 테스의 이름은 가게에서 인사와 자기소개 뒤, 핀·풍차 언덕은 테스 t5에서, 루비는 테스 t4의 노트 채점 통과로 발견한다. 엘라의 질문은 인물을 해금하지 않는다.

### 엘라 — 선택지 4개 · 받아쓰기 3개 · 빈칸 5칸

| ID | 질문 / 해석 | 대답 / 해석 | 노트 빈칸 | 단어 카드 | 채점 뒤 해금 |
|---|---|---|---|---|---|
| ella:e0 | Hello. How can I help? / 안녕. 무슨 일이야? | Someone left that umbrella here. Can you help me? / 누가 저 우산을 여기 두고 갔어. 좀 도와줄래? | • someone [left] the umbrella at the village hall<br>• Ella asked for my help | left · lost · lent · felt | 없음 · 채점 뒤 e1·e2·inspect 표시 |
| ella:e1 | Whose umbrella is that? / 저건 누구 우산이야? | I don't know. No one came back for it. / 몰라. 아무도 찾으러 오지 않았어. | • Ella does not [know] the owner<br>• no one came [back] for the umbrella | know · see · back · here | 없음 |
| ella:e2 | How long has it been here? / 얼마나 오래 여기 있었어? | It's been here for a week. / 일주일째 여기 있어. | • umbrella at the hall for a [week] | week · day · month | 없음 |
| ella:inspect | Can I take a closer look at that umbrella? / 저 우산 좀 자세히 봐도 될까? | Of course. Here you go. / 물론이지. 여기 있어. | 없음 · 조사 시작 선택지 | 없음 | 채점 없이 답변 뒤 우산 확대 조사 시작 · 소지품 등록 없음 |

e2는 조사 전에도 물을 수 있으므로 this/that 대신 it으로 묻는다. e0 뒤 조사부터 선택해도 e1·e2는 남는다. 확대 조사를 닫으면 엘라의 대화로 돌아와 미완료 질문을 선택할 수 있다. 다시 조사하기를 선택하면 같은 우산을 살펴보며 이미 촬영한 증거는 중복 추가하지 않는다.

### 핀 — 질문 2개

| ID | 질문 / 해석 | 대답 / 해석 | 노트 빈칸 | 단어 카드 | 채점 뒤 해금 |
|---|---|---|---|---|---|
| finn:f1 | What is your umbrella like? / 네 우산은 어떻게 생겼어? | Mine is dark blue. It has a blue handle. / 내 거는 남색이야. 파란 손잡이가 있어. | • Finn's umbrella: [dark blue]<br>• [blue] [handle] | dark blue · white · blue · red · handle · star | 없음 |
| finn:f2 | What pattern is on your umbrella? / 네 우산에는 어떤 무늬가 있어? | Mine has no pattern. It's plain. / 내 거는 무늬가 없어. 민무늬야. | • Finn's umbrella: [no] [pattern]<br>• [plain] | no · gold · pattern · stars · plain · small | 없음 |

사용자 결정: 핀에게도 테스·루비와 같은 무늬 질문을 한다(탐정이 실물의 별무늬를 먼저 말하지 않게).

### 테스 — 질문 6개

| ID | 질문 / 해석 | 대답 / 해석 | 노트 빈칸 | 단어 카드 | 채점 뒤 해금 |
|---|---|---|---|---|---|
| tess:t0 | It rained that day. Did you bring an umbrella? / 그날 비가 왔잖아. 우산 가져왔어? | Yes. But I often lend mine to friends. I'm not sure where it is now. / 응. 그런데 친구들에게 우산을 자주 빌려줘서, 지금 어디 있는지 잘 모르겠어. | • Tess brought his umbrella that day<br>• Tess's habit: to [lend] his umbrella to friends<br>• not sure [where] his umbrella is now | lend · borrow · where · when | 없음 · 채점 뒤 t1–t5 표시 |
| tess:t1 | What is your umbrella like? / 네 우산은 어떻게 생겼어? | Mine is dark blue. It has a blue handle. / 내 거는 남색이야. 파란 손잡이가 있어. | • Tess's umbrella: [dark blue]<br>• [blue] [handle] | dark blue · black · blue · red · handle · bottle | 없음 |
| tess:t2 | What pattern is on your umbrella? / 네 우산에는 어떤 무늬가 있어? | Mine has gold stars. / 내 거에는 금빛 별무늬가 있어. | • Tess's umbrella: [gold] [stars] | gold · silver · stars · stripes | 없음 |
| tess:t3 | What color is your umbrella inside? / 네 우산 안쪽은 무슨 색이야? | Mine is dark blue inside. / 내 거는 안쪽이 남색이야. | • Tess's umbrella: [dark blue] [inside] | dark blue · gold · inside · outside | 없음 |
| tess:t4 | Who else was at the bazaar? / 바자회에 또 누가 있었어? | Ask Ruby, too. She works here. We were at the bazaar together. / 루비한테도 물어봐. 여기서 일하는 친구야. 그날 바자회에 함께 있었어. | • ask [Ruby]<br>• Ruby works at Toy Nest (“[here]”)<br>• Tess and Ruby were at the bazaar [together] | Ruby · Finn · here · there · together · alone | 루비 발견 · 토이 네스트의 새 대화 상대 |
| tess:t5 | Do you know anyone who lost an umbrella? / 우산을 잃어버린 친구를 알아? | Finn is looking for his umbrella. You can find him on Windmill Hill. / 핀이 자기 우산을 찾고 있어. 풍차 언덕에서 만날 수 있어. | • [Finn] is looking for his [umbrella]<br>• find Finn on [Windmill Hill] | Finn · Ruby · umbrella · bag · Windmill Hill · Toy Nest | 핀·풍차 언덕 발견 |

처음에는 t0만 보이고, t0을 바르게 적으면 t1–t5가 나온다(소풍의 벤 b1과 같은 방식). “우산 가져왔어?”를 먼저 물어야 “어떻게 생겼어?”가 자연스럽다. 빈칸에서 mine은 뺐다(mine은 이미 충분히 들림).

t4의 “works here”로 루비가 토이 네스트 직원이며 같은 가게에서 만날 수 있음을 알린다. 진술을 바르게 기록한 뒤 루비의 이름·대화 대상을 발견하며, 현재 테스와의 대화 화면에 머문다. 우산을 가져왔는지 여부를 루비 소개의 근거로 쓰지 않는다. 분실 사실은 루비 본인에게 듣고, 발견 우산의 주인은 특징 비교로 판단한다.

t5는 우산을 찾는 핀에게 문의할 이유와 만날 장소를 알려 준다. 핀의 행사 참석 여부·분실 날짜·분실 장소는 단정하지 않는다. 채점 뒤 핀·풍차 언덕만 발견 알림으로 표시하며 현재 대화에 머문다.

### 루비 — 질문 3개

| ID | 질문 / 해석 | 대답 / 해석 | 노트 빈칸 | 단어 카드 | 채점 뒤 해금 |
|---|---|---|---|---|---|
| ruby:r1 | What is your umbrella like? / 네 우산은 어떻게 생겼어? | Mine is dark blue. It has a blue handle. / 내 거는 남색이야. 파란 손잡이가 있어. | • Ruby's umbrella: [dark blue]<br>• [blue] [handle] | dark blue · black · blue · red · handle · star | 없음 |
| ruby:r2 | What pattern is on your umbrella? / 네 우산에는 어떤 무늬가 있어? | Mine has gold stars. / 내 거에는 금빛 별무늬가 있어. | • Ruby's umbrella: [gold] [stars] | gold · silver · stars · stripes | 없음 |
| ruby:r3 | What color is your umbrella inside? / 네 우산 안쪽은 무슨 색이야? | Mine is gold inside. / 내 거는 안쪽이 금빛이야. | • Ruby's umbrella: [gold] [inside] | gold · dark blue · inside · outside | 없음 |

## 6. 현장 사진·소지품·주변 물건

엘라의 조사 시작 질문은 첫 질문 e0 뒤에 나오고, 선택하면 허락 답변 뒤 우산 확대 조사로 넘어간다. e1·e2 질문과 선택 순서는 자유다. 사진은 총 6종이며, 필수 5장과 선택 1장으로 나눈다. 필수는 우산 손잡이·겉무늬·안감 3장과 회관의 현수막·장소 변경 안내문 2장이다. 실내 바자회 사진은 게시판에 그대로 두고 선택 관찰·촬영 대상으로 삼는다. 촬영하면 증거 노트에 남지만 촬영하지 않아도 인물 발견·추리 진입·사건 완료를 막지 않는다. 실루엣 배경 사진은 수집 대상에 넣지 않는다.

필수 사진 ID: umbrella-handle, umbrella-pattern, umbrella-inside, toy-bazaar-record, venue-change-notice. 선택 사진 ID: toy-bazaar-photo. 이 구분과 개수는 제작자용 조건이며 플레이 화면에는 필수·선택 표식이나 남은 촬영 수를 표시하지 않는다.

| 사진 ID | 제목 | 사진 속 사실 | 탐정 나레이션 / 해석 | 비교 |
|---|---|---|---|---|
| umbrella-handle | 우산 손잡이 | 접힌 우산의 파란 손잡이. 주인 표식 없음 | This handle is blue. / 이 손잡이는 파란색이야. | 세 후보 모두 같은 손잡이. 단독으로 주인 특정 불가 |
| umbrella-pattern | 우산 겉무늬 | 접힌 상태에서도 보이는 남색 겉감·금빛 별무늬 | This umbrella has gold stars on dark blue fabric. / 이 우산은 남색 천에 금빛 별무늬가 있어. | 무늬 없는 핀 제외. 루비·테스는 겉이 같음 |
| umbrella-inside | 우산 안쪽 | 펼친 상태에서만 촬영할 수 있는 전체 금빛 안감. 안쪽에는 별무늬 없음 | This umbrella is gold inside. / 이 우산은 안쪽이 금빛이야. | 루비의 gold inside와 테스의 dark blue inside를 구별하는 결정 단서 |
| toy-bazaar-record | 바닥에 떨어진 장난감 바자회 현수막 | Toy Bazaar, October 24, Hosted by Toy Nest. 현수막에는 영어만 인쇄하며 한글 병기는 하지 않는다. 개인 이름 없이 행사명·날짜·주관 가게 명칭만 있음 | A toy bazaar banner. October 24. Hosted by Toy Nest. / 장난감 바자회 현수막이야. 10월 24일. 토이 네스트에서 열었네. | 현수막만으로 방문 대상 해금 없음. 같은 날짜의 장소 변경 안내문까지 촬영하면 토이 네스트만 발견. 테스 이름은 가게에서 자기소개를 들은 뒤 알게 됨 |
| toy-bazaar-photo | 게시판의 실내 장난감 바자회 사진 | 회관 게시판에 걸린 행사 사진. 실내 벽·천장·조명과 사선으로 놓인 장난감 탁자가 보임. 어린 동물 친구들이 부모 동물과 함께 방문해 장난감을 고르고, 부모는 곁에서 함께 살펴봄. 사진은 행사장 한쪽에서 비스듬히 포착한 자연스러운 활동 장면. 앞쪽 아이가 장난감에 손을 뻗고, 뒤쪽 도우미가 물건을 건네며 인물들이 서로 겹쳐 보임. 카메라를 정면으로 바라보며 나란히 서는 기념촬영 구도는 피함. 하단에는 October 24 · Toy Bazaar. 우산과 주인 표식·빗방울·날씨 정답 단어는 넣지 않음 | A toy bazaar inside the village hall. October 24. / 마을회관 안에서 열린 장난감 바자회야. 10월 24일이네. | 선택 촬영. 미촬영이어도 추리·완료 가능. 현수막·장소 변경 안내문의 같은 날짜와 연결해 실내 진행을 확인. 실내라는 사실만으로 비가 왔다고 판단하지 않음. 인물·장소 해금 없음 |
| venue-change-notice | 장난감 바자회 장소 변경 안내문 | October 24(10월 24일), Toy Bazaar · Venue Change 제목, Courtyard → Village Hall 장소 변경, “The toy bazaar is indoors because of rain.”라는 변경 이유. 바자회 참가자에게 붙였던 안내 한 장이며 우산 주인 정보 없음 | A venue change notice. “The toy bazaar is indoors because of rain.” / 장소 변경 안내문이야. “비가 와서 장난감 바자회를 실내에서 진행합니다.” | 현수막과 같은 10월 24일을 연결해 비 때문에 실내로 옮긴 행사를 확인. 현수막도 수집했다면 토이 네스트만 발견. 두 기록 수집 순서는 자유 |

### 단서 기획을 보는 배치도

[장면 2의 시각 배치도](case-02-unclaimed-umbrella.html#scene-2)에서 바닥의 현수막, 게시판의 실내 바자회 사진, 장소 변경 안내문을 그림과 짧은 설명으로 비교한다. 날짜는 2026년 10월 24일, 게임 속 조사일은 10월 31일로 잡은 초안이다. 실제 게임 그림·화면 구현 방식은 정하지 않는다.

### 바자회와 날씨를 발견하는 순서 — 사용자 결정

- 현수막은 바자회 날짜와 주관 가게 명칭을 알려 준다. 개인 이름은 알려 주지 않는다. 핀·풍차 언덕은 현장 사진이 아니라 테스 t5의 진술을 기록해 발견한다.
- **게시판 구성 — 사용자 결정:** 게시판 위쪽에 “이달의 행사” 제목을 붙인다. 큰 행사 사진 한 장(10월 24일 실내 바자회)과 실루엣 위주의 작은 배경 사진 여러 장을 섞는다. 배경 사진은 날짜·이름·문구가 읽히지 않고 인물과 동작의 윤곽만 보인다. 추가 행사·새 NPC·용의자·방문 장소를 확정하지 않으며 필수 촬영 수에도 넣지 않는다.
- 장소 변경 안내문에는 장난감 바자회 이름·10월 24일 날짜, 마당→마을회관 안으로 바뀐 장소, 비 때문에 실내에서 진행한다는 이유가 있다. 안내문은 바자회 참가자가 바뀐 장소를 찾아오도록 당일 붙인 것이다. 날짜와 변경 이유를 연결해야 바자회 날 비가 왔음을 판단할 수 있다. 발견 알림·촬영 완료 문구로 날짜 연결이나 추리 결론을 미리 알려 주지 않는다.
- 게임 속 조사일 10월 31일은 바자회에서 7일 뒤이므로 엘라의 “일주일째”와 맞는다. 날짜는 초안이며 문서끼리 같은 값을 사용한다. 조사일과 일주일을 계산해야 가게에 갈 수 있게 하지는 않는다.

### 날씨에서 탐문으로 이어지는 연결

현수막과 장소 변경 안내문 두 장을 모두 수집하면 아래 탐정의 연결 독백을 한 번 듣는다. 두 기록 중 어느 것을 먼저 촬영해도 된다. 새 받아쓰기 질문은 추가하지 않는다. 독백 뒤 토이 네스트만 방문 대상으로 추가하되 현재 회관 화면에 머문다. 이때 테스의 이름은 아직 모른다.

> It rained at the toy bazaar. Maybe someone brought an umbrella. Let's ask at Toy Nest.
> 장난감 바자회 날 비가 왔어. 우산을 가져온 사람이 있을지도 몰라. 토이 네스트에 가서 물어보자.

비는 문의할 행사를 고르는 보조 근거다. 회관 우산이 바자회 참석자의 것이라고 확정하지 않는다. 최종 추리 Q1은 이때 사용한 근거를 다시 확인한다.

### 소지품

- **반환용 소지품 우산**: 초반 확대 조사는 잠시 살피는 연출이며 소지품이 아니다. 추리 뒤 엘라에게 주인을 알린 뒤 우산을 받아 소지품으로 챙긴다. 제목에는 루비의 이름을 미리 붙이지 않는다(예: Umbrella from Ella). 엘라가 준 실제 물건이며 증거 사진과 구분한다.
- 소지품 짧은 설명: The umbrella Ella gave me. / 엘라가 맡긴 우산. 주인 정답은 소지품 문구로 새로 알려 주지 않는다.
- 이 우산은 토이 네스트의 루비에게 건네면 소지품에서 빠진다. 조사 사진은 수사 기록에 남는다. 반환 전에는 최종 보고·사건 완료로 넘어갈 수 없다.

### 단서가 아닌 주변 물건

| 장소 | 물건 | 나레이션 / 해석 |
|---|---|---|
| 회관 | 벽의 시계 | A clock on the wall. / 벽에 걸린 시계야. |
| 회관 | 빈 의자 | An empty chair. / 빈 의자야. |
| 회관 | 창문 | Sunlight through the window. / 창문으로 햇빛이 들어와. |
| 토이 네스트 | 장난감 선반 | Toys on the shelf. / 선반 위의 장난감들이야. |
| 토이 네스트 | 곰 인형 | A teddy bear on the counter. / 계산대 위의 곰 인형이야. |
| 풍차 언덕 | 풍차 | A windmill on the hill. / 언덕 위의 풍차야. |
| 풍차 언덕 | 바람개비 | A small pinwheel. / 작은 바람개비야. |

창문의 햇빛은 게임 속 조사일 10월 31일의 배경 정보다. 10월 24일의 비는 장난감 바자회 장소 변경 안내문의 because of rain이 근거다. 과거 날씨를 엘라에게 묻지 않으며 오늘 햇빛을 과거의 근거로 쓰지 않는다. 바람개비 행사를 뺐으므로 풍차 언덕의 바람개비는 풍경 소품일 뿐이다.

## 7. 장면·진행 조건

| 순서 | 일어나는 일 | 다음 조건 |
|---|---|---|
| 00 | 공통 열쇠 예습 → 첫 플레이 공통 튜토리얼 → 엘라 인사 | e0 선택지 하나만 표시 |
| 01 | e0으로 엘라의 의뢰를 듣고 받아 적은 뒤 e1·e2 질문 또는 inspect 질문을 선택 | e0 뒤 순서 자유. e0·e1·e2는 받아쓰기, inspect는 답변 뒤 확대 조사 |
| 01A | inspect 선택 → 허락 답변 → 엘라가 우산꽂이에서 가져와 잠시 건넴 → 접기·펴기·사진 3장 | 소지품 등록 없음. 조사 뒤 우산꽂이에 두고 엘라가 보관. 손 그래픽 생략 |
| 02 | 회관 필수 기록 2장 조사·실내 바자회 사진 선택 관찰 | 현수막+장소 변경 안내문으로 토이 네스트 발견. 우산 사진은 01A에서 촬영 |
| 03 | 가게에서 서로 인사 → 테스의 이름을 알게 됨 → 테스 6문항(t0 먼저) → t4 기록 뒤 루비 3문항·t5 기록 뒤 핀 2문항 | 테스 소개 뒤 핀·루비 순서는 자유. 루비는 t4, 핀은 t5 채점 통과 뒤 등장. 받아쓰기 14개·32칸 및 조사 시작 선택·필수 사진 5장 필요. 실내 바자회 사진은 미수집이어도 진행 |
| 04 | 추리 5문항: 비 때문에 옮긴 바자회 → 손잡이 → 핀 제외 → 테스 제외 → 주인 | 마지막 노트 채점 뒤에도 현재 장면 유지. 공통 추리 진입으로 시작 |
| 05 | 회관에서 엘라가 주인을 묻고, 탐정이 설명한 뒤 우산을 받음 | 소지품 우산 획득. 탐정의 생각 뒤 `Toy Nest로 가기` |
| 06 | 토이 네스트에서 우산을 펼쳐 보여 줌 → 테스가 누구 우산인지 묻고 탐정이 답함 → 루비에게 묻고 실물 확인 후 건넴 | 우산 소지품 제거·반환 완료. 탐정의 생각 뒤 `Village Hall로 가기` |
| 07 | 회관 엘라에게 보고하고 감사 인사를 들음 | 이때 사건 완료·복습 |

엘라의 부탁을 받기 전에는 사건의 진상·후보·의뢰인 직업을 팝업이나 이름표로 설명하지 않는다. 결말 장소로 옮길 때는 탐정의 생각과 이동 버튼을 보여 주고 플레이어가 누른다(소풍 사건 결말과 같은 방식). 발견 연출에 자동 카메라 이동을 섞지 않는다. 새 사건 전용 화면을 만들지 않고 기존 공통 화면에서 이 사건의 이야기가 일어나야 한다.

## 8. 추리 5문항

| Q | 질문 / 해석 | 완성 문장 | 보기 | 출처·판단 |
|---|---|---|---|---|
| 1 | Why did the toy bazaar move indoors? / 장난감 바자회는 왜 실내로 옮겼지? | The toy bazaar moved indoors because of [rain]. | rain / wind / snow / fog / thunder / sun | venue-change-notice의 because of rain과 toy-bazaar-record의 같은 날짜·주관 가게 명칭을 연결. 토이 네스트를 찾아간 이유를 복습한다. 우산 소유 확정 근거는 아님 |
| 2 | Can the handle tell us the owner? / 손잡이로 주인을 알 수 있을까? | Finn, Tess, and Ruby all lost umbrellas with [blue] handles. | blue / red / yellow / green / white / black | umbrella-handle + finn:f1·tess:t1·ruby:r1 — 실물과 세 후보 모두 파란 손잡이다. 손잡이 하나만으로는 주인을 구별할 수 없음을 확인한다. |
| 3 | Is this umbrella Finn's? / 이 우산은 핀의 것일까? | Finn's umbrella is [plain]. This one has gold stars. | plain / striped / spotted / red / white / green | finn:f2 + umbrella-pattern — 핀은 무늬가 없어 제외. 루비·테스는 계속 후보 |
| 4 | Is this umbrella Tess's? / 이 우산은 테스의 것일까? | Tess's umbrella is [dark blue] inside. This one is gold inside. | dark blue / gold / red / white / green / silver | tess:t3 + umbrella-inside — 겉모습은 같지만 펼쳐 본 안감 색이 다르다. 테스 제외 |
| 5 | Whose umbrella is this? / 그럼 이 우산은 누구 것일까? | This umbrella is [Ruby Cat]'s. It has a blue handle and gold stars, and it is gold inside. | Ruby Cat / Finn Frog / Tess Tortoise | ruby:r1·r2·r3 + 우산 사진 3장 + Q3·Q4 — 겉이 같은 두 후보를 안감 색으로 구별한다. 이름 뒤 소유격과 마지막 설명은 문장 틀로 제공한다. |

**맞장구·힌트 — 개발 초안을 사용자가 검토함(2026-11-04: Q2–Q4를 No로 고침, 나머지는 그대로):** 추리 보드는 문항마다 맞혔을 때의 맞장구와 두 번째 오답부터의 힌트가 필요해 개발에서 써 넣었다. 첫 오답은 공통 "Hmm… that doesn't fit."이다.

| Q | 맞장구 / 해석 | 힌트 / 해석 |
|---|---|---|
| 1 | Right. It rained that day. That's why we asked at Toy Nest. / 맞아. 그날 비가 왔어. 그래서 토이 네스트에 물어보러 갔지. | Look at the notice in the village hall. / 회관의 안내문을 봐. |
| 2 | No, it can't. All three are the same. The handle isn't enough. / 아니, 알 수 없어. 셋 다 똑같아. 손잡이만으로는 부족해. | Look at the handle photo. What did Finn, Tess, and Ruby say? / 손잡이 사진을 봐. 핀, 테스, 루비는 뭐라고 했지? |
| 3 | No, it isn't. Finn's umbrella has no pattern. / 아니야. 핀의 우산에는 무늬가 없어. | What did Finn say about the pattern? / 핀이 무늬에 대해 뭐라고 했지? |
| 4 | No, it isn't. The outside is the same, but the inside is not. / 아니야. 겉은 같지만 안쪽이 달라. | Look at the photo of the inside. What did Tess say about his? / 안쪽 사진을 봐. 테스는 자기 우산에 대해 뭐라고 했지? |
| 5 | It's Ruby's umbrella. Let's tell Ella. / 루비의 우산이야. 엘라에게 알려 주자. | Whose umbrella is gold inside? / 안쪽이 금빛인 우산은 누구 거지? |

Q1은 비 때문에 실내로 옮긴 바자회를 확인해 토이 네스트를 찾아간 근거를 복습한다. Q3·Q4는 “Is this umbrella …'s?”로 묻고 Q5는 “Whose umbrella is this?”로 묻는다. Q3·Q4에서 서로 다른 후보를 제외한다. 주인 확정 근거는 각자의 독립적인 설명과 우산 사진 3장이다. 겉무늬 사진만으로 루비를 확정하지 않는다. 오답은 같은 문항에서 다시 선택하며 앞서 맞힌 진척을 유지한다.

## 9. 반환·의뢰인 보고 대본

아래 대사는 노트 빈칸·필수 질문 수에 포함하지 않는다. 반환은 물건을 건네는 일이며 경찰 심문·압박·자백이 아니다. 엘라에게 주인을 알린 시점에는 아직 반환하지 않았으므로 완료 처리하지 않는다. 장소를 옮길 때는 탐정의 생각(꿀색 말풍선, 음성 없음)과 이동 버튼이 나온다.

| 장소·시점 | 화자 | 영어 | 한국어 | 행동 |
|---|---|---|---|---|
| 회관 · 추리 뒤 | 탐정 생각 | — | 엘라에게 우산 주인을 알려 주자. | 우산은 우산꽂이에 있음 |
| 회관 | 엘라 | So, whose umbrella is that? | 그래서, 저건 누구 우산이야? | 우산꽂이의 우산을 가리킴 |
| 회관 | 탐정 | That umbrella is Ruby's. Hers has gold stars, and it's gold inside. | 저 우산은 루비 거야. 루비 우산에는 금빛 별이 있고, 안쪽도 금빛이야. | |
| 회관 | 엘라 | Then please take it to her. Here you go. | 그럼 루비에게 가져다줘. 여기 있어. | 엘라가 우산을 건넴. 이때 처음 소지품으로 받음 |
| 회관 | 탐정 | I will. | 그럴게. | 생각 “루비에게 우산을 가져다주자.” · `Toy Nest로 가기` |
| 토이 네스트 | — | — | — | 탐정이 소지품 우산을 펼쳐 겉무늬와 금빛 안감이 보이게 듦. 아직 건네지 않음 |
| 토이 네스트 | 테스 | Oh! Whose umbrella is that? Is it mine? | 어! 저건 누구 우산이야? 내 거야? | |
| 토이 네스트 | 탐정 | No. Yours is dark blue inside. This one is gold inside. | 아니. 네 우산은 안쪽이 남색이야. 이건 안쪽이 금빛이야. | |
| 토이 네스트 · 루비 앞 | 탐정 | Ruby, I found this at the village hall. Is this umbrella yours? | 루비, 회관에서 이걸 찾았어. 이 우산 네 거야? | |
| 토이 네스트 | 루비 | Yes, it's mine! Gold stars, and it's gold inside too. | 응, 내 거야! 금빛 별에 안쪽도 금빛이야. | 겉무늬와 안감으로 잃어버린 자기 우산임을 확인 |
| 토이 네스트 | 탐정 | Here you go. | 여기 있어. | 우산을 소지품에서 골라 건네기 |
| 토이 네스트 | 루비 | So I left it at the bazaar! Thank you, Detective. | 바자회에 두고 왔구나! 고마워, 탐정. | 반환 완료. 생각 “엘라에게 알려 주자.” · `Village Hall로 가기` |
| 회관 · 의뢰인 보고 | 탐정 | I gave the umbrella back to Ruby. | 루비에게 우산을 돌려줬어. | 반환 완료 뒤에만 말할 수 있음 |
| 회관 | 엘라 | Wonderful! Thank you for your help, Detective. | 잘됐다! 도와줘서 고마워, 탐정. | 이 대사 뒤 사건 완료·복습 |

반환할 때의 “this umbrella”·“This one”은 추리 뒤 탐정이 받아 온 실물을 가리키고, 회관에서 엘라와 테스가 말하는 “that umbrella”는 떨어져 있는 우산을 가리킨다. 탐정이 가게에 들어서며 우산을 펼쳐 들므로 테스도 안감을 보고, 루비는 보이는 금빛 안감을 확인한다. 별도 촬영·받아쓰기 없이 행동으로 연결한다. 탐문 인사에서는 우산을 들고 있거나 후보가 조사 사실을 이미 안다고 가정하지 않는다. NPC는 각자의 장소에 두며 세 후보를 회관에 모으지 않는다. 핀·테스를 범인으로 지목하거나 사과시키는 결말은 넣지 않는다.

## 10. 복습과 제작 점검

- 해결 뒤 요약: 일주일째 남은 우산을 돌려주려 엘라가 의뢰했다. 장난감 바자회 현수막과 장소 변경 안내로 10월 24일 바자회가 비 때문에 회관 안에서 열렸음을 알아냈다. 바자회를 연 토이 네스트에 찾아가 테스와 인사했다. 테스의 진술로 우산을 찾는 핀과, 같은 가게에서 일하며 함께 바자회에 참여한 루비를 알게 됐다. 루비는 우산을 잃어버린 것을 알지만 어디에 두고 왔는지는 몰랐다. 실제 우산의 금빛 안감과 일치하는 루비에게 반환했고 루비는 실물을 보고 자기 우산임을 확인했다. 탐정은 엘라에게 보고했다.
- 선택 관찰 사진(실내 바자회)은 요약에 넣지 않는다.
- 다시 들을 문장: 틀린 질문의 실제 대답. 14개 중 사용자의 기록에 따라 고른다.
- 핵심 문법: Whose…?, this/that, 소유 표현. 추가 문법에는 has, no + 명사 등 실제 대사에서 쓴 표현만 둔다.
- 단어: umbrella 우산, owner 주인, week 일주일, handle 손잡이, pattern 무늬, plain 무늬가 없는, fabric 천, star 별(stars), mine 내 것, yours 네 것, sunlight 햇빛, indoors 실내에서, venue 장소, rain 비, dark blue 남색, gold 금빛, inside 안쪽. know 알다, lend 빌려주다, here 여기, together 함께 등 실제 대사에서 사용한 표현도 복습한다.
- 확정된 그림: 접힌 우산·펼친 우산 한 장(4절). 준비할 그림: 신규 장소 3곳(회관은 입구 우산꽂이 포함), 인물 4명, 우산 접힘·펼침 분리, 우산 촬영 부위 3곳, 회관 기록 3종(10월 24일 현수막·게시판의 실내 바자회 사진·10월 24일 장소 변경 안내문), 게시판의 실루엣 위주 배경 사진 여러 장, 오늘 맑은 하늘이 보이는 창문.
- 음성: 위 첫인사·질문·대답·단서 나레이션·주변 물건·결말·추리. 모두 녹음했다(대본 `design/case-02-unclaimed-umbrella-recording.md`).
- 확인 필요: 실제 음성으로 mine의 지시 대상과 no pattern을 구별하는지, 14문항·32칸·필수 사진 5장의 부담, 두 가지 특징을 모두 듣는지. 소요 시간·학생 난도·학습 효과는 아직 미검증이다.
- **개발 1단계(2026-11-03)**: 게임에 넣었다(`index.html`의 `UMBRELLA_CASE`, `?case=umbrella`, 사건 목록 Case 02). 녹음 없이 브라우저 음성으로 재생한다. **개발 2단계 그림(2026-11-03)**: 인물 4명(두 명씩 한 장, 루비 옷은 사용자 요청으로 다시 그림)·장소 3곳(바닥까지 한 장)·게시판의 실내 바자회 사진을 Higgsfield로 만들어 넣었고, 접힌 우산 아랫단의 금빛 안감을 남색으로 고쳤다. 지도에 회관·토이 네스트·풍차를 더하고 핀을 옮겼다. **개발 3단계 녹음(2026-11-03)**: 85줄을 모두 녹음해 넣었다. 목소리는 사용자가 골랐다: 엘라 Petra, 테스 Callan, 루비 Gracie, 핀 Dylan(모두 감정 행복), 탐정 Grady(중립).
- 개발 점검에서 나온 엔진 작업(1단계에서 모두 넣음): 우산 확대 조사(접기·펴기·부분 촬영), 증거 두 장으로 장소 해금과 탐정 독백, 자기소개 전 이름 없는 인물, 추리 진입 조건에 필수 사진, 추리 빈칸의 새 종류(이유·무늬), 결말의 받기만 하는 차례·보고만 하는 차례·펼치기 연출·같은 장소의 두 인물 대사. 기존 화면 모양 그대로 엔진에 더한다.

이 문서는 2026-11-02 사용자 결정으로 Claude Code에 인계한 1차 기획을 2026-11-03 개발 점검 뒤 사용자와 함께 고친 2차 수정본이다. 이후 설계서·대본의 수정·개발은 Claude Code와 사용자가 진행하며 Codex는 이 사건 설계서를 수정하지 않는다. 인계 기록은 design/STORY_LOG.md의 2026-11-02 16:05 항목을 따른다.
