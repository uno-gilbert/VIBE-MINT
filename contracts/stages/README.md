# Stage 0 → 3 따라하기

VibeMint NFT 컨트랙트를 **한 단계씩** 만듭니다.  
각 Stage 폴더의 README를 **위에서 아래로** 따라가면 됩니다.

> **규칙**: 「NFT 전부 만들어줘」금지. Stage마다 **추가분만** Cursor에 요청하고, Remix에서 **Compile → Deploy → 테스트** 합니다.

---

## 시작 전 (한 번만)

| # | 준비 | 확인 |
| --- | --- | --- |
| 1 | [GitHub 저장소](https://github.com/uno-gilbert/VIBE-MINT) clone 또는 ZIP | Cursor로 폴더 열기 |
| 2 | Chrome + [Remix](https://remix.ethereum.org) 로그인 | 계정 OK |
| 3 | Cursor 로그인 | AI 채팅 가능 |
| 4 | [00-rules.md](../../docs/prompts/00-rules.md) 첫 메시지에 붙여넣기 | 규칙 고정 |

**Remix 기본** (모든 Stage 공통)

| 항목 | 값 |
| --- | --- |
| 파일 | `VibeMintNFT.sol` |
| Compiler | **0.8.31** · EVM Version **osaka** |

**EVM** = 컨트랙트를 실행하는 가상 컴퓨터. Compile 시 “어느 세대 규격으로 번역할지”를 고릅니다.  
자세한 설명: [stage-0-base/README.md](stage-0-base/README.md#evm이란-컴파일할-때-왜-고르나)

| Environment | **Remix VM** (Sepolia는 나중에) |
| 코드 고친 뒤 | 반드시 **재Compile → 재Deploy** |

더 자세한 Remix 버튼 설명: [docs/prompts/03-stage-build/README.md](../../docs/prompts/03-stage-build/README.md)

---

## Stage 순서

| Stage | 무엇을 하나 | 폴더 | 대략 |
| --- | --- | --- | --- |
| **0** | ERC-721 뼈대 (mint 없음) | [stage-0-base](stage-0-base/README.md) | 20분 |
| **1** | public mint + 가격·한도 | [stage-1-mint](stage-1-mint/README.md) | 20분 |
| **2** | pause · ownerMint · withdraw | [stage-2-access](stage-2-access/README.md) | 25분 |
| **3** | whitelist mint | [stage-3-whitelist](stage-3-whitelist/README.md) | 25분 |
| **끝** | AI 보안 Audit → Sepolia | [04-security-audit](../../docs/prompts/04-security-audit.md) | 15분+ |

```text
Stage 0 뼈대 → Stage 1 출고 → Stage 2 운영 → Stage 3 VIP → Audit → 배포
```

⏱ Stage 3이 어려우면 [solution/VibeMintNFT.sol](../solution/VibeMintNFT.sol) 참고 후 **Audit은 필수**.

---

## 매 Stage 루프 (기억)

```text
1) Intent 한 줄
2) Cursor: 00-rules + Stage 프롬프트 (+ Stage 1부터 @파일 멘션)
3) Remix에 코드 반영 → Compile
4) Remix VM Deploy → README 테스트
5) 체크리스트 OK → 다음 Stage
```

---

## 바로 시작

→ **[Stage 0 README](stage-0-base/README.md)** 부터 열기
