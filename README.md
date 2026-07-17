# VibeMint — AI 바이브 코딩 NFT DApp 워크숍 키트

**메인 테마**: 쉽게 이해하고 빠르게 AI 바이브 코딩으로 만들어 보는 NFT

**6시간 만에 Sepolia 테스트넷 NFT DApp을 완성하는** 교육용 저장소입니다.  
2026년 실무 트렌드 **Intent → Spec → Generate → Review → Ship** 워크플로우를 Cursor + Remix + MetaMask로 학습합니다.

> 테스트넷 교육용입니다. 메인넷 배포 전 반드시 전문 스마트 컨트랙트 Audit을 받으세요.

**GitHub 저장소**: [https://github.com/uno-gilbert/VIBE-MINT](https://github.com/uno-gilbert/VIBE-MINT)

<div align="center">

[![VIBE-MINT GitHub QR 코드](docs/images/vibe-mint-github-qr.png)](https://github.com/uno-gilbert/VIBE-MINT)

*스마트폰으로 QR 스캔 → 저장소 바로 열기*

</div>

---

## 누구를 위한 자료인가

| 역할 | 시작점 |
| --- | --- |
| **수강생** | **[한 단계씩 따라하기](docs/student/00-walkthrough.md)** ← 실습은 여기서 시작 |
| **수강생 (사전)** | [docs/pre-course-checklist.md](docs/pre-course-checklist.md) |
| **강사** | [docs/curriculum.md](docs/curriculum.md) → [docs/instructor/timing-script.md](docs/instructor/timing-script.md) |
| **강사 (PPT)** | [docs/presentation/VibeMint-Workshop-2026.pptx](docs/presentation/VibeMint-Workshop-2026.pptx) |

---

## 6시간 로드맵 (AI 바이브 코딩)

| 시간 | 내용 | 문서 |
| --- | --- | --- |
| 10:00–10:30 | 오리엔테이션 | [curriculum.md](docs/curriculum.md) |
| 10:30–11:30 | NFT 스마트 컨트랙트의 이해 | [01-nft-concepts.md](docs/student/01-nft-concepts.md) |
| 11:30–12:30 | 유명 NFT 프로젝트 분석 | [02-spec-writing.md](docs/student/02-spec-writing.md) |
| 13:30–15:00 | NFT 개발 및 배포 과정 학습 | [03-incremental-build.md](docs/student/03-incremental-build.md) |
| 15:00–16:30 | NFT 컨트랙트 작성 및 멀티체인 배포 | [04-deploy-sepolia.md](docs/student/04-deploy-sepolia.md) |
| 16:30–18:00 | NFT DApp 개발 및 오픈씨 거래 | [05-frontend-mint.md](docs/student/05-frontend-mint.md) |

---

## 저장소 구조

```
vibe-mint/
├── docs/           # 커리큘럼, 수강생·강사 가이드, AI 프롬프트 팩
├── contracts/      # Stage 0–3 스타터 + solution
└── frontend/       # starter (최소 UI) + solution (완성 DApp)
```

---

## 빠른 시작 (수강생)

**실습 전체 흐름**: [docs/student/00-walkthrough.md](docs/student/00-walkthrough.md) — Part 0부터 순서대로 따라하기

### 사전 준비

1. Chrome, MetaMask (Sepolia), [Cursor](https://cursor.com/), Node.js 20+
2. [pre-course-checklist.md](docs/pre-course-checklist.md) 완료

### 컨트랙트

1. [Remix IDE](https://remix.ethereum.org)에서 `contracts/stages/stage-0-base/VibeMintNFT.sol`부터 시작
2. [docs/prompts/00-rules.md](docs/prompts/00-rules.md) + Stage 프롬프트로 점진적 빌드
3. [docs/prompts/04-security-audit.md](docs/prompts/04-security-audit.md) **배포 전 필수**

### 프론트엔드

```bash
cd frontend/starter
cp .env.example .env   # Sepolia 배포 주소 입력
npm install && npm run dev
```

---

## AI 프롬프트 팩

모든 Cursor 작업 전에 [docs/prompts/00-rules.md](docs/prompts/00-rules.md)를 붙여넣으세요.

- [역분석](docs/prompts/01-reverse-engineer.md)
- [Spec 생성](docs/prompts/02-spec-generator.md)
- [Stage 빌드](docs/prompts/03-stage-build/stage-0.md) · [Remix·확인 가이드](docs/prompts/03-stage-build/README.md)
- [보안 Audit](docs/prompts/04-security-audit.md) ← **필수**
- [프론트 연동](docs/prompts/05-frontend-connect.md)

---

## 실습 NFT 스펙 (VibeMint)

| 항목 | 값 |
| --- | --- |
| 표준 | ERC-721 |
| maxSupply | 100 |
| mintPrice | 0.001 ETH |
| per-wallet cap | 3 |
| 체인 | Ethereum Sepolia |

완성 컨트랙트: [contracts/solution/VibeMintNFT.sol](contracts/solution/VibeMintNFT.sol)

---

## 문제 해결

[docs/instructor/troubleshooting.md](docs/instructor/troubleshooting.md)

---

## 라이선스

교육용 자료 — MIT (컨트랙트 SPDX: MIT)
