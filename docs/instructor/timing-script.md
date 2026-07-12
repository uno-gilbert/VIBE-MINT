# 강사 진행 스크립트 (6시간 · 2026 · AI 바이브 코딩)

주최측 시간표 기준 **목표 · 진행 · 체크포인트**입니다. 세부 분량은 현장 상황에 맞게 조절하세요.

**구성**: 차시(**대제목**) → **중제목** 3개 → 중제목당 **소제목** 3개

---

## 3차시 구성 (한눈에 보기)

| 차시 (대제목) | 중제목 |
| --- | --- |
| **1차시** AI 바이브 코딩으로 이해하는 NFT · Spec 설계 | ① 오리엔테이션 · ② NFT·ERC 이해 · ③ Spec 설계 |
| **2차시** 점진적 빌드로 만드는 NFT 컨트랙트 · AI Audit | ① Remix·AI 규칙 · ② Stage 0→3 빌드 · ③ AI 보안 Audit |
| **3차시** Sepolia 배포와 NFT DApp · OpenSea | ① Sepolia 배포·mint · ② 프론트 DApp · ③ OpenSea·마무리 |

| 차시 | 워크플로우 | 핵심 이미지 |
| --- | --- | --- |
| 1차시 | Intent → Spec | [워크플로우](images/isgrs-workflow.png) |
| 2차시 | Generate → Review | [Stage 0→3](images/stage-build-flow.png) |
| 3차시 | Ship | [배포 흐름](images/deploy-dapp-flow.png) |

중제목·소제목 발표 그림: [../presentation/images/](../presentation/images/) · [../presentation/README.md](../presentation/README.md)

![6시간 워크숍 로드맵](images/workshop-timeline.png)

---

# 1차시 (대제목) — AI 바이브 코딩으로 이해하는 NFT · Spec 설계

**목표**: 바이브 코딩 워크플로우 이해 + NFT 개념 + VibeMint Spec 확정  
**워크플로우**: **Intent → Spec**

![AI 바이브 코딩 워크플로우](images/isgrs-workflow.png)

---

## 중제목 1-1. 오리엔테이션 — 바이브 코딩 워크플로우와 사전 준비

**목표**: 당일 로드맵·워크플로우·실습 환경 이해

### 소제목

1. **강사 소개·수업 환경** — 인사, Wi-Fi, Q&A 채널, 3차시 로드맵 안내  
   ![강사 소개·수업 환경](../presentation/images/session1-1-1-instructor-env.png)
2. **AI 바이브 코딩·워크플로우** — Intent→Spec→Generate→Review→Ship, iExec 등 사례, 「한 번에 전체 생성」의 위험  
   ![AI 바이브 코딩·워크플로우](../presentation/images/session1-1-2-vibe-workflow.png)
3. **오늘의 목표·사전 준비 점검** — VibeMint DApp 소개, MetaMask·Cursor·Sepolia 체크 ([pre-course-checklist](../pre-course-checklist.md))  
   ![오늘의 목표·사전 준비](../presentation/images/session1-1-3-prep-checklist.png)

**체크포인트**
- [ ] MetaMask + Sepolia 네트워크
- [ ] Cursor 로그인

---

## 중제목 1-2. NFT·ERC 이해 — 개념·표준·AI 역분석

**목표**: NFT와 ERC-721을 설명하고, AI로 컨트랙트를 읽을 수 있다

### 소제목

1. **NFT 핵심 개념** — 대체 가능/불가능(펀저블), 쪼갤 수 있음과의 차이, 온체인·오프체인 ([01-nft-concepts](../student/01-nft-concepts.md))  
   ![NFT 핵심 개념](../presentation/images/session1-2-1-nft-concepts.png)
2. **ERC 표준·OpenZeppelin** — ERC-721 vs ERC-1155, Ownable·Pausable·ReentrancyGuard, VibeMint 아키텍처  
   ![ERC 표준·OpenZeppelin](../presentation/images/session1-2-2-erc-openzeppelin.png)
3. **Cursor AI 역분석** — solution 컨트랙트를 자연어로 읽기, mint/owner/pause 역할 ([01-reverse-engineer](../prompts/01-reverse-engineer.md))  
   ![Cursor AI 역분석](../presentation/images/session1-2-3-cursor-reverse.png)

**체크포인트**
- [ ] mint / owner / pause 역할 설명 가능

---

## 중제목 1-3. Spec 설계 — 벤치마킹과 VibeMint 명세 확정

**목표**: 오후 Generate에 쓸 Spec을 확정한다

### 소제목

1. **유명 NFT 프로젝트 분석** — BAYC·Azuki 민팅·화이트리스트·maxSupply 구조 벤치마킹  
   ![유명 NFT 프로젝트 분석](../presentation/images/session1-3-1-nft-benchmark.png)
2. **Spec 템플릿·AI 작성** — YAML/표 명세, [02-spec-writing](../student/02-spec-writing.md) · [02-spec-generator](../prompts/02-spec-generator.md)  
   ![Spec 템플릿·AI 작성](../presentation/images/session1-3-2-spec-template.png)
3. **VibeMint Spec 확정·공유** — mintPrice·per-wallet cap·whitelist 조건 점검, 팀 공유  
   ![VibeMint Spec 확정·공유](../presentation/images/session1-3-3-spec-confirm.png)

**체크포인트**
- [ ] maxSupply, mintPrice, per-wallet cap, whitelist in Spec

### 1차시 마무리 한 줄

> Intent·Spec까지 확정. 다음은 코드를 **한 단계씩** 만든다.

---

## 점심

---

# 2차시 (대제목) — 점진적 빌드로 만드는 NFT 컨트랙트 · AI Audit

**목표**: Stage 0→3 점진적 빌드 + 배포 전 보안 Audit  
**워크플로우**: **Generate → Review**

![점진적 빌드 Stage 0→3](images/stage-build-flow.png)

---

## 중제목 2-1. Remix·AI 규칙 — Generate 준비

**목표**: AI 규칙과 Remix 연습 환경을 맞춘다

### 소제목

1. **00-rules 공통 규칙** — 한 번에 전체 생성 금지, Stage diff만, OpenZeppelin만 ([00-rules](../prompts/00-rules.md))  
   ![00-rules 공통 규칙](../presentation/images/session2-1-1-00-rules.png)
2. **Remix VM 환경** — Remix VM vs Injected Provider, Stage 테스트는 VM  
   ![Remix VM 환경](../presentation/images/session2-1-2-remix-vm.png)
3. **Compile·Deploy·Read/Write** — 컴파일, 배포, 파란(읽기)/주황(쓰기), Value(ether) ([03-stage-build/README](../prompts/03-stage-build/README.md))  
   ![Compile·Deploy·Read/Write](../presentation/images/session2-1-3-compile-deploy.png)

---

## 중제목 2-2. Stage 0→3 점진적 빌드 — 기능별 컨트랙트 완성

**목표**: Incremental prompt로 NFT 컨트랙트를 완성한다

### 소제목

1. **Stage 0~1** — ERC-721 뼈대 + public mint(0.001 ETH·지갑당 3개) ([stage-0](../prompts/03-stage-build/stage-0.md) · [stage-1](../prompts/03-stage-build/stage-1.md))  
   ![Stage 0~1](../presentation/images/session2-2-1-stage-0-1.png)
2. **Stage 2** — pause · ownerMint · withdraw · publicMint 토글 ([stage-2](../prompts/03-stage-build/stage-2.md))  
   ![Stage 2](../presentation/images/session2-2-2-stage-2.png)
3. **Stage 3** — whitelist · whitelistMint (시간 부족 시 solution) ([stage-3](../prompts/03-stage-build/stage-3.md) · [03-incremental-build](../student/03-incremental-build.md))  
   ![Stage 3](../presentation/images/session2-2-3-stage-3.png)

**체크포인트**
- [ ] Remix Stage 3 compile OK

**시간 부족 시**: Stage 3 생략 → `contracts/solution/` 참고

---

## 중제목 2-3. AI 보안 Audit — 배포 전 Review

**목표**: Critical/High 0건까지 수정한다

### 소제목

1. **Audit 프롬프트 실행** — findings 표 수령 ([04-security-audit](../prompts/04-security-audit.md))  
   ![Audit 프롬프트 실행](../presentation/images/session2-3-1-audit-run.png)
2. **Critical/High 수정** — diff만 적용, 전체 재작성 금지  
   ![Critical/High 수정](../presentation/images/session2-3-2-critical-fix.png)
3. **재컴파일·재테스트** — Remix Compile, mint/pause/withdraw 짧은 확인  
   ![재컴파일·재테스트](../presentation/images/session2-3-3-retest.png)

**체크포인트**
- [ ] Audit Critical/High 0건

### 2차시 마무리 한 줄

> 컨트랙트 완성 + **Audit(Review) 없이 배포하지 않는다.**

---

# 3차시 (대제목) — Sepolia 배포와 NFT DApp · OpenSea

**목표**: Sepolia 배포 · mint · 민팅 DApp · OpenSea 확인  
**워크플로우**: **Ship**

![Sepolia 배포 ~ DApp 완성 흐름](images/deploy-dapp-flow.png)

---

## 중제목 3-1. Sepolia 배포·mint — 테스트넷에 올리고 검증

**목표**: Injected Provider로 Sepolia 배포 + mint + Etherscan

### 소제목

1. **Faucet·Injected Provider 배포** — Sepolia ETH 확보, MetaMask 연결 Deploy, 컨트랙트 주소 저장  
   ![Faucet·Injected Provider 배포](../presentation/images/session3-1-1-faucet-deploy.png)
2. **설정·테스트 mint** — setBaseURI, (선택) whitelist, Value 0.001 ether mint  
   ![설정·테스트 mint](../presentation/images/session3-1-2-seturi-mint.png)
3. **Etherscan·멀티체인 개념** — tx/컨트랙트 확인, L1 Sepolia vs L2 소개 (hands-on은 Sepolia) ([04-deploy-sepolia](../student/04-deploy-sepolia.md))  
   ![Etherscan·멀티체인 개념](../presentation/images/session3-1-3-etherscan-multichain.png)

**체크포인트**
- [ ] Etherscan Sepolia contract
- [ ] 1회 mint 성공
- [ ] Contract Address 저장

---

## 중제목 3-2. 프론트 DApp — MetaMask 민팅 UI

**목표**: 브라우저에서 Connect Wallet → Mint

### 소제목

1. **환경 설정** — `frontend/starter`, `.env`에 `VITE_CONTRACT_ADDRESS`  
   ![환경 설정](../presentation/images/session3-2-1-env-setup.png)
2. **로컬 서버 실행** — `npm install` · `npm run dev` · localhost 접속  
   ![로컬 서버 실행](../presentation/images/session3-2-2-npm-dev.png)
3. **Connect · Mint** — MetaMask Sepolia 연결, 0.001 ETH mint ([05-frontend-mint](../student/05-frontend-mint.md))  
   ![Connect · Mint](../presentation/images/session3-2-3-connect-mint.png)

**체크포인트**
- [ ] Connect Wallet → Mint

---

## 중제목 3-3. OpenSea·마무리 — 마켓 확인과 수업 정리

**목표**: 테스트넷에서 NFT를 확인하고 워크플로우를 닫는다

### 소제목

1. **OpenSea 테스트넷 조회** — testnets.opensea.io, 인덱싱 지연(5~30분) 안내  
   ![OpenSea 테스트넷 조회](../presentation/images/session3-3-1-opensea.png)
2. **(선택) UI 보완** — [05-frontend-connect](../prompts/05-frontend-connect.md) 또는 solution 비교  
   ![(선택) UI 보완](../presentation/images/session3-3-2-ui-polish.png)
3. **마무리 Q&A·고지** — Intent→…→Ship 복습, Sepolia 교육용, 메인넷 전문 Audit 필수  
   ![마무리 Q&A·고지](../presentation/images/session3-3-3-wrap-qa.png)

**체크포인트**
- [ ] OpenSea testnet 또는 Etherscan으로 확인

### 3차시 마무리 한 줄

> 테스트넷에 **Ship** 완료. Intent → Spec → Generate → Review → Ship 전 구간을 하루 만에 경험.

---

## 마무리 멘트 (필수)

> 오늘 코드는 **Sepolia 테스트넷 교육용**입니다. 메인넷 배포 전 **전문 Audit** 필수. AI는 주니어처럼 쓰되 **Review(Audit)는 생략하지 마세요.**

---

## 대제목 · 중제목 · 소제목 요약

### 1차시

| 중제목 | 소제목 (3) |
| --- | --- |
| 1-1 오리엔테이션 | 강사·환경 / 바이브 코딩·워크플로우 / 목표·사전 준비 |
| 1-2 NFT·ERC 이해 | NFT 개념 / ERC·OpenZeppelin / Cursor 역분석 |
| 1-3 Spec 설계 | 프로젝트 분석 / Spec 템플릿·AI / Spec 확정·공유 |

### 2차시

| 중제목 | 소제목 (3) |
| --- | --- |
| 2-1 Remix·AI 규칙 | 00-rules / Remix VM / Compile·Deploy·Read/Write |
| 2-2 Stage 0→3 빌드 | Stage 0~1 / Stage 2 / Stage 3 |
| 2-3 AI 보안 Audit | Audit 실행 / Critical·High 수정 / 재컴파일·재테스트 |

### 3차시

| 중제목 | 소제목 (3) |
| --- | --- |
| 3-1 Sepolia 배포·mint | Faucet·Deploy / 설정·mint / Etherscan·멀티체인 |
| 3-2 프론트 DApp | .env 설정 / npm run dev / Connect·Mint |
| 3-3 OpenSea·마무리 | OpenSea 조회 / UI 보완(선택) / Q&A·Audit 고지 |

---

## 학습 자료 매핑

| 중제목 | 수강생 문서 |
| --- | --- |
| 1-1 오리엔테이션 | [pre-course-checklist](../pre-course-checklist.md) |
| 1-2 NFT·ERC 이해 | [01-nft-concepts](../student/01-nft-concepts.md) |
| 1-3 Spec 설계 | [02-spec-writing](../student/02-spec-writing.md) |
| 2-1 Remix·AI 규칙 | [03-stage-build/README](../prompts/03-stage-build/README.md) |
| 2-2 Stage 0→3 빌드 | [03-incremental-build](../student/03-incremental-build.md) |
| 2-3 AI 보안 Audit | [04-security-audit](../prompts/04-security-audit.md) |
| 3-1 Sepolia 배포·mint | [04-deploy-sepolia](../student/04-deploy-sepolia.md) |
| 3-2 프론트 DApp | [05-frontend-mint](../student/05-frontend-mint.md) |
| 3-3 OpenSea·마무리 | [00-walkthrough](../student/00-walkthrough.md) |

전체 따라하기: [00-walkthrough.md](../student/00-walkthrough.md)

---

## 이미지 파일 위치

| 파일 | 용도 |
| --- | --- |
| [images/workshop-timeline.png](images/workshop-timeline.png) | 수업 시작·전체 소개 |
| [images/isgrs-workflow.png](images/isgrs-workflow.png) | 1차시 워크플로우 |
| [images/stage-build-flow.png](images/stage-build-flow.png) | 2차시 Stage 실습 |
| [images/deploy-dapp-flow.png](images/deploy-dapp-flow.png) | 3차시 배포·DApp |
| [../presentation/images/](../presentation/images/) | 중제목 9장 · 소제목 27장 |

PPT에 넣을 때: `docs/instructor/images/` · `docs/presentation/images/`  
소제목 매핑 표: [../presentation/README.md](../presentation/README.md)
