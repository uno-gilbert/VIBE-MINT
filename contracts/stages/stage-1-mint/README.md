# Stage 1: Public Mint + Supply Cap

## 이 Stage에서 추가되는 것

| 함수/변수 | 설명 |
| --- | --- |
| `mintPrice` | 0.001 ether |
| `MAX_PER_WALLET` | 3 |
| `mintedCount` | 지갑별 mint 횟수 |
| `mint()` | payable public mint |

## Spec 요약

- `msg.value >= mintPrice`
- `_totalMinted < maxSupply`
- `mintedCount[sender] < 3`
- 초과 ETH refund

## Audit 전 체크

1. supply cap 우회 불가?
2. 지갑당 cap enforced?
3. `_safeMint` 사용?

## 다음

→ [Stage 2](../stage-2-access/README.md) | [stage-1.md](../../../docs/prompts/03-stage-build/stage-1.md)
