# VibeMint 워크숍 PPT · 차시별 그림

6시간 AI 바이브 코딩 NFT 실습용 발표 자료와 **차시·소제목 인포그래픽**입니다.

## 파일

| 파일 | 설명 |
| --- | --- |
| `VibeMint-Workshop-2026.pptx` | 생성된 발표 자료 |
| `generate_slides.py` | PPT 재생성 스크립트 |
| `images/` | 차시별 소제목 그림 (9장) |

---

## 차시별 소제목 그림 (`images/`)

### 1차시 — AI 바이브 코딩으로 이해하는 NFT · Spec 설계

| 소제목 | 파일 |
| --- | --- |
| 1-1 오리엔테이션 | ![1-1](images/session1-1-orientation.png) |
| 1-2 NFT·ERC 이해 | ![1-2](images/session1-2-nft-erc.png) |
| 1-3 Spec 설계 | ![1-3](images/session1-3-spec.png) |

### 2차시 — 점진적 빌드로 만드는 NFT 컨트랙트 · AI Audit

| 소제목 | 파일 |
| --- | --- |
| 2-1 Remix·AI 규칙 | ![2-1](images/session2-1-remix-rules.png) |
| 2-2 Stage 0→3 빌드 | ![2-2](images/session2-2-stage-build.png) |
| 2-3 AI 보안 Audit | ![2-3](images/session2-3-audit.png) |

### 3차시 — Sepolia 배포와 NFT DApp · OpenSea

| 소제목 | 파일 |
| --- | --- |
| 3-1 Sepolia 배포·mint | ![3-1](images/session3-1-sepolia-deploy.png) |
| 3-2 프론트 DApp | ![3-2](images/session3-2-frontend-dapp.png) |
| 3-3 OpenSea·마무리 | ![3-3](images/session3-3-opensea-wrap.png) |

---

## PPT에 넣는 방법

1. PowerPoint에서 해당 차시·소제목 슬라이드 열기
2. `docs/presentation/images/sessionX-Y-....png` 삽입
3. 강사 진행은 [../instructor/timing-script.md](../instructor/timing-script.md)와 맞춤

---

## 기존 PPT 슬라이드 구성

| 구간 | 섹션 |
| --- | --- |
| 오전 | 오리엔테이션 · NFT · Spec |
| 오후 | Stage 빌드 · Audit · Sepolia · DApp · OpenSea |

재생성:

```bash
python3 docs/presentation/generate_slides.py
```

## 강사 체크

- [ ] 「강사 소개」 슬라이드에 본인 정보 입력
- [ ] 차시별 소제목 그림 9장 PPT에 배치
- [ ] 실습 시 `docs/student/00-walkthrough.md` 병행
