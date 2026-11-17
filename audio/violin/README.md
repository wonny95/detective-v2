# 바이올린 사건 녹음

탐정이 소리 내어 하는 줄만 녹음했다(다른 인물은 아직 브라우저 음성). 목록은 `scripts/violin-detective-lines.js`가 `VIOLIN_CASE`에서 뽑는다. 같은 문장은 녹음 하나를 파일 이름마다 복사했다.

- Higgsfield MCP `generate_audio`, `text2speech_v2` · MiniMax · 프리셋 **Grady**(`e2a2d2e6-9ed2-59cd-82af-feaa27f8a678`), 감정 없음(우산·소풍 탐정과 같음). 2026-11-08, 90문장·95파일, 문장당 약 0.15크레딧.
- 파일 이름: 인사·행동 뒤 줄·생각·심문·반환 `detective-<키>.mp3`, 질문 `detective-<인물>-<질문>.mp3`, 행동 `detective-<인물>-act-<id>.mp3`, 살펴본 물건 `detective-<장소>-<번호>.mp3`, 추리 `deduce/q·r·h<번호>.mp3`와 `deduce/miss.mp3`.

| job | 문장 | 파일 |
|---|---|---|
| `c6da8d41` | How can I help you? | detective-tara-t0.mp3 |
| `eed043f0` | When did you notice your violin was missing? | detective-tara-t5.mp3 |
| `2611182c` | Where did you leave it? | detective-tara-t1.mp3 |
| `bcc339b5` | What does your case look like? | detective-tara-t2.mp3 |
| `ab095460` | Where did you look? | detective-tara-t3.mp3 |
| `8d63da83` | Who did you see before you left? | detective-tara-t4.mp3 |
| `d55b9de0` | Can you check this violin? | detective-tara-act-check.mp3 |
| `5b282cfa` | I found this behind the curtain. The violin is in it. | detective-r1.mp3 |
| `22e5b57d` | I'll keep it safe for now. | detective-r4.mp3 |
| `060a8735` | The strings are broken. I should tell the officer. | detective-contact-thought.mp3 |
| `3cb6925b` | Officer, I found Tara's violin. All four strings are broken. | detective-call.mp3 |
| `7606e470` | There is a yellow moon sticker on this case. | detective-photo.mp3, detective-taraphoto-0.mp3 |
| `e3c583ef` | I'd like to ask about Tara's violin. | detective-owen-open.mp3 |
| `f3e881e6` | Where were you after rehearsal? | detective-owen-o1.mp3, detective-ivo-i1.mp3 |
| `c329c6a9` | Why were you there? | detective-owen-o8.mp3 |
| `23317cce` | When did you last see Tara's case? | detective-owen-o2.mp3 |
| `44447df0` | Did you see anything strange? | detective-owen-o9.mp3 |
| `ec056520` | Can I look at your sleeves? | detective-owen-act-sleeves.mp3, detective-ivo-act-sleeves.mp3, detective-momo-act-sleeves.mp3 |
| `87da5d11` | I'm looking for Tara's violin. | detective-ivo-open.mp3, detective-momo-open.mp3 |
| `bba19b57` | Why did you stay on stage? | detective-ivo-i3.mp3 |
| `62f3de60` | What could you see from the stage? | detective-ivo-i4.mp3 |
| `fe7478c7` | What did you see when the light came back on? | detective-ivo-i2.mp3 |
| `1f5057cd` | What did you do after rehearsal? | detective-momo-m1.mp3 |
| `1ec532c8` | Did you go behind the curtain? | detective-momo-m3.mp3 |
| `76f791b8` | What did you carry? | detective-momo-m4.mp3 |
| `b2316ff5` | Who else was nearby? | detective-momo-m2.mp3 |
| `37af672f` | Whose cutters are these? | detective-momo-m5.mp3 |
| `31604f88` | Did you see a violin? | detective-pip-p1.mp3 |
| `e78d4e92` | Could you see who it was? | detective-pip-p2.mp3 |
| `cb22c730` | There is a contest poster on the wall. | detective-foyer-0.mp3 |
| `138f5529` | There are programs on the table. | detective-foyer-1.mp3 (2026-11-09 다시: more를 뺌) |
| `c815c150` | A contest program under the bench. Someone dropped it. | detective-foyer-2.mp3 |
| `f9818ad3` | There are two chairs next to the door. The case isn't there. | detective-waiting-0.mp3 |
| `cda57863` | A big mirror. My hat looks fine. | detective-waiting-1.mp3 |
| `d5aa6087` | There is a water bottle on the table. | detective-waiting-2.mp3 |
| `b0ff4454` | There is a pair of cutters under the right chair. | detective-c1.mp3 |
| `9004305f` | There is a short piece of string on the blades. | detective-c2.mp3 |
| `388a275e` | There is sheet music on the stand. | detective-stage-0.mp3 |
| `fd005adc` | There is a stool next to the music stand. | detective-stage-1.mp3 |
| `5a708f83` | The side curtain is open. I can see a ladder. | detective-stage-2.mp3 (2026-11-09 다시, 첫 판 `22515469`는 문 대사) |
| `798bb189` | The ladder is next to the light. | detective-backstage-0.mp3 |
| `42852a0e` | There is a long curtain here. I should ask more first. | detective-backstage-1.mp3 |
| `453d70d0` | There is a case behind the curtain. | detective-s1.mp3 |
| `0283c41a` | The yellow moon is on the case. The violin is in it. | detective-s2.mp3 |
| `e1a28c67` | There are four strings. All four are broken. | detective-s4.mp3 |
| `b937d2df` | There is a gold button under the curtain. | detective-s3.mp3 |
| `8dc9b9ec` | A black toolbox under the shelf. | detective-backstage-5.mp3 |
| `cad1297b` | There are spare bulbs on the shelf. | detective-backstage-6.mp3 |
| `41192830` | One sleeve has a gold button. The button on the other sleeve is missing. | detective-sleeves-owen-0.mp3 (2026-11-09 다시: 왼쪽·오른쪽을 뺌) |
| `e359dc2c` | There are dark buttons on both sleeves. | detective-sleeves-ivo-0.mp3 |
| `d65ad10c` | There are small silver buttons on both sleeves. | detective-sleeves-momo-0.mp3 |
| `e41a5edc` | I should look at everyone's sleeves. | detective-think-sleeves.mp3 |
| `276e5cb7` | I should ask who owns these cutters. | detective-think-cutters.mp3 |
| `8f6b6a54` | I should compare this piece with the broken strings. | detective-think-compare.mp3 |
| `d4fa3ff4` | The piece looks the same as this broken string. | detective-c3.mp3 |
| `3b324099` | Where was the case hidden? | deduce/q1.mp3 |
| `3a305dad` | Yes. That is where we found it. | deduce/r1.mp3 |
| `c6e65911` | What did Pip see? Where did we find the case? | deduce/h1.mp3 |
| `ffe900ef` | How do we know it is Tara's case? | deduce/q2.mp3 |
| `1269f7e0` | Yes. The same mark is in the photo. | deduce/r2.mp3 |
| `766f8308` | Look at Tara's photo. Then look at the case. | deduce/h2.mp3 |
| `c9f081c5` | Why did Momo seem strange? | deduce/q3.mp3 |
| `8cd300fb` | That's why Momo seemed strange. But we don't know yet. | deduce/r3.mp3 |
| `0887310d` | What did Owen see? What did Momo carry? | deduce/h3.mp3 |
| `9054b035` | Where was Momo when the case moved? | deduce/q4.mp3 |
| `0ec2fe48` | Right. He could not carry the case at that moment. | deduce/r4.mp3 |
| `1dafb581` | What did Pip say about the light? What did Ivo say? | deduce/h4.mp3 |
| `d8e89ff2` | Whose clothes match the button? | deduce/q5.mp3 |
| `b4eac91b` | Yes. A matching button remains on the other sleeve. | deduce/r5.mp3 |
| `227e93e8` | Look at the button. Then look at the sleeve photo. | deduce/h5.mp3 |
| `fd9175eb` | According to Momo, who borrowed the cutters? | deduce/q6.mp3 |
| `e9dc2cc4` | That is what Momo said. We still need to ask about the strings. | deduce/r6.mp3 |
| `43303f81` | Listen to what Momo said about the cutters. | deduce/h6.mp3 |
| `06ba467f` | Who should we talk to? | deduce/q7.mp3 |
| `0257c34a` | Right. Let's talk to him. | deduce/r7.mp3 |
| `3af63c71` | Think about the button and the cutters. | deduce/h7.mp3 |
| `1d895e5e` | Check the records again. | deduce/miss.mp3 |
| `0c46062b` | I should ask Owen about the button and the cutters. | detective-question-thought.mp3 |
| `65462cf1` | Officer, I'm ready. | detective-call2.mp3 |
| `53354373` | Owen, did you move Tara's case? | detective-d0.mp3 |
| `4d52d80a` | Ivo saw Momo on the ladder when the light came back on. Pip saw the case move at that moment. | detective-d1.mp3 |
| `07f04d13` | The case was next to the chair. The chair is next to the door. You didn't see anyone? | detective-d8.mp3 |
| `152258a8` | This matches the button on your sleeve. The other one is missing. | detective-d2.mp3 (2026-11-09 다시) |
| `bbb8efb0` | Why was this button under the curtain? | detective-d2-question.mp3 |
| `db39a836` | Momo says he lent you these cutters. Did you borrow them? | detective-d6.mp3 |
| `769f5826` | This piece looks like a broken string from the violin. | detective-d7.mp3 |
| `47d6d247` | Did you cut the strings? | detective-d4.mp3 |
| `dceaf0e4` | Why did you do that? | detective-d5.mp3 |
| `8b2a141d` | Owen hid your case behind the curtain. He cut the strings. | detective-end1.mp3 |
| `b363282d` | Here is your violin. | detective-end2.mp3 |

## 오소리 경사

도서관 사건의 경사와 같은 목소리(MiniMax 프리셋 **Fraser** `6705e465-7b52-5915-a1d8-b1222885e01d`, 감정 없음, 사용자 결정). 2026-11-09, 3문장 약 0.45크레딧. 게임에서는 `VIOLIN_CASE.people.badger.audio`.

| job | 문장 | 파일 |
|---|---|---|
| `d04da025` | Keep the violin safe. Call me when you're ready. | badger-b1.mp3 (전화) |
| `6f27ac7f` | I'm here, Detective. You can begin. | badger-b2.mp3 |
| `20fa943a` | I'll talk to Owen. Please tell Tara what happened. | badger-b3.mp3 |

## 타라

MiniMax 프리셋 **Evie** `7a6845a2-5865-5669-a0ca-8fc8d8e96528`(사용자 결정). 첫 인사는 사용자가 Higgsfield 웹에서 감정 **sad**로 만든 것, 나머지 11줄은 감정 없이 MCP로(사용자 결정: Claude in Chrome이 연결되지 않아). 2026-11-09, 약 1.65크레딧. 여러 문장 대답의 구간은 `SENTENCE_TIMES`(브라우저에서 디코딩해 무음 구간으로 잼).

| job | 문장 | 파일 |
|---|---|---|
| `871bc905` | Hello, Detective. I'm Tara. | tara-hello.mp3 |
| `039dc496` | My violin is missing. Can you find it before the contest? | tara-t0.mp3 |
| `4ff89379` | I played it at rehearsal. It was gone when I came back from the lobby. | tara-t5.mp3 |
| `3010d72d` | I left it in its case, next to the left chair in the waiting room. | tara-t1.mp3 |
| `5ae89722` | There is a yellow moon sticker on my black case. | tara-t2.mp3 |
| `527632bc` | There are two chairs by the door. I looked under both, but the case wasn't there. | tara-t3.mp3 |
| `f6bc7b8d` | A dog in the waiting room, a goat on stage, a mole backstage. I don't know their names. | tara-t4.mp3 (2026-11-09 범인을 강아지로 바꾸며 다시 녹음, 이전 `d55e6314`는 fox) |
| `a99cb1db` | Here's a photo of my case. | tara-photo-give.mp3 |
| `7d6e18aa` | My moon sticker! This is my violin. But the strings are broken. | tara-r2.mp3 |
| `d24f1f6b` | I can't play it. Please find out what happened. | tara-r3.mp3 |
| `0b026639` | Thank you for finding my violin and telling me what happened. | tara-end1.mp3 |
| `b8502f0d` | I can't play today. I'm sad, but I'll get new strings. | tara-end2.mp3 |

## 오웬

MiniMax 프리셋 **Miles `e18664a7-…`**, 감정 없음(사용자 결정, 2026-11-09). 여러 문장 대답의 구간은 `SENTENCE_TIMES`.

| job | 문장 | 파일 |
|---|---|---|
| `6a2fb7b4` | Oh, hello. I'm Owen. | owen-hello.mp3 |
| `5e1f924c` | I'll tell you what I can. | owen-hello2.mp3 |
| `f42ae74c` | I stayed next to the door the whole time. | owen-o1.mp3 |
| `e5167cfb` | I waited for my turn. | owen-o8.mp3 |
| `82b3aeb9` | Next to the chair, before Tara went to the lobby. | owen-o2.mp3 |
| `cdd276cf` | Momo, the stage helper, carried a black toolbox behind the curtain. | owen-o9.mp3 |
| `06a8da44` | My sleeves? OK. | owen-sleeves.mp3 |
| `6a22da19` | No. Maybe Momo moved it. Momo went behind the curtain. | owen-o3.mp3 |
| `8917980d` | Then it was someone else. I stayed next to the door. | owen-o4.mp3 |
| `85db216f` | My sleeve caught on the curtain hook. I hid the case behind the curtain. | owen-o6.mp3 |
| `0e200956` | I only moved the case. I didn't break the violin. | owen-o11.mp3 |
| `47c3054e` | Yes, I borrowed them for my music stand. I didn't cut the strings. | owen-o12.mp3 |
| `6a2d6063` | Yes. I cut them. | owen-o10.mp3 |
| `0f0b8741` | I wanted to win. I'm sorry. | owen-o7.mp3 |
| `eda65d2d` | That doesn't explain anything. | owen-wrong.mp3 |

## 이보

MiniMax 프리셋 **Jasper `a7b8abe9-…`**, 감정 없음(사용자 결정, 2026-11-09). 여러 문장 대답의 구간은 `SENTENCE_TIMES`.

| job | 문장 | 파일 |
|---|---|---|
| `819c0b96` | Hello, I'm Ivo. | ivo-hello.mp3 |
| `c5abeb18` | Of course. What would you like to know? | ivo-hello2.mp3 |
| `7f0bdb72` | I was next to the music stand on the stage. | ivo-i1.mp3 |
| `b414bc65` | I wanted to practice the last part once more before the contest. | ivo-i3.mp3 |
| `46aeb34b` | The side curtain was open. I could see the ladder next to the light. | ivo-i4.mp3 |
| `d8d402b7` | Momo was on the ladder, next to the light. I was still on the stage. | ivo-i2.mp3 |
| `ef17169d` | Sure. Take a look. | ivo-sleeves.mp3 |

## 모모

MiniMax 프리셋 **Barrett `d603a8cd-…`**, 감정 없음(사용자 결정, 2026-11-09). 여러 문장 대답의 구간은 `SENTENCE_TIMES`.

| job | 문장 | 파일 |
|---|---|---|
| `bb0a975e` | Come in. I'm Momo. | momo-hello.mp3 |
| `68fb6381` | Oh, I see. I help with the stage lights. | momo-hello2.mp3 |
| `6eee774c` | I fixed the light next to the ladder. It went out after rehearsal. | momo-m1.mp3 |
| `7d679df1` | Yes. There are spare bulbs on the shelf behind the curtain. I needed one. | momo-m3.mp3 |
| `fa79002c` | My black toolbox. I put it under the shelf before climbing the ladder. | momo-m4.mp3 |
| `f6247e88` | Pip was by the side passage. I was busy with the light. | momo-m2.mp3 |
| `3325199b` | They're mine. I lent them to Owen. | momo-m5.mp3 |
| `0a17b081` | OK. These are my work clothes. | momo-sleeves.mp3 |

## 핍

MiniMax 프리셋 **Pixie `0178ef57-…`**, 감정 없음(사용자 결정, 2026-11-09). 여러 문장 대답의 구간은 `SENTENCE_TIMES`.

| job | 문장 | 파일 |
|---|---|---|
| `d0fce8d1` | Hi there! I'm Pip. | pip-hello.mp3 |
| `dbbd6217` | No, but someone carried a black case behind the curtain when the light came back on. | pip-p1.mp3 |
| `7289b453` | No. I only saw the case through the door, and I couldn't see a sticker. | pip-p2.mp3 |

## 옆 통로 (2026-11-17)

탐정 MiniMax **Grady**, 감정 없음. 그림: 옆 통로 배경 Nano Banana 2.1 16:9 1K(준비실 원본을 참고 그림으로, 1.5크레딧, job `a0b72a2d`) → `assets/places/violin/passage.jpg`, 원본 `passage-higgsfield-original.jpg`. 대화용 바닥 outpaint 3:4(2크레딧, job `e767181a`, 원본 `passage-outpaint-original.jpg`) → `scripts/cut-picnic-floors.py passage`로 `passage-floor.webp`(원본 아래 150px에 겹쳐 서서히 나타남). 핍 실루엣 `pip-silhouette.png`는 핍 그림을 어둡게 칠해 준비실 문간에 맞춰 자른 것(크레딧 없음).

| job | 문장 | 파일 |
|---|---|---|
| `ddc78fd9` | There is a mop bucket by the wall. | detective-passage-1.mp3 |
| `18e5e97b` | A long scarf hangs on the hook. | detective-passage-2.mp3 |

## 바이올린 의견 반영 (2026-11-17)

Higgsfield MCP `text2speech_v2` · MiniMax, 감정 없음, 줄당 약 0.15크레딧(11줄 약 1.65).

- 탐정 **Grady**: `detective-ivo-i4.mp3`(How could you see Momo from the stage?, job `07abe72d`), `detective-take-cutters.mp3`(`0af5969a`), `detective-take-button.mp3`(`386f773a`), `detective-take-case.mp3`(`e8299420`), `detective-violincase-0.mp3`(There is a yellow moon on the case., `9d6a4954`), `detective-end-sorry.mp3`(`64b8e7f2`), 추리 `deduce/q6.mp3`(`816c4b33`)·`r6.mp3`(`193929c7`)·`h6.mp3`(`6a873dde`). 예전 추리 6·7번은 7·8번으로 이름을 바꿈.
- 핍 **Pixie** `0178ef57-ada4-43d9-992b-8d9221045bb4`: `pip-p2.mp3`(No. I only saw the case through the door. I couldn't see who carried it., `fae1eb60`). 문장 구간은 `SENTENCE_TIMES`.
- 타라 **Evie**: `tara-end2.mp3`(I knew the strings were broken. Now I know why. I'll get new strings.). Higgsfield 웹(Claude in Chrome)에서 **감정 sad**로 다시 만듦(job `40ee491d`, `emotion: sad` 확인, 0.3크레딧, 2026-11-17). 감정 없는 예전 판(`4bf901ac`)은 스크래치패드 `old-audio/tara-end2-neutral.mp3`.
- 쓰지 않게 된 녹음(경사 없음, 비교하기 없음): `badger-b1·b2·b3`, `detective-call`, `detective-call2`, `detective-contact-thought`, `detective-c3`, `detective-think-compare`. 사용자 결정으로 지우지 않고 둔다(2026-11-17).
- 쓰지 않게 된 녹음(2026-11-17, 중간에 타라에게 바이올린을 보여 주는 장면을 없앰): `detective-r1`, `tara-r2`, `tara-r3`, `detective-r4`. 지우려면 사용자 승인. `tara-end2.mp3`는 새 대사 My poor strings... I'll get new strings before the contest.로 다시 만듦(Higgsfield 웹 Evie, 감정 sad, job `c6ef462c`, `emotion: sad` 확인, 0.3크레딧). 예전 판(I knew the strings were broken..., `40ee491d`)은 스크래치패드 `old-audio/tara-end2-knew-sad.mp3`.
- 커튼 젖히는 소리 `curtain.mp3`: 사용자가 준 파일 `49603404-curtain-closing-323254.mp3`(약 1.2초)를 그대로 복사(2026-11-17). 준비실 커튼을 누르면 커튼이 열리며 재생되고, 그다음 탐정의 s1 줄이 나온다.
