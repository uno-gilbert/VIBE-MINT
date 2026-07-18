# 04. Sepolia 테스트넷 배포

## 학습 목표

- Remix + WalletConnect(MetaMask)로 Sepolia 배포
- Etherscan에서 컨트랙트·트랜잭션 확인
- 테스트 mint 1회 성공

---

## 1. Sepolia ETH 받기

MetaMask 네트워크: **Sepolia** (Chain ID 11155111)

Faucet (택 1):

- [Alchemy Sepolia Faucet](https://www.alchemy.com/faucets/ethereum-sepolia)
- [Sepolia PoW Faucet](https://sepolia-faucet.pk910.de/)

잔액 **0.05 ETH** 이상 권장.

---

## 2. Remix 배포

1. [Remix](https://remix.ethereum.org) → Compile `VibeMintNFT.sol` (0.8.31 · EVM osaka)
2. **Deploy & Run** → Environment: **WalletConnect**
3. **Connect Wallet** 클릭 → 지갑 목록에서 **MetaMask** 선택
4. Chrome에 설치한 **MetaMask 확장 프로그램** 팝업 → **연결(Connect)** 승인  
   (QR 코드만 보이면 MetaMask 앱에서 스캔 — 확장 프로그램 사용 시 보통 3–4단계로 연결됨)
5. MetaMask 네트워크 **Sepolia** 확인 → **Deploy**
6. MetaMask에서 가스 확인 → **Confirm**
7. 배포된 **Contract Address** 복사 (프론트 `.env`에 사용)

> **Injected Provider - MetaMask**가 안 되거나 MetaMask가 Remix에 안 잡히면 **WalletConnect**를 쓰세요. 로컬 MetaMask와 연결하는 데 더 안정적입니다.

---

## 3. 배포 후 설정 (owner)

Deployed Contracts 패널에서 **배포한 지갑(owner)** 으로:

### `setBaseURI` (권장 — Etherscan NFT 이미지)

1. 주황색 **`setBaseURI`** 클릭
2. 아래 URL 중 **하나** 입력 — **끝 `/` 필수** (없으면 `metadata1`처럼 깨짐):

```text
https://raw.githubusercontent.com/uno-gilbert/VIBE-MINT/main/assets/nft/metadata/
```

GitHub **Raw** 버튼을 누르면 `refs/heads/main` 형태로 보일 수 있습니다. **같은 주소**이며, 역시 **끝 `/`** 를 붙이세요:

```text
https://raw.githubusercontent.com/uno-gilbert/VIBE-MINT/refs/heads/main/assets/nft/metadata/
```

| baseURI 끝 | + tokenId `1` | 결과 |
| --- | --- | --- |
| `…/metadata/` ✅ | `1` | `…/metadata/1` → JSON OK |
| `…/metadata` ❌ | `1` | `…/metadata1` → **404** |

3. **transact** → MetaMask Confirm

| tokenId | `tokenURI` 결과 (예) |
| --- | --- |
| `0` | `…/metadata/0` → Hero **Alchemist** |
| `1` | `…/metadata/1` → Hero **Archmage** |

> **mint 전에** 호출해 두는 것을 권장합니다.  
> `owner`가 아닌 지갑으로 호출하면 revert.

**확인**: Read **`tokenURI`** → `0` 입력 → 위 URL + `0` 이 나오면 OK.

에셋 상세: [assets/nft/README.md](../../assets/nft/README.md)

### (선택) `setWhitelist`

본인 주소를 whitelist에 추가:

```text
accounts: ["0x내주소"]
allowed: true
```

---

## 4. 테스트 mint

컨트랙트 `mintPrice`는 **0.001 ETH**입니다. Remix에서 `mint` 호출 시 **Value**에 이 금액을 넣어야 합니다.

1. Deploy & Run 상단 **Value** 설정 (아래 [ETH 단위](#eth-단위-ether--gwei--wei) 참고)
2. 주황색 **`mint`** → **transact**
3. MetaMask Confirm — 보내는 금액이 **0.001 ETH + gas**인지 확인
4. **`totalMinted`** Read → `1`
5. **`ownerOf`** `0` → 본인 주소

> **Deploy**는 Value **0**. **mint** / **whitelistMint**만 Value **0.001 ETH** 필요.  
> `MAX_PER_WALLET = 3`은 **지갑당 mint 횟수**이지 Value 금액이 **아닙니다** (3 ETH 넣지 않기).

### ETH 단위: Ether · Gwei · Wei

이더리움 ETH는 **소수점 단위**로 나뉩니다. Remix **Value** 옆 드롭다운에서 단위를 고릅니다.

| 단위 | 설명 | mint 0.001 ETH 예시 |
| --- | --- | --- |
| **ether** | 사람이 읽기 쉬운 단위 (MetaMask에 표시되는 단위) | `0.001` |
| **gwei** | 가스 가격 표시에 자주 씀. 1 ether = 10⁹ gwei | `1000000` |
| **wei** | 최소 단위. 1 ether = 10¹⁸ wei | `1000000000000000` |

관계: **1 ether = 1,000,000,000 gwei = 1,000,000,000,000,000,000 wei**

### Remix Value 입력 (소수점 버그 우회)

Remix Value 칸에 `0.001`을 넣으면 `001`로 바뀌거나 `0`만 남는 UI 버그가 있을 수 있습니다. 아래 중 하나를 쓰세요.

| 방법 | Value | 단위 |
| --- | --- | --- |
| **권장** | `1000000000000000` | **wei** |
| 대안 | `1000000` | **gwei** |
| 소수 입력 | `.001` (`0.` 없이) | ether |

MetaMask Confirm 팝업에서 **0.001 ETH**로 보이면 맞습니다. **3 ETH** 등으로 보이면 Value를 다시 확인하세요.

### mint 실패 시

| 에러 / 증상 | 원인 | 해결 |
| --- | --- | --- |
| `Insufficient payment` | Value 0 또는 부족 | wei `1000000000000000` |
| `insufficient funds` … `want 3000000000000000000` | Value를 **3 ether**로 잘못 입력 | **0.001** ether (또는 wei 위 값) |
| Gas estimation errored | 위와 동일 | Force sending **누르지 말고** Value 수정 |

---

## 5. Etherscan 확인

```
https://sepolia.etherscan.io/address/YOUR_CONTRACT_ADDRESS
```

- Contract creation tx
- Internal tx / mint tx

**NFT 이미지** (tokenId `0` = 첫 mint):

```text
https://sepolia.etherscan.io/nft/YOUR_CONTRACT_ADDRESS/0
```

`setBaseURI` 후 **수 분** 지나면 Hero 카드 이미지가 표시될 수 있습니다. 안 보이면 §3 `tokenURI` Read부터 확인.

> metadata `image`는 **JPEG** (`.jpg`) — Etherscan·MetaMask 호환. WebP만 쓰면 이미지가 안 보일 수 있습니다.  
> repo의 metadata·`images/*.jpg`를 GitHub **main에 push**한 뒤, Etherscan NFT 페이지에서 **Refresh NFT Metadata**(로그인) 또는 재시도.

**(선택) Verify**: Remix Plugin "Etherscan Verification" 또는 수동 verify.

---

## 체크리스트

- [ ] Sepolia에 컨트랙트 배포됨
- [ ] `setBaseURI` — GitHub metadata URL 설정
- [ ] mint 1회 성공
- [ ] Contract address 저장 (.env 준비)
- [ ] (선택) Etherscan NFT 페이지에서 이미지 확인

---

## 다음

→ [05-frontend-mint.md](05-frontend-mint.md)
