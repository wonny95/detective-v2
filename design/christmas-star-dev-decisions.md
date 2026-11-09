# 크리스마스트리의 별 — 개발 점검 결정 (인계 전)

Claude Code의 점검(AGENTS.md "사건 진행 순서" 2단계)에서 사용자와 정한 것. 설계서 `design/case-10-christmas-star.md`·`.html`은 아직 코덱스 파일(STORY_LOG: 개발 미인계)이라 고치지 않았다. **개발 인계가 STORY_LOG에 적히면** 아래를 설계서에 반영하고 이 파일은 지운다.

## A. 엔진 (기존 화면 모양 그대로)

1. **경사의 퇴장**: 인물이 조건에 따라 사라지는 기능을 더한다(장소 지점의 `when`/`unless`처럼). 경사는 광장 대화(의뢰·안내대 신고·순찰)를 마치면 광장에서 사라진다. 심문 때는 말풍선(얼굴·`Sgt. Badger`)으로만 나온다.
2. **심문 중 개봉**: 경사의 개봉 지시 뒤 심문 화면을 잠시 닫고 썰매 현장으로 돌아간다. 상자 열기·c-open 촬영·별 뒷면 확대·c-mark 촬영은 지금의 현장 조사·확대 조사 화면을 그대로 쓴다. 다 찍으면 심문이 멈춘 곳(니코의 "It isn't the missing star.")부터 다시 열린다. 엔진에는 심문 멈춤·재개를 더한다.
3. **증거 두 개**: 둘 중 하나를 내밀면 정답(바이올린의 `accept` 목록). 선물 주장은 `tess:t3` 또는 c-toys, 썰매 주장은 c-track-sleigh 또는 c-track-yard. 탐정의 대사가 두 증거를 함께 말한다. 엔진은 고치지 않는다.
4. **결말**: 자백 뒤 "Let Ella know we found the star."는 말하지 않는 행동(바이올린의 경사에게 알리기처럼). 누르면 엘라가 썰매 앞에 나타나 그 자리에서 반환 대화를 한다. 엔진에는 이동 없는 반환을 더한다. 엘라는 우산 사건의 서 있는 그림을 다시 쓴다(새 자세 그림 없음).
5. **안내대**: 경사와의 대화가 끝나 경사가 사라지면 같은 광장 그림의 안내대 자리에 이름 없는 사슴(엘라)이 나타난다(A1의 기능). 탐정 생각 "I'll ask at the information desk."는 남기고 "안내대로 가기" 버튼은 뺀다.

## B. 앞뒤 맞추기

1. **테스는 토이 네스트 직원**(우산 사건 데이터와 같게). "I run Toy Nest."와 설계서의 "사장"을 고친다.
2. **다시 만난 인사**(엘라·테스는 우산 사건에서 탐정을 만났다):
   - 탐정 → 엘라: "Hi, Ella! I'm looking into the missing star. / 안녕, 엘라! 사라진 별을 조사하고 있어."
   - 엘라: "Detective! Nice to see you again. I reported it. / 탐정! 다시 만나서 반가워. 내가 신고했어."
   - 테스: "Detective! Nice to see you again. I'm a volunteer today. / 탐정! 다시 만나서 반가워. 오늘은 자원봉사를 해."
   - 이름은 이 인사 뒤부터 표시한다.
3. **c-track-sleigh**: 썰매 앞에 오면 바로 찍을 수 있다. 찍은 뒤 니코에게 썰매 질문(n5)이 열린다(창고 자국 → 홀리 h4와 같은 순서).
4. **천막 작업대**: 썰매에서 테스 작업대를 관찰한 뒤에는 천막 배경도 포장이 진행된 그림(완료 4·포장 중 1·포장 전 1, 준비표 체크 4)으로 바뀐다. 썰매에서 보는 작업대 그림은 이 그림에서 잘라 쓴다.

## C. 분량·받아쓰기

1. **분량 초과 유지**: 인물 6명, 필수 사진 6장, 천막 소품 4개.
2. **두 현장 진술을 받아쓰기로**(면담 17개·빈칸 40개):
   - **holly:h4** "Did you move any decorations today? / 오늘 장식품을 옮겼어?" → "Yes. I took some decorations to the [Tree Square] in a [handcart]." 보기: Tree Square · gift tent · storeroom · handcart · sleigh · basket. c-track-yard를 찍은 뒤 열린다.
   - **nico:n5** "Did you move the sleigh this morning? / 오늘 아침에 썰매를 옮겼어?" → "No. It [stayed] right here all [morning]." 보기: stayed · moved · started · morning · evening · night. c-track-sleigh를 찍은 뒤 열린다.
   - 두 질문 모두 추리를 여는 필수 기록. 균형표·복습 단어(Tree Square·handcart·stayed·morning)도 고친다.
3. **보기 개수**: 보기가 4장뿐인 질문(e0·h1·h2·h3·m0·m1·t1·n1·n4)은 개발 규칙(6장 이상, 오답 4장 이상, 동음어 없음)에 맞춰 개발에서 늘린다.

## D. 남은 것

- 그림·음성 계획(새 인물 홀리·메이·니코와 니코 표정, 장소 4곳·진행된 천막·창고 안 시야, 증거 사진, 상자 속 별·별 뒷면, 축제장 지도, 새 인물 목소리와 탐정 대사)은 인계 뒤 장면별로 사용자와 정하고 크레딧을 알린 뒤 만든다.
