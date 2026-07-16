# VibeMint NFT 메타데이터 (HeroGate 영웅 카드)

Sepolia `VibeMintNFT`용 **오프체인 메타데이터**입니다.  
HeroGate `assets/images/hero_cards` 이미지 **53장**을 tokenId **0–52** 순으로 매핑했습니다.

## Remix `setBaseURI`

owner 계정으로 한 번 호출:

```text
https://raw.githubusercontent.com/uno-gilbert/VIBE-MINT/main/assets/nft/metadata/
```

> 끝 **`/`** 필수. `tokenURI(n)` → 위 URL + `n`

## URL 예시

| tokenId | metadata JSON | image |
| --- | --- | --- |
| 0 | [metadata/0](https://raw.githubusercontent.com/uno-gilbert/VIBE-MINT/main/assets/nft/metadata/0) | [images/0.webp](https://raw.githubusercontent.com/uno-gilbert/VIBE-MINT/main/assets/nft/images/0.webp) |
| 1 | [metadata/1](https://raw.githubusercontent.com/uno-gilbert/VIBE-MINT/main/assets/nft/metadata/1) | [images/1.webp](https://raw.githubusercontent.com/uno-gilbert/VIBE-MINT/main/assets/nft/images/1.webp) |

## Etherscan NFT 확인

```text
https://sepolia.etherscan.io/nft/{CONTRACT_ADDRESS}/{TOKEN_ID}
```

`setBaseURI` 후 새로고침. 반영까지 수 분 걸릴 수 있습니다.

## 파일 구조

```text
assets/nft/
  images/0.webp … 52.webp
  metadata/0 … 52          ← ERC-721 tokenURI JSON (확장자 없음)
  manifest.json            ← tokenId ↔ 영웅 이름 매핑
```

## manifest

[`manifest.json`](manifest.json)에서 tokenId별 영웅 이름·이미지 URL을 확인할 수 있습니다.

---

Sepolia 테스트넷 교육용 — 메인넷 전문 Audit 필수
