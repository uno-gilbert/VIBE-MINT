# 문제 해결 FAQ (강사용)

---

## MetaMask

### "Wrong network" / 트랜잭션 실패

- MetaMask 네트워크가 **Sepolia**인지 확인 (Chain ID 11155111)
- Remix Deploy 탭에서 Environment가 **Injected Provider - MetaMask**인지 확인

### Faucet에서 ETH를 받지 못함

- Alchemy Faucet은 계정·일일 한도 제한 있음 → PoW Faucet 백업
- 강사 지갑에서 소량 전송 (0.01 Sepolia ETH) — 테스트넷만

### 시드 구문 노출 사고

- 즉시 해당 지갑 사용 중단, 새 지갑 생성 안내
- 수업에서는 **테스트넷 전용 지갑** 사용 권장

---

## Remix IDE

### OpenZeppelin import 컴파일 오류

Remix Compiler 0.8.20+, `viaIR` 비활성 기본값 사용.

import 경로 예:

```solidity
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
```

Remix에서 **GitHub** import 사용 시 `@openzeppelin/contracts` 버전이 맞는지 확인.

### "Stack too deep"

- 교육용 컨트랙트는 단순화. 발생 시 `solution/VibeMintNFT.sol` 참고
- Compiler optimization runs 200

### Deploy 후 컨트랙트 주소가 안 보임

- Deployed Contracts 패anel 확장
- 트랜잭션 Etherscan Sepolia에서 `Contract Creation` 확인

---

## Cursor / AI

### AI가 전체 파일을 매번 새로 작성함

- [00-rules.md](../prompts/00-rules.md)를 채팅 첫 메시지에 붙여넣기
- "기존 코드 유지, **Stage N 변경분만** diff로 적용" 명시
- `@파일명`으로 컨텍스트 고정

### AI가 존재하지 않는 라이브러리 import

- OpenZeppelin `@openzeppelin/contracts`만 허용
- Remix 호환 import 경로 재지시

### 코드가 "맞아 보이지만" 동작 안 함

- Spec과 구현 diff 비교
- Audit 프롬프트 재실행

---

## 프론트엔드

### `npm install` 실패

- Node.js v20+ 확인: `node -v`
- `rm -rf node_modules package-lock.json && npm install`

### Connect Wallet 후 mint 실패

- `.env`의 `VITE_CONTRACT_ADDRESS`가 Sepolia 배포 주소와 일치하는지
- MetaMask Sepolia + 충분한 ETH (0.001+ gas)
- `publicMintEnabled`가 true인지 (Remix Read Contract)

### OpenSea에 NFT 안 보임

- Sepolia testnet OpenSea: [testnets.opensea.io](https://testnets.opensea.io/)
- 인덱싱 5~30분 지연 가능 — Etherscan에서 tokenId 확인 후 안내

---

## 시간 관리

| 지연 원인 | 대응 |
| --- | --- |
| Stage 2까지 밀림 | Stage 3 whitelist 생략, solution diff 참고 |
| Faucet 지연 | 강사 일괄 전송 |
| 프론트 밀림 | starter 대신 solution 실행, 코드 walkthrough만 |
