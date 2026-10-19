# 글꼴

게임 전체 글꼴은 **페이퍼로지(Paperlogy)** 하나다(사용자 결정). 인터넷 글꼴 서비스에 기대지 않도록 파일을 여기에 두고 `index.html`의 `@font-face`로 불러온다.

| 파일 | 굵기 | 쓰는 곳 |
|---|---|---|
| `Paperlogy-4Regular.woff2` | 400 | 본문·손글씨 자리(`--f-body`, `--f-hand`) |
| `Paperlogy-6SemiBold.woff2` | 400으로 등록(`Paperlogy Display`) | 제목·버튼·도장(`--f-display`) |
| `Paperlogy-7Bold.woff2` | 700 | 굵은 글자 |

- 출처: 이주임 제작 Paperlogy v1.0, 눈누 배포본(jsDelivr `projectnoonnu/2408-3@1.0`). 2026-10-19 Claude가 받았다.
- 라이선스: SIL Open Font License 1.1. 상업적 사용·웹 임베딩·재배포가 가능하고, 글꼴 파일 자체를 단독으로 판매할 수 없다.
- `--f-display`의 SemiBold는 `font-weight:400` 규칙을 그대로 둔 채 제목 굵기를 내려고 별도 이름으로 등록했다.
