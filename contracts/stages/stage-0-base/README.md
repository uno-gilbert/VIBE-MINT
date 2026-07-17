# Stage 0: ERC-721 기본 뼈대 — 따라하기

Solidity를 **처음** 보는 분을 위한 Stage입니다.  
지금은 mint가 없습니다. **자동차 차체(뼈대)만** 만듭니다.

> **한 줄**: Stage 0 = 이름표·생산 한도·차키(owner)만 있는 차체. 시동(mint)은 Stage 1.

목록으로 돌아가기: [../README.md](../README.md)

---

## 이 Stage 목표

- [ ] Remix에 `VibeMintNFT.sol` 만들고 Compile 성공
- [ ] Remix VM에 Deploy
- [ ] `name` / `maxSupply` / `owner` 읽기 OK
- [ ] `setBaseURI`는 owner만, 다른 계정은 revert

---

## 따라하기 (순서대로)

### Step 0-1. Intent 말하기

> “VibeMint 이름 ERC-721 뼈대만. mint는 아직 없음.”

### Step 0-2. Cursor로 코드 받기

1. Cursor 채팅에 [00-rules.md](../../../docs/prompts/00-rules.md) 붙여넣기  
2. [stage-0.md](../../../docs/prompts/03-stage-build/stage-0.md) **복붙용 프롬프트** 실행  
3. 나온 코드를 복사  

막히면 정답: [VibeMintNFT.sol](./VibeMintNFT.sol) 전체를 Remix에 붙여넣어도 됩니다.

- [ ] Stage 0 코드 준비됨

### Step 0-3. Remix — 메뉴별 순서 (VibeMintNFT.sol)

> 상세·PPT 그림: [03-stage-build/README.md](../../../docs/prompts/03-stage-build/README.md) · ![Compile·Deploy](../../../docs/presentation/images/session2-1-3-compile-deploy.png)

#### ① File Explorer (📁)

1. Chrome → [remix.ethereum.org](https://remix.ethereum.org) (필요 시 로그인)  
2. **File Explorer** → `contracts` 폴더  
3. 새 파일 **`VibeMintNFT.sol`**  
4. [VibeMintNFT.sol](./VibeMintNFT.sol) 또는 Cursor 코드 **전체 붙여넣기** → 저장 (`Cmd/Ctrl + S`)

- [ ] Remix에 파일 저장됨

#### ② Solidity Compiler (⚙️)

1. Compiler **0.8.31**  
2. Advanced → EVM **osaka**  
3. **Compile VibeMintNFT.sol** → 초록 체크  

> **초록 체크 ≠ Stage 완료**  
> 초록 체크 = 「문법·버전이 맞아서 **설계도가 기계어로 번역됐다**」는 뜻입니다.  
> Stage 0 **완료**는 ③ Deploy + ④ Read/Write 테스트(아래 목표 체크리스트)까지 끝낸 때입니다.

#### ③ Deploy & Run (🚀)

1. Environment **Remix VM**  
2. Account **#0** → **Deploy**  
3. Deployed Contracts 등장 확인  

#### ④ Read / Write

| 함수 | Account | 기대 |
| --- | --- | --- |
| `name`, `maxSupply`, `owner` (파란) | #0 | VibeMint / 100 / owner 주소 |
| `setBaseURI` (주황) | #0 | 성공 |
| `setBaseURI` (주황) | #1 | **revert** |
| `mint` | — | **버튼 없음** |

- [ ] Remix ①→④ 완료

### Step 0-4. Compile (② 상세)

#### 자주 나는 Compile 오류

| 오류 | 원인 | 해결 |
| --- | --- | --- |
| `requires different compiler version` | Compiler가 0.8.31이 아님 | Compiler를 **0.8.31**로 |
| `Function "mcopy" not found` | Compiler가 0.8.31 미만이거나 EVM≠osaka, 또는 import에 `@5.1.0` 없음 | **0.8.31 + osaka** + import `@5.1.0` |

수업 기본: **Compiler 0.8.31 + EVM osaka**  
저장소 Stage import: `@openzeppelin/contracts@5.1.0/...`  
소스 `pragma`: `^0.8.31`

#### EVM이란? (컴파일할 때 왜 고르나)

**EVM** = **E**thereum **V**irtual **M**achine  
이더리움(그리고 Sepolia 같은 테스트넷)에서 스마트 컨트랙트를 **실행하는 가상 컴퓨터**입니다.

| 단계 | 쉬운 말 | 자동차 비유 |
| --- | --- | --- |
| `.sol` 소스 | 사람이 읽는 설계도 | 조립 설명서 |
| **Compile** | 설계도 → EVM이 이해하는 **바이트코드(기계어)** | 설명서 → 엔진이 읽는 신호 |
| **EVM Version** | “어느 세대 엔진 규격으로 번역할지” | 2024형 / 2025형 엔진 |
| **Deploy** | 그 바이트코드를 체인(또는 Remix VM)에 올림 | 조립된 차를 도로(연습장)에 세움 |

Solidity 컴파일러는 코드를 **한 가지 EVM 규격**에 맞춰 번역합니다.  
이더리움은 업그레이드(하드포크)마다 새 명령어가 생깁니다.

| EVM 이름 (예) | 느낌 |
| --- | --- |
| `shanghai` | 비교적 이전 세대 |
| `cancun` | `mcopy` 추가 (참고) |
| **`osaka`** | **수업 기준** · Compiler **0.8.31**과 짝 |

**왜 맞춰야 하나?**

1. **컴파일** — `osaka`는 solc **0.8.29+**부터 인식 → **0.8.24 + osaka**면 `mcopy not found`  
2. **실행** — 컴파일 EVM과 Remix VM / Sepolia가 지원하는 명령이 맞아야 함  
3. **수업** — **Compiler 0.8.31 + EVM osaka**로 통일  

```text
사람 코드 (.sol, pragma ^0.8.31)
    → [Compiler 0.8.31 + EVM osaka] 컴파일
    → 바이트코드
    → Remix VM 또는 Sepolia에서 실행
```

> **Compiler 버전**(0.8.31)과 **EVM Version**(osaka)은 **다른 설정**입니다.  
> Deploy 탭의 “Remix VM”은 **어디에 올릴지**, EVM Version은 **어떤 규격으로 번역할지**입니다.

- [ ] Compile 에러 0

### Step 0-5. Deploy (③ 상세)

1. **Deploy & Run**  
2. Environment: **Remix VM** (Injected Provider 아님)  
3. Contract: `VibeMintNFT`  
4. **Deploy**  
5. 아래 Deployed Contracts에 컨트랙트 등장

- [ ] Remix VM Deploy 성공

### Step 0-6. 읽기·쓰기 테스트 (④ 상세)

| 함수 | 기대 |
| --- | --- |
| `name` | `VibeMint` |
| `symbol` | `VMINT` |
| `maxSupply` | `100` |
| `totalMinted` | `0` |
| `owner` | 배포한 Account 주소 |

- [ ] 위 값 확인

### Step 0-7. 쓰기·권한 테스트

1. Account **#0** → `setBaseURI`에 `https://example.com/metadata/` → **transact** → 성공  
2. Account **#1** → 같은 `setBaseURI` → **revert** (정상!)  
3. Deployed Contracts 목록에 **`mint` 버튼이 없음** 확인  

- [ ] owner만 setBaseURI 가능  
- [ ] mint 없음 확인  

### Step 0-8. Stage 0 완료 체크

- [ ] `setBaseURI`는 owner만?  
- [ ] `maxSupply` = 100 (constant)?  
- [ ] 불필요한 payable receive/fallback 없음?  

**통과** → [Stage 1 따라하기](../stage-1-mint/README.md)

---

## 읽어 두면 좋은 설명

### Solidity · 용어 (자동차 비유)

| 현실 | 코드 |
| --- | --- |
| 설계도 | `.sol` 파일 |
| 조립된 차 한 대 | Deploy된 컨트랙트 |
| 버튼 | 함수 |
| 계기판 숫자 | 변수 (`_totalMinted` 등) |
| 출고 규격(안 바뀜) | 상수 `maxSupply = 100` |
| 차키 | `onlyOwner` |

### 왜 OpenZeppelin import?

#### 먼저 구분: 「표준」vs「부품」

| | 누가 정하나 | 무엇인가 |
| --- | --- | --- |
| **ERC-721** | 이더리움 커뮤니티의 **표준(스펙)** ([EIP-721](https://eips.ethereum.org/EIPS/eip-721)) | “NFT면 `ownerOf`, `transferFrom` 같은 함수를 **이렇게** 가져야 한다”는 **약속** |
| **OpenZeppelin** | [OpenZeppelin](https://www.openzeppelin.com/) (보안·컨트랙트 전문 팀/오픈소스) | 그 약속을 **이미 안전하게 구현해 둔 Solidity 코드(라이브러리)** |

비유:

- **ERC-721** = “자동차는 핸들·브레이크·번호판이 있어야 한다”는 **도로 교통 규격**
- **OpenZeppelin ERC721.sol** = 그 규격에 맞춰 **이미 인증·테스트된 차체 부품 세트**

즉, “ERC-721 스펙이 OpenZeppelin 것이라서 그걸 쓴다”가 **아닙니다.**  
스펙은 이더리움 쪽이고, 우리는 그 스펙을 **처음부터 직접 다 짜는 대신**, OpenZeppelin이 만든 **구현체(부품)** 를 가져와 씁니다.

#### OpenZeppelin은 “부품 창고” 개념이 맞나?

**맞습니다.** 소속·성격은 **오픈소스 스마트 컨트랙트 라이브러리**(보안으로 유명한 팀/프로젝트가 관리)이고,  
`import`로 **모듈(부품)을 조립**하는 방식입니다.

```solidity
import "@openzeppelin/contracts@5.1.0/token/ERC721/ERC721.sol";  // NFT 표준 구현
import "@openzeppelin/contracts@5.1.0/access/Ownable.sol";       // owner 권한
```

Remix가 `@openzeppelin/...` 경로를 보고 **자동 다운로드**합니다.

#### 그럼 왜 “반드시” OpenZeppelin ERC-721을 쓰나?

**반드시 OZ여야만 ERC-721인 것은 아닙니다.**  
원하면 스펙을 읽고 스스로 구현해도 됩니다. 다만 이 워크숍에서는 **OpenZeppelin만** 쓰라고 정했습니다.

| 이유 | 설명 |
| --- | --- |
| **실수·보안** | 전송·권한을 초보가 직접 짜면 버그가 나기 쉬움 |
| **지갑·마켓 호환** | MetaMask·OpenSea가 기대하는 ERC-721 동작을 OZ가 이미 맞춤 |
| **수업 집중** | 우리는 mint 규칙·Spec에 시간 쓰고, 뼈대는 검증된 부품 사용 |
| **실무와 동일** | 현업 NFT도 OZ(또는 동급 검증 라이브러리)를 쓰는 경우가 많음 |

> **정리**: ERC-721 = **표준(스펙)** · OpenZeppelin = **그 표준의 검증된 구현(부품)**.  
> “OZ 스펙을 써야 해서”가 아니라, “이더리움 ERC-721을 **직접 안 만들고 OZ 부품으로 조립**해서” 씁니다.

### Spec 요약

- ERC721(`VibeMint`, `VMINT`) + Ownable  
- `maxSupply = 100`  
- `setBaseURI` / `tokenURI`  
- **mint 없음**

자세한 Remix UI: [stage-0.md](../../../docs/prompts/03-stage-build/stage-0.md) · [03-stage-build/README.md](../../../docs/prompts/03-stage-build/README.md)
