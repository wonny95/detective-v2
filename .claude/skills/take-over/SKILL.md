---
name: take-over
description: 개발(Claude Code) 쪽에서 Pioo 작업을 이어받는다. 기획 브랜치(story)를 받아 오고 인수인계 문서를 읽어 요약하고 최신 미리보기를 띄운다. 사용자가 "코덱스에서 넘어왔어", "인수인계 읽어줘", "최신 미리보기 띄워줘", "어디까지 했는지 봐줘"라고 할 때 쓴다. 코드를 고치지 않는다.
---

# 작업 이어받기 (Pioo)

개발은 Claude Code(`E:\GPT\Detective\Detective-dev`, `main`), 스토리 기획은 Codex(`E:\GPT\Detective\Detective-story`, `story`)가 동시에 맡는다(`AGENTS.md` 분업). 이 스킬은 `AGENTS.md`의 "시작 절차"를 따라 상태를 파악하고, 사용자에게 요약과 미리보기를 보여 주는 데서 멈춘다. **작업은 시작하지 않는다.** 사용자가 이어서 무엇을 할지 말하거나 CHANGELOG의 "다음"을 하라고 할 때 진행한다.

## 1. 상태 보기와 기획 받아 오기

```bash
git rev-parse --show-toplevel; git branch --show-current   # E:/GPT/Detective/Detective-dev · main 이어야 한다
git status --short
git log -8 --format='%h %an %ad %s' --date=format:'%m-%d %H:%M'
git log --oneline main..story                              # 기획 쪽 새 커밋
```

- 폴더·브랜치가 다르면 멈추고 사용자에게 알린다.
- 이 폴더는 개발만 쓴다. 모르는 미커밋 파일은 사용자가 둔 것이다(예: 아직 정하지 않은 튜토리얼 시안). HANDOFF·CHANGELOG에서 언급되는지 확인하고, 모르는 파일이면 사용자에게 묻는다.
- `story`에 새 커밋이 있으면 `git merge --no-edit story`로 받는다(기획 파일만 들어온다). 충돌이 나면 `git merge --abort` 후 충돌한 파일을 사용자에게 알린다.

## 2. 인수인계 읽기

1. `design/STORY_LOG.md` 맨 위 항목들에서 아직 반영하지 않은 **개발 요청**을 찾는다(반영한 것은 CHANGELOG에 "기획 반영: STORY_LOG <날짜>"로 적혀 있다). 반영은 사용자가 하라고 할 때 한다.
2. `CHANGELOG.md`에서 `---` 아래 **맨 위 항목**(작업자·시각·바뀐 점·확인·**다음**)을 읽는다. 마지막 작업 묶음이 여러 커밋이면 같은 작업자의 바로 아래 항목 몇 개도 훑는다.
3. `HANDOFF.md`는 통째로 읽지 않는다.
   - 제목 목록: `grep -n "^## \|^### " HANDOFF.md`
   - 0절(요약)과 4절(설계 규칙)을 읽는다. 4절에 새로 생긴 사용자 결정이 있는지 본다.
   - 최근 커밋이 다룬 기능의 절(예: 3.x 흐름, 8절 테스트 도구·퀵버튼)만 더 읽는다.
4. `AGENTS.md`의 "지켜야 할 규칙"이 바뀌었으면 그 차이를 보고에 넣는다. 기획 쪽은 AGENTS.md를 고치지 않으니, 바뀌었다면 개발 쪽 커밋이다.

## 3. 최신 미리보기 띄우기

- `preview_start`로 `.claude/launch.json`의 `pioo-dev`를 띄운다(`http://localhost:5173/`, 이미 떠 있으면 재사용).
- 이 탭은 **사용자가 볼 화면**이다. 스크립트를 돌리거나 테스트 버튼을 누르지 않는다. 사용자의 `localStorage` 진행을 바꾸지 않는다.
- 최근 작업이 특정 사건·파트에 있으면 들어가는 주소를 보고에 적는다(예: 소풍 사건 `?case=picnic`, 파트 `?preview=map|place|deduce|interview`). 사용자가 보여 달라고 하면 그때 이동한다.
- 스크린샷을 한 장 찍어 화면이 뜬 것을 확인한다. 콘솔 오류가 있으면 `read_console_messages`(onlyErrors)로 보고 알린다.

## 4. 사용자에게 한국어로 보고

- 맨 앞: 마지막 작업자·시각·최신 커밋 해시, 미리보기를 띄운 주소.
- **지금 상태**: 플레이 가능한 사건과 흐름을 HANDOFF 0절 기준으로 짧게.
- **최근 바뀐 것**: 마지막 작업 묶음의 커밋들을 사용자 관점(화면에서 무엇이 달라졌는지)으로.
- **새로 생긴 규칙**: AGENTS.md·HANDOFF 4절에서 새로 정해진 것.
- **기획에서 온 것**: 받아 온 `story` 커밋과 아직 반영하지 않은 STORY_LOG 개발 요청.
- **남은 것**: CHANGELOG의 "다음", 확인하지 못한 것, 미커밋 파일.
- "다음"이 "사용자 지시 대기"이면 HANDOFF 10절에서 후보 2–3개를 골라 묻는다.
- 문서만 읽었으므로 커밋·마무리(`/wrap-up`)는 하지 않는다.
