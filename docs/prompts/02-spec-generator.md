# 프롬프트: NFT Spec 생성기

[00-rules.md](00-rules.md) 공통 규칙을 붙여넣은 뒤 사용하세요.

---

## 복붙용 프롬프트

```
NFT ERC-721 컨트랙트 Spec을 작성해 주세요. 코드는 아직 작성하지 마세요.

[비즈니스 요구]
- 컬렉션명: VibeMint, 심볼: VMINT
- 최대 발행량: 100
- public mint 가격: 0.001 ETH
- 지갑당 public mint 최대: 3개
- owner 전용 mint (예약분)
- 긴급 pause / unpause
- owner만 withdraw (컨트랙트 ETH 잔액 인출)
- whitelist: mapping 기반, whitelist만 mint 가능한 함수 1개
- public mint on/off 토글 (owner)
- 배포 체인: Ethereum Sepolia 테스트넷 only

[출력 형식 — YAML]
contract:
  name: VibeMint
  standard: ERC-721
  ...
state:
  - name: ...
    type: ...
    description: ...
functions:
  - name: ...
    access: ...
    inputs: ...
    effects: ...
    reverts: ...
invariants:
  - ...
events:
  - ...
security_notes:
  - ...

Spec만 출력하고, 모호한 부분은 [ASSUMPTION]으로 표시하세요.
```

---

## Spec 검증 체크리스트

- [ ] `totalSupply() <= maxSupply` 불변 조건 있음
- [ ] mint 함수별 ETH 요구량 명시
- [ ] pause 시 mint 차단 명시
- [ ] withdraw reentrancy 고려 (Checks-Effects-Interactions)

Spec 확정 후 Stage 0 빌드를 시작하세요 → [03-stage-build/stage-0.md](03-stage-build/stage-0.md)
