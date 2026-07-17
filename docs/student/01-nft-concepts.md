# 01. NFT 스마트 컨트랙트 이해

## 학습 목표

- **NFT가 무엇인지** 일상 언어로 설명할 수 있다
- **대체 가능 vs 쪼갤 수 있음** 차이를 구분한다
- **ERC-721 vs ERC-1155** 차이를 이해한다
- OpenZeppelin ERC721 기본 구조를 안다
- **유명 NFT(BAYC·베이씨 / Azuki·아즈키)** 민팅 규칙을 Spec 항목으로 옮길 수 있다
- AI로 컨트랙트 **역분석** 실습

---

## 1. NFT란? (먼저 이해하기)

### NFT = Non-Fungible Token (대체 불가능한 토큰)

![대체 가능 vs 대체 불가능 (NFT)](images/nft-fungible-vs-nonfungible.png)

| 구분 | 설명 | 예시 |
| --- | --- | --- |
| **대체 가능** (Fungible · **펀저블**) | 서로 바꿔도 **가치·쓰임이 같음** | 내 1 ETH ↔ 남의 1 ETH |
| **대체 불가능** (Non-Fungible) | 각각 고유함 | NFT #3 ↔ #7 (가치 다를 수 있음) |

![대체 가능 = 가치가 같아서 바꿔도 된다](images/fungible-value-same.png)

![ETH · ERC-721 · ERC-1155 한눈에 비교](images/fungible-three-types.png)

**한 줄 정리**: NFT는 블록체인에 **「이 디지털 자산의 주인이 누구인지」** 기록해 두는 **디지털 소유권 증명**입니다.

### 대체 가능 vs 쪼갤 수 있음 — 같은 말이 아닙니다

헷갈리기 쉬운 **두 가지 질문**을 구분합니다.

| 개념 | 영어 | 묻는 것 | 예 |
| --- | --- | --- | --- |
| **대체 가능 / 불가능** | Fungible | **서로 바꿔도 되나?** | 1 ETH ↔ 1 ETH (됨) · NFT #1 ↔ #2 (안 됨) |
| **쪼갤 수 있음 / 없음** | Divisible | **잘라서 일부만 줄 수 있나?** | 1 ETH → 0.001 ETH (됨) · NFT #5 “반쪽” (안 됨) |

![대체 가능 vs 쪼갤 수 있음 — 4가지 조합](images/fungible-divisible-matrix.png)

| | **쪼갤 수 있음** | **쪼갤 수 없음** |
| --- | --- | --- |
| **대체 가능** | ETH, USDC (같은 종류·나눠서 전송) | 희귀 동전 1호 한 장 (같은 종류라도 그 장은 통째로) |
| **대체 불가능** | ERC-1155 (검 10자루 중 3자루만 전송) | **ERC-721 NFT** (#0, #1 — 통째로만, **오늘 워크숍 ★**) |

![ERC-1155: 같은 종류(검)는 대체 가능, 다른 종류(방패)는 불가](images/erc1155-semi-fungible.png)

**수업용 한 줄**:

> **대체 불가능** = “이 NFT와 저 NFT는 서로 바꿀 수 없다”  
> **쪼갤 수 없음** = “NFT #3을 반만 보낼 수 없다”  
> 둘 다 NFT에 자주 해당하지만, **같은 말은 아닙니다.**

### NFT에 무엇이 담기나?

![NFT 구조 — 온체인 vs 오프체인](images/nft-onchain-offchain.png)

| 위치 | 저장 내용 | 특징 |
| --- | --- | --- |
| **온체인** | tokenId, owner, tokenURI(링크) | 소유권·거래 기록, 위조 어려움 |
| **오프체인** | name, image, description, attributes | IPFS·웹 URL에 JSON 저장 |

### NFT로 할 수 있는 것 — Mint(민팅) 흐름

![Mint(민팅) 흐름](images/nft-mint-flow.png)

| 할 수 있는 것 | 설명 |
| --- | --- |
| **민팅(Mint)** | 새 NFT 발행 — **오늘 실습 핵심** |
| **소유·전송** | 지갑 간 NFT 보내기 |
| **거래** | OpenSea 등 마켓에서 사고팔기 |
| **조건 부여** | 화이트리스트, 가격, 수량 제한 (컨트랙트로 구현) |

### 왜 스마트 컨트랙트가 필요한가?

NFT 규칙을 **코드로 고정**하기 위해서입니다.

| 사람이 정하는 규칙 | 컨트랙트가 하는 일 |
| --- | --- |
| "최대 100개만 발행" | `maxSupply = 100` |
| "0.001 ETH 내야 mint" | `mintPrice` 검증 |
| "지갑당 3개까지만" | `mintedCount` cap |
| "긴급 중지" | `pause()` |

> 오늘 만드는 **VibeMint**도 이 규칙들을 스마트 컨트랙트에 담습니다.

---

## 2. ERC 표준 (NFT를 코드로 만드는 규칙)

블록체인 위에서 NFT를 만들려면 **공통 규칙(표준)**이 필요합니다.  
이더리움에서는 **ERC(Ethereum Request for Comments)** 로 표준이 정해져 있습니다.

### ERC란?

- **E**thereum **R**equest for **C**omments
- 지갑·마켓·앱이 모두 이해할 수 있는 **약속된 인터페이스**
- ERC-20 = 대체 가능 토큰 (일반 코인)
- **ERC-721** = 대체 불가 NFT ← **오늘 사용**
- **ERC-1155** = 한 컨트랙트에 여러 종류 토큰

### ERC-721 vs ERC-1155

![ERC-721 vs ERC-1155](images/erc721-vs-erc1155.png)

| | ERC-721 | ERC-1155 |
| --- | --- | --- |
| **단위** | 토큰마다 고유 ID (#0, #1, …) | 한 컨트랙트에 여러 token type |
| **비유** | 명화 한 점 한 점 | 게임 인벤토리 (검 1개, 방패 3개) |
| **대표 사용** | PFP, 아트 NFT (BAYC·베이씨, Azuki·아즈키) | 게임 아이템, 다종류 에셋 |
| **본 워크숍** | **★ 사용** | 개념만 |

### ERC-721 핵심 함수 (꼭 알아둘 것)

| 함수 | 하는 일 |
| --- | --- |
| `balanceOf(owner)` | 이 지갑이 NFT 몇 개 보유? |
| `ownerOf(tokenId)` | 이 번호 NFT 주인은 누구? |
| `safeTransferFrom` | NFT를 안전하게 전송 |
| `tokenURI(tokenId)` | 메타데이터 JSON 주소 (이미지·이름) |
| `approve` / `setApprovalForAll` | 마켓(OpenSea)이 대신 옮기도록 허용 |

### OpenZeppelin — 검증된 ERC 구현체

![VibeMint 컨트랙트 구조](images/vibemint-architecture.png)

직접 ERC-721 전체를 짜기보다, **OpenZeppelin** 라이브러리를 씁니다.

| 모듈 | 역할 |
| --- | --- |
| ERC721 | mint, transfer, tokenURI 등 NFT 기본 |
| Ownable | `onlyOwner` — 배포자만 설정 변경 |
| Pausable | `whenNotPaused` — 긴급 시 mint 중지 |
| ReentrancyGuard | `withdraw` 보안 |

---

## 3. 유명 NFT 프로젝트 분석 (벤치마킹)

개념만 외우지 말고, **실제 유명 컬렉션**이 어떤 민팅 규칙을 쓰는지 봅니다.  
목표는 **BAYC(베이씨)**·**Azuki(아즈키)**를 **똑같이 복제**하는 것이 아니라,  
그 규칙을 **VibeMint Spec 항목**으로 번역하는 연습입니다.

> **한 줄**: 누가 / 얼마에 / 몇 개까지 / 언제 멈출 수 있는지가 **컨트랙트에 어떻게 박히는지** 봅니다.

### 이름 한글 발음 (수업용)

| 영어 / 약어 | 한글 발음 | 참고 |
| --- | --- | --- |
| **BAYC** | **베이씨** (또는 베익) | Bored Ape Yacht Club의 약자 |
| **Bored Ape Yacht Club** | **보어드 에이프 요트 클럽** | “Bored Ape” = 심심한 원숭이 |
| **Yuga Labs** | **유거 랩스** | BAYC를 운영하는 스튜디오 |
| **MAYC** | **메이씨** | Mutant Ape Yacht Club (돌연변이 에이프) |
| **Otherside** | **아더사이드** | Yuga의 메타버스/게임 IP |
| **Azuki** | **아즈키** | 일본어 あずき(팥)에서 온 이름 |
| **The Garden** | **더 가든** | Azuki 커뮤니티·세계관 공간 |
| **OpenSea** | **오픈씨** | NFT 마켓플레이스 |
| **PFP** | **피에프피** | Profile Picture (프로필 사진 NFT) |
| **whitelist** | **화이트리스트** | 사전 허용 명단 |
| **mint** | **민트** | 새로 발행하다 |

> 약어는 현장마다 조금 다르게 읽습니다. 수업에서는 **베이씨 / 아즈키 / 오픈씨**로 통일해도 충분합니다.

### 왜 벤치마킹하나?

| 이유 | 설명 |
| --- | --- |
| Spec의 재료 | “느낌으로 NFT 만들어줘”보다 **실제 프로젝트에 있는 규칙**이 Spec이 된다 |
| 오후 Generate 연결 | `maxSupply`, whitelist, pause 등이 Stage 0~3에 그대로 등장 |
| 오해 줄이기 | 그림·커뮤니티와 **민팅 규칙(온체인)** 을 구분한다 |

### 왜 이 프로젝트들이 유명해졌나?

수업에서는 **민팅·supply 규칙**을 배우지만, 유명해진 이유는 “코드만”이 아닙니다.  
아래를 훑어 보면 **브랜드·커뮤니티·희소성**이 어떻게 겹치는지 감이 옵니다.  
(가격·시세는 수시로 변합니다. **투자 권유가 아닙니다.**)

#### BAYC(베이씨) — 왜 화제가 됐나

| 요인 | 쉬운 설명 |
| --- | --- |
| **고정 발행 · PFP(피에프피)** | 약 1만 개 한정 아바타 → “프로필에 걸 수 있는” 디지털 명함 |
| **멤버십 브랜드** | NFT = 그림 + **클럽 소속감** (커뮤니티·이벤트·IP) |
| **유명인·미디어** | 셀럽·브랜드 콜라보로 대중에게 이름이 알려짐 |
| **2차 마켓** | 민팅 이후 OpenSea(오픈씨) 등에서 거래·문화가 이어짐 |
| **스튜디오 확장** | Yuga Labs(유거 랩스)가 MAYC(메이씨)·Otherside(아더사이드) 등으로 IP를 확장 |

**둘러보기 링크**

| 구분 | 링크 |
| --- | --- |
| 공식 사이트 | [boredapeyachtclub.com](https://boredapeyachtclub.com/) |
| 스튜디오 (Yuga Labs · 유거 랩스) | [yuga.com](https://yuga.com/) |
| OpenSea(오픈씨) 컬렉션 | [opensea.io/collection/boredapeyachtclub](https://opensea.io/collection/boredapeyachtclub) |

#### Azuki(아즈키) — 왜 화제가 됐나

| 요인 | 쉬운 설명 |
| --- | --- |
| **애니메·아트 세계관** | “The Garden(더 가든)” 등 **스토리·비주얼**이 강한 PFP |
| **커뮤니티·드롭** | 홀더 대상 경험·추가 드롭으로 **소속감**을 키움 |
| **민팅 설계** | 화이트리스트·단계 민팅 등 **공정·봇 대응** 이슈와 함께 회자 |
| **브랜드 확장** | 굿즈·스토리·TCG 등 **IP를 웹 밖으로도** 확장 |
| **10,000 컬렉션** | 대표 ERC-721 PFP 규모로 마켓에서 자주 벤치마크됨 |

**둘러보기 링크**

| 구분 | 링크 |
| --- | --- |
| 공식 사이트 | [azuki.com](https://www.azuki.com/) |
| 갤러리 (공식) | [azuki.com/gallery](https://www.azuki.com/gallery) |
| OpenSea(오픈씨) 컬렉션 | [opensea.io/collection/azuki](https://opensea.io/collection/azuki) |

**수업용으로 정리하면**

> 유명함 ≈ **희소성(supply)** + **소속감(커뮤니티/IP)** + **거래·노출(마켓)**  
> 우리가 Spec에 적는 것은 그중 **온체인으로 강제할 수 있는 규칙**(누가·얼마·몇 개·pause)입니다.

> 메인넷 사이트·OpenSea([opensea.io](https://opensea.io/))는 **구경·학습용**입니다.  
> 오늘 실습 mint·확인은 **Sepolia + Etherscan**에서 합니다.  
> (OpenSea **테스트넷**은 2025-07-24부터 지원 종료)

### BAYC(베이씨) — Bored Ape Yacht Club(보어드 에이프 요트 클럽) — 무엇을 배울까

PFP(피에프피 · 프로필 사진) NFT의 대표 사례입니다. **고정된 발행량·커뮤니티·브랜드**가 핵심입니다.  
(위 [공식](https://boredapeyachtclub.com/) · [OpenSea(오픈씨)](https://opensea.io/collection/boredapeyachtclub)에서 컬렉션 형태를 확인)

| 관찰 포인트 | 쉬운 설명 | VibeMint로 옮기면 |
| --- | --- | --- |
| **고정 supply** | 처음부터 “몇 개까지”가 정해짐 → 희소성 | `maxSupply = 100` (교육용으로 축소) |
| **PFP·커뮤니티** | NFT = 그림만이 아니라 멤버십·정체성 | 오늘은 **소유권·민팅 규칙**에 집중 |
| **민팅 이후 거래** | 발행 규칙과 OpenSea 거래는 별개 | 민팅 Spec ≠ 마켓 규칙 |
| **관리·운영** | 대형 프로젝트도 권한·긴급 대응이 필요 | Stage 2 `pause` / `withdraw` |

**기억할 것**: “몇 개만 판다”는 말이 코드에서는 `maxSupply`와 `totalMinted` 검사로 구현됩니다.

### Azuki(아즈키) — 무엇을 배울까

아트·브랜드와 함께, **화이트리스트·단계적 민팅**이 잘 드러나는 사례입니다.  
(위 [공식](https://www.azuki.com/) · [OpenSea(오픈씨)](https://opensea.io/collection/azuki)에서 세계관·컬렉션을 확인)

| 관찰 포인트 | 쉬운 설명 | VibeMint로 옮기면 |
| --- | --- | --- |
| **화이트리스트 민팅** | 미리 **초대된 주소만** 먼저 mint → 봇·가스전쟁 완화 | Stage 3 `whitelist` + `whitelistMint` |
| **단계적 민팅** | WL → public처럼 **창구를 나눔** | `publicMintEnabled` 토글 + WL 별도 경로 |
| **지갑당 수량 제한** | 한 지갑이 supply를 쓸어가지 못하게 | `maxPerWallet = 3` |
| **아트·브랜딩** | 그림은 보통 오프체인, 규칙은 온체인 | `setBaseURI` / `tokenURI` |

**기억할 것**: public mint와 whitelist mint는 **문이 두 개**인 것과 같습니다.  
한쪽을 닫아도(`publicMintEnabled = false`) 다른 쪽(WL)은 열릴 수 있습니다.

### 스스로 답해 보기 — 분석 질문 5개

아무 NFT 프로젝트(또는 VibeMint)를 두고 아래를 채워 보세요.  
이 답이 곧 [02-spec-writing.md](02-spec-writing.md)의 빈칸이 됩니다.

| # | 질문 | Spec / 코드로 쓰면 |
| --- | --- | --- |
| 1 | **누가** mint할 수 있는가? | public / whitelist / owner |
| 2 | **얼마**를 내야 하는가? | `mintPrice` (예: 0.001 ETH) |
| 3 | **최대 몇 개**까지? | `maxSupply`, `maxPerWallet` |
| 4 | **언제 멈출** 수 있는가? | `pause` / `unpause` |
| 5 | **수익은 어디로?** | `withdraw` (owner only) |

### 공통 패턴 → VibeMint Spec 후보

유명 프로젝트에서 반복해서 보이는 규칙을 오늘 Spec에 이렇게 담습니다.

```text
maxSupply          ← 희소성·발행 한도
mintPrice          ← 유료 mint
maxPerWallet       ← 독과점·봇 완화
whitelist          ← 사전 허용 민팅
publicMint on/off  ← 공개 창구 개폐
pause / withdraw   ← 운영·안전
```

| 유명 프로젝트에서 본 것 | 오늘 VibeMint (교육용) |
| --- | --- |
| 수천~수만 개 supply | `maxSupply = 100` |
| 메인넷·복잡한 WL(Merkle 등) | Sepolia + 단순 `mapping` whitelist |
| 브랜드·로열티·이벤트 | **범위 밖** (개념만) |
| 실제 상업 배포 | **테스트넷 교육용** — 메인넷 Audit 필수 |

> **범위 주의**: BAYC/Azuki **전체 소스를 따라 구현하지 않습니다.**  
> “그들도 쓰는 규칙”을 Spec 언어로 옮기는 것이 목표입니다.

### 연습 (5~10분)

1. 위 **질문 5개**에 VibeMint 기준 답을 노트에 적기  
2. 옆 사람과 비교 — 빠진 항목(특히 whitelist·pause)이 있는지 확인  
3. 다음 문서 [02-spec-writing.md](02-spec-writing.md) YAML에 그대로 옮겨 적기

---

## 4. 실습: AI 역분석

NFT·ERC·벤치마킹까지 봤다면, 이제 **완성된 컨트랙트**를 AI로 읽어 봅니다.  
앞에서 적은 질문 5개(누가·얼마·몇 개…)가 solution 코드에 **어디에 있는지** 찾아보세요.

1. Cursor에서 `contracts/solution/VibeMintNFT.sol` 열기
2. [01-reverse-engineer.md](../prompts/01-reverse-engineer.md) 프롬프트 복붙
3. 결과를 노트에 정리 — **Spec 작성 예습**

### 스스로 확인

- [ ] **대체 불가능**과 **쪼갤 수 없음**이 같은 말이 아님을 설명할 수 있다
- [ ] NFT와 ERC-721의 관계를 한 문장으로 설명할 수 있다
- [ ] BAYC·Azuki에서 배운 규칙을 Spec 항목으로 말할 수 있다
- [ ] public mint와 whitelist mint 차이를 설명할 수 있다
- [ ] `pause()`가 호출되면 어떤 함수가 막히는지 안다
- [ ] `maxSupply`와 `mintedCount` 역할을 구분한다

---

## 이미지 한눈에 보기

| 그림 | 파일 |
| --- | --- |
| 대체 가능 vs NFT | [nft-fungible-vs-nonfungible.png](images/nft-fungible-vs-nonfungible.png) |
| **가치 같음 = 대체 가능 (ETH)** | [fungible-value-same.png](images/fungible-value-same.png) |
| **ETH · 721 · 1155 비교** | [fungible-three-types.png](images/fungible-three-types.png) |
| **ERC-1155 세미펀저블** | [erc1155-semi-fungible.png](images/erc1155-semi-fungible.png) |
| **대체 가능 vs 쪼갤 수 있음 (4분면)** | [fungible-divisible-matrix.png](images/fungible-divisible-matrix.png) |
| 온체인 / 오프체인 | [nft-onchain-offchain.png](images/nft-onchain-offchain.png) |
| Mint 흐름 | [nft-mint-flow.png](images/nft-mint-flow.png) |
| ERC-721 vs 1155 | [erc721-vs-erc1155.png](images/erc721-vs-erc1155.png) |
| VibeMint 구조 | [vibemint-architecture.png](images/vibemint-architecture.png) |
| (참고) 벤치마킹 발표 그림 | [session1-3-1-nft-benchmark.png](../presentation/images/session1-3-1-nft-benchmark.png) |

---

## 다음

→ [02-spec-writing.md](02-spec-writing.md) — 벤치마킹으로 뽑은 규칙을 **YAML Spec**으로 확정
