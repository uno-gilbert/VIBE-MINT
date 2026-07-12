# 강사 진행 스크립트 (6시간 · 2026 · AI 바이브 코딩)

주최측 시간표 기준 **목표 · 진행 · 체크포인트**입니다. 세부 분량은 현장 상황에 맞게 조절하세요.

---

## 3차시 구성 (한눈에 보기)

| 차시 | 시간 | 대제목 | 소제목 |
| --- | --- | --- | --- |
| **1차시** | 10:00 ~ 12:30 | **AI 바이브 코딩으로 이해하는 NFT · Spec 설계** | ① 오리엔테이션 · ② NFT 이해 · ③ Spec 설계 |
| **2차시** | 13:30 ~ 15:00 | **점진적 빌드로 만드는 NFT 컨트랙트 · AI Audit** | ① 점진적 빌드 · ② AI 보안 Audit |
| **3차시** | 15:00 ~ 18:00 | **Sepolia 배포와 NFT DApp · OpenSea** | ① Sepolia 배포 · ② DApp · OpenSea |

| 차시 | 워크플로우 | 핵심 이미지 |
| --- | --- | --- |
| 1차시 | Intent → Spec | [워크플로우](images/isgrs-workflow.png) |
| 2차시 | Generate → Review | [Stage 0→3](images/stage-build-flow.png) |
| 3차시 | Ship | [배포 흐름](images/deploy-dapp-flow.png) |

![6시간 워크숍 로드맵](images/workshop-timeline.png)

---

# 1차시 — AI 바이브 코딩으로 이해하는 NFT · Spec 설계

**시간**: 10:00 ~ 12:30 (점심 전)  
**목표**: 바이브 코딩 워크플로우 이해 + NFT 개념 + VibeMint Spec 확정  
**워크플로우**: **Intent → Spec**

![AI 바이브 코딩 워크플로우](images/isgrs-workflow.png)

### 1차시 소제목 목차

1. **오리엔테이션** — AI 바이브 코딩과 오늘의 목표 (10:00~10:30)
2. **NFT 이해** — 스마트 컨트랙트와 역분석 (10:30~11:30)
3. **Spec 설계** — 유명 프로젝트 분석과 명세 작성 (11:30~12:30)

---

## 1-1. 오리엔테이션 — AI 바이브 코딩과 오늘의 목표

**시간**: 10:00 ~ 10:30  
**목표**: 당일 로드맵·AI 바이브 코딩 워크플로우 이해

**진행**
1. 강사 소개, Wi-Fi, Q&A 채널 (5분)
2. 2026 Web3 + AI 바이브 코딩 (iExec 등 사례) (10분) — **위 워크플로우 그림 설명**
3. 오늘의 결과물: VibeMint NFT DApp on Sepolia (10분)
4. [pre-course-checklist.md](../pre-course-checklist.md) 점검 (5분)

**체크포인트**
- [ ] MetaMask + Sepolia 네트워크
- [ ] Cursor 로그인

---

## 1-2. NFT 이해 — 스마트 컨트랙트와 역분석

**시간**: 10:30 ~ 11:30  
**목표**: ERC-721/1155, AI 역분석

**진행**
1. ERC-721 vs ERC-1155 (15분) → [01-nft-concepts.md](../student/01-nft-concepts.md)
2. OpenZeppelin ERC721 개요 (15분)
3. Cursor 역분석 실습 (25분) → [01-reverse-engineer.md](../prompts/01-reverse-engineer.md)
4. Q&A (5분)

**체크포인트**
- [ ] mint / owner / pause 역할 설명 가능

---

## 1-3. Spec 설계 — 유명 프로젝트 분석과 명세 작성

**시간**: 11:30 ~ 12:30  
**목표**: 벤치마킹 + VibeMint Spec 확정

**진행**
1. BAYC, Azuki 등 민팅·화이트리스트 구조 (20분)
2. Spec 템플릿 (15분) → [02-spec-writing.md](../student/02-spec-writing.md) — **Spec 단계 강조**
3. [02-spec-generator.md](../prompts/02-spec-generator.md) 실습 (20분)
4. Spec 공유 (5분)

**체크포인트**
- [ ] maxSupply, mintPrice, per-wallet cap, whitelist in Spec

### 1차시 마무리 한 줄

> 「무엇을 만들지(Intent)·어떻게 만들지(Spec)」까지 확정. 오후는 코드를 **한 단계씩** 만든다.

---

## 12:30 ~ 13:30 | 점심

---

# 2차시 — 점진적 빌드로 만드는 NFT 컨트랙트 · AI Audit

**시간**: 13:30 ~ 15:00  
**목표**: Stage 0→3 점진적 빌드 + 배포 전 보안 Audit  
**워크플로우**: **Generate → Review**

![점진적 빌드 Stage 0→3](images/stage-build-flow.png)

### 2차시 소제목 목차

1. **점진적 빌드** — Stage 0→3로 NFT 컨트랙트 만들기 (13:30~14:40)
2. **AI 보안 Audit** — 배포 전 Review (14:40~15:00)

---

## 2-1. 점진적 빌드 — Stage 0→3로 NFT 컨트랙트 만들기

**시간**: 13:30 ~ 14:40 (약 70분)  
**목표**: Incremental prompt로 기능별 컨트랙트 완성

**진행**
1. [00-rules.md](../prompts/00-rules.md) (10분) — **Generate 규칙** (한 번에 전체 생성 금지)
2. Stage 0→3 실습 (60분)  
   → [03-incremental-build.md](../student/03-incremental-build.md)  
   → [03-stage-build/README.md](../prompts/03-stage-build/README.md)

| Stage | 소주제 |
| --- | --- |
| Stage 0 | ERC-721 뼈대 |
| Stage 1 | Public mint |
| Stage 2 | Pause · ownerMint · withdraw |
| Stage 3 | Whitelist |

**체크포인트**
- [ ] Remix Stage 3 compile OK

**시간 부족 시**: Stage 3 whitelist 생략 → `contracts/solution/` 참고

---

## 2-2. AI 보안 Audit — 배포 전 Review

**시간**: 14:40 ~ 15:00 (약 20분)  
**목표**: Critical/High 0건까지 수정

**진행**
1. [04-security-audit.md](../prompts/04-security-audit.md) 실행
2. Critical/High 수정 + Remix 재컴파일
3. 버퍼

**체크포인트**
- [ ] Audit Critical/High 0건

### 2차시 마무리 한 줄

> 컨트랙트 뼈대~whitelist까지 완성하고, **Audit(Review) 없이 배포하지 않는다.**

---

# 3차시 — Sepolia 배포와 NFT DApp · OpenSea

**시간**: 15:00 ~ 18:00  
**목표**: Sepolia 배포 · mint · 민팅 DApp · OpenSea 확인  
**워크플로우**: **Ship**

![Sepolia 배포 ~ DApp 완성 흐름](images/deploy-dapp-flow.png)

### 3차시 소제목 목차

1. **Sepolia 배포** — 테스트넷에 컨트랙트 올리고 mint (15:00~16:30)
2. **DApp · OpenSea** — 민팅 사이트와 마켓 연동 (16:30~18:00)

---

## 3-1. Sepolia 배포 — 테스트넷에 컨트랙트 올리고 mint

**시간**: 15:00 ~ 16:30  
**목표**: Injected Provider로 Sepolia 배포 + mint + 멀티체인 개념

**진행**
1. Faucet (15분)
2. Remix Deploy Sepolia (25min) → [04-deploy-sepolia.md](../student/04-deploy-sepolia.md)  
   Environment: **Injected Provider - MetaMask** (Remix VM 아님)
3. 테스트 mint + Etherscan (20min)
4. **멀티체인 개념** (15min): L1 Sepolia vs L2 — 당일 hands-on은 Sepolia
5. 버퍼 (15min)

**체크포인트**
- [ ] Etherscan Sepolia contract
- [ ] 1회 mint 성공
- [ ] Contract Address 저장 (프론트용)

---

## 3-2. DApp · OpenSea — 민팅 사이트와 마켓 연동

**시간**: 16:30 ~ 18:00  
**목표**: MetaMask 민팅 UI + OpenSea testnet

**진행**
1. `frontend/starter` + `.env` (15min)
2. Mint UI 실습 (45min) → [05-frontend-mint.md](../student/05-frontend-mint.md)
3. OpenSea testnet (15min)
4. 마무리 Q&A (15min)

**체크포인트**
- [ ] Connect Wallet → Mint
- [ ] OpenSea testnet (인덱싱 지연 안내)

### 3차시 마무리 한 줄

> 테스트넷에 **Ship** 완료. Intent → Spec → Generate → Review → Ship 전 구간을 하루 만에 경험.

---

## 마무리 멘트 (필수)

> 오늘 코드는 **Sepolia 테스트넷 교육용**입니다. 메인넷 배포 전 **전문 Audit** 필수. AI는 주니어처럼 쓰되 **Review(Audit)는 생략하지 마세요.**

---

## 차시 · 소제목 ↔ 학습 자료

| 차시 | 소제목 | 수강생 문서 |
| --- | --- | --- |
| 1차시 | 1-1 오리엔테이션 | [pre-course-checklist](../pre-course-checklist.md) |
| 1차시 | 1-2 NFT 이해 | [01-nft-concepts](../student/01-nft-concepts.md) |
| 1차시 | 1-3 Spec 설계 | [02-spec-writing](../student/02-spec-writing.md) |
| 2차시 | 2-1 점진적 빌드 | [03-incremental-build](../student/03-incremental-build.md) |
| 2차시 | 2-2 AI 보안 Audit | [04-security-audit](../prompts/04-security-audit.md) |
| 3차시 | 3-1 Sepolia 배포 | [04-deploy-sepolia](../student/04-deploy-sepolia.md) |
| 3차시 | 3-2 DApp · OpenSea | [05-frontend-mint](../student/05-frontend-mint.md) |

전체 따라하기: [00-walkthrough.md](../student/00-walkthrough.md)

---

## 이미지 파일 위치

| 파일 | 용도 |
| --- | --- |
| [images/workshop-timeline.png](images/workshop-timeline.png) | 수업 시작·전체 소개 |
| [images/isgrs-workflow.png](images/isgrs-workflow.png) | 1차시 워크플로우 |
| [images/stage-build-flow.png](images/stage-build-flow.png) | 2차시 Stage 실습 |
| [images/deploy-dapp-flow.png](images/deploy-dapp-flow.png) | 3차시 배포·DApp |

PPT에 넣을 때: `docs/instructor/images/` 폴더에서 그대로 삽입 가능
