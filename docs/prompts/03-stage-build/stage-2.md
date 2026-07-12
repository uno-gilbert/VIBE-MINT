# Stage 2 프롬프트: Owner Mint, Pause, Withdraw

Stage 1 코드 `@` 멘션 + [00-rules.md](../00-rules.md).

Remix 기본 조작: [README.md](README.md)

---

## Intent

Pausable, ownerMint, withdraw, publicMint 토글 추가.

---

## 복붙용 프롬프트

```
Stage 1 VibeMintNFT.sol에 Stage 2 diff만 추가하세요.

[추가 Spec]
- import Pausable, inherit Pausable
- bool public publicMintEnabled (default true)
- setPublicMintEnabled(bool) onlyOwner
- mint()에 whenNotPaused, require publicMintEnabled
- ownerMint(address to, uint256 quantity) onlyOwner whenNotPaused
  - quantity loop, each _safeMint, supply cap check
- pause() / unpause() onlyOwner
- withdraw() onlyOwner nonReentrant (ReentrancyGuard 추가)
  - CEI: balance 기록 후 call
- receive() external payable

OpenZeppelin ReentrancyGuard 사용.
```

---

## Remix 테스트 (구체적으로)

1. **재Compile → 재Deploy** (Remix VM)
2. Value `0.001` ether → `mint` 1회 (컨트랙트에 ETH 쌓기)
3. `pause` → **transact** → `mint` → **revert**
4. `unpause` → `mint` 다시 가능
5. `setPublicMintEnabled(false)` → `mint` → **revert**
6. `setPublicMintEnabled(true)`로 복구(선택)
7. `ownerMint`:
   - `to` = Account #0 또는 #1 주소
   - `quantity` = `1`
   - Value는 **0** → **transact** → 성공
8. Account를 **#1**로 바꿔 `ownerMint` / `withdraw` → **revert**
9. Account **#0**으로 `withdraw` → 성공 (잔액 증가)

### 이 Stage에서 이해하는 것

| 확인 | 이해 |
| --- | --- |
| pause 후 mint 실패 | 긴급 중지 (`whenNotPaused`) |
| publicMintEnabled | public 판매 on/off |
| ownerMint Value 0 | 관리자 예약분(무료) |
| #1 withdraw 실패 | 수익은 owner만 인출 |

---

## Audit 전 체크

1. withdraw에 reentrancy guard?
2. pause 시 ownerMint도 중지? (Spec: whenNotPaused on all mint paths)
3. withdraw CEI 순서?

## 다음

→ [stage-3.md](stage-3.md)
