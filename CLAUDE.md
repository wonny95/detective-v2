# CLAUDE.md

이 프로젝트의 작업 규칙은 Codex와 함께 쓰는 `AGENTS.md`에 있다. 시작·마무리 절차("이어서 해줘"의 뜻 포함)도 거기를 따른다.

사용자 확인은 `localhost:5176`(`detective-review`, 복사본·자동 새로고침 없음), Claude·Codex의 테스트는 `localhost:5177`(`detective-test`, 작업 파일)로 분리한다. UI 시안은 `localhost:5179`(`detective-design`)의 새 탭으로 띄운다. 사용자 서버에서는 테스트하지 않는다. 검증을 마친 게임은 `node scripts/update-review.js`로 확인용에 반영하고 사용자가 원할 때 직접 새로고침하게 한다. 자세한 규칙은 AGENTS.md의 "사용자 확인과 AI 테스트 분리"를 따른다.

@AGENTS.md
