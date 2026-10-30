# 단어장 발음

단어장 카드의 ▶는 이 폴더의 단어·표현 한 항목만 재생한다. 예문 대사 녹음은 사용하지 않는다.

- 제작: Codex, 로컬 Windows SAPI `Microsoft Zira Desktop`(en-US). 외부 음성 생성 서비스·크레딧 없음.
- 형식: 22,050Hz, 16비트, 모노 PCM WAV. 현재 사전의 58개 항목(소풍 사건 단어 포함, Claude가 같은 설정으로 추가)에 각각 한 파일. 인물 이름은 단어가 아니라서(사용자 결정) 없다.
- 원문: `index.html`의 `WORDS`. 시간은 세 번째 값의 읽는 법(`nine p.m.`, `eight thirty` 등), 나머지는 사전 키를 읽는다. 여러 단어인 항목도 그 표현만 읽는다.
- 설정: Rate -1, Volume 85. 앱의 `천천히` 설정에서는 같은 파일을 0.75배속으로 재생한다.
- 파일명: 사전 키의 소문자 영숫자 외 문자를 `-`로 바꾸고 `.wav`를 붙인다. 예: `library.wav`, `9-pm.wav`, `lake-cafe.wav`.
- `regular-customer.wav`와 `bread.wav`는 피오나 q3의 새 빈칸에 맞춰 같은 Zira 설정으로 추가했다. 빠져 있던 기존 단어 발음 7개도 채우고, 쓰지 않는 `upset.wav`는 제거했다.
- 재생: `data-word-play` → `pronounceWord(key)` → `#wordVoice`. 새 발음을 누르면 기존 대사·단어 재생을 정지한다.

사전에 항목을 추가하거나 읽는 법을 바꾸면 프로젝트 루트에서 Windows PowerShell 5.1로 다시 생성한다(Node와 en-US SAPI 목소리 필요).

```powershell
powershell.exe -NoProfile -File scripts/generate-word-audio.ps1
```
