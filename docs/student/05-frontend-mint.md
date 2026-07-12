# 05. 프론트엔드 — MetaMask 민팅 DApp

## 학습 목표

- `frontend/starter`에 배포 주소 연결
- Connect Wallet → Mint UI
- OpenSea Sepolia에서 NFT 확인 (인덱싱 지연 가능)

---

## 1. 환경 설정

```bash
cd frontend/starter
cp .env.example .env
```

`.env` 편집:

```
VITE_CONTRACT_ADDRESS=0xYourSepoliaAddress
```

---

## 2. 실행

```bash
npm install
npm run dev
```

Chrome + MetaMask Sepolia에서 `http://localhost:5173` 접속.

---

## 3. Cursor로 UI 보완 (선택)

[05-frontend-connect.md](../prompts/05-frontend-connect.md) 프롬프트로:

- supply 표시
- 에러 메시지 개선
- OpenSea 링크

정답 참고: `frontend/solution/`

---

## 4. Mint 테스트

1. **Connect Wallet**
2. 네트워크 Sepolia 아니면 Switch
3. **Mint** — 0.001 ETH + gas
4. Success 후 `totalMinted` 증가 확인

---

## 5. OpenSea Sepolia

인덱싱 **5~30분** 걸릴 수 있음.

```
https://testnets.opensea.io/
```

지갑 연결 → Profile → NFT 표시 확인.

Token 직링크 (tokenId 0 예):

```
https://testnets.opensea.io/assets/sepolia/{CONTRACT}/{TOKEN_ID}
```

---

## 체크리스트

- [ ] Connect / Disconnect 동작
- [ ] Mint 트랜잭션 success
- [ ] Etherscan에서 mint tx 확인

---

## 마무리

오늘 완성한 DApp은 **교육·테스트넷 전용**입니다.  
프로덕션(메인넷) 배포 전 **전문 스마트 컨트랙트 Audit**을 받으세요.

Intent → Spec → Generate → **Review** → Ship — **Review를 생략하지 마세요.**
