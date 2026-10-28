# 곰 부인의 집 — 피오나의 거짓말을 증언으로 깨기 (계획)

사용자 결정: 계산대 쪽지 대신 곰 부인의 증언으로 피오나의 알리바이를 깬다. 곰 부인은 새 장소 **곰 부인의 집**에 있다. 피오나의 주장은 **절반은 사실**(부엌 불을 켜 두고 나감)이라 곰 부인의 말을 끝까지 들어야 거짓이 드러난다(사용자 선택 A, 곰 부인은 기다리다 지쳐 돌아감). 진술 내밀기(심문 증거 서랍 `진술` 탭)는 적용됨. 적용하면 이 문서는 지운다(HANDOFF에 지금 상태로 옮긴다).

## 이야기

피오나는 8시 30분쯤 도서관에 가면서 빵집 부엌 불을 켜 두었다. 지나가던 사람이 보면 안에서 일하는 줄 알게. 곰 부인이 8시 30분에 빵을 사러 와 불빛을 보고 문을 두드렸지만 아무도 나오지 않았고, 기다리다 지쳐 빵 없이 집에 갔다.

## 바뀌는 대사

### 피오나 q2 (다시 녹음, Petra)
- "Of course! Mrs. Bear walked by at eight thirty. She saw the light on in my kitchen. You can ask her."
- 노트: `{{Mrs. Bear}} walked by at {{8:30}}.` / `She saw the {{light}} on in the kitchen.`
- 바르게 적으면 지도에 **곰 부인의 집**과 곰 부인이 나타난다(`unlocks.q2`).

### 곰 부인 (새 인물, 참고인 `witness`, 대화는 필수 아님)
- hello: "Oh, hello, detective! I'm Mrs. Bear. Would you like some honey tea?"
- b1 "Did you go to Fiona's bakery tonight?" (오늘 밤 피오나의 빵집에 갔었나요?)
  → "Yes, at eight thirty. The kitchen light was on, so I knocked on the door. But nobody came."
  노트: `She went to the bakery at {{8:30}}.` / `The kitchen {{light}} was on.` / `She knocked, but {{nobody}} came.`
- b2 "What did you do then?" (그다음엔 어떻게 했나요?)
  → "I waited and waited, but I got tired. So I went home with no bread."
  노트: `She {{waited}} for a long time.` / `She went {{home}} with no bread.`

### 추리 보드 q8 (다시 녹음 q8·r8·h8)
- 질문: "She said Mrs. Bear saw her kitchen light. When did Mrs. Bear knock?"
- 카드: "Mrs. Bear knocked at {time:8:30}, but nobody came to the door."
- 정답 대사: "The light was on, but nobody opened the door. Fiona wasn't in her bakery. She lied." (동그라미 시점 `xAt`은 "She lied." 시작 초로 다시 잼)
- 힌트: "What did Mrs. Bear say? Did anyone open the door?"

### 심문 q2
- 피오나의 주장은 새 q2 녹음 그대로("Mrs. Bear … saw the light on in my kitchen").
- 정답: 곰 부인의 진술 `bear:b1`(노트 문장 "She knocked, but nobody came.")과 계산대 쪽지 사진 `bakery-2`("Sorry, Mrs. Bear! No bread tonight." — 피오나가 그날 빵을 안 팔 줄 알았다는 뜻).

## 새 장소: 곰 부인의 집

- 배경 16:9, 밤: 통나무집 부엌·거실, 식탁 위 빈 빵 바구니, 꿀단지 선반, 흔들의자와 뜨개질, 창밖 밤 숲. 대화용 바닥 확장(outpaint).
- 물건(모두 소품, 탐정 나레이션 녹음): 빈 빵 바구니("Mrs. Bear's bread basket is empty."), 꿀단지, 뜨개질 바구니.
- 지도: 그림은 다시 그리지 않고 빈 숲 자리에 핀(위치는 지도를 보고 정함).

## 그림 (한 번에 한 장)

1. **곰 부인** 전신(다른 인물과 같은 화풍, 흰 스티커 테두리 없이 자름) + 얼굴 아이콘(같은 그림에서). 따뜻한 갈색 곰, 숄이나 꽃무늬 앞치마, 안경 없이(두더지와 겹치지 않게).
2. **곰 부인의 집** 배경.
3. 바닥 확장(outpaint).

## 녹음

곰 부인 hello·b1·b2(새 목소리, 프리셋 하나), 피오나 q2, 추리 q8·r8·h8, 집 물건 나레이션 3줄. 약 10줄.

## 대략의 비용

그림 3장 약 4.5크레딧 + 녹음 약 10줄 약 1.5크레딧 = **약 6크레딧**.
