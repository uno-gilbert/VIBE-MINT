# 프롬프트: 프론트엔드 지갑 연동 + Mint UI

[00-rules.md](00-rules.md) 참고. 프론트엔드는 `frontend/starter` 기준.

---

## 복붙용 프롬프트

```
@frontend/starter

Sepolia 테스트넷 VibeMint NFT 민팅 DApp을 완성해 주세요.

[요구사항]
- Vite + React + wagmi v2 + viem (기존 stack 유지)
- MetaMask connect / disconnect
- chainId 11155111 (Sepolia) 아니면 switch network UI
- .env VITE_CONTRACT_ADDRESS 사용
- contracts/solution/VibeMintNFT.sol ABI 기반 mint() payable 호출
- mintPrice 표시 (0.001 ETH)
- totalSupply / maxSupply 읽기 (가능하면)
- 트랜잭션 pending / success / error 상태
- OpenSea Sepolia 링크 (collection URL 템플릿)

[금지]
- 전체 프로젝트 재 scaffold
- ethers v5 (viem/wagmi v2 유지)
- Private key 입력 UI

변경된 파일 목록과 npm run dev 테스트 방법을 알려주세요.
```

---

## 환경 변수

`frontend/starter/.env`:

```
VITE_CONTRACT_ADDRESS=0xYourSepoliaDeployAddress
```

---

## OpenSea Sepolia URL 템플릿

```
https://testnets.opensea.io/assets/sepolia/{CONTRACT_ADDRESS}/{TOKEN_ID}
```

Collection:

```
https://testnets.opensea.io/collection/vibemint-{CONTRACT_ADDRESS.slice(0,8)}
```

(실제 slug는 OpenSea 인덱싱 후 확인 — 인덱싱 지연 5~30분 가능)
