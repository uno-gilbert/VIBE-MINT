# Stage 3 프롬프트: Whitelist Mint

Stage 2 코드 `@` 멘션 + [00-rules.md](../00-rules.md).

Remix 기본 조작: [README.md](README.md)

---

## Intent

`mapping(address => bool) whitelist` + `whitelistMint()` 추가.

---

## 복붙용 프롬프트

```
Stage 2 VibeMintNFT.sol에 Stage 3 diff만 추가하세요.

[추가 Spec]
- mapping(address => bool) public whitelist
- setWhitelist(address[] calldata accounts, bool allowed) onlyOwner
  - unbounded loop 주의: 교육용으로 배열 길이 require <= 200
- function whitelistMint() external payable whenNotPaused
  - require whitelist[msg.sender]
  - mintPrice 동일, mintedCount / maxSupply 동일 규칙
  - publicMintEnabled와 무관 (whitelist 전용 경로)
- event WhitelistUpdated(address indexed account, bool allowed)

Merkle tree는 구현하지 마세요 (보너스).
```

---

## Remix 테스트 (구체적으로)

1. **재Compile → 재Deploy** (Remix VM)
2. Account #0(owner):
   - `setWhitelist`  
     - `accounts`: `["0x...Account0주소"]` (Remix 배열 형식)  
     - `allowed`: `true`  
     → **transact**
3. `whitelist(내주소)` → `true`
4. `setPublicMintEnabled(false)` → **transact**
5. Value `0.001` ether → `mint` → **revert** (public 꺼짐)
6. 같은 Value → `whitelistMint` → **성공**
7. Account **#1**(미등록) → Value 0.001 → `whitelistMint` → **revert**
8. (선택) `pause` → `whitelistMint` → **revert**

### `setWhitelist` 입력 팁

Remix에서 address 배열은 대략 다음처럼 넣습니다.

```text
["0x5B38Da6a701c568545dCfcB03FcB875f56beddC4"]
```

Account 주소를 복사해 따옴표·대괄호로 감쌉니다.

### 이 Stage에서 이해하는 것

| 확인 | 이해 |
| --- | --- |
| public off + whitelistMint OK | 화이트리스트는 **별도 경로** |
| 미등록 주소 revert | 허용된 지갑만 mint |
| mintedCount 공유 | public+whitelist 합쳐 지갑당 3개 |
| pause 공통 | 긴급 중지는 모든 mint에 적용 |

---

## Audit 전 체크

1. whitelist와 public mint 카운터 공유 — per-wallet cap 3 유지?
2. setWhitelist loop gas / length limit?
3. Stage 2 pause/withdraw 여전히 동작?

완료 후 → [04-security-audit.md](../04-security-audit.md) **필수**
