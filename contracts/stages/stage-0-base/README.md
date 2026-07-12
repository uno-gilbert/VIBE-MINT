# Stage 0: ERC-721 기본 뼈대

## 이 Stage에서 추가되는 것

| 항목 | 설명 |
| --- | --- |
| `ERC721("VibeMint", "VMINT")` | NFT 표준 기본 |
| `Ownable` | 배포자 = owner |
| `maxSupply` | 100 (상수) |
| `setBaseURI` | 메타데이터 base URI (owner) |
| `tokenURI` | baseURI + tokenId |

**아직 mint 함수 없음** — Stage 1에서 추가.

## Spec 요약

- totalMinted counter (private, read via `totalMinted()`)
- mint 없음

## Remix 사용

1. [remix.ethereum.org](https://remix.ethereum.org) → 새 파일 `VibeMintNFT.sol`
2. Compiler 0.8.20, OpenZeppelin import
3. Deploy (Mock) — Stage 0만 테스트

## Audit 전 체크 (3문항)

1. `setBaseURI`는 `onlyOwner`인가?
2. `maxSupply`가 100으로 고정되어 있는가?
3. 불필요한 `payable` fallback/receive가 없는가?

## 다음

→ [Stage 1](../stage-1-mint/README.md) | 프롬프트: [docs/prompts/03-stage-build/stage-0.md](../../../docs/prompts/03-stage-build/stage-0.md)
