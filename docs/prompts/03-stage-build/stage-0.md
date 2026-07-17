# Stage 0 프롬프트: ERC-721 기본 뼈대

[00-rules.md](../00-rules.md) + 아래 Intent.

Remix 공통 가이드 · Stage별 체크리스트: **[README.md](README.md)**

---

## Intent

**VibeMint** NFT의 뼈대만 만든다. 이름은 붙이고, 총 100개 한도와 관리자(owner)만 두고, **아직 mint(발행)는 하지 않는다.**

---

## 복붙용 프롬프트

아래를 Cursor에 그대로 붙여넣으세요. (`00-rules`를 먼저 붙인 뒤 이어서)

```
지금 Stage 0만 만들어 주세요. 파일 이름: VibeMintNFT.sol

하고 싶은 것 (쉬운 말):
- NFT 컬렉션 이름은 VibeMint, 심볼은 VMINT
- 이더리움 NFT 표준(ERC-721)과 관리자(owner) 기능을 OpenZeppelin으로 붙이기
- 전체 발행 한도는 100개로 고정
- 지금까지 몇 개 나왔는지 세는 숫자(아직 0)
- 관리자만 메타데이터 기본 주소(base URI)를 바꿀 수 있게
- 토큰마다 주소 = 기본 주소 + 번호 로 조회되게
- 아직 “발행(mint)” 함수는 만들지 마세요 (다음 Stage에서 함)

버전·환경:
- Solidity ^0.8.31
- Remix에서 돌아가게, OpenZeppelin은 @5.1.0 경로로 import
- 파일 하나로 Remix 컴파일 가능하게

응답 방식:
- 완성된 VibeMintNFT.sol 코드를 주세요
- 무엇을 만들었는지 한글로 짧게 설명해 주세요
```

---

## Remix 테스트 (구체적으로)

![Remix Compile·Deploy 메뉴 순서](../../presentation/images/session2-1-3-compile-deploy.png)

> **메뉴 순서**: ① File Explorer → ② Solidity Compiler → ③ Deploy & Run → ④ Read/Write  
> 전체 가이드: [03-stage-build/README.md](README.md) · 실습 파일: `contracts/stages/stage-0-base/VibeMintNFT.sol`

> Stage 0은 **실제 Sepolia 배포 전**에 Remix **가상 환경(Remix VM)** 으로 충분합니다.  
> Compiler **0.8.31** + Advanced → **EVM Version = osaka**. Environment: `Remix VM` 권장.

### Remix 메뉴별 순서 (요약)

| # | 메뉴 | 할 일 |
| --- | --- | --- |
| ① | **File Explorer** | `contracts/VibeMintNFT.sol`에 stage-0 코드 붙여넣기 · 저장 |
| ② | **Solidity Compiler** | 0.8.31 · EVM osaka · **Compile VibeMintNFT.sol** |
| ③ | **Deploy & Run** | Environment **Remix VM** · Account #0 · **Deploy** |
| ④ | **Deployed Contracts** | 파란 Read / 주황 Write · `setBaseURI` owner 테스트 |


### Environment란? (Remix VM vs Injected Provider)

**Deploy & Run Transactions** 탭 맨 위 **Environment**는  
「이 컨트랙트를 **어디에** 배포·실행할지」를 고르는 설정입니다.

![Environment 선택 위치](../../student/images/walkthrough-part-1.png)

#### 한 줄 비교

| Environment | 어디에 올라가나 | ETH | MetaMask | Stage 0에서 |
| --- | --- | --- | --- | --- |
| **Remix VM** | 브라우저 안 **가짜 블록체인** | 가짜 ETH (무제한에 가까움) | **불필요** | ✅ **사용** |
| **Injected Provider - MetaMask** | **실제 네트워크** (Sepolia/메인넷 등) | 진짜 테스트/실제 ETH | **필수** | ❌ Stage 0에선 쓰지 않음 |

---

#### Remix VM이란?

- Remix가 브라우저 메모리에 만드는 **연습용 가상 체인**
- 이름 예: `Remix VM`, `Remix VM (Cancun)` 등 — Stage 0은 Remix VM이면 OK  
- Compiler **EVM Version**은 **osaka**로 맞춤 (기본값)

- Account #0, #1, #2… 가 **자동으로** 생기고, 각각 가짜 ETH를 많이 보유
- 배포·트랜잭션이 **즉시** 처리됨 (Faucet·가스비·네트워크 대기 없음)
- 브라우저를 새로고침하면 VM 상태가 **초기화**될 수 있음 (연습용이라 괜찮음)

**비유**: 집 안 연습장. 코드가 돌아가는지 확인만 하면 됨.

---

#### Injected Provider (MetaMask)란?

- 브라우저에 설치된 **MetaMask**를 Remix에 “연결(inject)”하는 방식
- MetaMask가 가리키는 네트워크(예: Sepolia)에 **진짜로** 배포
- 트랜잭션마다 MetaMask 승인 팝업 → 가스비(테스트 ETH) 소모
- Faucet으로 Sepolia ETH가 있어야 Deploy 가능

**비유**: 실제 도로에 나가기. Stage 6(Sepolia 배포)에서 사용.

---

#### Stage 0에서 Remix VM을 쓰는 이유

1. **아직 mint도 없는 뼈대** — 실넷에 올릴 단계가 아님  
2. **빠른 확인** — Compile → Deploy → Read/Write를 몇 초 안에 반복  
3. **비용·준비 없음** — Faucet, MetaMask 연결 불필요  
4. **owner 테스트 쉬움** — Account #0 / #1 전환만으로 `onlyOwner` 확인  
5. **실수해도 안전** — 실넷에 잘못된 컨트랙트가 안 남음  

> **Injected Provider로 Stage 0을 배포해도 동작은 하지만**,  
> gas·대기·지갑 연결까지 필요해서 **학습용 뼈대 검증에는 과함**입니다.  
> Sepolia 배포는 [Part 6 / stage 이후](../../student/04-deploy-sepolia.md)에서 합니다.

---

#### Remix에서 설정하는 방법

1. 왼쪽 **Deploy & Run Transactions** (이더리움 아이콘) 클릭  
2. 맨 위 **Environment** 드롭다운 클릭  
3. Compiler EVM Version이 **osaka**인지 확인 후, Environment에서 **`Remix VM`** 선택  
4. 그 아래 **Account**에 `0x...` 주소와 잔액(100 ETH 등)이 보이면 OK  
5. **절대** 지금은 `Injected Provider - MetaMask`를 고르지 않기
  

| 지금 화면 | 의미 |
| --- | --- |
| Environment = Remix VM, Account에 잔액 많음 | ✅ Stage 0 테스트 준비됨 |
| Environment = Injected Provider, MetaMask 팝업 | ❌ Stage 0이 아님 → VM으로 다시 변경 |

---

### 1) 컴파일

1. [remix.ethereum.org](https://remix.ethereum.org) → `VibeMintNFT.sol` 열기  
   (실습 기준: `contracts/stages/stage-0-base/VibeMintNFT.sol`)
2. **Solidity Compiler** → **0.8.31**
3. **Advanced Configurations** → **EVM Version** = **osaka**
4. **Compile VibeMintNFT.sol** → 초록 체크(에러 0)

| 확인 | 기대 |
| --- | --- |
| import `@openzeppelin/contracts@5.1.0/...` | Remix가 **5.1.0** 다운로드 |
| Compilation | Successful |

---

### 2) 배포 (Deploy)

1. **Deploy & Run Transactions**
2. Environment: **Remix VM** ← [위에서 설명](#environment란-remix-vm-vs-injected-provider) (Injected Provider 아님)
3. Contract: `VibeMintNFT`
4. **Deploy** 클릭 (생성자 인자 없음)
5. 아래 **Deployed Contracts**에 컨트랙트 등장

| 확인 | 기대 | 의미 |
| --- | --- | --- |
| Account 주소 | Deploy한 계정과 동일 | 이 계정이 **owner** |
| Deployed Contracts | `VIBE MINTNFT AT ...` | 배포 성공 |

---

### 3) 읽기(Read) — 파란색 버튼

Deployed Contracts에서 아래를 **call** 합니다.

| 함수 | 입력 | 기대 결과 | 이해 포인트 |
| --- | --- | --- | --- |
| `name` | 없음 | `"VibeMint"` | ERC-721 컬렉션 이름 |
| `symbol` | 없음 | `"VMINT"` | 심볼 |
| `maxSupply` | 없음 | `100` | 최대 발행량(상수) |
| `totalMinted` | 없음 | `0` | 아직 mint 없음 |
| `owner` | 없음 | Deploy한 Account 주소 | Ownable — 배포자 = 관리자 |

**이해**: Stage 0은 **「NFT 공장 뼈대」**만 있음. 제품은 아직 0개.

---

### 4) 쓰기(Write) — `setBaseURI` (주황색 버튼)

#### 파란색 vs 주황색 — 먼저 구분

Deployed Contracts에 함수 버튼이 **두 색**으로 나뉩니다.

| 색 | 종류 | 블록체인 상태를 바꾸나? | 가스비 | 버튼 예 |
| --- | --- | --- | --- | --- |
| **파란색** | **Read** (읽기) | 안 바꿈 | 거의 없음 | `name`, `owner`, `maxSupply` |
| **주황색** | **Write** (쓰기) | **바꿈** | 필요 (Remix VM에선 가짜 ETH) | `setBaseURI` |

- Read = 「지금 값이 뭐야?」만 물어봄  
- Write = 「값을 **저장**해」 → 트랜잭션(`transact`) 발생  

Stage 0에서 우리가 쓰는 **유일한 Write**가 바로 `setBaseURI`입니다. (mint는 아직 없음)

---

#### `setBaseURI`가 하는 일

컨트랙트 안에 `_baseTokenURI`라는 **문자열 저장소**가 있습니다.

```text
setBaseURI("https://example.com/metadata/")
        ↓
컨트랙트에 baseURI 저장
        ↓
(나중에 mint 후) tokenURI(3)
        ↓
"https://example.com/metadata/" + "3"
        ↓
https://example.com/metadata/3
```

| 용어 | 의미 |
| --- | --- |
| **baseURI** | 모든 NFT 메타데이터의 **공통 앞부분** (폴더 주소처럼) |
| **tokenURI(tokenId)** | baseURI + 토큰 번호 → 그 NFT의 JSON/이미지 링크 |
| **setBaseURI** | owner만 baseURI를 **설정·변경**하는 함수 |

**비유**:  
- baseURI = 앨범 폴더 경로 `사진/vibemint/`  
- tokenId = 파일 번호 `0`, `1`, `2`  
- tokenURI = `사진/vibemint/0`  

Stage 0에서는 아직 사진(파일)이 없고, **폴더 경로만** 적어 두는 연습입니다.

---

#### Remix에서 클릭하는 순서 (상세)

1. **Deployed Contracts**에서 방금 배포한 `VIBE MINTNFT AT ...` 펼치기  
2. 아래로 스크롤해 **주황색** `setBaseURI` 찾기  
3. 입력칸(string `baseURI`)에 아래처럼 입력 (따옴표 없이, 끝에 `/` 권장):

```text
https://example.com/metadata/
```

4. 입력칸 **오른쪽** (또는 아래) **transact** 버튼 클릭  
5. Remix VM이면 MetaMask 팝업 **없이** 바로 처리됨  
6. 하단 **터미널/콘솔**에 초록 체크 + `status: 0x1` (성공) 확인  

| UI 위치 | 할 일 |
| --- | --- |
| `setBaseURI` 옆 입력란 | URL 문자열 입력 |
| **transact** | 쓰기 실행 (상태 변경) |
| 하단 콘솔 | success / gas 사용량 확인 |

---

#### 성공했는지 어떻게 아나?

Stage 0 코드에는 baseURI를 **바로 읽어 주는 public getter**가 없을 수 있습니다.  
그래서 성공 여부는 이렇게 봅니다.

| 확인 방법 | 기대 |
| --- | --- |
| 하단 콘솔 | `transact` 성공, 에러 없음 |
| Account 잔액 | Remix VM 가짜 ETH가 조금 감소 (가스) |
| 다른 Account로 다시 `setBaseURI` | **실패** (owner만 가능) → 다음 절 |

mint 이후에는 `tokenURI(0)`이  
`https://example.com/metadata/0` 형태로 나오는지로 **최종 확인**합니다.  
(Stage 0에서는 `tokenURI(0)`이 **revert**하는 것이 정상 — NFT가 아직 없음)

---

#### 자주 하는 실수

| 실수 | 결과 | 해결 |
| --- | --- | --- |
| URL 끝에 `/` 없음 | 나중에 `...metadata0`처럼 붙음 | `.../metadata/` 처럼 슬래시 권장 |
| Read처럼 call만 누름 | 상태 안 바뀜 | 반드시 **transact** |
| Injected Provider인데 Sepolia ETH 없음 | MetaMask 실패 | Stage 0은 **Remix VM** 사용 |
| owner가 아닌 Account | revert | Account를 배포한 #0으로 |

---

#### 이 테스트로 이해하는 것

1. **쓰기 = 상태 변경** — 주황색 `transact`가 블록체인(여기선 VM)에 값을 저장한다  
2. **owner 권한** — `setBaseURI`는 아무나 못 바꾸고, 배포자만 가능 (`onlyOwner`)  
3. **메타데이터 경로 ≠ NFT 발행** — URI만 설정했다고 tokenId가 생기지 **않는다**  
4. **나중에 OpenSea** — mint 후 `tokenURI`가 가리키는 JSON/이미지를 마켓이 읽어 보여 줌  

**한 줄**: `setBaseURI`는 「NFT 사진·설명이 어디 있는지 **주소록의 앞부분**을 적어 두는 관리자 기능」입니다.

### 5) `tokenURI` — 아직 NFT가 없을 때

1. `tokenURI`에 `0` 입력 → call
2. **기대: revert / 에러** (예: token does not exist)

| 확인 | 기대 | 이해 포인트 |
| --- | --- | --- |
| tokenId `0` 조회 | **실패** | mint 전엔 토큰이 없음 → `tokenURI`도 의미 없음 |

**이해**: `setBaseURI`만 했다고 NFT가 생긴 게 **아닙니다.** mint(Stage 1)가 있어야 tokenId가 생깁니다.

---

### 6) owner 권한 확인 (중요)

1. Account 드롭다운에서 **다른 계정**으로 전환 (Account #1 → #2)
2. `setBaseURI`에 아무 URL → **transact**
3. **기대: revert** (`OwnableUnauthorizedAccount` 등)

| 확인 | 기대 | 이해 포인트 |
| --- | --- | --- |
| 다른 계정의 `setBaseURI` | **실패** | `onlyOwner` 접근 제어가 동작함 |

다시 Account #0(배포자)으로 돌아가면 `setBaseURI` 성공.

---

### 7) mint가 없는지 확인

Deployed Contracts 목록을 훑어봅니다.

| 확인 | 기대 | 이해 포인트 |
| --- | --- | --- |
| `mint` 함수 | **없음** | Stage 0 범위 — Stage 1에서 추가 |
| `balanceOf(주소)` | `0` | NFT 보유 0개 |

---

## 이 Stage에서 무엇을 이해할 수 있는가

### 핵심 개념

| 개념 | Stage 0에서 배우는 것 |
| --- | --- |
| **ERC-721 뼈대** | 이름·심볼·표준 인터페이스가 먼저 있고, mint는 나중에 붙는다 |
| **Ownable** | 배포한 지갑 = owner. 관리 함수(`setBaseURI`)는 owner만 |
| **상수(maxSupply)** | 코드에 박힌 한도(100). 배포 후 바꿀 수 없음 |
| **메타데이터 URI** | `baseURI + tokenId` 패턴. 실제 이미지 링크는 mint 이후에 의미 있음 |
| **점진적 빌드** | 「전체 NFT」를 한 번에 안 만들고, **뼈대만** 먼저 검증 |

### Remix로 직접 확인한 사실

1. **Compile 성공** → OpenZeppelin import·문법 OK  
2. **Deploy 후 `owner` = 내 주소** → 생성자 `Ownable(msg.sender)` 이해  
3. **`totalMinted == 0`** → mint 없으면 발행량 0  
4. **`tokenURI(0)` revert** → 존재하지 않는 토큰은 조회 불가  
5. **다른 계정 `setBaseURI` 실패** → 접근 제어(보안의 기본)

### 아직 이해하면 안 되는 것(다음 Stage)

| 다음 | Stage |
| --- | --- |
| ETH 내고 mint | Stage 1 |
| pause / withdraw | Stage 2 |
| whitelist | Stage 3 |

---

## Audit 전 체크 (3문항)

1. `setBaseURI`는 **owner만** 호출 가능한가? (다른 Account로 revert 확인)
2. 아직 mint 없이도 ERC721 **조회 함수**(`name`, `symbol`, `owner`)가 정상인가?
3. 불필요한 **payable** / `receive` / `fallback`이 없는가? (Stage 0엔 mint·입금 불필요)

---

## 막혔을 때

- 정답 코드: [`contracts/stages/stage-0-base/VibeMintNFT.sol`](../../../contracts/stages/stage-0-base/VibeMintNFT.sol)
- Stage README: [`contracts/stages/stage-0-base/README.md`](../../../contracts/stages/stage-0-base/README.md)

## 다음

→ [stage-1.md](stage-1.md) — `mint()` 추가
