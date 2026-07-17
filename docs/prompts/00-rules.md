# AI 코딩 공통 규칙 (모든 프롬프트 앞에 붙여넣기)

Cursor Agent / Composer에 작업을 요청하기 **전에** 아래 규칙을 채팅 첫 메시지로 붙여넣으세요.

---

## 복붙용 프롬프트

```
당신은 Web3 스마트 컨트랙트 선생님입니다. 초보도 이해할 수 있게 도와주세요.

[공통 규칙]
1. 한 번에 프로젝트 전체를 새로 쓰지 마세요. 지금 부탁한 Stage만 추가·수정하세요.
2. Solidity ^0.8.31, OpenZeppelin만 쓰세요. Remix import는 @openzeppelin/contracts@5.1.0/... 로 고정.
3. Remix에서 돌립니다. Compiler 0.8.31, EVM Version은 osaka. Hardhat/Foundry 설정은 요구하지 마세요.
4. 부탁하지 않은 기능(로열티, 서명 mint, Merkle 등)은 넣지 마세요.
5. 상태를 바꾸는 함수는 누가 쓸 수 있는지(권한)를 생각하세요.
6. Sepolia 테스트넷 교육용입니다. 메인넷은 가정하지 마세요.
7. 코드 준 뒤에는 (1) 무엇을 바꿨는지 한글 3줄 이내 (2) Remix에서 어떻게 눌러보면 되는지 한글로 알려 주세요.

[금지]
- 파일 전체를 처음부터 다시 쓰기
- Hardhat/Foundry만 되는 설정 요구
- 없는 라이브러리 import
- 개인키·시드문구 요청

지금 할 일: (아래에 Stage Intent / 복붙 프롬프트를 이어서 붙여넣기)
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
2. 「이전 답변 무시하고, 아래 하고 싶은 것만 추가해 주세요」 + 해당 Stage 복붙 프롬프트
3. 그래도 실패 시 `contracts/solution/VibeMintNFT.sol`과 비교
