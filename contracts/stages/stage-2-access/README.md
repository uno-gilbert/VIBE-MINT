# Stage 2: Pause, Owner Mint, Withdraw

## 이 Stage에서 추가되는 것

| 함수/변수 | 설명 |
| --- | --- |
| `Pausable` | pause / unpause |
| `ReentrancyGuard` | withdraw 보호 |
| `publicMintEnabled` | public mint 토글 |
| `ownerMint(to, qty)` | owner 예약 mint (무료) |
| `withdraw()` | 컨트랙트 ETH 인출 |

## Spec 요약

- 모든 mint 경로: `whenNotPaused`
- public `mint()`: `publicMintEnabled` + payment
- `withdraw`: CEI + `nonReentrant`

## Audit 전 체크

1. pause 시 mint 차단?
2. withdraw reentrancy guard?
3. ownerMint가 payment 없이 cap만큼 mint?

## 다음

→ [Stage 3](../stage-3-whitelist/README.md) | [stage-2.md](../../../docs/prompts/03-stage-build/stage-2.md)
