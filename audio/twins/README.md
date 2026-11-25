# Case 06 같은 얼굴의 운전자 녹음 (2026-11-25)

Higgsfield `text2speech_v2` MiniMax. 사용자 승인(목소리·약 8.55크레딧). 감정 없음은 MCP, 에반의 자백 세 줄만 Higgsfield 웹에서 감정 슬픔(생성 기록에서 `emotion: sad` 확인). 파일 이름은 `<인물>-<키>.mp3`, 탐정은 `detective-<키>.mp3`, 질문 `detective-<인물>-<질문>.mp3`. 홈 클리어 멘트는 `audio/detective-clear-twins.mp3`(job `11e3d3f0`).

| 인물 | 목소리 | 줄과 job |
|---|---|---|
| 테리 | Nadine | hello `97329314`, t0 `fbbae513`, t1 `8eec7134`, t2 `a81abf07`, which `7343e7ac`, right `4285d485`, wrong `3f327ba2`, again(wrong의 2.0초부터 잘라 씀), thanks1 `75736063`, thanks2 `470553ae` |
| 아이리스 | Maeve | hello `ce55a16a`, i1 `d38bec58`, i2 `fa4c190e` |
| 빅터 | Harrison(사용자 결정) | hello `4bd8bf84`, v1 `70d65f93`, v2 `df8d4ed5` |
| 에이다 | Giselle | hello `24627859`, a1 `4ab241d2`, a2 `ed3c6a53`, a3 `47c5655d`, a4 `6d2f9302` |
| 에반 | Reid | room `ef831a00`, 슬픔: sorry1 `2fc77cab`("OK. …", 앞의 …은 읽지 않음), sorry2 `785be532`, sorry3 `ae48e955` |
| 마일로 | Reid | room `2a211d1f` |
| 탐정 | Grady | badger-t0("What happened?", 꿀 가게 `detective-badger-act-what` 복사; 우산의 같은 이름 파일은 "Hello. How can I help?"), badger-t1 `52f2af74`, badger-t2 `5b38554f`, iris-i1 `fbe4178c`, iris-i2 `fc70f297`, victor-v1 `a753a3e2`, victor-v2 `b5cc6ae9`, ada-a1 `e60ebfd6`, ada-a4 `2e51e9cb`, ada-a2 `a23bf677`, ada-a3 `ea0b2e4f`, badger-act-evan `32d8bab9`, badger-act-milo `c02ec4f6`, because `93ab1883`, think-station `55689436`, think-terry `912ffa1e`, station-laptop `91a6404a`, station-papers `134465f3`, station-photo `a008fbe3`. 2026-11-25 살펴보기 8줄(1.2크레딧): van-wheel `8b78cf51`, van-photo `def8b8f7`, van-cactus `e61c53d3`, van-candy `2868e688`, van-bread `18181b98`, van-clock `5e245f4c`, workshop-musicbox `798dcd8b`, think-look `ba65f31b` |

2026-11-25 사용자 결정으로 workshop을 repair shop으로 바꾸며 테리 t2·빅터 v1·탐정 ada-a3을 다시 녹음(0.75크레딧). 테리 t2는 사용자 결정으로 따옴표 없는 한 문장으로 또 바꿔 녹음(0.3크레딧, 앞 job `7d6c7b3e`). 처음 녹음 job은 `938973c7`·`6973358f`·`25365eb7`.

문장 구간은 `SENTENCE_TIMES`(쌍둥이), ffmpeg silencedetect로 잼.
