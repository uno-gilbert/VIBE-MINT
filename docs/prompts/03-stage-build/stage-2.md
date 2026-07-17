# Stage 2 프롬프트: 긴급 중지 · 관리자 발행 · 수익 인출

Stage 1 코드 `@` 멘션 + [00-rules.md](../00-rules.md).

Remix 기본 조작: [README.md](README.md)

---

## Intent

판매를 **잠깐 멈출 수 있게** 하고, 관리자가 무료로 몇 개 주고할 수 있게 하며,  
쌓인 이더를 **관리자만 꺼내가게** 만든다. 일반 판매 on/off 스위치도 둔다.

---

## 복붙용 프롬프트

아래를 Cursor에 그대로 붙여넣으세요. (Stage 1의 `VibeMintNFT.sol`을 `@`로 멘션)

```
지금 열린 Stage 1 VibeMintNFT.sol에 Stage 2만 추가해 주세요.
기존 mint·가격·한도 로직은 유지하고, 필요한 기능만 덧붙이세요.

하고 싶은 것 (쉬운 말):
- 위급할 때 발행을 전부 멈출 수 있는 “일시정지 / 재개” (관리자만)
- 일반 사람 판매를 켜고 끄는 스위치 (기본은 켜짐, 관리자만 변경)
- 일시정지 중이거나 판매가 꺼져 있으면 일반 mint는 거절
- 관리자가 원하는 주소에 NFT를 무료로 여러 개 줄 수 있는 기능
  (이때도 전체 100개 한도는 지키기, 일시정지면 불가)
- 컨트랙트에 쌓인 이더를 관리자만 안전한 방식으로 인출
- 이더를 그냥 보낼 수 있게 receive 허용

하지 말 것:
- 파일 전체 다시 쓰기
- 화이트리스트(다음 Stage)
- 기존 Stage 1 기능 삭제

버전은 그대로 (^0.8.31, OpenZeppelin @5.1.0 — 일시정지·재진입 방지 포함)

응답 방식:
- 바뀐 코드(또는 완성본)를 주세요
- 무엇을 추가했는지 한글로 짧게 설명해 주세요
- Remix에서 pause / mint / 관리자 발행 / 인출 순서로 어떻게 시험하면 되는지 한글로 알려 주세요
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
| pause 후 mint 실패 | 긴급 중지 |
| publicMintEnabled | 일반 판매 on/off |
| ownerMint Value 0 | 관리자 예약분(무료) |
| #1 withdraw 실패 | 수익은 관리자만 인출 |

---

## Audit 전 체크

1. 인출할 때 재진입 공격을 막는가?
2. 일시정지 때 관리자 발행도 막히는가?
3. 인출 순서가 “잔액 확인 → 상태 반영 → 송금”인가?

## 다음

→ [stage-3.md](stage-3.md)
