# 사라진 음악 대회 바이올린 — 녹음 대본

`scripts/violin-recording-script.js`가 게임 데이터(`index.html`의 `VIOLIN_CASE`)에서 뽑은 목록이다. 대사를 고치면 이 파일도 다시 뽑는다. 파일 이름은 게임이 재생할 녹음 파일이다(`audio/violin/`).

- **탐정 줄은 모두 녹음됨**(90문장, MiniMax Grady·감정 없음, 목록과 job은 `audio/violin/README.md`). 아래는 아직 브라우저 음성으로 나오는 인물들의 줄이다.
- **목소리는 정할 것**(사용자 결정): 앞 사건처럼 Higgsfield MiniMax 프리셋에서 인물마다 하나. 오소리 경사는 도서관 사건과 같은 **Fraser**·감정 없음으로 녹음했다(사용자 결정). 녹음된 줄은 **녹음** 칸에 ✓.
- **감정**: 오웬의 심문 줄 가운데 표정이 바뀌는 줄(당황·슬픔)은 감정을 넣으려면 Higgsfield 웹(`higgsfield.ai/audio`)에서 만든다(MCP는 감정을 저장하지 않음). 나머지는 앞 사건 인물처럼 행복 또는 감정 없음.
- 여러 문장 대답(**문장** 칸이 2 이상)은 노트의 문장별 다시 듣기에 문장 구간(`SENTENCE_TIMES`)이 필요하다(녹음 뒤 무음 구간으로 잰다).
- 같은 화자의 같은 문장은 한 번만 녹음하고 파일을 함께 쓴다(**같은 녹음**에 처음 나온 번호).

| 화자 | 줄 수 | 녹음할 문장 | 녹음됨 |
|---|---|---|---|
| 타라 | 12 | 12 | 12 |
| 오웬 | 15 | 15 | 15 |
| 이보 | 7 | 7 | 7 |
| 모모 | 8 | 8 | 8 |
| 핍 | 3 | 3 | 3 |
| 오소리 경사 | 3 | 3 | 3 |
| **합계** | **48** | **48** | **48** |

## 타라 (12줄)

| # | 파일 | 장면 | 영어 | 문장 | 표정 | 해석 | 녹음 |
|---|---|---|---|---|---|---|---|
| 1 | `tara-hello.mp3` | 첫 인사 | Hello, Detective. I'm Tara. | 2 |  | 안녕, 탐정. 난 타라야. | ✓ |
| 2 | `tara-t0.mp3` | 대답 t0 (질문: How can I help you?) | My violin is missing. Can you find it before the contest? | 2 |  | 바이올린이 없어졌어. 대회 전에 찾아줄 수 있어? | ✓ |
| 3 | `tara-t5.mp3` | 대답 t5 (질문: When did you notice your violin was missing?) | I played it at rehearsal. It was gone when I came back from the lobby. | 2 |  | 리허설에서 연주했어. 로비에 갔다 돌아왔더니 없어졌어. | ✓ |
| 4 | `tara-t1.mp3` | 대답 t1 (질문: Where did you leave it?) | I left it in its case, next to the left chair in the waiting room. | 1 |  | 케이스에 넣어서 출연자 대기실 왼쪽 의자 옆에 두었어. | ✓ |
| 5 | `tara-t2.mp3` | 대답 t2 (질문: What does your case look like?) | There is a yellow moon sticker on my black case. | 1 |  | 내 검은 케이스에는 노란 달 스티커가 있어. | ✓ |
| 6 | `tara-t3.mp3` | 대답 t3 (질문: Where did you look?) | There are two chairs by the door. I looked under both, but the case wasn't there. | 2 |  | 문 옆에 의자가 두 개 있어. 둘 다 아래를 찾아봤지만 케이스가 없었어. | ✓ |
| 7 | `tara-t4.mp3` | 대답 t4 (질문: Who did you see before you left?) | A dog in the waiting room, a goat on stage, a mole backstage. I don't know their names. | 2 |  | 대기실의 강아지, 무대 위의 염소, 무대 뒤의 두더지를 봤어. 이름은 몰라. | ✓ |
| 8 | `tara-photo-give.mp3` | t2를 적은 뒤 | Here's a photo of my case. | 1 |  | 내 케이스 사진이야. | ✓ |
| 9 | `tara-r2.mp3` | ~~행동 (Can you check this violin?)~~ 없앰(2026-11-17), 파일은 안 씀 | My moon sticker! This is my violin. But the strings are broken. | 3 |  | 내 달 스티커네! 내 바이올린이야. 그런데 현이 끊어져 있어. | ✓ |
| 10 | `tara-r3.mp3` | ~~행동 (Can you check this violin?)~~ 없앰(2026-11-17), 파일은 안 씀 | I can't play it. Please find out what happened. | 2 |  | 이걸로는 연주할 수 없어. 무슨 일이 있었는지 알아봐 줘. | ✓ |
| 11 | `tara-end1.mp3` | 결말 (바이올린 반환) | Thank you for finding my violin and telling me what happened. | 1 |  | 바이올린을 찾아 주고 무슨 일이 있었는지 알려 줘서 고마워. | ✓ |
| 12 | `tara-end2.mp3` | 결말 (바이올린 반환), 감정 sad | My poor strings... I'll get new strings before the contest. | 2 |  | 불쌍한 내 현… 대회 전에 현을 새로 갈 거야. | ✓ (2026-11-17 다시, job `c6ef462c`) |

## 오웬 (15줄)

| # | 파일 | 장면 | 영어 | 문장 | 표정 | 해석 | 녹음 |
|---|---|---|---|---|---|---|---|
| 1 | `owen-hello.mp3` | 첫 인사 | Oh, hello. I'm Owen. | 2 |  | 어, 안녕. 난 오웬이야. | ✓ |
| 2 | `owen-hello2.mp3` | 첫 인사 | I'll tell you what I can. | 1 |  | 내가 아는 건 말해 줄게. | ✓ |
| 3 | `owen-o1.mp3` | 대답 o1 (질문: Where were you after rehearsal?) | I stayed next to the door the whole time. | 1 |  | 난 줄곧 문 옆에 있었어. | ✓ |
| 4 | `owen-o8.mp3` | 대답 o8 (질문: Why were you there?) | I waited for my turn. | 1 |  | 내 차례를 기다렸어. | ✓ |
| 5 | `owen-o2.mp3` | 대답 o2 (질문: When did you last see Tara's case?) | Next to the chair, before Tara went to the lobby. | 1 |  | 타라가 로비로 가기 전, 의자 옆에서 봤어. | ✓ |
| 6 | `owen-o9.mp3` | 대답 o9 (질문: Did you see anything strange?) | Momo, the stage helper, carried a black toolbox behind the curtain. | 1 |  | 무대 일을 돕는 모모가 검은 공구함을 들고 커튼 뒤로 갔어. | ✓ |
| 7 | `owen-sleeves.mp3` | 행동 (Can I look at your sleeves?) | My sleeves? OK. | 2 |  | 내 소매? 그래. | ✓ |
| 8 | `owen-o3.mp3` | 심문 · 오웬의 주장 | No. Maybe Momo moved it. Momo went behind the curtain. | 3 |  | 아니. 모모가 옮겼을지도 몰라. 모모는 커튼 뒤에 갔잖아. | ✓ |
| 9 | `owen-o4.mp3` | 심문 · 오웬의 주장 | Then it was someone else. I stayed next to the door. | 2 | 당황 | 그럼 다른 누군가였겠지. 난 문 옆에 있었어. | ✓ |
| 10 | `owen-o6.mp3` | 심문 | My sleeve caught on the curtain hook. I hid the case behind the curtain. | 2 | 당황 | 소매가 커튼 고리에 걸렸어. 내가 케이스를 커튼 뒤에 숨겼어. | ✓ |
| 11 | `owen-o11.mp3` | 심문 · 오웬의 주장 | I only moved the case. I didn't break the violin. | 2 | 당황 | 케이스를 옮겼을 뿐이야. 바이올린을 망가뜨리지는 않았어. | ✓ |
| 12 | `owen-o12.mp3` | 심문 · 모순을 짚은 뒤 | Yes, I borrowed them for my music stand. I didn't cut the strings. | 2 | 당황 | 응, 악보대를 고치려고 빌렸어. 현은 끊지 않았어. | ✓ |
| 13 | `owen-o10.mp3` | 심문 | Yes. I cut them. | 2 | 슬픔(고개 숙임) | 응. 내가 끊었어. | ✓ |
| 14 | `owen-o7.mp3` | 심문 | I wanted to win. I'm sorry. | 2 | 슬픔(고개 숙임) | 내가 이기고 싶었어. 미안해. | ✓ |
| 15 | `owen-wrong.mp3` | 심문 · 틀린 것을 내밀었을 때 | That doesn't explain anything. | 1 |  | 그걸로는 아무것도 설명이 안 되잖아. | ✓ |

## 이보 (7줄)

| # | 파일 | 장면 | 영어 | 문장 | 표정 | 해석 | 녹음 |
|---|---|---|---|---|---|---|---|
| 1 | `ivo-hello.mp3` | 첫 인사 | Hello, I'm Ivo. | 1 |  | 안녕, 난 이보야. | ✓ |
| 2 | `ivo-hello2.mp3` | 첫 인사 | Of course. What would you like to know? | 2 |  | 물론이야. 무엇이 궁금하니? | ✓ |
| 3 | `ivo-i1.mp3` | 대답 i1 (질문: Where were you after rehearsal?) | I was next to the music stand on the stage. | 1 |  | 무대 위 악보대 옆에 있었어. | ✓ |
| 4 | `ivo-i3.mp3` | 대답 i3 (질문: Why did you stay on stage?) | I wanted to practice the last part once more before the contest. | 1 |  | 대회 전에 마지막 부분을 한 번 더 연습하고 싶었어. | ✓ |
| 5 | `ivo-i4.mp3` | 대답 i4 (질문: What could you see from the stage?) | The side curtain was open. I could see the ladder next to the light. | 2 |  | 옆 가림막이 열려 있었어. 조명 옆 사다리가 보였어. | ✓ |
| 6 | `ivo-i2.mp3` | 대답 i2 (질문: What did you see when the light came back on?) | Momo was on the ladder, next to the light. I was still on the stage. | 2 |  | 모모는 조명 옆 사다리 위에 있었어. 나는 여전히 무대 위에 있었고. | ✓ |
| 7 | `ivo-sleeves.mp3` | 행동 (Can I look at your sleeves?) | Sure. Take a look. | 2 |  | 그럼. 봐. | ✓ |

## 모모 (8줄)

| # | 파일 | 장면 | 영어 | 문장 | 표정 | 해석 | 녹음 |
|---|---|---|---|---|---|---|---|
| 1 | `momo-hello.mp3` | 첫 인사 | Come in. I'm Momo. | 2 |  | 들어와. 난 모모야. | ✓ |
| 2 | `momo-hello2.mp3` | 첫 인사 | Oh, I see. I help with the stage lights. | 2 |  | 아, 그렇구나. 나는 무대 조명을 돕고 있어. | ✓ |
| 3 | `momo-m1.mp3` | 대답 m1 (질문: What did you do after rehearsal?) | I fixed the light next to the ladder. It went out after rehearsal. | 2 |  | 사다리 옆 조명을 고쳤어. 리허설 뒤에 꺼졌거든. | ✓ |
| 4 | `momo-m3.mp3` | 대답 m3 (질문: Did you go behind the curtain?) | Yes. There are spare bulbs on the shelf behind the curtain. I needed one. | 3 |  | 응. 커튼 뒤 선반에 예비 전구들이 있어. 하나 필요했어. | ✓ |
| 5 | `momo-m4.mp3` | 대답 m4 (질문: What did you carry?) | My black toolbox. I put it under the shelf before climbing the ladder. | 2 |  | 내 검은 공구함이야. 사다리에 올라가기 전에 선반 아래에 두었어. | ✓ |
| 6 | `momo-m2.mp3` | 대답 m2 (질문: Who else was nearby?) | Pip was by the side passage. I was busy with the light. | 2 |  | 핍이 옆 통로에 있었어. 난 조명 일로 바빴어. | ✓ |
| 7 | `momo-m5.mp3` | 대답 m5 (질문: Whose cutters are these?) | They're mine. I lent them to Owen. | 2 |  | 내 거야. 오웬에게 빌려줬어. | ✓ |
| 8 | `momo-sleeves.mp3` | 행동 (Can I look at your sleeves?) | OK. These are my work clothes. | 2 |  | 그래. 이건 내 작업복이야. | ✓ |

## 핍 (3줄)

| # | 파일 | 장면 | 영어 | 문장 | 표정 | 해석 | 녹음 |
|---|---|---|---|---|---|---|---|
| 1 | `pip-hello.mp3` | 첫 인사 | Hi there! I'm Pip. | 2 |  | 안녕! 난 핍이야. | ✓ |
| 2 | `pip-p1.mp3` | 대답 p1 (질문: Did you see a violin?) | No, but someone carried a black case behind the curtain when the light came back on. | 1 |  | 아니. 하지만 조명이 다시 켜졌을 때 누군가 검은 케이스를 커튼 뒤로 가져갔어. | ✓ |
| 3 | `pip-p2.mp3` | 대답 p2 (질문: Could you see who it was?) | No. I only saw the case through the door, and I couldn't see a sticker. | 2 |  | 아니. 문 너머로 케이스만 봤고, 스티커도 보지 못했어. | ✓ |

## 오소리 경사 (3줄)

| # | 파일 | 장면 | 영어 | 문장 | 표정 | 해석 | 녹음 |
|---|---|---|---|---|---|---|---|
| 1 | `badger-b1.mp3` | 행동 (Call the officer.) (전화) | Keep the violin safe. Call me when you're ready. | 2 |  | 바이올린을 잘 보관해 둬. 준비되면 불러 줘. | ✓ |
| 2 | `badger-b2.mp3` | 심문 시작 | I'm here, Detective. You can begin. | 2 |  | 왔어, 탐정. 시작해도 돼. | ✓ |
| 3 | `badger-b3.mp3` | 심문 | I'll talk to Owen. Please tell Tara what happened. | 2 |  | 난 오웬과 이야기할게. 타라에게 무슨 일이 있었는지 알려 줘. | ✓ |
