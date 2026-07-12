# 03. 점진적 NFT 컨트랙트 빌드

## 학습 목표

- **점진적 빌드(Incremental Build)** 가 무엇인지 이해한다
- Stage 0 → 3 순서로 Cursor + Remix 실습을 완료한다
- 각 Stage 후 **컴파일 확인** 습관을 든다
- 배포 전 **AI 보안 Audit**을 1회 실행한다

---

## 1. 점진적 빌드란? (먼저 이해하기)

### 한 번에 vs 한 단계씩

![한 번에 전체 생성 X vs 점진적 빌드 O](images/incremental-vs-all-at-once.png)

| 방식 | 하는 일 | 문제 |
| --- | --- | --- |
| **한 번에 전체 생성** ❌ | “NFT 컨트랙트 전부 짜줘” | AI가 꼬임, 보안 누락, 디버깅 어려움 |
| **점진적 빌드** ✅ | Stage 0 → 1 → 2 → 3 **기능만 추가** | 어디서 틀렸는지 명확, Audit하기 쉬움 |

**한 줄 정리**: AI를 **주니어 개발자**처럼 — **작업을 나눠서** 시키고, **매번 Compile**로 확인합니다.

### 오늘 쓰는 도구

![Cursor → Remix → MetaMask 흐름](images/incremental-tools-flow.png)

| 도구 | 역할 |
| --- | --- |
| **Cursor** | AI에게 Stage별 코드 **diff** 요청 |
| **Remix** | Solidity **컴파일·배포** (브라우저) |
| **MetaMask** | Sepolia 지갑 (배포·mint 시) |

---

## 2. Stage 0 → 3 — 무엇이 쌓이나?

![Stage 0→3 계단 — 추가되는 기능](images/stage-0-to-3-detail.png)

| Stage | 한 줄 요약 | 새로 생기는 것 |
| --- | --- | --- |
| **0** | NFT **뼈대** | ERC721, Ownable, maxSupply=100, tokenURI |
| **1** | **민팅** | `mint()` + 0.001 ETH + 지갑당 3개 cap |
| **2** | **관리·안전** | pause, ownerMint, withdraw |
| **3** | **화이트리스트** | whitelist + `whitelistMint()` |

> Stage 0에는 **mint 함수가 없습니다.** 1부터 추가됩니다.

---

## 3. Stage마다 반복하는 5단계

![Stage마다 반복하는 5단계](images/stage-repeat-loop.png)

```
Intent → Spec 확인 → Cursor Generate → Remix Compile → 체크 3문항
```

| 단계 | 하는 일 |
| --- | --- |
| **Intent** | “Stage 1에서 mint만 추가” 한 문장 |
| **Spec** | [02-spec-writing.md](02-spec-writing.md) 명세와 맞는지 확인 |
| **Generate** | Cursor + Stage 프롬프트 ( **00-rules 먼저** ) |
| **Compile** | Remix 0.8.20 — **에러 0** 확인 |
| **체크** | Stage README의 Audit 전 3문항 |

---

## 4. 시작 전 준비 (3가지)

1. **[00-rules.md](../prompts/00-rules.md)** — Cursor **첫 메시지**에 붙여넣기
2. **[Remix IDE](https://remix.ethereum.org)** — `VibeMintNFT.sol` 파일 생성
3. **참고 코드** — `contracts/stages/` 각 Stage 폴더

| Stage | 폴더 | 프롬프트 |
| --- | --- | --- |
| 0 | [stage-0-base](../../contracts/stages/stage-0-base/) | [stage-0.md](../prompts/03-stage-build/stage-0.md) |
| 1 | [stage-1-mint](../../contracts/stages/stage-1-mint/) | [stage-1.md](../prompts/03-stage-build/stage-1.md) |
| 2 | [stage-2-access](../../contracts/stages/stage-2-access/) | [stage-2.md](../prompts/03-stage-build/stage-2.md) |
| 3 | [stage-3-whitelist](../../contracts/stages/stage-3-whitelist/) | [stage-3.md](../prompts/03-stage-build/stage-3.md) |

**Remix 사용법 · Stage별 확인 체크리스트**: [../prompts/03-stage-build/README.md](../prompts/03-stage-build/README.md)

---

## 5. Stage별 따라하기

### Stage 0 — ERC-721 뼈대 (약 20분)

**Intent**: “VibeMint 이름의 ERC-721 뼈대만. mint는 아직 없음.”

1. Remix에 `VibeMintNFT.sol` 생성
2. Cursor + [stage-0.md](../prompts/03-stage-build/stage-0.md) → 코드 반영
3. Remix **Compile** (Solidity **0.8.20**)
4. 막히면 → `contracts/stages/stage-0-base/VibeMintNFT.sol` 비교

**체크 3문항**
- [ ] `setBaseURI`는 owner만?
- [ ] `maxSupply` = 100?
- [ ] 불필요한 `payable` 없음?

---

### Stage 1 — Public Mint (약 20분)

**Intent**: “Stage 0에 `mint()` payable만 추가. 나머지 유지.”

1. Cursor에서 `@VibeMintNFT.sol` 멘션
2. [stage-1.md](../prompts/03-stage-build/stage-1.md) 실행
3. **전체 재작성 금지** — mint 관련만
4. Recompile → (VM) Deploy 후 `mint` **0.001 ETH** 테스트

**체크 3문항**
- [ ] `msg.value` 검증?
- [ ] `totalMinted` < `maxSupply`?
- [ ] `_safeMint` 사용?

---

### Stage 2 — Pause · Owner · Withdraw (약 25분)

**Intent**: “Pausable, ownerMint, withdraw 추가.”

1. [stage-2.md](../prompts/03-stage-build/stage-2.md) 실행
2. Recompile
3. `pause()` 호출 후 `mint` → **revert** 확인
4. `ownerMint` 1회, `withdraw` (owner만) 테스트

**체크 3문항**
- [ ] withdraw에 reentrancy guard?
- [ ] pause 시 mint 중지?
- [ ] withdraw CEI 순서?

---

### Stage 3 — Whitelist (약 25분)

**Intent**: “whitelist mapping + `whitelistMint()` 추가.”

1. [stage-3.md](../prompts/03-stage-build/stage-3.md) 실행
2. Recompile
3. `setWhitelist([내주소], true)`
4. `setPublicMintEnabled(false)` → public mint 막힘, whitelist mint 성공

**체크 3문항**
- [ ] non-whitelist가 `whitelistMint` revert?
- [ ] `setWhitelist` batch 길이 제한?
- [ ] Stage 2 pause/withdraw 여전히 동작?

**⏱ 시간 부족 시**: Stage 3 생략 → [solution](../../contracts/solution/VibeMintNFT.sol) 참고

---

## 6. 배포 전 AI 보안 Audit (필수 · 약 15분)

![배포 전 AI 보안 Audit](images/security-audit-before-deploy.png)

Stage 3(또는 solution) 완료 후, **Sepolia 배포 전** 반드시:

1. Cursor에 `@VibeMintNFT.sol` + [04-security-audit.md](../prompts/04-security-audit.md)
2. **Critical / High** 항목 수정
3. Remix **Recompile**

| 합격 기준 | |
| --- | --- |
| Critical | **0건** |
| High | **0건** (또는 수정 완료) |

> **Sepolia 테스트넷 교육용** — 메인넷 배포 전 **전문 Audit** 필수

---

## 7. 막혔을 때

| 증상 | 해결 |
| --- | --- |
| AI가 전체 파일 재작성 | 00-rules + “Stage N diff만” |
| Compile error | OpenZeppelin import, 0.8.20 확인 |
| 여전히 실패 | [troubleshooting.md](../instructor/troubleshooting.md) |
| 정답 비교 | [VibeMintNFT.sol](../../contracts/solution/VibeMintNFT.sol) |

---

## 이미지 한눈에 보기

| 그림 | 파일 |
| --- | --- |
| 한 번에 vs 점진적 | [incremental-vs-all-at-once.png](images/incremental-vs-all-at-once.png) |
| 도구 흐름 | [incremental-tools-flow.png](images/incremental-tools-flow.png) |
| Stage 0→3 | [stage-0-to-3-detail.png](images/stage-0-to-3-detail.png) |
| Stage 반복 5단계 | [stage-repeat-loop.png](images/stage-repeat-loop.png) |
| 보안 Audit | [security-audit-before-deploy.png](images/security-audit-before-deploy.png) |

---

## 다음

→ [04-deploy-sepolia.md](04-deploy-sepolia.md) — Audit 통과 후 Sepolia 배포
