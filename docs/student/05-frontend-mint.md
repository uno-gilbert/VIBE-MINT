# 05. 프론트엔드 — MetaMask 민팅 DApp

이 문서는 **Ship(배포)의 마지막 구간**입니다.  
Remix 버튼 대신 **웹페이지(민팅 사이트)**에서 MetaMask로 mint하고, **Etherscan·MetaMask**에서 NFT를 확인합니다.

> **한 줄**: `.env`에 컨트랙트 주소만 넣으면 → **Connect Wallet → Mint (0.001 ETH)** 로 브라우저에서 민팅합니다.

```text
브라우저 DApp  →  MetaMask 승인  →  Sepolia 컨트랙트 mint  →  Etherscan / MetaMask에서 확인
```

---

## 학습 목표

이 장을 끝내면 다음을 할 수 있어야 합니다.

- [ ] `frontend/starter`에 Sepolia **배포 주소**를 연결한다
- [ ] **Connect Wallet → Mint** UI로 민팅에 성공한다
- [ ] Etherscan에서 mint **트랜잭션**을 확인한다
- [ ] (선택) MetaMask NFT 탭 또는 Etherscan NFT 페이지에서 토큰을 본다

**전제**: [04-deploy-sepolia.md](04-deploy-sepolia.md)에서 컨트랙트를 Sepolia에 배포하고 **Contract Address**를 저장해 둔 상태

**대략 시간**: 환경 설정·실행 15분 + mint·확인 15분 + (선택) UI 보완 10~20분

---

## 1. DApp이란? (먼저 이해하기)

### 쉬운 비유

| 구분 | 비유 | 오늘 |
| --- | --- | --- |
| **스마트 컨트랙트** | 자동판매기 (규칙·가격이 코드로 고정) | Sepolia의 `VibeMintNFT` |
| **Remix** | 기술자가 기계 버튼을 직접 누르는 것 | Stage·배포 때 사용 |
| **DApp (프론트)** | 손님용 터치스크린 UI | **지금 만드는 민팅 사이트** |
| **MetaMask** | 결제·서명용 지갑 | Connect / Confirm |

손님이 보는 화면은 브라우저이고,  
**실제 mint는 여전히 블록체인 컨트랙트**에서 일어납니다.  
프론트는 「지갑을 연결하고, 컨트랙트 `mint()`를 **대신 호출**」해 줄 뿐입니다.

### 오늘 쓰는 스택 (이름만 알아도 OK)

| 기술 | 역할 |
| --- | --- |
| **Vite + React** | 로컬에서 빠르게 뜨는 웹 UI |
| **wagmi + viem** | MetaMask 연결 · 컨트랙트 읽기/쓰기 |
| **`.env`** | 「어느 컨트랙트에 mint할지」주소 저장 |

코드 위치: `frontend/starter/`  
더 꾸민 예시: `frontend/solution/`

---

## 2. 시작 전 확인 (3가지)

| # | 확인 | 없으면 |
| --- | --- | --- |
| 1 | Sepolia에 **배포된** Contract Address | → [04-deploy-sepolia.md](04-deploy-sepolia.md) |
| 2 | MetaMask **Sepolia** + 테스트 ETH | Faucet으로 충전 (mint 0.001 + gas) |
| 3 | **Chrome** + MetaMask 확장 | 다른 브라우저는 확장이 없을 수 있음 |
| 4 | Node.js **v20+** | `node -v`로 확인 |

주소를 메모장에 붙여 두고 시작하세요.  
예: `0xAbCd...` (Remix Deployed Contracts에서 복사)

> **Remix VM에 올린 주소는 안 됩니다.**  
> 반드시 **Injected Provider → Sepolia**로 배포한 주소여야 합니다.

---

## 3. 환경 설정 — `.env`에 주소 넣기

### 따라하기

터미널에서 프로젝트 루트 기준:

```bash
cd frontend/starter
cp .env.example .env
```

`.env` 파일을 Cursor(또는 메모장)로 열고 **한 줄**을 고칩니다.

```text
VITE_CONTRACT_ADDRESS=0x여기에_Sepolia_배포주소
```

### 예시

```text
VITE_CONTRACT_ADDRESS=0x1234567890abcdef1234567890abcdef12345678
```

| 주의 | 설명 |
| --- | --- |
| `0x`로 시작 | Remix에서 복사한 그대로 |
| 따옴표 | 보통 **없이** 입력 |
| 공백 | 주소 앞뒤에 공백·줄바꿈 없게 |
| placeholder | `0x0000…0000` 이면 아직 안 바꾼 것 |
| 저장 후 | 아래 `npm run dev`를 **재시작**해야 반영되는 경우 많음 |

### 이 한 줄이 하는 일

프론트 코드(`contract.js` 등)가 시작할 때  
`VITE_CONTRACT_ADDRESS`를 읽어 **「이 주소의 `mint()`를 호출」**합니다.

주소를 틀리면:

- Connect는 되어도 mint가 실패하거나  
- **전혀 다른(없는) 컨트랙트**를 찌르게 됩니다.

- [ ] `.env`에 Sepolia 컨트랙트 주소 입력·저장

---

## 4. 로컬 서버 실행

### 따라하기

`frontend/starter` 폴더에서:

```bash
npm install
npm run dev
```

| 명령 | 쉬운 설명 |
| --- | --- |
| `npm install` | 필요한 라이브러리 받기 (처음 한 번, 1~몇 분) |
| `npm run dev` | 내 컴퓨터에서 웹서버 켜기 |

터미널에 비슷한 문구가 보입니다.

```text
  ➜  Local:   http://localhost:5173/
```

**Chrome**으로 그 주소를 엽니다.

> 포트가 `5173`이 아닐 수 있습니다. 터미널에 나온 **Local 주소**를 그대로 쓰세요.

### 페이지가 열리면

- **VibeMint** 제목과 **Connect Wallet** 버튼이 보이면 OK  
- `.env` 주소가 비어 있으면 빨간 안내:  
  `.env에 VITE_CONTRACT_ADDRESS를 설정하세요.`

주소를 고친 뒤에는:

1. 터미널에서 `Ctrl + C`로 서버 중지  
2. 다시 `npm run dev`  
3. 브라우저 새로고침

- [ ] 로컬 DApp 페이지가 열림

---

## 5. Connect · Mint (핵심 실습)

### Step A — Connect Wallet

1. 페이지에서 **Connect Wallet** 클릭  
2. MetaMask 팝업 → 계정 선택 → **연결(Connect / 다음 / 확인)**  
3. 화면에 지갑 주소 일부 (`0x12ab…90cd`)가 보이면 연결 성공  

| 화면 | 의미 |
| --- | --- |
| Connect Wallet | 사이트 ↔ 지갑 **연결** |
| Disconnect | 연결 해제 |
| 주소 표시 | 어떤 계정으로 서명할지 확정됨 |

### Step B — 네트워크가 Sepolia인지

Chain ID **11155111** = Sepolia.

| 보이는 것 | 할 일 |
| --- | --- |
| 주소만 정상 표시 | Sepolia일 가능성 높음 → Mint 진행 |
| 「Sepolia로 전환 필요」 | MetaMask에서 **Sepolia** 선택 또는 화면의 Switch |
| 메인넷 / 다른 테스트넷 | **반드시 Sepolia로 변경** 후 mint |

잘못된 네트워크에서 mint하면 **실패**하거나,  
의도하지 않은 체인에 요청이 갑니다.

### Step C — Mint (0.001 ETH)

1. **Mint (0.001 ETH)** 클릭  
2. MetaMask 팝업:
   - 보낼 금액 **0.001 ETH**
   - **가스비(예상)** 별도
3. 금액·네트워크(Sepolia) 확인 → **Confirm**  
4. 버튼이 `Minting…` → 잠시 대기  
5. **Mint 성공!** 메시지 / Tx 해시 일부 표시  

| 상태 | 의미 |
| --- | --- |
| Minting… | 지갑 승인 대기 또는 체인 확인 중 |
| Success | Sepolia에 mint tx가 **포함**됨 |
| 빨간 에러 | revert·거절·네트워크 문제 (아래 표 참고) |

### Step D — 성공 확인 (Etherscan)

Tx 해시가 보이면 Sepolia Etherscan에서 검색하거나:

```text
https://sepolia.etherscan.io/tx/여기에_tx_해시
```

컨트랙트 페이지:

```text
https://sepolia.etherscan.io/address/여기에_컨트랙트주소
```

추가로 Remix(Injected Provider)나 다른 도구로:

| 확인 | 기대 |
| --- | --- |
| `totalMinted` | 이전보다 **+1** |
| `ownerOf(최신 tokenId)` | **내 지갑** 주소 |

- [ ] Connect / Disconnect 동작
- [ ] Mint 트랜잭션 success
- [ ] Etherscan에서 mint tx 확인

---

## 6. 프론트에서 무슨 일이 일어나나? (이해용)

코드를 외울 필요는 없습니다. **흐름만** 보면 됩니다.

```text
1. Connect  → wagmi가 MetaMask와 연결
2. Mint 클릭 → writeContract({ functionName: "mint", value: 0.001 ETH })
3. MetaMask  → 사용자가 서명·가스 승인
4. Sepolia   → 컨트랙트 mint() 실행 → NFT 소유권 기록
5. UI        → success / tx 해시 표시
```

| 용어 | 쉬운 설명 |
| --- | --- |
| **ABI** | 컨트랙트 함수 설명서 (프론트가 `mint`를 어떻게 부를지 앎) |
| **payable mint** | mint 호출 때 **ETH를 같이 보냄** |
| **gas** | 트랜잭션 처리 수수료 (테스트 ETH로 지불) |
| **tx hash** | 그 거래의 **영수증 번호** |

Remix의 주황 `mint` + Value 0.001과 **같은 일**을,  
버튼 한 번으로 하는 것이 DApp입니다.

---

## 7. (선택) Cursor로 UI 보완

**Connect → Mint 성공**이면 이 장의 핵심은 달성입니다.  
시간이 남으면 UI를 다듬어 보세요.

### 프롬프트

[05-frontend-connect.md](../prompts/05-frontend-connect.md) 를 Cursor에 붙여넣고 `@frontend/starter` 멘션.

예: supply 표시, 에러 메시지 개선, Etherscan 링크, pending 상태 문구 등.

### 정답 참고

`frontend/solution/` — 발행량·화이트리스트 mint·Etherscan 링크 등이 들어간 예시

> 전체 프로젝트를 **처음부터 다시 scaffold**하지 마세요.  
> starter 구조를 유지한 채 **필요한 파일만** 수정하는 것이 규칙입니다.

---

## 8. mint한 NFT 확인하기

민팅이 체인에 **기록**됐는지 확인하는 것이 Ship의 마지막 단계입니다.

> **OpenSea 테스트넷 종료 (2025-07-24)**  
> OpenSea는 OS2 출시와 함께 **testnets.opensea.io 등 테스트넷 전용 환경 지원을 중단**했습니다.  
> Sepolia 실습 NFT는 **OpenSea 테스트넷에서 더 이상 볼 수 없습니다.** 아래 **Etherscan · MetaMask**로 확인하세요.

### OpenSea는 여전히 뭔가?

| 구분 | 설명 |
| --- | --- |
| **OpenSea(오픈씨)** | 지갑·컨트랙트를 읽어 NFT 카드처럼 **보여주는 마켓** (주로 **메인넷**) |
| **민팅** | 우리 DApp / Remix가 컨트랙트 `mint()`를 호출해 **발행** |
| **관계** | 민팅 ≠ OpenSea 업로드. 마켓은 온체인 데이터를 **나중에 읽어 표시** |

수업에서 BAYC·Azuki를 구경하는 [opensea.io](https://opensea.io/)는 **메인넷** 마켓입니다.  
오늘 VibeMint(Sepolia) 확인에는 **Etherscan**을 씁니다.

### 따라하기 — Etherscan (권장)

#### 1) mint 트랜잭션 확인

DApp mint 성공 후 나온 tx 해시, 또는 MetaMask Activity에서:

```text
https://sepolia.etherscan.io/tx/{TX_HASH}
```

| 확인 | OK |
| --- | --- |
| Status | Success |
| To | 내 `VITE_CONTRACT_ADDRESS` |
| Value | 0.001 ETH (mintPrice) |

#### 2) 컨트랙트 · 토큰 소유 확인

**컨트랙트 페이지**

```text
https://sepolia.etherscan.io/address/{CONTRACT_ADDRESS}
```

**특정 NFT (tokenId `0` = 첫 mint)**

```text
https://sepolia.etherscan.io/nft/{CONTRACT_ADDRESS}/{TOKEN_ID}
```

| mint 횟수 | tokenId |
| --- | --- |
| 1번째 성공 | `0` |
| 2번째 | `1` |
| 3번째 | `2` |

Remix 또는 Etherscan **Read Contract**에서 `ownerOf(0)` → 내 주소면 소유권 확인 완료.

### 따라하기 — MetaMask NFT 탭 (선택)

1. MetaMask → **NFTs** 탭 (또는 **자산 → NFTs**)
2. 네트워크 **Sepolia** 선택
3. **Import NFT** / 자동 표시된 VibeMint 확인  
   - Contract address: 배포 주소  
   - Token ID: `0`

안 보여도 Etherscan `ownerOf`가 맞으면 **민팅은 성공**한 것입니다.

### 판단 기준

| 상황 | 판단 |
| --- | --- |
| Etherscan mint tx Success + `ownerOf(0)` = 나 | **민팅 성공** ✅ |
| OpenSea testnet 접속 | **2025-07-24부터 지원 종료** — 사용하지 않음 |
| 이미지 없음 | `setBaseURI` placeholder면 정상 — **소유권 확인이 우선** |

> **OpenSea에 없어도, Etherscan이 맞으면 Ship의 mint는 성공입니다.**

### 이 단계에서 이해하는 것

| 포인트 | 내용 |
| --- | --- |
| DApp mint | 체인에 NFT **발행** |
| Etherscan | 발행·소유를 **증명** (Sepolia 실습의 기본 확인 도구) |
| OpenSea (메인넷) | 2차 마켓 UI · [Studio](https://opensea.io/studio) 발행 도구 — 유명 컬렉션 **구경·학습용** |
| OpenSea testnet | **종료됨** — Sepolia 확인에 쓰지 않음 |
| OpenSea Studio | **메인넷** 컬렉션 발행 — Sepolia VibeMint와 **무관** ([§9](#9-수업-후--opensea-studio로-nft-발행-선택)) |

- [ ] Etherscan에서 mint tx Success 확인  
- [ ] `ownerOf(0)` 또는 Etherscan NFT 페이지로 소유 확인  

---

## 9. (수업 후) OpenSea Studio로 NFT 발행 (선택)

수업 **마지막 10분** 또는 **수업 후** 참고용입니다.  
오늘 Sepolia 실습과 **별개** — [OpenSea Studio](https://opensea.io/studio)는 **메인넷** 컬렉션 발행·관리 도구입니다.

### OpenSea Studio란?

| 구분 | 설명 |
| --- | --- |
| **URL** | [opensea.io/studio](https://opensea.io/studio) |
| **역할** | 지갑 연결 → 컬렉션 생성 · 드롭 설정 · **민팅 페이지** 제공 |
| **대상 체인** | Ethereum, Base, Polygon, Arbitrum 등 **메인넷·L2** (Sepolia **미지원**) |
| **비유** | 오늘 만든 **DApp + 컨트랙트** 대신, OpenSea UI로 발행하는 **크리에이터 경로** |

OpenSea는 **자기 지갑·커스터디 없이** 연결된 지갑으로 온체인 자산을 탐색·거래·**민팅**할 수 있는 P2P 마켓입니다. Studio는 그중 **발행(creation/mint)** 쪽 도구입니다.

### 오늘 수업 vs OpenSea Studio

| | 오늘 VibeMint (Sepolia) | OpenSea Studio (메인넷) |
| --- | --- | --- |
| **경로** | 개발자 — Solidity + Remix + DApp | 크리에이터 — Studio UI |
| **컨트랙트** | 직접 작성·배포 (`VibeMintNFT`) | Studio **신규 배포** 또는 **owner 지갑으로 기존 컬렉션 관리** |
| **민팅** | Remix / 우리 DApp `mint()` | Studio 민팅 페이지 또는 드롭 |
| **확인** | **Etherscan Sepolia** | [opensea.io](https://opensea.io) 컬렉션 페이지 |
| **Sepolia NFT** | ✅ 오늘 실습 | ❌ Studio·마켓에 **표시 안 됨** |

> **OpenSea 테스트넷**(`testnets.opensea.io`)은 2025-07-24 **종료**되었습니다.  
> Sepolia 확인은 Etherscan, **메인넷 발행**은 Studio·메인넷 Etherscan을 봅니다.

### Studio 발행 흐름 (개념)

1. [opensea.io/studio](https://opensea.io/studio) 접속 → **Connect Wallet** (MetaMask)
2. **Create new** — Studio가 **새 컨트랙트 배포** (오늘 VibeMint처럼 **이미 배포한** 컨트랙트는 **방법 B** — owner 지갑 연결 후 목록에서 선택)
3. **체인 선택** — Ethereum, Base, Polygon 등 (가스비·대상 사용자에 맞게)
4. **에셋 업로드** — 이미지·메타데이터 (IPFS 등 Studio 안내 따름)
5. **로열티·민팅 가격·supply** 설정
6. **Deploy / Mint / Drop** — 지갑에서 트랜잭션 승인

자세한 UI는 OpenSea [Learn Center](https://opensea.io/learn) · [개발자 문서](https://docs.opensea.io)를 참고하세요.

### 우리가 만든 컨트랙트를 OpenSea에 올리려면?

**메인넷**에 Audit·배포된 ERC-721은 OpenSea가 `tokenURI`·metadata를 읽어 **자동으로 컬렉션 페이지를 만들 수 있습니다** (반영까지 수 시간~수 일).

| 순서 | 할 일 |
| --- | --- |
| 1 | Stage 3 + **전문 Audit** |
| 2 | **Ethereum·Base 등 메인넷** 배포 (Sepolia 아님) |
| 3 | `setBaseURI` — **IPFS** 등 영구 metadata (GitHub raw는 프로덕션 비권장) — 따라하기: [06-ipfs-metadata.md](06-ipfs-metadata.md) |
| 4 | **최소 1회 mint** — 소유 확인 (메인넷 Etherscan) |
| 5 | 아래 **방법 A 또는 B**로 OpenSea에서 확인·편집 |

**오늘 Sepolia 주소·VibeMint는 이 단계에 해당하지 않습니다.**

#### 방법 A — OpenSea에서 컬렉션 **검색** (자동 인덱싱)

OpenSea는 지원 체인에서 mint·transfer가 발생한 ERC-721을 **크롤링**합니다. 별도 “등록” 버튼이 없어도 컬렉션이 생길 수 있습니다.

1. [opensea.io](https://opensea.io) 접속
2. 검색창에 **컨트랙트 주소** 입력 (예: `0xabc…`)
3. 컬렉션 페이지가 보이면 → `tokenURI`·이미지가 정상인지 확인
4. 안 보이면 → mint·metadata·체인 지원 여부 확인 후 **몇 시간~하루** 재시도

컬렉션 URL 예시:

```text
https://opensea.io/collection/{slug}
https://opensea.io/assets/ethereum/{CONTRACT_ADDRESS}/{TOKEN_ID}
```

> 인덱싱 전에는 검색에 안 나올 수 있습니다. **mint 1건 + 유효한 metadata**가 선행 조건입니다.

#### 방법 B — [OpenSea Studio](https://opensea.io/studio)에서 **소유자 지갑으로 관리**

Studio에 “컨트랙트 주소만 붙여 넣기”하는 **별도 Import 메뉴**가 있는 구조가 아닙니다.  
**배포자(또는 `Ownable` owner) 지갑**을 연결하면, OpenSea가 **그 지갑과 연결된 컬렉션**을 Studio 목록에 보여 줍니다.

VibeMint는 OpenZeppelin **Ownable** — Remix로 배포한 **그 지갑** = owner.

1. [opensea.io/studio](https://opensea.io/studio) → **Connect Wallet**
2. 네트워크를 **배포한 메인넷**으로 맞춤 (Ethereum, Base 등)
3. Studio 홈에 **기존 컬렉션(Existing collections)** 목록 확인
4. VibeMint 컬렉션 선택 → **Collection Details**에서 이름·설명·카테고리·로열티 등 편집  
   → [컬렉션 상세 편집 가이드](https://support.opensea.io/en/articles/8867025-how-do-i-edit-my-collection-details)
5. (선택) **Create new**는 Studio가 **새 컨트랙트를 배포**하는 경로 — 오늘처럼 **이미 만든** `VibeMintNFT`와는 다른 흐름

| 상황 | 조치 |
| --- | --- |
| Studio에 컬렉션이 안 보임 | **배포한 지갑**으로 연결했는지, **메인넷**인지, mint가 1건이라도 있는지 확인 |
| 편집 권한 없음 | owner가 아닌 지갑 — 배포 계정 또는 `transferOwnership` 받은 지갑 사용 |
| Sepolia 배포 | Studio·메인넷 마켓 **대상 아님** |

#### (선택) 컬렉션 대표 이미지·설명 — `contractURI`

토큰 metadata(`tokenURI`)와 별도로, **컬렉션 페이지**용 배너·설명은 `contractURI()`로 줄 수 있습니다 ([OpenSea contract-level metadata](https://docs.opensea.io/docs/contract-level-metadata)).

```solidity
function contractURI() public view returns (string memory) {
    return "ipfs://..."; // name, description, image, banner_image 등 JSON
}
```

VibeMint Stage 3에는 **없음** — 메인넷 전에 Audit과 함께 추가 검토.

#### 방법 A vs B 한눈에

| | 방법 A (검색) | 방법 B (Studio) |
| --- | --- | --- |
| **목적** | 컬렉션이 **올라왔는지** 확인 | **설명·로열티·URL** 등 **편집** |
| **필요** | mint + metadata | **owner 지갑** + Studio 연결 |
| **Sepolia** | ❌ | ❌ |

### 강사·수강생 한 줄 정리

| 질문 | 답 |
| --- | --- |
| Sepolia NFT가 Studio에 안 보여요 | **정상** — Studio는 테스트넷 미지원 |
| Studio에 내 컬렉션이 없어요 | **배포 owner 지갑** + **메인넷** + mint 1건 이상 — 주소 Import 메뉴가 아니라 **소유권 연동** |
| Studio = 오늘 DApp 대체? | **아니요** — 개발 학습은 오늘 경로, **실서비스 발행**은 Studio 또는 메인넷 배포 후 마켓 |
| 메인넷 전에? | **전문 Audit 필수** — Studio로 올려도 컨트랙트 취약점은 그대로 |

---

## 10. 막혔을 때

| 증상 | 원인 · 해결 |
| --- | --- |
| `.env` 안내 에러 | 주소 미설정 → 수정 후 **dev 서버 재시작** |
| Connect 안 됨 | Chrome + MetaMask, 팝업 차단 해제, 페이지 새로고침 |
| Wrong network / Sepolia 필요 | MetaMask에서 **Sepolia** 선택 |
| mint 실패 · ETH 부족 | Faucet으로 Sepolia ETH 충전 |
| mint revert (public disabled) | Remix에서 `setPublicMintEnabled(true)` (owner) |
| `gas limit too high` (Infura RPC) | MetaMask Sepolia **RPC 변경** → `https://ethereum-sepolia.publicnode.com` · dev 서버 재시작 · Remix에서 mint 가능한지 확인 |
| Chain ID를 못 가져옴 | `rpc.sepolia.org` **404** — RPC를 `https://1rpc.io/sepolia` 등으로 교체, Chain ID **11155111** 수동 입력 |
| 이미 3개 mint | 지갑당 cap — 다른 계정 또는 whitelist 경로 |
| 주소는 맞는데 이상 동작 | **Remix VM 주소**를 넣지 않았는지 확인 (Sepolia 주소여야 함) |
| `npm install` 실패 | Node v20+, 네트워크, `frontend/starter`에서 실행했는지 |
| NFT가 MetaMask에 안 보임 | Etherscan `ownerOf(0)` · NFT 페이지로 먼저 확인 |

### 스스로 점검하는 질문

1. `.env` 주소가 **Sepolia 배포 주소**와 글자 단위로 같은가?  
2. MetaMask 네트워크가 **Sepolia**인가?  
3. 주소를 고친 뒤 `npm run dev`를 **다시** 켰는가?

---

## 11. 이 장 마무리 체크리스트

- [ ] `.env`에 `VITE_CONTRACT_ADDRESS` 설정  
- [ ] `npm run dev`로 로컬 페이지 접속  
- [ ] Connect Wallet 성공  
- [ ] Sepolia에서 Mint (0.001 ETH) success  
- [ ] Etherscan에서 mint tx 확인  
- [ ] (선택) UI 보완 또는 MetaMask NFT / Etherscan NFT 페이지 확인  

---

## 마무리

오늘 완성한 DApp은 **교육·Sepolia 테스트넷 전용**입니다.  
프로덕션(메인넷) 배포 전 **전문 스마트 컨트랙트 Audit**을 받으세요.

```text
Intent → Spec → Generate → Review → Ship
```

프론트 mint까지 했다면 **Ship** 구간을 브라우저에서 닫은 것입니다.  
다만 **Review(Audit)를 생략한 채** 메인넷으로 가지 마세요.

### 수업 후 — OpenSea Studio (선택)

메인넷에서 컬렉션을 **마켓에 올리는** 다음 단계는 [OpenSea Studio](https://opensea.io/studio)입니다.  
Sepolia VibeMint와는 **별개** — 자세한 흐름은 [§9 OpenSea Studio](05-frontend-mint.md#9-수업-후--opensea-studio로-nft-발행-선택) 참고.

### 관련 문서

| 문서 | 내용 |
| --- | --- |
| [04-deploy-sepolia.md](04-deploy-sepolia.md) | Sepolia 배포 · 주소 확보 |
| [05-frontend-connect.md](../prompts/05-frontend-connect.md) | (선택) UI 보완 프롬프트 |
| [00-walkthrough.md](00-walkthrough.md) | 전체 실습 Part 7 |
| `frontend/starter/README.md` | starter 요약 |
| `frontend/solution/` | 참고 구현 |
