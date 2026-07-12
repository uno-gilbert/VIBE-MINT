# Stage 1 프롬프트: Public Mint + Supply Cap

Stage 0 코드를 `@` 멘션 + [00-rules.md](../00-rules.md).

Remix 기본 조작: [README.md](README.md) (Compile · Remix VM · 파란/주황 버튼 · Value)

---

## Intent

payable `mint()` 추가: 가격 검증, maxSupply, 지갑당 3개 cap.

---

## 복붙용 프롬프트

```
Stage 0 VibeMintNFT.sol에 Stage 1 diff만 추가하세요. 기존 코드 구조 유지.

[추가 Spec]
- mintPrice = 0.001 ether (immutable 또는 constant)
- MAX_PER_WALLET = 3
- mapping(address => uint256) public mintedCount
- function mint() external payable
  - require msg.value >= mintPrice
  - require totalMinted < maxSupply
  - require mintedCount[msg.sender] < MAX_PER_WALLET
  - _safeMint(msg.sender, nextTokenId)
  - mintedCount++, totalMinted++
- refund excess ETH if msg.value > mintPrice (optional but recommended)

Stage 0 함수/변수 삭제 금지.
```

---

## Remix 테스트 (구체적으로)

1. **재Compile → 재Deploy** (Remix VM) — Stage 0 배포본은 버림
2. Deploy 패널 **Value** = `0.001`, 단위 **ether**
3. 주황색 `mint` → **transact**
4. 파란색으로 확인:
   - `totalMinted` → `1`
   - `ownerOf(0)` → 내 주소
   - `mintedCount(내주소)` → `1`
5. Value `0` → `mint` → **revert** (가격 검증)
6. 같은 Account로 mint를 **총 3회** 성공시킨 뒤 **4번째** → **revert** (지갑당 3개)

### 이 Stage에서 이해하는 것

| 확인 | 이해 |
| --- | --- |
| Value + mint 성공 | payable = ETH를 내야 NFT 발행 |
| Value 0 → revert | `msg.value` 검증 |
| 4번째 mint revert | per-wallet cap |
| `ownerOf(0)` | tokenId 0번 NFT의 주인 |

---

## Audit 전 체크

1. `msg.value` 검증 있는가?
2. `totalMinted`가 `maxSupply` 초과 불가한가?
3. `_safeMint` 사용하는가?

## 다음

→ [stage-2.md](stage-2.md)
