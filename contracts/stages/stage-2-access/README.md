# Stage 2: Pause · OwnerMint · Withdraw — 따라하기

Stage 1 출고 창구에 **운영·안전** 기능을 추가합니다.

> **한 줄**: 비상등(pause) · 관리자 무료 출고(ownerMint) · 금고 인출(withdraw)

이전: [Stage 1](../stage-1-mint/README.md) · 목록: [../README.md](../README.md)

---

## 이 Stage 목표

- [ ] Pausable · ReentrancyGuard · publicMint 토글 추가
- [ ] pause 후 mint revert / unpause 후 성공
- [ ] ownerMint(Value 0) 성공, #1은 revert
- [ ] withdraw는 owner(#0)만 성공

---

## 따라하기 (순서대로)

### Step 2-1. Intent

> “Pausable, ownerMint, withdraw, publicMintEnabled 토글 추가.”

### Step 2-2. Cursor로 diff 받기

1. `@VibeMintNFT.sol` 멘션 + [00-rules](../../../docs/prompts/00-rules.md)  
2. [stage-2.md](../../../docs/prompts/03-stage-build/stage-2.md) 복붙용 프롬프트  
3. **diff만** 확인 (Stage 1 mint 삭제 금지)  

막히면: [VibeMintNFT.sol](./VibeMintNFT.sol)

- [ ] Stage 2 코드 반영 준비

### Step 2-3. Remix 재Compile · 재Deploy

1. 코드 붙여넣기·저장  
2. Compiler **0.8.31** · EVM **osaka** Compile  
3. Remix VM → **Deploy**

- [ ] 새 Deploy 완료 (`pause`, `withdraw`, `ownerMint` 보임)

### Step 2-4. ETH 쌓기

1. Value `0.001` **ether** → `mint` → transact  
2. (출고 1회 + 컨트랙트에 ETH 적립)

- [ ] mint 1회 성공

### Step 2-5. pause 테스트

1. Account #0 → `pause` → transact  
2. Value 0.001 → `mint` → **revert**  
3. `unpause` → mint 다시 **성공**

- [ ] pause 중 mint 차단  
- [ ] unpause 후 mint OK  

### Step 2-6. public 창구만 닫기

1. `setPublicMintEnabled(false)` → mint → **revert**  
2. (선택) `true`로 다시 열기  

- [ ] publicMintEnabled 동작 확인

### Step 2-7. ownerMint

1. Value = **0** (비우기)  
2. `ownerMint` — `to` = 내 주소(또는 #1), `quantity` = `1` → transact → **성공**  
3. Account **#1** → `ownerMint` → **revert**

- [ ] owner만 ownerMint 가능

### Step 2-8. withdraw

1. Account **#1** → `withdraw` → **revert**  
2. Account **#0** → `withdraw` → **성공** (잔액 증가)

- [ ] owner만 withdraw 가능

### Step 2-9. Stage 2 완료 체크

- [ ] pause 시 mint(·ownerMint) 차단?  
- [ ] withdraw에 `nonReentrant`?  
- [ ] ownerMint는 결제 없이 cap 안?

**통과** → [Stage 3 따라하기](../stage-3-whitelist/README.md)

---

## 막히면

| 증상 | 해결 |
| --- | --- |
| ownerMint 실패 | Value를 **0**으로 |
| #1 withdraw 성공? | 비정상 — owner는 Deploy한 #0 |
| 버튼 없음 | 재Compile + 재Deploy |

---

## 읽어 두면 좋은 설명

| 기능 | 쉬운 말 | 비유 |
| --- | --- | --- |
| `pause` | 긴급 중지 | 공장 비상등 |
| `publicMintEnabled` | 일반 mint만 on/off | 매장 셔터 |
| `ownerMint` | 관리자 무료 발행 | 예약·팀용 출고 |
| `withdraw` | 모인 ETH 인출 | 금고 → 사장 |
| `nonReentrant` | 인출 중 재호출 방지 | 금고 이중 개방 잠금 |

### Spec 요약

- 모든 mint 경로: `whenNotPaused`  
- public mint: `publicMintEnabled` + 결제  
- withdraw: onlyOwner + nonReentrant  

프롬프트: [stage-2.md](../../../docs/prompts/03-stage-build/stage-2.md)
