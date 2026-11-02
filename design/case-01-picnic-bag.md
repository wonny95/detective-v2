# Case 01 A — 바뀐 소풍 가방

교육용 L1-01 A의 **제작자용** 기획. 게임에 구현되어 있다(`index.html`의 `PICNIC_CASE`, `?case=picnic`). 2026-10-30 개발 인계 뒤 점검·수정은 개발(Claude)이 사용자와 한다(`AGENTS.md` 사건 진행 순서). 장면별 화면은 [스토리보드](case-01-picnic-bag.html)를 본다. 플레이 중에는 소유 관계를 진술과 가방 안의 물건을 살펴보며 알아낸다.

## 사건의 진실

로지는 소풍 탁자에서 자신과 **겉모습이 똑같은 파란 가방**을 열었다가 초록 서류 폴더와 파란 펜을 발견한다. 자기 빨간 도시락과 노란 물병이 없어 탐정에게 의뢰한다. 로지는 조사에 쓰도록 그 가방을 탐정에게 맡긴다. 탐정은 소지품에 넣은 가방을 열어 폴더와 펜을 확인한다. 로지와 벤은 호수 카페에서 가방을 잘못 집었다. 노라는 자기 파란 가방을 벤의 집에 두고 갔다. 벤은 그 가방을 노라의 회사로 가져다주는 길에 카페에 들렀고, 로지의 똑같은 가방과 바뀐 줄 모르고 회사에 전달한 뒤 집으로 돌아왔다. 벤은 가방을 열지 않아 내용물을 전혀 모른다. 노라의 원래 가방 안에는 초록 서류 폴더와 파란 펜이 있다. 회사 일이 바빠 벤이 가져온 가방을 아직 열지 못한 노라는 **회사 1층 로비**에서 탐정을 만나 가방을 열어 보고, 빨간 도시락과 노란 물병이 있다고 말한다. 대화를 마치면 **그 자리에서 추리**한다. 탐정은 이미 챙긴 가방을 소지품에서 골라 노라에게 바뀐 경위를 설명하며 건넨다. 노라가 건넨 로지의 가방을 소풍 탁자로 가져와 돌려주며 끝낸다.

| 가방 | 겉모습 | 실제 내용 | 실제 주인 | 조사 위치 |
|---|---|---|---|---|
| 로지가 들고 온 것 | 동일한 파란 가방 | 초록 서류 폴더, 파란 펜 | 노라 | 소풍 탁자 |
| 벤이 전달한 것 | 동일한 파란 가방 | 빨간 도시락·노란 물병 | 로지 | 노라의 회사 1층 로비 |

노라는 탐정을 만나기 전까지 받은 가방을 열지 않아 내용물을 모른다. 로비에서 처음 열어 보고 말한 내용과 로지의 진술을 비교한다.

미아와 올리는 정원에서 소풍 준비를 시작한다. 올리의 가방은 빨간색이다. 미아는 파란 가방을 열어 보고 자기 소풍 준비물이 들어 있는 자기 가방이라고 확인한다. 두 사람은 가방을 바꿔 들지 않았다. 노라는 로지가 맡긴 가방의 실제 주인이자 벤이 전달한 가방의 수령인이다. 내용물의 소유를 진술과 소지품 조사로 연결한다. 이름표·가방 외형·인물 그림에 정답을 표시하지 않는다.

## 학습과 등장인물

- 목표: `my/your/his/her`, `mine/yours`를 듣고 사람과 물건을 연결한다. 단서 두 가지를 함께 대조한다.
- 핵심 낱말: bag, folder, pen, lunch box, bottle와 색 표현. `'s`는 추리·엔딩의 고정 문장 틀로 제공한다.
- 인물: 로지(의뢰인, 소풍 탁자), 오리 아저씨(카페 주인), 벤(노라 가방 전달인, 집), 생쥐 미아·수달 올리(Mia Mouse·Ollie Otter, 물건 비교 참고인, 정원), 노라 고슴도치(벤이 건넨 가방의 수령인, 회사 1층 로비). 모두 탐정과 초면이다. 로지·오리의 기존 첫인사는 유지한다.
- 로지의 인물 카드와 노트에는 `she/her`를 표시한다. 귀의 작은 보라색 리본은 시각적 일관성을 돕지만 옷차림으로 성별을 채점하지 않는다.
- 장소: 소풍 탁자, **낮의 호수 카페**, 벤의 집, 정원, **노라의 회사 1층 로비**. 오소리 경사와 심문 단계는 등장하지 않는다.

### 이번 사건의 열쇠 — 소유 표현 3쪽

기존 게임의 사건 열쇠 카드 형식을 사용한다. 이 사건에 필요한 표현이 세 묶음이어서 3쪽이며, 사건마다 쪽수를 고정하지 않는다. 한국어 문법 설명은 바로 보여 주고 예문 번역은 각 `해석` 버튼으로 연다. 예문에는 사건의 인물·가방·정답 물건을 쓰지 않는다. 문법 저장 ID는 `ownership`으로 묶는다.

| 쪽 | 표현과 뜻 | 사건 밖 예문 3개 |
|---|---|---|
| 1 | `my / your + 물건`: 말하는 사람의 것 / 듣는 사람의 것 | My book is big. / 내 책은 커요.<br>Your pen is black. / 네 펜은 검은색이에요.<br>Is this your hat? / 이건 네 모자니? |
| 2 | `his / her + 물건`: 그 남자의 것 / 그 여자의 것 | His cup is white. / 그의 컵은 흰색이에요.<br>Her notebook is small. / 그녀의 공책은 작아요.<br>His hat is black. / 그의 모자는 검은색이에요. |
| 3 | `mine / yours`: 물건 이름 없이 내 것 / 네 것 | This pencil is mine. / 이 연필은 내 것이에요.<br>Is this ruler yours? / 이 자는 네 것이니?<br>This book is not mine. / 이 책은 내 것이 아니에요. |

이 예습 뒤 첫 플레이에만 공통 튜토리얼을 거쳐 로지의 의뢰로 간다. 이름 뒤의 소유격 `'s`는 추리·엔딩의 고정 문장 틀로 제공한다. 노트 빈칸은 **대답에서 실제로 들리는 말** 가운데 단서가 되거나 공부할 만한 말(색·물건·장소·과거형 동사·표현)만 둔다(사용자 결정: 들리지 않는 대명사 바꾸기 빈칸 her/his/she/hers는 쓰지 않는다). 소유 표현은 이번 사건의 열쇠, 지문의 문법 표시, 복습의 문법 단계에서 익힌다.

## 장면과 해금

| 장면 | 핵심 행동 | 다음 해금 |
|---|---|---|
| 00 준비 | 소유 표현 예습, 최초 플레이 튜토리얼 | 소풍 탁자 시작 |
| 01 로지 | 직접 의뢰, 질문 r1–r4 | r4 기록 뒤 호수 카페 |
| 02 소풍 탁자 | 로지가 가방을 탐정에게 맡김. 소지품으로 챙겨 열어 보면 초록 폴더·파란 펜 확인 | 소지품 `로지가 맡긴 파란 가방` |
| 03 카페 | 주인이 손님으로 맞고 세 질문에 답함. 처음에는 v2(분실물)·v1(손님) 두 질문만 고르고, 둘 다 기록하면 v3 | v1 뒤 벤·미아·올리 이름, v3 뒤 벤의 집·정원 |
| 03B 벤의 집 | 노라가 집에 두고 간 가방을 회사에 전한 경로와 내용물을 아는지 질문함 | b1 기록 뒤 노라와 노라의 회사 |
| 04 정원 | 두 친구와 인사하고 파란 가방 여부를 묻는다. 미아의 파란 가방과 올리의 빨간 가방을 촬영한 뒤 사진을 보여 주며 미아의 가방인지 확인하고 감사 인사로 마무리함 | 사진 2장, 별도 필수 해금 없음 |
| 04B 회사 1층 로비 | 노라가 받은 가방을 처음 열고 내용물을 말함 | 노라 n3까지 기록하면 바로 추리 |
| 05 추리 | Q1에서 로지의 의뢰, Q2에서 로지가 말한 가방의 색·내용물, Q3에서 노라가 받은 가방과의 일치를 확인 | 마지막 Q4에서 바뀐 두 사람 특정 |
| 06 노라에게 설명·전달 | 추리 직후 `노라에게 바뀐 가방에 대해서 설명하자.`가 나온 뒤 소지품의 가방을 골라 `건네주기`. 탐정의 설명과 노라의 확인 대사가 이어짐 | 로지의 가방을 소지품에 받기 |
| 07 로지에게 전달 | 소풍 탁자에서 로지의 가방과 도시락·물병을 돌려줌. 로지의 감사 인사로 사건 종료 | 복습 |
| 08 복습 | 사건 요약, 소유 표현·단어 담기 | 완료 |

발견 알림은 인물·장소 이름만 짧게 표시하고 자동 이동하지 않는다. 대화를 시작한 인물의 질문은 끝까지 기록한다. 필수 질문은 **14개**(로지 4, 오리 3, 벤 2, 정원 공동 2, 노라 3)다. 정원에서는 미아·올리와 함께 한 번 인사한 뒤 두 질문을 이어서 기록한다. 오리 아저씨는 벤·미아·올리만 말하고 노라는 언급하지 않는다. 노라의 이름·회사 위치·가방을 받았다는 사실은 벤에게서 처음 듣는다. 이름을 들은 인물은 노트 인물 목록에 먼저 나오고, 지도에는 장소가 열릴 때 나타난다.

회사 로비에 가면 바로 노라와 대화한다. 노라가 탐정이 자기를 찾는다는 것을 어떻게 알았는지는 스토리에서 생략한다. 노라는 벤이 전달한 가방을 들고 있어서 첫인사의 “날 찾았다고 들었어”와 가방을 즉시 열어 보는 행동이 이어진다.

## 인사와 탐문 대본

탐정 이름은 저장된 `detective.detectiveName`을 화면에만 넣는다. 탐정 대사의 “Detective {플레이어 이름}”은 음성(녹음)에서 “the detective”로 읽는다(예: 화면 “I'm Detective Kim.” / 음성 “I'm the detective.”). 한국어 해석은 실제 게임에서는 버튼을 누른 뒤 보인다.

| 첫 만남 | 영어 | 한국어 |
|---|---|---|
| 로지 | Hi, I'm Rosie. Are you the detective? | 안녕, 난 로지야. 혹시 네가 탐정이야? |
| 탐정 | Yes. How can I help you? | 응. 어떻게 도와줄까? |
| 로지 | This isn't my bag. Can you help me find mine? | 이건 내 가방이 아니야. 내 가방을 찾아줄래? |
| 오리 | Hello! Welcome to the Lake Cafe. What would you like? | 안녕! 호수 카페에 온 걸 환영해. 뭘 주문할래? |
| 탐정 | Hello! I'm Detective {플레이어 이름}. I'm looking for a blue bag. | 안녕! 나는 탐정 {플레이어 이름}이야. 파란 가방을 찾고 있어. |
| 오리 | Oh! I see. How can I help? | 아, 그렇구나! 어떻게 도와줄까? |
| 벤 | Hi there! What can I do for you? | 안녕! 무슨 일이야? |
| 탐정 | Hi, I'm Detective {플레이어 이름}. Are you Ben? | 안녕하세요, 저는 탐정 {플레이어 이름}이에요. 혹시 벤인가요? |
| 벤 | Yes, that's me! | 응, 맞아! |
| 탐정 | You were at the Lake Cafe today, right? | 오늘 호수 카페에 오셨었죠? |
| 벤 | Yes, I stopped there this morning. | 응, 오늘 아침에 들렀어. |
| 올리 | Oh, hi! I'm Ollie. Nice to meet you. | 오, 안녕! 난 올리야. 만나서 반가워. |
| 미아 | I'm Mia. Want to join our picnic? | 난 미아야. 같이 피크닉 할래? |
| 탐정 | Nice to meet you, Ollie and Mia! I'm Detective {플레이어 이름}. | 만나서 반가워, 올리, 미아! 난 탐정인 {플레이어 이름}이야. |
| 올리 | A detective? That's cool! | 탐정이라고? 멋진걸! |
| 탐정 | You were at the Lake Cafe today, right? | 너희 오늘 호수 카페에 왔었지? |
| 미아 | Yes. We stopped there before coming here. | 응, 여기 오기 전에 들렀어. |
| 노라 | Hi, I heard you were looking for me. What's going on? | 안녕, 날 찾았다고 들었어. 무슨 일이야? |
| 탐정 | Hi, I'm Detective {플레이어 이름}. Can I ask about a blue bag? | 안녕, 난 탐정 {플레이어 이름}이야. 파란 가방에 관해 물어봐도 될까? |

| ID | 질문 / 해석 | 대답 / 해석 | 노트 빈칸 |
|---|---|---|---|
| rosie:r1 · 첫 질문 | Did your bags get mixed up? / 그럼 다른 사람과 가방이 바뀐 거야? | I'm not sure. My bag is blue, just like this one. / 잘 모르겠어. 내 가방도 이 가방처럼 파란색이야. | She is not [sure]. Her bag is [blue], just like this one. |
| rosie:r2 | What is in your bag? / 네 가방 안에는 뭐가 들어 있니? | My bag has a red lunch box and a yellow bottle. / 내 가방에는 빨간 도시락과 노란 물병이 있어. | Her bag has a [red] [lunch box] and a [yellow] [bottle]. |
| rosie:r3 | Do you know whose bag this is? / 이 가방이 누구 것인지 알아? | I don't know. Please find out for me. / 모르겠어. 네가 조사해 줬으면 좋겠어. | She does not [know] whose bag this is. She wants me to [find out]. |
| rosie:r4 | Who did you see today? / 오늘 누구를 봤어? | I can't remember who I saw. But I went to the lakeside cafe before I came here. Maybe the bags got mixed up there. / 누구를 봤는지 기억 안 나. 그런데 여기 오기 전 호수 카페에 들렀어. 거기서 가방이 바뀐 게 아닐까? | She can't [remember] who she saw. She went to the [cafe]. Maybe the bags got [mixed up] there. |
| duck:v2 · 첫 질문 | Did anyone leave a blue bag here? / 여기 파란 가방을 두고 간 사람이 있나요? | No. Nobody left a bag here today. / 아니요. 오늘 가방을 두고 간 손님은 없어요. | [Nobody] [left] a bag at the cafe. |
| duck:v1 · 첫 질문 | Who came to the cafe today? / 오늘 카페에 누가 왔나요? | Rosie, Ben, Mia, and Ollie came today. / 오늘 로지, 벤, 미아, 올리가 왔어요. | Rosie, [Ben], Mia, and Ollie came to the cafe. |
| duck:v3 | Where are they now? / 그들은 지금 어디 있나요? | They told me their plans. Ben went home. Mia and Ollie went to the garden. / 어디로 갈지 말해 줬어요. 벤은 집에 갔고, 미아와 올리는 정원으로 갔어요. | Ben went [home]. Mia and Ollie went to the [garden]. |
| ben:b1 | Do you have a blue bag? / 혹시 파란 가방을 가지고 있나요? | Nora left her blue bag at my house. I stopped at the cafe, then took it to her office. / 노라가 내 집에 파란 가방을 두고 갔어. 카페에 들렀다가 노라의 회사로 가져다줬어. | Nora left [her] blue bag at Ben's [house]. Ben stopped at the [cafe]. Then he [took] it to her [office]. |
| ben:b2 | What was in the bag? / 가방에는 뭐가 들어 있었어? | I don't know. I didn't open it. / 몰라. 가방을 열어 보지 않았어. | He does not [know] what was inside. He did not [open] it. |
| garden:g1 | Do either of you have a blue bag? / 혹시 너희 중에 파란 가방을 가진 사람이 있니? | 올리: No. Mine is red. / 아니, 내 가방은 빨간색이야.<br>미아: Mine is blue. Why? / 내 가방은 파란색이야. 왜 그래? | Ollie's bag is [red]. Mia's bag is [blue]. |
| garden:g2 | Mia, is this your blue bag? Have you checked inside? / 미아, 사진 속 이 파란 가방이 네 거야? 안을 확인했어? | 미아: Yes, it's mine. I opened it. My picnic things are inside. / 응, 내 가방이야. 열어 봤어. 내 소풍 준비물이 들어 있어. | The blue bag is Mia's. She [opened] it. Her [picnic] things are [inside]. |
| nora:n1 | Did you leave a blue bag at Ben's house? / 벤의 집에 파란 가방을 두고 왔니? | Yes. I left it there, but Ben brought it to me. / 응. 거기에 두고 왔어. 하지만 벤이 가져다줬지. | Nora [left] her bag at Ben's house. Ben [brought] it to her. |
| nora:n2 | What was in your bag? / 네 가방에는 무엇이 들어 있었니? | My green folder and blue pen. / 내 초록 폴더와 파란 펜이 들어 있었어. | Her bag had a [green] [folder] and a [blue] [pen]. |
| nora:n3 | Could you check the bag Ben brought? / 벤이 가져온 가방을 확인해 줄래? | I was in a meeting all morning, so I didn't open it yet. Let me look... A red lunch box and a yellow bottle? That's strange. / 아침 내내 회의가 있어서 아직 열어 보지 못했어. 어디 보자... 빨간 도시락이랑 노란 물병? 이상하네. | She was in a [meeting], so she did not open it. Inside are a [red] lunch box and a [yellow] bottle. She thinks that is strange. |

정원에서 g1을 기록한 뒤 두 친구에게 조사 이유를 말하고 사진 촬영을 부탁해 가방 두 개를 찍는다. 이 촬영은 같은 대화 안의 짧은 연출로 진행하며 지도·자유 조사는 열지 않는다. 두 가방은 건드리지 않고 주인 곁에 둔다. g2에서는 파란 가방 사진을 미아에게 보여 주며 자기 가방인지 묻는다. 정원의 두 질문을 모두 기록한 뒤 탐정이 “Thanks for answering my questions. Enjoy your picnic!” / “답변 고마워. 피크닉 재밌게 즐기길 바래.”라고 말한다. 로지가 맡긴 가방의 내부 확인, 카페·벤·정원의 기록, 정원 사진 2장까지 마친 뒤 노라의 세 질문을 모두 기록하면 로비에서 바로 추리 단계로 넘어간다. 회사가 먼저 해금되어도 조사 순서의 마지막 방문지로 둔다. 대괄호 37칸. `my`를 `his/her`로 바꾸어 기록하는 칸은 소유 관계 이해 과제이며 받아쓰기 정확도와 구분한다. 이름·장소·색 보기에는 오답 카드를 섞되 정답을 미리 알려 주지 않는다. 카페 주인은 분실물로 남은 가방이 없다는 것만 알고 누구의 가방이 무엇인지는 모른다(사용자 결정: 손님의 가방 색을 기억하는 대사는 어색해 분실물 질문으로 바꿈). 가방이 카페에 남지 않았으니 누군가 들고 갔다는 단서가 된다. 카페 주인은 노라에게 전달한 사실을 모르며, 벤은 노라가 집에 두고 간 가방과 카페에서 가져온 가방 모두 열어 보지 않아 내용물을 모르고, 바뀐 사실도 모른다.

## 소지품 조사·음성 전용 물건

| 소지품 | 얻는 곳 | 열어 본 내용 | 탐정의 짧은 음성 | 사용 |
|---|---|---|---|---|
| 로지가 맡긴 파란 가방 | 소풍 탁자 | 초록 서류 폴더, 파란 펜 | There is a green folder and a blue pen inside. | 추리 Q4 근거, 노라에게 건네기 |

소지품 제목에는 가방을 맡긴 사람과 색만 표시한다. 실제 주인 이름은 표시하지 않는다. 가방을 열어 보았을 때 폴더와 펜의 색을 탐정 음성으로 알려 준다. 회사 로비에서는 물건 촬영·증거 카드를 만들지 않고, 노라의 `n3` 음성 진술에서 빨간 도시락과 노란 물병을 듣는다. 카페에도 가방 소품은 없다.

정원 사진은 **소지품이 아닌 증거 노트**에 저장한다. 촬영 전에 탐정이 “I'm helping Rosie find her bag. Can I take a picture of your bags?” / “로지의 가방을 찾고 있어. 가방 사진을 찍어도 될까?”라고 묻고, 올리와 미아가 허락한다. 사진은 외형과 색만 보여 주고 주인의 이름을 제목에 적지 않는다.

| 사진 ID | 촬영 장소 | 제목 | 보이는 것 | 쓰임 |
|---|---|---|---|---|
| garden-blue-bag | 정원 | 파란 가방 | 미아 곁의 파란 가방 | g2에서 미아에게 보여 주고 주인 확인. 추리에서 혼동 후보 |
| garden-red-bag | 정원 | 빨간 가방 | 올리 곁의 빨간 가방 | g1 진술과 대조해 제외하는 혼동 후보 |

음성만 나오는 주변 물건(2026-11-02 사용자와 확정): 장소 화면에서 누르면 탐정이 한 줄을 말한다. 소지품·증거·해금에 쓰지 않고, 정답이나 가방 주인을 알려 주지 않는다. 사건 물건(소풍 탁자의 파란 가방, 정원 벤치의 두 가방)은 주변 물건으로 만들지 않는다. 회사 로비에는 사건 물건 조사가 없고 주변 물건만 있다. `해석`은 버튼을 눌렀을 때만 보인다.

| 장소 | 물건 | 탐정 음성 | 해석 |
|---|---|---|---|
| 소풍 탁자 | 바구니 | A brown picnic basket sits on the table. | 탁자 위에 갈색 소풍 바구니가 놓여 있다. |
| 소풍 탁자 | 식탁보 | A red and white cloth covers the table. | 빨간색과 흰색 천이 탁자를 덮고 있다. |
| 소풍 탁자 | 호수 | The lake is quiet and blue. | 호수가 조용하고 파랗다. |
| 카페 | 선반의 컵 | Blue, red, and gray cups are on the shelf. | 선반 위에 파란색, 빨간색, 회색 컵이 있다. |
| 카페 | 기타 | A guitar leans on the stage. Nobody is playing it now. | 기타 한 대가 무대에 기대어 있다. 지금은 아무도 연주하지 않는다. |
| 카페 | 창밖 | Through the window, the lake is bright and blue. | 창밖으로 밝고 파란 호수가 보인다. |
| 벤의 집 | 선반 | Books, plates, and cups are on the shelf. | 선반 위에 책, 접시, 컵이 있다. |
| 벤의 집 | 통나무 | A pile of logs. A little wooden horse sits on top. | 통나무 더미. 위에 작은 나무 말이 앉아 있다. |
| 벤의 집 | 러그 | A round rug in the middle of the room. | 방 한가운데에 둥근 러그가 있다. |
| 정원 | 꽃 | Red, yellow, and blue flowers grow everywhere. | 빨간 꽃, 노란 꽃, 파란 꽃이 여기저기 피어 있다. |
| 정원 | 돌길 | A stone path goes to the gate. | 돌길이 대문까지 이어진다. |
| 정원 | 울타리 | A white wooden fence goes around the garden. | 하얀 나무 울타리가 정원을 둘러싸고 있다. |
| 회사 로비 | 게시판 | A board with notes for the workers. | 직원들을 위한 쪽지가 붙은 게시판. |
| 회사 로비 | 계단 | The stairs go up to the offices. | 계단이 위층 사무실로 이어진다. |
| 회사 로비 | 화분 | A tall green plant by the window. | 창가에 키 큰 초록 식물이 있다. |

## 추리 4문항

| Q | 질문 / 해석 | 정답 카드 | 출처·판단 |
|---|---|---|---|
| 1 | What did Rosie ask me to do? / 로지가 나에게 부탁한 일은? | Find [her bag]. | 로지의 첫 의뢰. 자기 가방을 찾아 달라고 부탁함 |
| 2 | What is her bag like? / 그녀의 가방의 특징은? | Her bag is [blue]. It has a [red lunch box] and a [yellow bottle]. | rosie:r1·r2. 로지가 말한 자기 가방의 색과 내용물 |
| 3 | What shows that Nora has the wrong bag? / 노라가 잘못된 가방을 받았다는 근거는? | The [red lunch box] and [yellow bottle] are Rosie's. | Q2 + nora:n3. 로지가 말한 물건이 노라가 받은 가방에 있음 |
| 4 | Whose bags got mixed up? / 누구와 누구의 가방이 바뀐 걸까? | [Rosie Rabbit]'s and [Nora Hedgehog]'s bags. | Q3 + 소지품 속 폴더·펜 + nora:n2. 두 가방의 내용물과 각자의 진술을 연결 |

정원에서 찍은 파란·빨간 가방 사진은 처음에는 가방 후보를 늘린다. 올리의 빨간 가방과 미아가 사진을 보고 자기 것이라고 확인한 파란 가방은 탐문에서 제외된다. 추리에서는 이를 다시 묻지 않는다. Q1은 로지가 자기 가방을 찾아 달라고 한 의뢰를 확인한다. Q2는 로지의 진술에서 자기 가방의 파란색 외형과 빨간 도시락·노란 물병을 정리한다. Q3에서 그 물건이 노라가 받은 가방에도 있음을 대조한다. 마지막 Q4에서 소지품으로 챙긴 가방 안의 폴더·펜과 노라의 진술까지 연결해 탐정이 “누구와 누구의 가방이 바뀐 걸까?”라고 생각하며 로지·노라를 특정한다. 틀린 선택은 같은 문항에서 다시 풀며 진척을 보존한다.

정답을 고르면 탐정이 대답을 말하고 다음 문항으로 간다. 처음 틀리면 “Hmm… that doesn't fit.” / “음… 그건 맞지 않아.”, 두 번째부터는 문항별 힌트로 다시 볼 곳만 가리키고 정답은 말하지 않는다(2026-10-30 사용자 확정).

| Q | 탐정의 대답 (정답 뒤) | 힌트 (두 번째 오답부터) |
|---|---|---|
| 1 | Right. Rosie wants me to find her bag. / 맞아. 로지는 내가 자기 가방을 찾아 주길 바라. | What did Rosie say when we first met? / 처음 만났을 때 로지가 뭐라고 했지? |
| 2 | Yes. A blue bag with a red lunch box and a yellow bottle. / 맞아. 빨간 도시락과 노란 물병이 든 파란 가방이야. | Look at what Rosie said about her bag. / 로지가 자기 가방에 대해 한 말을 봐. |
| 3 | So the bag Ben brought to Nora is Rosie's bag. / 그러니까 벤이 노라에게 가져다준 가방은 로지의 가방이야. | What did Nora find in the bag Ben brought? / 노라가 벤이 가져온 가방에서 무엇을 찾았지? |
| 4 | The bag Rosie gave me has Nora's folder and pen. Their bags got mixed up. Let's give them back. / 로지가 맡긴 가방에는 노라의 폴더와 펜이 있어. 둘의 가방이 바뀐 거야. 돌려주자. | Look inside the bag Rosie gave me. What did Nora say was in her bag? / 로지가 맡긴 가방 안을 봐. 노라는 자기 가방에 뭐가 있었다고 했지? |

## 가방 전달·복습

로지의 대화가 끝나면 소풍 탁자에서 파란 가방을 탐정에게 맡긴다. `로지가 맡긴 파란 가방`이 소지품에 들어가고, 열어 보면 초록 폴더·파란 펜을 확인한다. 노라와의 대화가 끝나면 **회사 1층 로비에서 바로 추리**한다. 추리 직후 **“노라에게 바뀐 가방에 대해서 설명하자.”**가 뜬다. 이 단계는 심문 UI의 대사·제출 흐름을 사용하되 서랍 제목은 `소지품`, 선택 항목은 파란 가방, 제출 버튼은 `건네주기`다. 증거 선택·내밀기·압박 게이지는 없다. 소지품에서 건네주기를 누르면 탐정의 설명 뒤 가방을 전달하고 노라가 폴더·펜을 확인한 뒤 로지의 가방을 준다. 소지품은 로지의 가방으로 교체된다. 전달 경로는 **소풍 탁자(가방 수령) → 회사 1층 로비(노라에게 전달) → 소풍 탁자(로지에게 전달하며 종료)**다. 두 가방은 같은 외형이므로 대사와 내용물로 구별한다.

| 장소 | 인물 | 대사 / 해석 | 행동 |
|---|---|---|---|
| 소풍 탁자 | 로지 | Please take this bag and find mine. / 이 가방을 가져가서 내 가방을 찾아줘. | 탐정에게 가방을 맡김 |
| 소풍 탁자 | 탐정 | I will. / 그럴게. | `로지가 맡긴 파란 가방`을 소지품에 넣음 |
| 회사 1층 로비 | 탐정 | Rosie is looking for her bag. Her lunch box and bottle are in that one. / 로지가 자기 가방을 찾고 있어. 저 가방에 로지의 도시락과 물병이 들어 있네. | 소지품에서 가방을 선택해 건네주기를 누르면 설명 시작 |
| 회사 1층 로비 | 탐정 | This bag has your folder and pen. / 이 가방에는 네 폴더와 펜이 있어. | 챙겨 온 가방을 보여 줌 |
| 회사 1층 로비 | 탐정 | Your bags got mixed up. Here you go. / 너희 가방이 바뀐 거야. 여기 있어. | 가방 전달 연출 뒤 노라가 확인 |
| 회사 1층 로비 | 노라 | My folder and pen are here! Thank you. Here is Rosie's bag. / 내 폴더와 펜이 있네! 고마워. 여기 로지의 가방이야. | 로지의 가방을 탐정에게 건넴 |
| 소풍 탁자 | 탐정 | Rosie, I brought your bag back. / 로지, 네 가방을 가져왔어. | 로지의 가방을 전달 |
| 소풍 탁자 | 로지 | My lunch box and bottle are here! Thank you, Detective! / 내 도시락과 물병이 있네! 고마워, 탐정님! | 로지의 감사 인사로 사건 종료 |

벤을 엔딩에 다시 불러 설명하지 않는다. 노라에게 먼저 가방을 전한 뒤 의뢰인 로지에게 돌아와 사건을 마친다.

해결 뒤 복습 첫 장에만 두 가방의 교환과 서류·소풍 물건의 주인을 요약하고 `COMPLETE` 도장을 찍는다. 이어서 틀렸던 문장, 소유 표현 문법, 실제 나온 낱말을 복습한다. 문법과 단어는 항목별로 저장할 수 있다.

## 자산·구현 범위

- 소풍 대화 배경: `assets/places/picnic-storyboard/picnic-wide.png`. 참고 링크의 넓은 구도처럼 탁자를 오른쪽에 작게 두고 왼쪽에 인물이 설 공간을 둔다.
- 가방 내부 시안: `assets/places/picnic-storyboard/picnic-documents.png`. 소지품을 열어 보았을 때 보이는 **동일한 파란 가방**과 폴더·펜. 사진 촬영 UI에는 쓰지 않는다.
- 카페 낮 배경: `assets/places/picnic-storyboard/cafe-day.png`. 밤 포스터와 낙서가 없는 낮 장면이다. 도서관 사건의 밤 카페 그림은 건드리지 않는다.
- 정원: 기존 `garden.webp` 재사용. 미아·올리의 대화 배경이다. 사진 촬영용 파란·빨간 가방 소품 2개는 주인 곁에 배치해야 한다.
- 노라의 회사 1층 로비: 신규 장소 배경과 노라 전신·얼굴 그림이 필요하다. 벤이 가져온 파란 가방은 대화 소품이고, 로비 촬영 프레임·단서는 만들지 않는다.
- 벤의 집: `assets/places/picnic-storyboard/ben-home.png`. 크림색 벽과 둥근 강가 창, 왼쪽 벽 선반(책·그릇), 창 아래 통나무 더미와 나무 조각품, 바닥 가운데 둥근 러그, 오른쪽 작은 탁자·의자·화분과 문 옆 옷걸이가 있는 집 내부(2026-11-02 사용자와 정해 가구를 더함). 벤은 러그 위에 선다.
- 소지품 UI: 로지에게 받은 가방을 보관·열어 보고, 노라 앞에서 선택·건네주기 후 로지의 가방으로 교체하는 흐름은 게임에 있다(엔진 공용).
- 사건 ID 제안 `picnic-bag`. 현 도서관 사건의 `case01` 저장 데이터를 재사용하지 않는다.
