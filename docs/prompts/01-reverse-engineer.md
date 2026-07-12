# 프롬프트: 스마트 컨트랙트 역분석 (Reverse Engineering)

[00-rules.md](00-rules.md) 공통 규칙을 먼저 붙여넣은 뒤, 아래 프롬프트를 사용하세요.

---

## 복붙용 프롬프트

```
@VibeMintNFT.sol (또는 분석할 .sol 파일)

이 Solidity 컨트랙트를 역분석해 주세요. 코드를 수정하지 마세요.

다음 형식으로 한국어로 설명하세요:

1. **한 줄 요약**: 이 컨트랙트가 하는 일
2. **상속 구조**: ERC721, Ownable, Pausable 등
3. **상태 변수 표**: 이름 | 타입 | 역할
4. **공개 함수 표**: 함수명 | 접근 | payable | 하는 일
5. **민팅 흐름**: publicMint / ownerMint / whitelistMint 순서도 (텍스트)
6. **보안 포인트**: access control, reentrancy, supply cap 관련 3가지
7. **가스·최적화**: 눈에 띄는 비효율 1~2가지 (있다면)

초보 개발자가 Spec을 작성할 수 있을 정도로 구체적으로 작성하세요.
```

---

## 실습 팁

- `contracts/solution/VibeMintNFT.sol`을 Cursor 프로젝트에 열고 `@` 멘션
- 역분석 결과를 [02-spec-writing.md](../student/02-spec-writing.md) Spec과 비교해 누락 항목 찾기
