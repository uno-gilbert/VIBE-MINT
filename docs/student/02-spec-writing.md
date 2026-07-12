# 02. Spec 작성 — AI가 꼬이지 않게 주문하기

## 학습 목표

- 비즈니스 요구 → **구체적 Spec** 변환
- AI 프롬프트에 넣을 Spec 템플릿 작성

---

## 왜 Spec인가?

AI에게 "NFT 만들어줘"라고 하면 전체 코드를 한 번에 생성하다 **보안·로직 누락**이 빈번합니다.  
2026년 실무 워크플로우는 **Intent → Spec → Generate → Review** 입니다.

---

## VibeMint Spec 템플릿

아래를 복사해 빈칸을 채우거나, [02-spec-generator.md](../prompts/02-spec-generator.md)로 AI 초안을 받으세요.

```yaml
contract:
  name: VibeMint
  symbol: VMINT
  standard: ERC-721
  chain: Ethereum Sepolia (testnet only)

supply:
  maxSupply: 100
  maxPerWallet: 3

economics:
  mintPrice: 0.001 ether
  withdraw: owner only, full balance

access:
  owner: deployer (Ownable)
  publicMintEnabled: toggle by owner, default true
  whitelist: mapping(address => bool)

functions:
  - name: mint
    caller: anyone (if public enabled)
    payable: true
    checks: [not paused, public enabled, payment, supply, wallet cap]
  - name: whitelistMint
    caller: whitelisted only
    payable: true
  - name: ownerMint
    caller: owner
    payable: false
  - name: pause / unpause
    caller: owner
  - name: withdraw
    caller: owner
    guard: nonReentrant

invariants:
  - totalMinted <= maxSupply always
  - mintedCount[addr] <= maxPerWallet always
```

---

## Spec 품질 체크리스트

- [ ] revert 조건이 함수마다 명시됨
- [ ] ETH 금액 단위 (ether vs wei) 명확
- [ ] pause 시 영향받는 함수 목록 있음
- [ ] 테스트넷 only / 메인넷 Audit 필요 문구

---

## 실습 (30분)

1. Spec YAML 작성 (개인 또는 팀)
2. 옆 사람 Spec과 diff — **누락된 revert 조건** 찾기
3. 확정 Spec을 오후 Stage 빌드에 사용

---

## 다음

→ [03-incremental-build.md](03-incremental-build.md)
