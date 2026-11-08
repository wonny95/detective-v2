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
| `b00811eb` | There are more programs on the table. | detective-foyer-1.mp3 |
| `c815c150` | A contest program under the bench. Someone dropped it. | detective-foyer-2.mp3 |
| `f9818ad3` | There are two chairs next to the door. The case isn't there. | detective-waiting-0.mp3 |
| `cda57863` | A big mirror. My hat looks fine. | detective-waiting-1.mp3 |
| `d5aa6087` | There is a water bottle on the table. | detective-waiting-2.mp3 |
| `b0ff4454` | There is a pair of cutters under the right chair. | detective-c1.mp3 |
| `9004305f` | There is a short piece of string on the blades. | detective-c2.mp3 |
| `388a275e` | There is sheet music on the stand. | detective-stage-0.mp3 |
| `fd005adc` | There is a stool next to the music stand. | detective-stage-1.mp3 |
| `22515469` | The door is open. I can see a ladder. | detective-stage-2.mp3 |
| `798bb189` | The ladder is next to the light. | detective-backstage-0.mp3 |
| `42852a0e` | There is a long curtain here. I should ask more first. | detective-backstage-1.mp3 |
| `453d70d0` | There is a case behind the curtain. | detective-s1.mp3 |
| `0283c41a` | The yellow moon is on the case. The violin is in it. | detective-s2.mp3 |
| `e1a28c67` | There are four strings. All four are broken. | detective-s4.mp3 |
| `b937d2df` | There is a gold button under the curtain. | detective-s3.mp3 |
| `8dc9b9ec` | A black toolbox under the shelf. | detective-backstage-5.mp3 |
| `cad1297b` | There are spare bulbs on the shelf. | detective-backstage-6.mp3 |
| `35ae0221` | There is a button on the left sleeve. The button on the right sleeve is missing. | detective-sleeves-owen-0.mp3 |
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
| `230bedb7` | This matches your left sleeve button. Your right one is missing. | detective-d2.mp3 |
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
