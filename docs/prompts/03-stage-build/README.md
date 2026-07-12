# Stage 빌드 + Remix 사용 가이드

점진적 빌드(Stage 0→3)에서 **Remix로 무엇을 확인하고**, **Remix를 어떻게 쓰는지** 한곳에 정리했습니다.

| 문서 | 내용 |
| --- | --- |
| [stage-0.md](stage-0.md) | ERC-721 뼈대 |
| [stage-1.md](stage-1.md) | public mint |
| [stage-2.md](stage-2.md) | pause · ownerMint · withdraw |
| [stage-3.md](stage-3.md) | whitelist |
| [00-rules.md](../00-rules.md) | AI 공통 규칙 (매번 먼저) |

> Stage 0~3 테스트는 **Remix VM**으로 합니다.  
> Sepolia(Injected Provider) 배포는 [04-deploy-sepolia.md](../../student/04-deploy-sepolia.md)에서.

---

## 1. Remix란?

[Remix IDE](https://remix.ethereum.org) = 브라우저에서 Solidity를 **쓰고 · 컴파일하고 · 배포하고 · 테스트**하는 웹 도구입니다.  
설치 없이 Chrome만 있으면 됩니다.

### 왼쪽 아이콘 (자주 쓰는 3개)

| 아이콘 | 이름 | 하는 일 |
| --- | --- | --- |
| 📁 | **File Explorer** | `.sol` 파일 만들고 코드 붙여넣기 |
| ⚙️ (S 모양) | **Solidity Compiler** | 코드 → 바이트코드로 **컴파일** |
| 🚀 (이더리움) | **Deploy & Run** | **배포** + 함수 호출(읽기/쓰기) |

---

## 2. Remix 사용법 (처음부터)

### Step A — 파일 만들기

1. [remix.ethereum.org](https://remix.ethereum.org) 접속  
2. 왼쪽 **File Explorer**  
3. `contracts` 폴더(없으면 생성) → 새 파일 **`VibeMintNFT.sol`**  
4. Cursor가 만든 코드 **전체 붙여넣기** → 저장 (`Ctrl/Cmd + S`)

### Step B — 컴파일

1. **Solidity Compiler** 클릭  
2. Compiler: **0.8.20** 이상  
3. **Compile VibeMintNFT.sol**  
4. 초록 체크 = 성공 / 빨간 에러면 메시지 읽고 수정  

OpenZeppelin(`@openzeppelin/...`)은 Remix가 **자동 다운로드**합니다. 첫 컴파일은 조금 걸릴 수 있습니다.

### Step C — Environment 고르기 (중요)

**Deploy & Run** → 맨 위 **Environment**:

| 선택 | 의미 | Stage 0~3 |
| --- | --- | --- |
| **Remix VM (Cancun/Shanghai)** | 브라우저 안 **연습용** 체인 | ✅ **여기 사용** |
| **Injected Provider - MetaMask** | Sepolia 등 **실제 테스트넷** | ❌ 나중에 배포할 때 |

Remix VM = MetaMask·Faucet 없이 Account #0, #1… 과 가짜 ETH로 바로 테스트.

### Step D — 배포

1. Environment = **Remix VM**  
2. Account = 기본 Account #0 (나중에 owner)  
3. Contract = **`VibeMintNFT`**  
4. **Deploy** 클릭  
5. 아래 **Deployed Contracts**에 컨트랙트가 생기면 성공  

> 코드를 고친 뒤에는 **다시 Compile → 다시 Deploy** 하세요.  
> 옛 배포본은 예전 코드입니다. (옆 휴지통으로 지워도 됨)

### Step E — 함수 호출 (파란색 / 주황색)

Deployed Contracts에서 컨트랙트를 **펼칩니다**.

| 색 | 종류 | 클릭 | 하는 일 |
| --- | --- | --- | --- |
| **파란색** | Read | 버튼만 클릭 (call) | 값 **조회** (상태 안 바꿈) |
| **주황색** | Write | 값 입력 → **transact** | 상태 **변경** (가스 사용) |

#### VALUE(이더 보내는 칸) — mint할 때

주황색 `mint` / `whitelistMint`처럼 **ETH가 필요한** 함수:

1. 함수 **위쪽** 또는 Deploy 패널의 **Value** 칸에 `0.001`  
2. 단위를 **ether**로 선택 (wei 아님!)  
3. 그다음 `mint` → **transact**

Value를 0으로 두면 `Insufficient payment`로 **revert**됩니다.

### Step F — Account 바꾸기 (권한 테스트)

Deploy & Run 상단 **Account** 드롭다운:

| Account | 용도 |
| --- | --- |
| #0 | 보통 **owner** (배포자) |
| #1, #2 | 다른 사람 — `onlyOwner` / whitelist 테스트 |

owner만 되는 함수를 #1에서 호출하면 **revert**가 정상입니다.

### Step G — 하단 콘솔 읽기

| 표시 | 의미 |
| --- | --- |
| 초록 / `status 0x1` | 성공 |
| 빨간 에러 / revert | 조건 실패 (`require`에 걸림) — **의도한 실패도 테스트** |

---

## 3. Stage별 — 꼭 확인해야 할 내용

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

## 4. 자주 하는 실수 (전 Stage 공통)

| 실수 | 해결 |
| --- | --- |
| 코드 고쳤는데 예전처럼 동작 | **재Compile + 재Deploy** |
| Environment가 MetaMask | Stage 테스트는 **Remix VM** |
| mint Value 단위가 wei | **ether**로 `0.001` |
| owner 함수를 #1에서 호출 | Account를 #0으로 |
| revert가 나오면 무조건 실패 | **의도한 revert**도 테스트 성공 |
| OpenZeppelin not found | 네트워크 확인 후 Recompile |

---

## 5. 학습 흐름 요약

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
