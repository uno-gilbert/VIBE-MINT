# VibeMintNFT — Solution Reference (상세 가이드)

Sepolia 테스트넷 **교육용** 완성 컨트랙트입니다. Stage 0–3를 모두 통합한 **정답 예시**이며, 점진적 빌드가 막혔을 때 비교·배포 실습에 사용합니다.

> **메인넷 배포 금지.** 프로덕션 전 전문 Audit 필수.

---

## 이 파일이 무엇인가

| 항목 | 내용 |
| --- | --- |
| 파일 | [`VibeMintNFT.sol`](VibeMintNFT.sol) |
| 표준 | ERC-721 (`VibeMint` / `VMINT`) |
| 체인 | Ethereum **Sepolia** (테스트넷) |
| 포함 Stage | 0(뼈대) + 1(mint) + 2(pause/withdraw) + 3(whitelist) |

Stage별 중간 코드는 [`../stages/`](../stages/) 를 참고하세요.

---

## 완성본에 들어 있는 기능

| 함수 / 상수 | 역할 | 누가 호출 |
| --- | --- | --- |
| `maxSupply = 100` | 최대 발행량 | — (상수) |
| `mintPrice = 0.001 ether` | public / whitelist mint 가격 | — (상수) |
| `MAX_PER_WALLET = 3` | 지갑당 mint 한도 | — (상수) |
| `mint()` | public mint (ETH 필요) | 누구나 (`publicMintEnabled`일 때) |
| `whitelistMint()` | 화이트리스트 mint | whitelist 등록 주소 |
| `ownerMint(to, qty)` | 예약 mint (무료) | owner |
| `setBaseURI` | 메타데이터 base URL | owner |
| `setPublicMintEnabled` | public mint on/off | owner |
| `setWhitelist` | whitelist 일괄 등록 | owner |
| `pause` / `unpause` | 긴급 중지 | owner |
| `withdraw` | 컨트랙트 ETH 인출 | owner |
| `totalMinted` / `ownerOf` / `tokenURI` | 조회 | 누구나 (view) |

---

## 사전 준비

1. **Chrome** + **MetaMask**
2. MetaMask에 **Sepolia** 추가 (Chain ID `11155111`)
3. **Sepolia ETH** 확보 (Faucet)
   - [Alchemy Sepolia Faucet](https://www.alchemy.com/faucets/ethereum-sepolia)
   - [Sepolia PoW Faucet](https://sepolia-faucet.pk910.de/)
4. 잔액 **0.05 ETH 이상** 권장 (배포 gas + mint 0.001 + 여유)

---

## Step 1 — Remix에 코드 넣기

1. [remix.ethereum.org](https://remix.ethereum.org) 접속
2. 왼쪽 **File Explorer** → 새 파일 `VibeMintNFT.sol` 생성  
   (또는 `contracts` 폴더 아래 생성)
3. [`VibeMintNFT.sol`](VibeMintNFT.sol) 내용 **전체 복사 → Remix에 붙여넣기**
4. 저장 (`Ctrl/Cmd + S`)

### OpenZeppelin import가 동작하는 이유

코드의 import는 아래와 같습니다.

```solidity
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Pausable.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
```

Remix는 `@openzeppelin/...` 경로를 **자동으로 GitHub에서 가져옵니다.**  
별도 `npm install`은 필요 없습니다. 첫 컴파일 때 다운로드가 조금 걸릴 수 있습니다.

---

## Step 2 — 컴파일

1. 왼쪽 아이콘 **Solidity Compiler** 클릭
2. 설정:

| 항목 | 값 |
| --- | --- |
| Compiler | **0.8.20** 이상 (예: 0.8.20 ~ 0.8.28) |
| Language | Solidity |
| EVM Version | default |
| Enable optimization | **켜기** (선택) |
| runs | **200** (선택) |

3. **Compile VibeMintNFT.sol** 클릭
4. 초록 체크(에러 0) 확인

### 컴파일이 실패하면

| 증상 | 해결 |
| --- | --- |
| `Source "@openzeppelin/..." not found` | Remix가 OZ를 못 받음 → 네트워크 확인 후 Recompile |
| `ParserError` / 버전 불일치 | Compiler를 `0.8.20+`로 맞춤 |
| `Stack too deep` | Optimization runs 200 켜기 |

---

## Step 3 — Sepolia에 배포

1. 왼쪽 **Deploy & Run Transactions** 클릭
2. **Environment**를 다음으로 변경:
   - `Injected Provider - MetaMask`
3. MetaMask 팝업이 뜨면:
   - 네트워크가 **Sepolia**인지 확인
   - Remix 연결 **승인**
4. Account에 MetaMask 주소·잔액이 보이는지 확인
5. Contract 드롭다운에서 **`VibeMintNFT`** 선택
6. 생성자 인자 없음 → **Deploy** 클릭
7. MetaMask에서 **가스비 확인 후 Confirm**
8. 아래 **Deployed Contracts**에 컨트랙트가 나타나면 성공

### 반드시 저장할 것

- **Contract Address** (예: `0xAbC...123`)  
  → 프론트엔드 `.env`의 `VITE_CONTRACT_ADDRESS`에 사용  
  → Etherscan: `https://sepolia.etherscan.io/address/주소`

### 배포가 실패하면

| 증상 | 해결 |
| --- | --- |
| Wrong network | MetaMask를 Sepolia로 전환 |
| insufficient funds | Faucet으로 Sepolia ETH 충전 |
| User rejected | MetaMask에서 거절함 → Deploy 다시 |
| Environment가 Remix VM | `Injected Provider - MetaMask`로 변경 (테스트넷에 안 올라감) |

---

## Step 4 — 배포 후 owner 설정

Deployed Contracts 패널에서 **주황색(쓰기)** / **파란색(읽기)** 버튼을 사용합니다.  
배포한 지갑 = **owner** 이므로 설정 함수를 호출할 수 있습니다.

### 4-1. `setBaseURI` (권장)

메타데이터 기본 URL을 넣습니다. (교육용 placeholder 가능)

```text
https://example.com/metadata/
```

1. `setBaseURI` 입력란에 위 URL 입력
2. **transact** → MetaMask Confirm
3. `tokenURI(0)` 호출 시 → `https://example.com/metadata/0` 형태가 됨

> 실제 이미지가 없어도 배포·mint 실습에는 문제 없습니다.

### 4-2. `setWhitelist` (선택 · Stage 3 테스트용)

1. `setWhitelist` 펼치기
2. `accounts`: `["0x내지갑주소"]` 형식 (Remix는 배열 입력 지원)
3. `allowed`: `true`
4. **transact** → Confirm
5. `whitelist(내주소)` Read → `true` 확인

### 4-3. `setPublicMintEnabled` (선택)

- `true` (기본값): 누구나 `mint()` 가능
- `false`: public mint 막고, whitelist / owner mint만 가능

---

## Step 5 — Mint 테스트

### A. Public mint

1. `mint` 함수 옆 **VALUE** 칸에 `0.001` 입력, 단위 **ether**
2. `mint` → **transact** → MetaMask Confirm
3. 확인:
   - `totalMinted` → `1`
   - `ownerOf(0)` → 내 지갑 주소
   - `mintedCount(내주소)` → `1`

### B. Whitelist mint

1. 먼저 `setWhitelist`로 본인 등록
2. (선택) `setPublicMintEnabled(false)`로 public 끄기
3. VALUE `0.001` ether → `whitelistMint` → transact

### C. Owner mint (무료)

1. `ownerMint`
   - `to`: 받을 주소
   - `quantity`: `1` (지갑당 한도 3 이내)
2. VALUE는 **0** (ETH 안 냄)
3. transact

### D. Pause 테스트

1. `pause` → transact
2. `mint` 시도 → **revert** (막힘)
3. `unpause` → 다시 mint 가능

### E. Withdraw (owner)

1. mint로 컨트랙트에 ETH가 쌓인 뒤
2. `withdraw` → transact
3. MetaMask 잔액 증가 확인

---

## Step 6 — Etherscan에서 확인

```text
https://sepolia.etherscan.io/address/YOUR_CONTRACT_ADDRESS
```

확인할 것:

- [ ] Contract Creation 트랜잭션
- [ ] mint / setBaseURI 등 쓰기 tx
- [ ] (선택) Contract 탭에서 Verify (소스 공개)

**(선택) Verify**: Remix Plugin `CONTRACT VERIFICATION` 또는 Etherscan 수동 verify.

---

## Step 7 — 프론트엔드 연결

배포 주소가 있으면:

```bash
cd frontend/starter
cp .env.example .env
# VITE_CONTRACT_ADDRESS=0x배포주소
npm install && npm run dev
```

상세: [docs/student/05-frontend-mint.md](../../docs/student/05-frontend-mint.md)

---

## 전체 체크리스트

- [ ] Remix Compile 성공 (0.8.20+)
- [ ] MetaMask Sepolia 연결
- [ ] Sepolia에 Deploy 성공 · 주소 저장
- [ ] `setBaseURI` 실행
- [ ] `mint` 1회 성공 (`totalMinted == 1`)
- [ ] Etherscan에서 컨트랙트·tx 확인
- [ ] (선택) whitelist / pause / withdraw 테스트
- [ ] 프론트 `.env`에 주소 반영

---

## 보안 고지

| 항목 | 내용 |
| --- | --- |
| 용도 | **교육 · Sepolia 테스트넷 only** |
| 메인넷 | **배포 금지** |
| AI Audit | 배포 전 [docs/prompts/04-security-audit.md](../../docs/prompts/04-security-audit.md) 권장 |
| 프로덕션 | 반드시 **전문 스마트 컨트랙트 Audit** |

---

## 관련 문서

| 문서 | 용도 |
| --- | --- |
| [../stages/](../stages/) | Stage 0–3 중간 코드 |
| [03-incremental-build.md](../../docs/student/03-incremental-build.md) | 점진적 빌드 실습 |
| [04-deploy-sepolia.md](../../docs/student/04-deploy-sepolia.md) | 배포 요약 |
| [00-walkthrough.md](../../docs/student/00-walkthrough.md) | 한 단계씩 따라하기 |
| [troubleshooting.md](../../docs/instructor/troubleshooting.md) | 문제 해결 FAQ |
