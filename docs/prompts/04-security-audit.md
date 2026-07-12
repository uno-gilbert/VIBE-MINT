# 프롬프트: 배포 전 보안 Audit (필수)

Stage 3 완료 후, Sepolia 배포 **전에** 반드시 1회 실행하세요.

[00-rules.md](00-rules.md) 공통 규칙 + 현재 `.sol` 파일 `@` 멘션.

---

## 복붙용 프롬프트

```
@VibeMintNFT.sol

이 ERC-721 컨트랙트를 배포 전 보안 관점에서 Audit해 주세요.
코드는 아직 수정하지 말고, 먼저 findings만 보고하세요.

[검사 항목]
1. Access control: onlyOwner, whenNotPaused 누락/우회
2. Reentrancy: withdraw, mint 등 external call 순서 (CEI 패턴)
3. Integer / overflow: Solidity 0.8+ 기준 안전성
4. Mint economics: maxSupply, per-wallet cap, msg.value 검증
5. Pause: pause 상태에서 state change 차단
6. DoS / unbounded loop
7. 가스: 불필요한 storage write, redundant SLOAD
8. Centralization / owner abuse (교육용 acceptable 여부 명시)

[출력 형식]
| Severity | Location | Issue | Recommendation |
| Critical | ... | ... | ... |
| High | ... | ... | ... |
| Medium | ... | ... | ... |
| Low / Info | ... | ... | ... |

Critical/High가 있으면 수정된 코드 diff를 제안하세요.
마지막에 "Sepolia 테스트넷 교육용 — 메인넷 전문 Audit 필수" 한 줄을 포함하세요.
```

---

## Audit 후 수정 프롬프트

```
위 Audit의 Critical/High 항목만 수정하세요.
전체 파일 재작성 금지. 변경 diff와 Remix 재테스트 체크리스트 3항목만 출력하세요.
```

---

## 교육용 합격 기준

- Critical: **0건**
- High: **0건** (또는 강사 승인 하 수정 완료)
- Medium: 문서화 또는 수정

---

## 심화 참고 (수업 범위外)

- [Certora Prover (오픈소스)](https://www.certora.com/blog/certora-goes-open-source)
- [Hashlock — Vibe Coding Web3 Security](https://hashlock.com/blog/security-for-vibe-coding-web3-projects-and-dapps)
