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

### OpenZeppelin import 컴파일 오류 / `ParserError: requires different compiler version`

**원인**: `pragma ^0.8.31` 또는 OZ와 Compiler 버전이 안 맞음.

**해결**: Compiler **0.8.31**

### `DeclarationError: Function "mcopy" not found`

**원인 (자주 겹침)**  
1. Compiler가 **0.8.31 미만**인데 EVM을 **osaka**로 고름 (`osaka`는 solc **0.8.29+**)  
2. EVM이 `shanghai` 등 → `mcopy` 없음  
3. import가 `@openzeppelin/contracts/...`(버전 없음) → Remix가 **최신 OZ**를 받음  

**해결**  
1. import를 `@openzeppelin/contracts@5.1.0/...`로 맞추고 저장  
2. Compiler **0.8.31** + EVM **osaka**  
3. 다시 Compile  

Deploy 탭 Environment: **Remix VM**

수업 기본 조합: **Compiler 0.8.31 + EVM osaka**


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
- **`gas limit too high` (Infura)**: 컨트랙트 revert가 아니라 **RPC 거절**인 경우가 많음 → MetaMask **Sepolia RPC**를 `https://ethereum-sepolia.publicnode.com` 등으로 변경 후 재시도. Remix `mint`가 되면 DApp·RPC 문제
- **Chain ID를 못 가져옴**: `https://rpc.sepolia.org` 가 **404**인 경우 있음 → `https://1rpc.io/sepolia` 또는 `https://sepolia.drpc.org`, Chain ID **11155111** 수동 입력
- `mintedCount(내주소)`가 **3**이면 지갑당 한도 초과

### NFT가 안 보일 때 (MetaMask · Etherscan)

- OpenSea **테스트넷**(`testnets.opensea.io`)은 **2025-07-24부터 지원 종료**
- Sepolia NFT 확인: [Etherscan Sepolia](https://sepolia.etherscan.io/) — `ownerOf`, `/nft/{address}/{tokenId}`
- MetaMask **NFTs** 탭 → Sepolia → Import NFT (선택)
- Sepolia NFT가 [OpenSea Studio](https://opensea.io/studio)에 없음 → **정상** (Studio는 메인넷 발행 도구)
- `setBaseURI` placeholder면 이미지 없을 수 있음 — **소유권(tx·ownerOf) 우선**

---

## 시간 관리

| 지연 원인 | 대응 |
| --- | --- |
| Stage 2까지 밀림 | Stage 3 whitelist 생략, solution diff 참고 |
| Faucet 지연 | 강사 일괄 전송 |
| 프론트 밀림 | starter 대신 solution 실행, 코드 walkthrough만 |
