# Stage 3 프롬프트: 화이트리스트만 미리 받기

Stage 2 코드 `@` 멘션 + [00-rules.md](../00-rules.md).

Remix 기본 조작: [README.md](README.md)

---

## Intent

**초대된 지갑만** 따로 민팅할 수 있게 한다.  
일반 판매가 꺼져 있어도, 화이트리스트는 받을 수 있다.

---

## 복붙용 프롬프트

아래를 Cursor에 그대로 붙여넣으세요. (Stage 2의 `VibeMintNFT.sol`을 `@`로 멘션)

```
지금 열린 Stage 2 VibeMintNFT.sol에 Stage 3만 추가해 주세요.
지금까지 만든 pause·mint·인출 기능은 유지하고, 화이트리스트만 덧붙이세요.

하고 싶은 것 (쉬운 말):
- 허용된 지갑인지 기록해 두는 목록
- 관리자가 여러 주소를 한 번에 “허용 / 해제”할 수 있게
  (한 번에 너무 많이 넣 않도록, 대략 200개 이하로 제한)
- 허용된 사람만 쓰는 별도 발행(화이트리스트 민팅)
  - 가격은 일반 mint와 같게 (0.001 ETH)
  - 전체 100개·지갑당 3개 한도도 같게
  - 일반 판매 스위치가 꺼져 있어도 이 경로는 가능
  - 일시정지 중이면 불가
- 목록이 바뀔 때 이벤트로 남기기

하지 말 것:
- Merkle 트리 같은 복잡한 방식
- 파일 전체 다시 쓰기
- 기존 Stage 2 기능 삭제

버전은 그대로 (^0.8.31, OpenZeppelin @5.1.0)

응답 방식:
- 바뀐 코드(또는 완성본)를 주세요
- 무엇을 추가했는지 한글로 짧게 설명해 주세요
- Remix에서 목록 등록 → 일반 mint 끄기 → 화이트리스트 민팅 시험 순서를 한글로 알려 주세요
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

Remix에서 주소 배열은 대략 다음처럼 넣습니다.

```text
["0x5B38Da6a701c568545dCfcB03FcB875f56beddC4"]
```

Account 주소를 복사해 따옴표·대괄호로 감쌉니다.

### 이 Stage에서 이해하는 것

| 확인 | 이해 |
| --- | --- |
| 일반 판매 off + 화이트리스트 mint OK | 화이트리스트는 **별도 창구** |
| 미등록 주소 revert | 초대된 지갑만 |
| mintedCount 공유 | 일반+화이트리스트 합쳐 지갑당 3개 |
| pause 공통 | 긴급 중지는 모든 발행에 적용 |

---

## Audit 전 체크

1. 일반 mint와 화이트리스트 mint가 같은 지갑 한도(3개)를 공유하는가?
2. 목록을 한 번에 너무 많이 넣지 못하게 막았는가?
3. Stage 2의 pause·인출이 여전히 동작하는가?

완료 후 → [04-security-audit.md](../04-security-audit.md) **필수**
