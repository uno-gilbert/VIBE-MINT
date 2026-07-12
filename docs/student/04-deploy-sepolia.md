# 04. Sepolia 테스트넷 배포

## 학습 목표

- Remix + MetaMask로 Sepolia 배포
- Etherscan에서 컨트랙트·트랜잭션 확인
- 테스트 mint 1회 성공

---

## 1. Sepolia ETH 받기

MetaMask 네트워크: **Sepolia** (Chain ID 11155111)

Faucet (택 1):

- [Alchemy Sepolia Faucet](https://www.alchemy.com/faucets/ethereum-sepolia)
- [Sepolia PoW Faucet](https://sepolia-faucet.pk910.de/)

잔액 **0.05 ETH** 이상 권장.

---

## 2. Remix 배포

1. [Remix](https://remix.ethereum.org) → Compile `VibeMintNFT.sol` (0.8.20)
2. **Deploy & Run** → Environment: **Injected Provider - MetaMask**
3. MetaMask Sepolia 확인 → Deploy
4. 배포된 **Contract Address** 복사 (프론트 `.env`에 사용)

---

## 3. 배포 후 설정 (owner)

Deployed Contracts 패널에서:

1. `setBaseURI` — 예: `https://example.com/metadata/` (교육용 placeholder)
2. (선택) `setWhitelist` — 본인 주소 추가

---

## 4. 테스트 mint

1. `mint` — Value **0.001** ether → transact
2. MetaMask confirm
3. `totalMinted` Read → 1
4. `ownerOf` 0 → 본인 주소

---

## 5. Etherscan 확인

```
https://sepolia.etherscan.io/address/YOUR_CONTRACT_ADDRESS
```

- Contract creation tx
- Internal tx / mint tx

**(선택) Verify**: Remix Plugin "Etherscan Verification" 또는 수동 verify.

---

## 체크리스트

- [ ] Sepolia에 컨트랙트 배포됨
- [ ] mint 1회 성공
- [ ] Contract address 저장 (.env 준비)

---

## 다음

→ [05-frontend-mint.md](05-frontend-mint.md)
