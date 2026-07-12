# Stage 3: Whitelist Mint

## 이 Stage에서 추가되는 것

| 함수/변수 | 설명 |
| --- | --- |
| `whitelist` | mapping(address => bool) |
| `setWhitelist` | batch 업데이트 (max 200) |
| `whitelistMint()` | whitelist + payment |
| `WhitelistUpdated` | event |

## Spec 요약

- whitelist mint는 `publicMintEnabled`와 무관
- 동일 `mintedCount` / `maxSupply` 규칙 공유
- Merkle tree는 **보너스** (기본 실습 제외)

## Audit 전 체크

1. non-whitelist가 `whitelistMint` 호출 시 revert?
2. `setWhitelist` batch length limit?
3. payment/refund 로직 public mint와 동일?

## 완료 후 필수

→ [04-security-audit.md](../../../docs/prompts/04-security-audit.md) 실행 후 Sepolia 배포

## 정답 예시

→ [contracts/solution/VibeMintNFT.sol](../../solution/VibeMintNFT.sol)
