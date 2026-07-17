# Stage 빌드 + Remix 사용 가이드

점진적 빌드(Stage 0→3)에서 **Remix로 무엇을 확인하고**, **Remix를 어떻게 쓰는지** 한곳에 정리했습니다.

| 문서 | 내용 |
| --- | --- |
| [stage-0.md](stage-0.md) | NFT 뼈대 (이름·한도·관리자, mint 없음) |
| [stage-1.md](stage-1.md) | 누구나 돈 내고 발행 (0.001 ETH · 지갑당 3개) |
| [stage-2.md](stage-2.md) | 일시정지 · 관리자 발행 · 수익 인출 |
| [stage-3.md](stage-3.md) | 화이트리스트만 미리 받기 |
| [00-rules.md](../00-rules.md) | AI 공통 규칙 (매번 먼저 붙여넣기) |

> **복붙 프롬프트**는 영어 Spec이 아니라 **한글 쉬운 말**로 적혀 있습니다. Cursor가 코드를 짜고, 설명·Remix 시험 방법도 한글로 답하도록 되어 있습니다.  
> Stage 0~3 테스트는 **Remix VM**으로 합니다.  
> Sepolia(Injected Provider) 배포는 [04-deploy-sepolia.md](../../student/04-deploy-sepolia.md)에서.

---

## 1. Remix란?

[Remix IDE](https://remix.ethereum.org) = 브라우저에서 Solidity를 **쓰고 · 컴파일하고 · 배포하고 · 테스트**하는 웹 도구입니다.  
설치 없이 Chrome만 있으면 됩니다.

![Remix Compile·Deploy 메뉴 순서](../../presentation/images/session2-1-3-compile-deploy.png)

> 실습 파일: [`contracts/stages/stage-0-base/VibeMintNFT.sol`](../../../contracts/stages/stage-0-base/VibeMintNFT.sol)  
> PPT 소제목: **2-1-3 Compile·Deploy·Read/Write**

---

## 2. Remix 메뉴별 순서 (VibeMintNFT.sol 기준)

아래 **①→④** 순서대로 진행합니다. Stage 1~3도 동일한 메뉴 흐름입니다.

### ① File Explorer (📁) — 코드 넣기

| 순서 | 할 일 | VibeMintNFT.sol에서 확인 |
| --- | --- | --- |
| 1 | [remix.ethereum.org](https://remix.ethereum.org) 접속 (필요 시 로그인) | — |
| 2 | 왼쪽 **File Explorer** 클릭 | 첫 번째 아이콘 |
| 3 | `contracts` 폴더 → 새 파일 **`VibeMintNFT.sol`** | 파일명 고정 |
| 4 | Cursor 코드 또는 [stage-0-base/VibeMintNFT.sol](../../../contracts/stages/stage-0-base/VibeMintNFT.sol) **전체 붙여넣기** | `pragma ^0.8.31` |
| 5 | **저장** (`Cmd/Ctrl + S`) | import 3줄 `@5.1.0` |

```solidity
pragma solidity ^0.8.31;
import "@openzeppelin/contracts@5.1.0/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts@5.1.0/access/Ownable.sol";
import "@openzeppelin/contracts@5.1.0/utils/Strings.sol";
```

---

### ② Solidity Compiler (⚙️) — 컴파일

| 순서 | 메뉴 / 항목 | 설정값 |
| --- | --- | --- |
| 1 | 왼쪽 **Solidity Compiler** 클릭 | S 모양 아이콘 |
| 2 | **COMPILER** 드롭다운 | **`0.8.31`** |
| 3 | **Advanced Configurations** 펼치기 | — |
| 4 | **EVM Version** | **`osaka`** |
| 5 | **Compile VibeMintNFT.sol** (파란 버튼) | — |
| 6 | 아이콘에 **초록 체크** | 에러 0 |

| 확인 | 기대 |
| --- | --- |
| CONTRACT 드롭다운 | `VibeMintNFT (VibeMintNFT.sol)` |
| OpenZeppelin | `@openzeppelin/contracts@5.1.0/...` 자동 다운로드 |
| Compilation | Successful |

> `mcopy not found` → Compiler **0.8.31** + EVM **osaka** + import `@5.1.0` 재확인

#### EVM이란? (한 줄)

**EVM** = 블록체인에서 컨트랙트를 실행하는 가상 컴퓨터.  
Compile = `.sol` → EVM 바이트코드. **EVM Version = osaka**는 수업 기준(Compiler **0.8.31**과 짝).

자세한 설명: [stage-0-base/README.md](../../../contracts/stages/stage-0-base/README.md)

---

### ③ Deploy & Run Transactions (🚀) — 배포

| 순서 | 메뉴 / 항목 | 설정값 |
| --- | --- | --- |
| 1 | 왼쪽 **Deploy & Run Transactions** 클릭 | 이더리움 아이콘 |
| 2 | **Environment** | **`Remix VM`** (Injected Provider 아님) |
| 3 | **Account** | **Account #0** (배포자 = owner) |
| 4 | **CONTRACT** | **`VibeMintNFT - VibeMintNFT.sol`** |
| 5 | **Deploy** (주황 버튼) | 생성자 인자 없음 |
| 6 | 아래 **Deployed Contracts** | `VIBEMINTNFT AT 0x...` 등장 |

> 코드 수정 후에는 **② Compile → ③ Deploy** 를 다시 합니다.

| Environment | Stage 0~3 | Sepolia 배포 |
| --- | --- | --- |
| **Remix VM** | ✅ 연습용 가짜 체인 | — |
| **Injected Provider - MetaMask** | ❌ 지금 쓰지 않음 | ✅ [04-deploy-sepolia.md](../../student/04-deploy-sepolia.md) |

---

### ④ Deployed Contracts — Read / Write

컨트랙트 이름을 **펼치면** 함수 버튼이 보입니다.  
색은 Remix가 **「이 함수가 무엇을 할 수 있는지」** 를 알려 주는 표시입니다.

| 색 | 종류 | 하는 일 | 클릭 방법 | VibeMint 예 |
| --- | --- | --- | --- | --- |
| **파란색** | **읽기** (`view` / `pure`) | 값만 **조회** · 상태 안 바꿈 · ETH 안 냄 | 버튼만 클릭 | `name`, `owner`, `maxSupply`, `totalMinted` |
| **주황색** | **쓰기** (일반) | 상태를 **바꿈** · ETH는 안 받음 | 값 입력 → **transact** | `setBaseURI`, `pause`, `setWhitelist` |
| **빨간색** | **쓰기 + ETH** (`payable`) | 상태를 바꾸면서 **이더를 받을 수 있음** | **Value**에 ETH → 버튼 → **transact** | `mint`, `whitelistMint` |

```text
파란 = 「지금 값이 뭐야?」 물어보기
주황 = 「저장해 줘」 (돈은 안 냄)
빨강 = 「돈 내고 해 줘」 (mint처럼 Value 필요)
```

> Stage 0에는 빨간 버튼이 **없습니다** (`mint`가 없어서).  
> Stage 1부터 `mint`가 **빨강**으로 보입니다.

#### Stage 0 꼭 확인

| # | 동작 | 기대 |
| --- | --- | --- |
| 1 | `name` / `symbol` Read | VibeMint / VMINT |
| 2 | `totalMinted` Read | 0 |
| 3 | Account **#0** → `setBaseURI` Write | 성공 |
| 4 | Account **#1** → `setBaseURI` Write | **revert** (onlyOwner) |
| 5 | 함수 목록 | **`mint` 없음** |

#### VALUE(ether) — Stage 1부터

`mint` / `whitelistMint` 호출 시 Deploy 패널 **Value** = `0.001`, 단위 **ether**.

#### Account 바꾸기

Deploy & Run 상단 **Account** → #1, #2로 전환해 권한·whitelist 테스트.

---

## 3. 왼쪽 아이콘 요약

| 순서 | 아이콘 | 이름 | Stage 0~3에서 |
| --- | --- | --- | --- |
| ① | 📁 | **File Explorer** | `.sol` 붙여넣기 |
| ② | ⚙️ | **Solidity Compiler** | 0.8.31 · osaka · Compile |
| ③ | 🚀 | **Deploy & Run** | Remix VM · Deploy |
| ④ | (③ 하단) | **Deployed Contracts** | Read / Write |

---

## 4. Stage별 — 꼭 확인해야 할 내용

### 한눈에 보기

| Stage | 추가된 것 | Remix에서 꼭 확인할 것 |
| --- | --- | --- |
| **0** | 뼈대 (mint 없음) | `name`/`owner`/`maxSupply`, `setBaseURI`, 다른 계정 setBaseURI 실패, `mint` 없음 |
| **1** | `mint()` | 0.001 ETH mint 성공, 4번째 mint 실패, value 0이면 실패 |
| **2** | pause / ownerMint / withdraw | pause 후 mint 실패, ownerMint, withdraw(owner만) |
| **3** | whitelist | setWhitelist → whitelistMint, public off여도 whitelist OK, 비허용 주소 실패 |

---

### Stage 0 — 확인 체크리스트

| # | 확인 | 기대 | 이해 |
| --- | --- | --- | --- |
| 1 | `name` / `symbol` | VibeMint / VMINT | ERC-721 이름 |
| 2 | `maxSupply` | 100 | 발행 한도 |
| 3 | `totalMinted` | 0 | 아직 mint 없음 |
| 4 | `owner` | Account #0 | 배포자 = 관리자 |
| 5 | `setBaseURI` (#0) | 성공 | owner 쓰기 |
| 6 | `setBaseURI` (#1) | **revert** | onlyOwner |
| 7 | `tokenURI(0)` | **revert** | NFT 아직 없음 |
| 8 | `mint` 버튼 | **없음** | Stage 1에서 추가 |

상세: [stage-0.md](stage-0.md)

---

### Stage 1 — 확인 체크리스트

**준비**: Stage 0 코드에 mint 추가 후 **재Compile → 재Deploy** (Remix VM)

| # | 확인 | 기대 | 이해 |
| --- | --- | --- | --- |
| 1 | Value `0.001` ether → `mint` | 성공 | 유료 mint |
| 2 | `totalMinted` | 1 | 발행량 증가 |
| 3 | `ownerOf(0)` | 내 Address | NFT #0 소유 |
| 4 | `mintedCount(내주소)` | 1 | 지갑별 카운트 |
| 5 | Value `0` → `mint` | **revert** | 가격 검증 |
| 6 | 같은 계정으로 mint 3회 후 4번째 | **revert** | MAX_PER_WALLET=3 |
| 7 | (선택) `balanceOf` | 3 | 보유 개수 |

> supply 100까지 테스트는 시간이 오래 걸림 → 코드상 `maxSupply` require만 확인하고, 수업에서는 **지갑당 3개** 테스트로 충분.

상세: [stage-1.md](stage-1.md)

---

### Stage 2 — 확인 체크리스트

**준비**: Stage 1 + pause/ownerMint/withdraw 후 **재Compile → 재Deploy**

| # | 확인 | 기대 | 이해 |
| --- | --- | --- | --- |
| 1 | `pause` → `mint` | **revert** | 긴급 중지 |
| 2 | `unpause` → `mint` | 성공 | 재개 |
| 3 | `setPublicMintEnabled(false)` → `mint` | **revert** | public 토글 |
| 4 | `ownerMint(주소, 1)` (Value 0) | 성공 | 관리자 무료 mint |
| 5 | Account #1에서 `ownerMint` | **revert** | onlyOwner |
| 6 | mint로 ETH 쌓인 뒤 `withdraw` (#0) | 성공, 잔액 증가 | 수익 인출 |
| 7 | Account #1에서 `withdraw` | **revert** | owner만 |
| 8 | pause 상태에서 `ownerMint` | **revert** | whenNotPaused |

상세: [stage-2.md](stage-2.md)

---

### Stage 3 — 확인 체크리스트

**준비**: Stage 2 + whitelist 후 **재Compile → 재Deploy**

| # | 확인 | 기대 | 이해 |
| --- | --- | --- | --- |
| 1 | `setWhitelist([내주소], true)` (#0) | 성공 | 허용 목록 등록 |
| 2 | `whitelist(내주소)` | true | 등록 확인 |
| 3 | `setPublicMintEnabled(false)` | 성공 | public 끔 |
| 4 | `mint` (public) | **revert** | public 막힘 |
| 5 | Value 0.001 → `whitelistMint` | **성공** | whitelist는 public과 무관 |
| 6 | Account #1(미등록) → `whitelistMint` | **revert** | 비허용 차단 |
| 7 | pause → `whitelistMint` | **revert** | pause는 공통 |
| 8 | `mintedCount` 합산 | public+whitelist ≤ 3 | 지갑당 cap 공유 |

완료 후 → [04-security-audit.md](../04-security-audit.md) **필수**

상세: [stage-3.md](stage-3.md)

---

## 5. 자주 하는 실수 (전 Stage 공통)

| 실수 | 해결 |
| --- | --- |
| 코드 고쳤는데 예전처럼 동작 | **재Compile + 재Deploy** |
| Environment가 MetaMask | Stage 테스트는 **Remix VM** |
| mint Value 단위가 wei | **ether**로 `0.001` |
| owner 함수를 #1에서 호출 | Account를 #0으로 |
| revert가 나오면 무조건 실패 | **의도한 revert**도 테스트 성공 |
| OpenZeppelin not found | 네트워크 확인 후 Recompile |

---

## 6. 학습 흐름 요약

```text
Cursor (Stage 프롬프트)
    → Remix Compile
    → Remix VM Deploy
    → 위 체크리스트대로 Read/Write
    → 통과하면 다음 Stage
    → Stage 3 후 AI Audit
    → Sepolia 배포 (Injected Provider)
```

**한 줄**: Remix는 「AI가 짠 코드를 **직접 눌러보며** 규칙이 맞는지 확인하는 실험실」입니다.
