# ■ 교육 커리큘럼 가이드 (2026년 · AI 바이브 코딩 · 강사 전달용)

주최측 기획 **메인 테마**: **쉽게 이해하고 빠르게 AI 바이브 코딩으로 만들어 보는 NFT**

**부제**: AI 바이브 코딩(Vibe Coding) 실무 워크플로우로 6시간 만에 NFT DApp 구축

아래 시간표는 운영 예시입니다. 수업 완성도를 위해 강사님의 노하우가 담긴 세부 내용으로 자유롭게 수정·보완하여 전달해 주시기 바랍니다.

**2026년 강의 특징 (권장)**: 현업 트렌드인 **AI 바이브 코딩** 워크플로우 `Intent → Spec → Generate → Review → Ship`을 적용합니다. AI에게 한 번에 전체 코드를 요청하는 방식 대신, **기능별 점진적 빌드**와 **배포 전 AI 보안 검증(Audit)**을 포함해 실무 수준의 완성도를 목표로 합니다.

---

## 시간표 (주최측 전달용 · 간략)

| 시간 | 교육 과목 | 세부 내용 |
| --- | --- | --- |
| **10:00 ~ 10:30** | **강사 소개 및 AI 바이브 코딩 오리엔테이션** | 강사 소개, 당일 로드맵, AI 바이브 코딩 개념, VibeMint DApp 목표, 사전 준비 점검 |
| **10:30 ~ 11:30** | **NFT 스마트 컨트랙트의 이해** | ERC-721 vs ERC-1155, OpenZeppelin 구조, Cursor AI 역분석 실습 |
| **11:30 ~ 12:30** | **유명 NFT 프로젝트 분석** | 대표 NFT 프로젝트 민팅 구조 분석, Spec 작성, 오후 실습 명세 확정 |
| **12:30 ~ 13:30** | **점심 식사** | — |
| **13:30 ~ 15:00** | **AI 바이브 코딩 NFT 개발 및 배포 과정 학습** | Remix + Cursor 점진적 컨트랙트 빌드, AI 보안 Audit |
| **15:00 ~ 16:30** | **NFT 컨트랙트 작성 및 멀티체인 배포** | Sepolia 테스트넷 배포·mint, Etherscan 확인, 멀티체인 개념 소개 |
| **16:30 ~ 18:00** | **AI 바이브 코딩 NFT DApp 개발 및 오픈씨 거래** | MetaMask 민팅 UI, OpenSea 테스트넷 거래 시뮬레이션, 마무리 |

---

## 시간표 및 세부 내용 (안 · 강사용 상세)

| 시간 | 교육 과목 | 세부 내용 (안) |
| --- | --- | --- |
| **10:00 ~ 10:30** | **강사 소개 및 AI 바이브 코딩 오리엔테이션** | · 강사 소개 및 당일 6시간 로드맵 안내<br><br>· **2026 Web3 개발 패러다임**: AI 바이브 코딩(Vibe Coding) 개념 — iExec Vibe Coding Challenge 등 사례 소개<br><br>· 오늘의 목표: Sepolia 테스트넷 NFT **VibeMint** DApp 완성<br><br>· [수강생 사전 준비](pre-course-checklist.md) 점검 (MetaMask, Cursor, Chrome) |
| **10:30 ~ 11:30** | **NFT 스마트 컨트랙트의 이해** | · NFT 핵심 개념: ERC-721 vs ERC-1155 구조 비교<br><br>· OpenZeppelin ERC-721 기본 구조 (mint, owner, tokenURI)<br><br>· **실습**: Cursor AI로 스마트 컨트랙트 **역분석(Reverse Engineering)** — 자연어로 온체인 로직 읽기<br><br>· 참고: [01-nft-concepts.md](student/01-nft-concepts.md) |
| **11:30 ~ 12:30** | **유명 NFT 프로젝트 분석** | · 국내외 대표 NFT 프로젝트(BAYC, Azuki 등) **컨트랙트·민팅 구조** 벤치마킹<br><br>· 민팅 조건, 화이트리스트, supply cap 등 **비즈니스 로직** 분석<br><br>· AI가 꼬이지 않게 요구사항을 **구체적 명세(Spec)**로 작성하는 방법 — 오후 실습용 VibeMint Spec 확정<br><br>· 참고: [02-spec-writing.md](student/02-spec-writing.md) |
| **12:30 ~ 13:30** | **점심 식사** | 개인 정비 및 휴식 |
| **13:30 ~ 15:00** | **AI 바이브 코딩 NFT 개발 및 배포 과정 학습** | · **실무 워크플로우**: Remix IDE + Cursor Agent로 Stage 0→3 **점진적 컨트랙트 빌드**<br><br>· AI 공통 규칙: "한 번에 전체 생성 금지", OpenZeppelin 표준 사용<br><br>· **[필수] AI 보안 Audit**: 배포 전 취약점·가스 낭비 코드 교차 검증 및 수정<br><br>· 참고: [03-incremental-build.md](student/03-incremental-build.md), [04-security-audit.md](prompts/04-security-audit.md) |
| **15:00 ~ 16:30** | **NFT 컨트랙트 작성 및 멀티체인 배포** | · Remix에서 컴파일·최적화 후 **Ethereum Sepolia** 테스트넷 배포 (MetaMask 연동)<br><br>· Faucet으로 테스트 ETH 수령 → 배포 → **테스트 mint** 성공까지<br><br>· Etherscan Sepolia에서 컨트랙트·트랜잭션 확인<br><br>· **멀티체인 개념 소개**: L2(Base, Arbitrum 등)와 Sepolia L1의 역할 비교 — *당일 hands-on은 Sepolia 중심*<br><br>· 참고: [04-deploy-sepolia.md](student/04-deploy-sepolia.md) |
| **16:30 ~ 18:00** | **AI 바이브 코딩 NFT DApp 개발 및 오픈씨 거래** | · Cursor + AI 웹 빌더로 **MetaMask 연동 민팅 사이트** 구축 (React/JavaScript, wagmi)<br><br>· 배포한 컨트랙트 주소를 프론트에 연결 → 브라우저에서 mint<br><br>· **OpenSea 테스트넷**에서 NFT 조회·거래 시뮬레이션<br><br>· 마무리: 테스트넷 교육용 한계, 메인넷 배포 전 **전문 Audit 필수** 안내<br><br>· 참고: [05-frontend-mint.md](student/05-frontend-mint.md) |

---

## 실습 NFT 스펙 (VibeMint · 교육용)

| 항목 | 값 |
| --- | --- |
| 표준 | ERC-721 |
| 이름 / 심볼 | VibeMint / VMINT |
| maxSupply | 100 |
| mintPrice | 0.001 ETH (Sepolia) |
| 지갑당 mint 한도 | 3 |
| ownerMint / pause / withdraw / whitelist | Stage 2~3에서 점진 추가 |
| 실습 체인 | **Ethereum Sepolia** (멀티체인은 개념·데모) |

---

## 2026년 트렌드 참고 (강사용 · 선택)

| 주제 | 비고 |
| --- | --- |
| iExec Vibe Coding Challenge | Cursor 등 AI 도구 활용 end-to-end 프로토타입 사례 |
| OpenLedger 생태계 | 바이브 코딩 플랫폼·학생 해커톤 후원 |
| AI 생성 코드 보안 | 업계에서 취약점 비율 **상당히 높다**는 공통 인식 — Audit 단계 강조 |
| Moonwell 사례 (2026) | AI 코드 + 검증 프로세스 부재 → "프로세스 문제"로 교육 |

---

## 강사용 보조 자료

- [강사 진행 스크립트](instructor/timing-script.md)
- [문제 해결 FAQ](instructor/troubleshooting.md)
- [AI 프롬프트 팩](prompts/00-rules.md)
- [수강생 사전 안내](pre-course-checklist.md)
