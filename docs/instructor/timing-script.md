# 강사 진행 스크립트 (6시간 · 2026 · AI 바이브 코딩)

주최측 시간표 기준 **목표 · 진행 · 체크포인트**입니다. 세부 분량은 현장 상황에 맞게 조절하세요.

**구성**: 차시(**대제목**) → **중제목** 3개 → 중제목당 **소제목** 3개

---

## 3차시 구성 (한눈에 보기)

| 차시 (대제목) | 중제목 |
| --- | --- |
| **1차시** AI 바이브 코딩으로 이해하는 NFT · Spec 설계 | ① 오리엔테이션 · ② NFT·ERC 이해 · ③ Spec 설계 |
| **2차시** 점진적 빌드로 만드는 NFT 컨트랙트 · AI Audit | ① Remix·AI 규칙 · ② Stage 0→3 빌드 · ③ AI 보안 Audit |
| **3차시** Sepolia 배포와 NFT DApp · 확인 | ① Sepolia 배포·mint · ② 프론트 DApp · ③ Etherscan·마무리 |

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

1. **강사 소개·수업 환경** — 인사, Q&A 채널, 3차시 로드맵 안내, 실습 저장소 GitHub 공유  
   > 저장소: [https://github.com/uno-gilbert/VIBE-MINT](https://github.com/uno-gilbert/VIBE-MINT)  
   > 수강생에게 clone 또는 ZIP 다운로드 안내 (`git clone https://github.com/uno-gilbert/VIBE-MINT.git`)  
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

   **왜 여기서 보나?**  
   오후 Generate에 넣을 Spec은 “느낌”이 아니라 **실제 NFT가 쓰는 비즈니스 규칙**에서 뽑습니다.  
   유명 프로젝트를 코드/민팅 관점으로 보면, VibeMint에 넣을 항목이 자연스럽게 드러납니다.

   **강사 멘트 (핵심)**  
   > “BAYC·Azuki를 따라 만들자는 게 아닙니다.  
   > **누가 / 얼마에 / 몇 개까지 / 언제 멈출 수 있는지**가 컨트랙트에 어떻게 박히는지 보는 겁니다.”

   **BAYC (Bored Ape Yacht Club) — 무엇을 배울까**

   | 관찰 포인트 | 수업용으로 말하는 법 | VibeMint로 옮기면 |
   | --- | --- | --- |
   | **고정 supply** | 컬렉션 크기가 처음부터 정해져 있음 → 희소성·기대감 | `maxSupply = 100` (교육용으로 축소) |
   | **PFP·커뮤니티** | NFT = 그림만이 아니라 **멤버십·브랜드** | 오늘은 소유권·민팅 규칙에 집중 |
   | **민팅 이후 거래** | 발행 규칙과 2차 마켓은 별개 | 민팅 Spec ≠ OpenSea 규칙 |
   | **관리·운영** | 대형 프로젝트도 접근 제어·일시 중지가 있음 | Stage 2 `pause` / `withdraw` 예고 |

   **Azuki — 무엇을 배울까**

   | 관찰 포인트 | 수업용으로 말하는 법 | VibeMint로 옮기면 |
   | --- | --- | --- |
   | **화이트리스트 민팅** | 먼저 **초대된 주소만** 민팅 → 봇·가스전쟁 완화 | Stage 3 `whitelist` + `whitelistMint` |
   | **단계적 민팅** | WL → public 처럼 **창구를 나눔** | `publicMintEnabled` 토글 + WL 별도 경로 |
   | **지갑당 수량 제한** | 한 지갑이 supply를 쓸어가지 못하게 | `maxPerWallet = 3` |
   | **아트·브랜딩** | 비주얼은 오프체인, 규칙은 온체인 | `setBaseURI` / `tokenURI` (메타데이터) |

   **보드에 적을 분석 질문 5개** (수강생과 함께 답하기)

   1. **누가** mint할 수 있는가? → public / whitelist / owner  
   2. **얼마**를 내야 하는가? → `mintPrice`  
   3. **최대 몇 개**까지? → `maxSupply`, per-wallet cap  
   4. **언제 멈출** 수 있는가? → `pause`  
   5. **수익은 어디로?** → `withdraw` (owner)

   **공통 패턴 → Spec 후보 (칠판 요약)**

   ```text
   maxSupply          ← 희소성·발행 한도
   mintPrice          ← 경제(유료 mint)
   maxPerWallet       ← 독과점·봇 완화
   whitelist          ← 사전 허용 민팅
   publicMint on/off  ← 공개 창구 개폐
   pause / withdraw   ← 운영·안전
   ```

   **오늘 수업에서의 범위 (오해 방지)**  
   - 메인넷 BAYC/Azuki **소스 전체를 따라 구현하지 않음**  
   - 숫자·이벤트·로열티·Merkle 등은 **개념만** (교육 Spec은 단순 mapping WL)  
   - 목표는 “유명 프로젝트에도 있는 규칙”을 **VibeMint YAML에 옮길 항목으로 번역**하는 것

   **진행 팁**  
   - 시간 촉박하면 BAYC=supply·브랜드, Azuki=WL·단계 민팅만 대비표로 끝  
   - “이 5질문이 Spec 템플릿의 빈칸”이라고 다음 소제목으로 연결  
   - 발표 그림(선택): [session1-3-1-nft-benchmark.png](../presentation/images/session1-3-1-nft-benchmark.png)

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
3. **Compile·Deploy·Read/Write** — Remix 메뉴 ①→④ 순서, `VibeMintNFT.sol` 실습 캡처 ([03-stage-build/README](../prompts/03-stage-build/README.md))  
   ![Compile·Deploy·Read/Write](../presentation/images/session2-1-3-compile-deploy.png)

---

## 중제목 2-2. Stage 0→3 점진적 빌드 — 기능별 컨트랙트 완성

**목표**: Incremental prompt로 NFT 컨트랙트를 완성한다

### 소제목

1. **Stage 0~1** — ERC-721 뼈대 + public mint(0.001 ETH·지갑당 3개). Remix 캡처로 Deploy·`mint` 버튼 확인 ([stage-0](../prompts/03-stage-build/stage-0.md) · [stage-1](../prompts/03-stage-build/stage-1.md) · [stage-1 README](../../contracts/stages/stage-1-mint/README.md))  
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

# 3차시 (대제목) — Sepolia 배포와 NFT DApp · 확인

**목표**: Sepolia 배포 · mint · 민팅 DApp · Etherscan 확인  
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

## 중제목 3-3. NFT 확인·마무리 — Etherscan 확인과 수업 정리

**목표**: Sepolia에서 mint·소유를 확인하고 워크플로우를 닫는다

> **OpenSea testnet 종료 (2025-07-24)** — `testnets.opensea.io` 사용 안 함. Etherscan·MetaMask NFT 탭으로 대체.

### 소제목

1. **Etherscan Sepolia 확인** — mint tx, `/nft/{address}/{tokenId}`, `ownerOf`  
   ![OpenSea 테스트넷 조회](../presentation/images/session3-3-1-opensea.png) *(슬라이드 이미지는 Etherscan 확인으로 설명 전환)*
2. **(선택) UI 보완** — [05-frontend-connect](../prompts/05-frontend-connect.md) 또는 solution 비교  
   ![(선택) UI 보완](../presentation/images/session3-3-2-ui-polish.png)
3. **(선택) OpenSea Studio — 메인넷 발행 소개** — [opensea.io/studio](https://opensea.io/studio) 화면 공유, 크리에이터 발행 흐름 · 오늘 Sepolia와의 차이 ([05-frontend-mint §9](../student/05-frontend-mint.md#9-수업-후--opensea-studio로-nft-발행-선택))
4. **마무리 Q&A·고지** — Intent→…→Ship 복습, Sepolia 교육용, 메인넷 전문 Audit 필수  
   ![마무리 Q&A·고지](../presentation/images/session3-3-3-wrap-qa.png)

**체크포인트**
- [ ] Etherscan에서 mint tx · 소유 확인
- [ ] (선택) OpenSea Studio 개념 이해 — **테스트넷 NFT는 Studio에 없음**

**강사 멘트 (OpenSea Studio · 3~5분)**

> “오늘은 **개발자 경로** — 컨트랙트 + DApp + Sepolia Ship — 를 완주했습니다.  
> 실제 [OpenSea Studio](https://opensea.io/studio)는 **메인넷**에서 컬렉션을 올릴 때 쓰는 **크리에이터 도구**입니다.  
> Sepolia VibeMint는 Studio에 안 뜹니다. 메인넷으로 갈 때는 **Audit → 배포 → metadata → (Studio 또는 자동 인덱싱)** 순서를 기억하세요.”

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
| 1-1 오리엔테이션 | 강사·GitHub / 바이브 코딩·워크플로우 / 목표·사전 준비 |
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
| 3-3 NFT 확인·마무리 | Etherscan 확인 / UI 보완(선택) / **OpenSea Studio(선택)** / Q&A·Audit 고지 |

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
| 3-3 NFT 확인·마무리 | [00-walkthrough](../student/00-walkthrough.md) |

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
