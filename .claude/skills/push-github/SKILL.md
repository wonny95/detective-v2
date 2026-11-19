---
name: push-github
description: Detective 저장소의 main과 story를 GitHub 비공개 저장소(https://github.com/wonny95/detective-v2)에 올린다. 사용자가 "깃허브에 푸시해줘", "깃허브에 올려줘"라고 요청할 때만 쓴다. 마무리나 배포 때 자동으로 하지 않는다.
---

# GitHub에 푸시 (Detective)

- 저장소: `https://github.com/wonny95/detective-v2.git`. **비공개**이고, 사용자가 만들었다. 원격 이름은 `origin`이다.
- 예전 저장소 `https://github.com/wonny95/detective`는 v1 백업이다(사용자 결정 2026-11-19). 그쪽으로는 절대 푸시하지 않는다.
- **사용자가 요청할 때만** 푸시한다(사용자 결정). `/wrap-up`이나 `/publish-artifact`에 넣지 않는다.
- 강제 푸시(`--force`, `--force-with-lease`)는 하지 않는다. 올리는 브랜치는 `main`과 스토리 기획 브랜치 `story`(`Detective-story` worktree) 둘이다. 다른 컴퓨터에서도 Codex가 `story`로 이어서 작업하기 때문이다(`AGENTS.md` 여러 컴퓨터에서 작업).

## 0. 먼저 작업 마무리

- `git status --short`가 비어 있지 않으면 `/wrap-up`부터 끝낸다. 푸시는 커밋된 것만 올라간다.
- 다른 에이전트가 작업 중인 것으로 보이는 미커밋 파일이 있으면, 그 파일은 건드리지 않는다. 사용자에게 알리고 나서 커밋된 것만 푸시한다.
- 기획 폴더도 본다: `git -C ../Detective-story status --short`. Codex의 미커밋 변경은 올라가지 않으므로 있으면 사용자에게 알린다.

## 1. 확인

```bash
git branch --show-current          # main이어야 한다
git remote get-url origin          # https://github.com/wonny95/detective-v2.git
```

- `origin`이 없으면 `git remote add origin https://github.com/wonny95/detective-v2.git`로 추가한다.
- `origin`이 예전 주소(`wonny95/detective` 또는 `wonny95/pioo`)면 푸시하지 말고 `git remote set-url origin https://github.com/wonny95/detective-v2.git`로 바꾼 뒤 진행한다.
- 올리면 안 되는 것이 섞이지 않았는지 본다. 결과가 나오면 멈추고 사용자에게 보여 준다.

  ```bash
  git grep -nIE 'ghp_[A-Za-z0-9]{20,}|github_pat_|sk-[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16}|BEGIN [A-Z ]*PRIVATE KEY|X-Amz-Security-Token'
  git ls-files | grep -iE '\.env|credential|secret|\.pem$|\.key$'
  git ls-files -z | xargs -0 du -k | sort -rn | head -3   # 파일당 100MB 제한(50MB부터 경고)
  ```

- `sites/detective-demo/`는 `.gitignore`로 빠져 있어야 한다. 별도 Git 체크아웃이라 올리지 않는다.

## 2. GitHub 쪽 변경 먼저 받기

```bash
git fetch origin
git rev-list --left-right --count main...origin/main   # "내 쪽 앞섬  GitHub 쪽 앞섬"
git rev-list --left-right --count story...origin/story
```

- `origin/story`가 없으면(첫 푸시) `story` 비교는 건너뛴다.
- GitHub 쪽에만 새 커밋이 있으면(예: 다른 기기에서 올림) `git merge --ff-only origin/main`으로 받는다. `story`는 `git -C ../Detective-story merge --ff-only origin/story`로 받는다.
- 양쪽에 서로 다른 커밋이 있으면 **멈추고 사용자에게 묻는다.** 임의로 rebase하거나 merge하지 않는다.

## 3. 푸시

```bash
git push -u origin main story    # 다음부터는 git push origin main story
```

- **로그인**: 처음 푸시할 때 Git Credential Manager의 GitHub 로그인 창이 뜰 수 있다. 로그인은 사용자가 직접 한다. 토큰이나 비밀번호를 대신 입력하거나 명령에 넣지 않는다.
- 인증이 실패하거나 창이 뜨지 않으면 멈춘다. 사용자에게 로그인을 부탁하거나, 사용자가 직접 위 명령을 실행하도록 안내한다.
- 푸시가 거부되면(GitHub 쪽이 앞섬) 2단계로 돌아간다. 강제로 밀어 넣지 않는다.

## 4. 확인과 보고

```bash
git status -sb             # "## main...origin/main"이고 ahead/behind가 없어야 한다
git log --oneline -1 origin/main
git log --oneline -1 origin/story
```

- 사용자에게 한국어로 보고한다: 브랜치별로 올라간 커밋 범위(이전 `origin/main` → 지금), 커밋 수, 저장소 링크(https://github.com/wonny95/detective-v2), 받아 온 GitHub 쪽 커밋이 있었는지.
- 푸시할 때마다 문서에 기록하지는 않는다. 기록하면 그것이 새 커밋이 되어, 항상 올라가지 않은 커밋이 하나 남는다. GitHub 커밋 목록이 기록이다.
