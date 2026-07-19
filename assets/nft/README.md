# VibeMint NFT 메타데이터 (HeroGate 영웅 카드)

Sepolia `VibeMintNFT`용 **오프체인 메타데이터**입니다.  
HeroGate `assets/images/hero_cards` 이미지 **53장**을 tokenId **0–52** 순으로 매핑했습니다.

## Remix `setBaseURI`

### A. GitHub Raw (수업 기본)

owner 계정으로 한 번 호출:

```text
https://raw.githubusercontent.com/uno-gilbert/VIBE-MINT/main/assets/nft/metadata/
```

(GitHub Raw UI: `…/refs/heads/main/assets/nft/metadata/` — **동일**, 끝 **`/`** 필수)

> 끝 **`/`** 필수. `tokenURI(n)` → 위 URL + `n`

### B. Pinata IPFS (선택 · 따라하기)

지정 서비스 **[Pinata Cloud](https://app.pinata.cloud/)** 웹 UI로 이미지·metadata를 올리고 Dedicated Gateway로 `setBaseURI`하는 실습:

→ **[docs/student/06-ipfs-metadata.md](../../docs/student/06-ipfs-metadata.md)**

실습 참고 (images pin 완료):

| 항목 | 값 |
| --- | --- |
| Gateway | `https://magenta-key-quokka-912.mypinata.cloud` |
| Images CID | `bafybeibzqlnvhkviwqytx2lx7pxk65yzjap3uunoeth2wknylzg6z4pm7e` |
| 확인 | [0.jpg](https://magenta-key-quokka-912.mypinata.cloud/ipfs/bafybeibzqlnvhkviwqytx2lx7pxk65yzjap3uunoeth2wknylzg6z4pm7e/0.jpg) |

## URL 예시

| tokenId | metadata JSON | image |
| --- | --- | --- |
| 0 | [metadata/0](https://raw.githubusercontent.com/uno-gilbert/VIBE-MINT/main/assets/nft/metadata/0) | [images/0.jpg](https://raw.githubusercontent.com/uno-gilbert/VIBE-MINT/main/assets/nft/images/0.jpg) |
| 1 | [metadata/1](https://raw.githubusercontent.com/uno-gilbert/VIBE-MINT/main/assets/nft/metadata/1) | [images/1.jpg](https://raw.githubusercontent.com/uno-gilbert/VIBE-MINT/main/assets/nft/images/1.jpg) |

> metadata `image`는 **JPEG** (Etherscan·MetaMask 호환). 원본 **WebP**는 `images/*.webp`에 보관.

## Etherscan NFT 확인

```text
https://sepolia.etherscan.io/nft/{CONTRACT_ADDRESS}/{TOKEN_ID}
```

`setBaseURI` 후 새로고침. metadata·이미지 URL을 GitHub에 **push**한 뒤 Etherscan **Refresh NFT Metadata**(로그인) 또는 수 분 대기.

## 파일 구조

```text
assets/nft/
  images/0.jpg … 52.jpg     ← metadata image (Etherscan용)
  images/0.webp … 52.webp   ← 원본 (DApp·보관)
  metadata/0 … 52           ← ERC-721 tokenURI JSON (확장자 없음)
  manifest.json             ← tokenId ↔ 영웅 이름 매핑
  scripts/rewrite-image-urls.mjs  ← IPFS 업로드 후 image URL 일괄 변경
```

## manifest

[`manifest.json`](manifest.json)에서 tokenId별 영웅 이름·이미지 URL을 확인할 수 있습니다.

---

Sepolia 테스트넷 교육용 — 메인넷 전문 Audit 필수
