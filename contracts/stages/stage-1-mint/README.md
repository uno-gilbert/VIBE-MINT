# Stage 1: Public Mint — 따라하기

Stage 0 차체에 **유료 출고 창구(`mint`)** 를 답니다.

> **한 줄**: 누구나 0.001 ETH를 내고 NFT를 받는다. 전체는 100개, 한 지갑은 3개까지.

이전: [Stage 0](../stage-0-base/README.md) · 목록: [../README.md](../README.md)

---

## Stage 1이 하는 일 (쉬운 말)

Stage 0까지는 **이름표·한도·관리자**만 있는 빈 차체였고, **NFT를 만드는 버튼(`mint`)이 없었습니다.**

Stage 1에서는 그 버튼을 답니다.

| 비유 | 코드에서 |
| --- | --- |
| 손님 창구 열기 | `mint()` 함수 추가 |
| 가격표: 0.001 ETH | `mintPrice = 0.001 ether` |
| 공장 전체 100대 한도 | `totalMinted < maxSupply`(100) |
| 손님당 3대까지만 | `mintedCount` + `MAX_PER_WALLET = 3` |
| 돈 안 내면 거절 | `msg.value >= mintPrice` 실패 시 **revert** |

```text
Stage 0: 뼈대만 (mint 없음)
    ↓
Stage 1: “돈 내고 NFT 받기” 창구 열기  ← 지금 여기
    ↓
Stage 2: pause · 관리자 발행 · 수익 인출
```

> **초록 체크**는 Compile(설계도 번역) 성공일 뿐입니다.  
> Stage 1 **완료** = mint 코드 추가 → 재Compile → **재Deploy** → 0.001 ETH mint 성공 + Value 0 / 4번째 mint **실패**까지 확인한 때입니다.

---

## 캡처로 보는 Remix 화면 (Stage 1)

![Stage 1 Deploy · mint](../../../docs/presentation/images/session2-2-1-stage-0-1.png)

원본 캡처: [remix-stage1-deploy-mint-screenshot.png](../../../docs/presentation/images/remix-stage1-deploy-mint-screenshot.png)

이 화면은 **Compile 성공 후 Deploy & Run 탭**에서 Stage 1 컨트랙트를 배포·호출하는 모습입니다.

| # | 화면에서 보이는 것 | 쉬운 설명 | 지금 해야 할 일 |
| --- | --- | --- | --- |
| **A** | 왼쪽 아이콘 **초록 체크** (Compiler) | 코드 문법·버전 OK | 끝! 다시 Compile할 필요 없음 (코드 안 고쳤다면) |
| **B** | **Deploy & Run** 탭이 선택됨 | 배포·함수 호출 메뉴 | ★ Stage 테스트는 여기 |
| **C** | Environment = **Remix VM (Osaka)** | 연습용 가짜 체인 | Sepolia(MetaMask) 아님 ✓ |
| **D** | Account + 잔액(~100 ETH) | 테스트용 가짜 지갑 | mint할 때 가스·0.001 ETH 씀 |
| **E** | Contract `VibeMintNFT` + **Compiled** 배지 | 배포할 준비된 설계도 | **Deploy** 누르면 연습장에 올림 |
| **F** | Deployed Contracts · 빨간·주황 **`mint`** | Stage 1에서 생긴 **유료 mint 버튼** | Value `0.001` ether → `mint` → transact |
| **G** | 오른쪽 에디터 `mint()` / `mintPrice` | Stage 1이 추가한 코드 | Stage 0에는 없던 부분 |

### Stage 0 화면과 다른 점

| | Stage 0 | Stage 1 (이 캡처) |
| --- | --- | --- |
| `mint` 버튼 | **없음** | **있음** (빨강/주황, payable) |
| 코드 | 뼈대만 | `mintPrice`, `MAX_PER_WALLET`, `mint()` |
| 다음 단계 | Deploy + setBaseURI | Deploy + **Value 넣고 mint** |

### 이 화면에서 mint 누르는 순서

1. **VALUE** 칸에 `0.001` 입력 → 단위 **ether**  
2. Deployed Contracts에서 **`mint`** 클릭 (또는 펼친 뒤 **transact**)  
3. 파란 버튼으로 확인: `totalMinted` → `1`, `ownerOf(0)` → 내 주소  
4. Value를 `0`으로 두고 mint → **revert** (정상)  

> 캡처처럼 **Deployed Contracts**에 컨트랙트가 안 보이면 → `Deploy`를 아직 안 한 것입니다.  
> `mint`만 없고 다른 버튼만 있으면 → **옛 Stage 0 배포본**입니다. 재Compile 후 **재Deploy**.

---

## 이 Stage 목표
- [ ] Stage 0 코드에 mint **diff만** 추가 (전체 재작성 금지)
- [ ] 재Compile → 재Deploy (옛 Deploy에는 mint가 없음)
- [ ] Value **0.001 ether**로 mint 성공 → `totalMinted` = 1
- [ ] Value 0 / 같은 계정 4번째 mint는 **revert** (의도한 실패)

---

## 따라하기 (순서대로)

### Step 1-1. Intent

> “Stage 0에 payable `mint()`만 추가. 가격 0.001 ETH, 지갑당 3개.”
### Step 1-2. Cursor로 diff 받기

1. Remix(또는 로컬)의 `VibeMintNFT.sol`을 Cursor에서 `@VibeMintNFT.sol` 멘션  
2. [00-rules](../../../docs/prompts/00-rules.md) 확인  
3. [stage-1.md](../../../docs/prompts/03-stage-build/stage-1.md) 복붙용 프롬프트 실행  
4. **전체 파일 재작성**이면 중단 → “Stage 1 diff만” 재요청  

막히면 참고: [VibeMintNFT.sol](./VibeMintNFT.sol)

- [ ] mint 관련 코드만 추가됨

### Step 1-3. Remix에 반영 (메뉴 ①→③)

1. ① File Explorer — Remix `VibeMintNFT.sol`에 코드 반영·저장  
2. ② Compiler **0.8.31** · EVM **osaka** → **Compile** → 초록 체크  
3. ③ Environment **Remix VM** → **Deploy** (Stage 0 배포본은 버림)

> 코드를 고쳤는데 예전 Deploy를 쓰면 **mint 버튼이 안 보입니다.** **반드시 재Deploy.**  
> 초록 체크만 보고 Stage 끝내지 마세요 → ④ mint 테스트까지.

- [ ] Compile OK · 새 Deploy 완료 · 주황 `mint` 버튼 보임

### Step 1-4. mint 성공 테스트

1. Deploy 패널 **Value** = `0.001`  
2. 단위 = **ether** (wei 아님!)  
3. 주황 `mint` → **transact**  
4. 파란 버튼 확인:

| 함수 | 기대 |
| --- | --- |
| `totalMinted` | `1` |
| `ownerOf(0)` | 내 주소 |
| `mintedCount(내주소)` | `1` |

- [ ] mint 1회 성공

### Step 1-5. 실패해야 하는 테스트 (중요)

| 테스트 | 기대 |
| --- | --- |
| Value `0` → mint | **revert** (가격) |
| 같은 계정으로 mint 3회 성공 후 **4번째** | **revert** (지갑당 3개) |

- [ ] Value 0 revert  
- [ ] 4번째 mint revert  

### Step 1-6. Stage 1 완료 체크

- [ ] `msg.value` 검증 있는가?  
- [ ] `totalMinted < maxSupply` 있는가?  
- [ ] `_safeMint` 사용?

**통과** → [Stage 2 따라하기](../stage-2-access/README.md)

---

## 막히면

| 증상 | 해결 |
| --- | --- |
| Value 단위 wei | **ether** + `0.001` |
| mint 버튼 없음 | 재Compile + 재Deploy |
| AI가 파일 통째 재작성 | “Stage 1 **diff만**, 삭제 금지” |

---

## 읽어 두면 좋은 설명

### 자동차 비유

| 용어 | 의미 | 비유 |
| --- | --- | --- |
| `payable` | ETH 받을 수 있는 함수 | 동전 투입구 |
| `msg.value` | 이번에 보낸 ETH | 손님이 낸 돈 |
| `require` | 조건 실패 시 revert | 출고 거절 |
| `mintedCount` | 지갑별 발행 수 | 손님별 구매 장부 |
| `_safeMint` | 안전한 NFT 발행 | 확인된 손님에게 키 전달 |

### Spec 요약

- `mintPrice = 0.001 ether`  
- `MAX_PER_WALLET = 3`  
- `msg.value >= mintPrice`  
- supply·지갑 cap · (권장) 초과 ETH refund  

프롬프트 상세: [stage-1.md](../../../docs/prompts/03-stage-build/stage-1.md)
