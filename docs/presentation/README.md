# VibeMint 워크숍 PPT

6시간 AI 바이브 코딩 NFT 실습용 PowerPoint입니다.

## 파일

| 파일 | 설명 |
| --- | --- |
| `VibeMint-Workshop-2026.pptx` | 생성된 발표 자료 |
| `generate_slides.py` | PPT 재생성 스크립트 |

## 슬라이드 구성 (총 33장)

| 시간 | 섹션 | 슬라이드 수 |
| --- | --- | --- |
| 10:00~10:30 | 오리엔테이션 | 표지 + 섹션 + 6장 |
| 10:30~11:30 | NFT 스마트 컨트랙트 | 섹션 + 5장 |
| 11:30~12:30 | 유명 NFT 프로젝트 분석 | 섹션 + 5장 |
| 12:30~13:30 | 점심 | 섹션 + 1장 |
| 13:30~15:00 | AI 바이브 코딩 NFT 개발 | 섹션 + 4장 |
| 15:00~16:30 | Sepolia 배포 | 섹션 + 4장 |
| 16:30~18:00 | DApp · OpenSea | 섹션 + 4장 + 마무리 |

## 수정 방법

1. **PowerPoint에서 직접 편집** — `VibeMint-Workshop-2026.pptx` 열기
2. **스크립트 수정 후 재생성** — `generate_slides.py`의 `강사 소개` 슬라이드 등 텍스트 수정 후:

```bash
python3 docs/presentation/generate_slides.py
```

## 강사 체크

- [ ] 「강사 소개」 슬라이드에 본인 정보 입력
- [ ] Wi-Fi / Q&A 채널 안내 (口頭 또는 슬라이드 추가)
- [ ] 실습 시 `docs/student/00-walkthrough.md` 병행
