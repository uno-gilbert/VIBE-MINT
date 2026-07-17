# Stage 1 프롬프트: 누구나 돈 내고 NFT 받기

Stage 0 코드를 `@` 멘션 + [00-rules.md](../00-rules.md).

Remix 기본 조작: [README.md](README.md) (Compile · Remix VM · 파란/주황 버튼 · Value)

---

## Intent

Stage 0 뼈대에 **유료 발행(mint)** 창구만 연다.  
가격 0.001 ETH, 전체 100개, **한 지갑당 3개**까지.

---

## 복붙용 프롬프트

아래를 Cursor에 그대로 붙여넣으세요. (Stage 0의 `VibeMintNFT.sol`을 `@`로 멘션)

```
지금 열린 Stage 0 VibeMintNFT.sol에 Stage 1만 추가해 주세요.
기존에 있는 코드는 지우지 말고, 필요한 부분만 덧붙이세요.

하고 싶은 것 (쉬운 말):
- 누구나 이더를 내고 NFT를 받을 수 있는 “발행” 기능 추가
- 가격은 0.001 ETH
- 전체는 100개를 넘지 않게
- 같은 지갑은 최대 3개까지만
- 돈을 덜 내면 거절
- 돈을 더 내면 남은 금액은 돌려주기 (가능하면)
- 안전한 방식으로 NFT를 민팅

하지 말 것:
- Stage 0에 있던 함수·변수 삭제
- 파일 전체를 처음부터 다시 쓰기
- pause, 화이트리스트 같은 다음 Stage 기능

버전은 그대로 (^0.8.31, OpenZeppelin @5.1.0)

응답 방식:
- 바뀐 코드(또는 완성본)를 주세요
- 무엇을 추가했는지 한글로 짧게 설명해 주세요
- Remix에서 어떻게 눌러보면 되는지 한글로 알려 주세요
```

---

## Remix 테스트 (구체적으로)

![Stage 1 Deploy · mint 캡처 해설](../../presentation/images/session2-2-1-stage-0-1.png)

따라하기·화면 해설: [stage-1-mint/README.md](../../../contracts/stages/stage-1-mint/README.md)

1. **재Compile → 재Deploy** (Remix VM) — Stage 0 배포본은 버림  
   - Deployed Contracts에 **빨간/주황 `mint`** 가 보이면 Stage 1 Deploy 성공  
2. Deploy 패널 **Value** = `0.001`, 단위 **ether**
3. 주황색(또는 빨간) `mint` → **transact**
4. 파란색으로 확인:
   - `totalMinted` → `1`
   - `ownerOf(0)` → 내 주소
   - `mintedCount(내주소)` → `1`
5. Value `0` → `mint` → **revert** (가격 검증)
6. 같은 Account로 mint를 **총 3회** 성공시킨 뒤 **4번째** → **revert** (지갑당 3개)

### 캡처에서 한눈에

| 화면 | 의미 |
| --- | --- |
| Compiler 초록 체크 · Compiled | Compile OK (Stage 완료 아님) |
| Remix VM (Osaka) | Stage 연습 환경 |
| Deployed Contracts의 `mint` | Stage 1에서 생긴 유료 발행 버튼 |
| 에디터의 `mint()` | 가격·100개·지갑당 3개 규칙 |

### 이 Stage에서 이해하는 것

| 확인 | 이해 |
| --- | --- |
| Value + mint 성공 | 이더를 내야 NFT 발행 |
| Value 0 → revert | 가격 검사 |
| 4번째 mint revert | 지갑당 3개 한도 |
| `ownerOf(0)` | 0번 NFT의 주인 |

---

## Audit 전 체크

1. 가격(이더) 검사를 하는가?
2. 전체 100개를 넘지 못하게 하는가?
3. 안전한 민팅 방식을 쓰는가?

## 다음

→ [stage-2.md](stage-2.md)
