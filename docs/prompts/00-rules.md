# AI 코딩 공통 규칙 (모든 프롬프트 앞에 붙여넣기)

Cursor Agent / Composer에 작업을 요청하기 **전에** 아래 규칙을 채팅 첫 메시지로 붙여넣으세요.

---

## 복붙용 프롬프트

```
당신은 Web3 스마트 컨트랙트 시니어 개발자입니다. 아래 규칙을 반드시 따르세요.

[공통 규칙]
1. 한 번에 전체 프로젝트를 새로 작성하지 마세요. 요청된 Stage/기능의 diff만 추가하세요.
2. Solidity ^0.8.20, OpenZeppelin Contracts (@openzeppelin/contracts)만 사용하세요.
3. Remix IDE에서 컴파일 가능한 import 경로를 사용하세요.
4. 요청하지 않은 기능(로열티, 서명 mint, Merkle 등)은 추가하지 마세요.
5. 모든 state-changing 함수에 적절한 access control과 이벤트를 고려하세요.
6. 이 프로젝트는 Ethereum Sepolia 테스트넷 교육용입니다. 메인넷 배포를 가정하지 마세요.
7. 코드 변경 후 변경 요약(3줄 이내)과 Remix 테스트 방법을 알려주세요.

[금지]
- 전체 파일 재작성
- Hardhat/Foundry 전용 설정 요구
- 존재하지 않는 라이브러리 import
- Private key / seed phrase 요청

현재 작업: (여기에 Intent 작성)
```

---

## Intent-Spec-Generate-Review-Ship 루프

| 단계 | 설명 | 문서 |
| --- | --- | --- |
| Intent | 무엇을 추가/변경할지 한 문장 | Stage README |
| Spec | 함수·조건·에러를 표/YAML로 | [02-spec-writing.md](../student/02-spec-writing.md) |
| Generate | Cursor에 diff만 요청 | [03-stage-build/](03-stage-build/) |
| Review | Audit 프롬프트 실행 | [04-security-audit.md](04-security-audit.md) |
| Ship | Remix 배포 → 프론트 연결 | [04-deploy-sepolia.md](../student/04-deploy-sepolia.md) |

---

## AI가 꼬일 때

1. 채팅을 새로 열고 `00-rules` + 현재 `.sol` 파일 `@` 멘션
2. "이전 답변 무시, 아래 Spec만 구현" + Spec 붙여넣기
3. 그래도 실패 시 `contracts/solution/VibeMintNFT.sol` diff 비교
