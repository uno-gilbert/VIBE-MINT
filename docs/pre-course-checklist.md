# ■ 수강생 사전 안내사항 (2026년 · AI 바이브 코딩 NFT 실습)

**교육 테마**: 쉽게 이해하고 빠르게 AI 바이브 코딩으로 만들어 보는 NFT

원활한 **AI 바이브 코딩** 기반 NFT·Web3 실습을 위해, 교육 참석 **전** 아래 사항을 반드시 확인하고 준비해 주세요.

---

## 필수 준비물

- **개인 노트북 지참 필수** (충전 어댑터 포함)

---

## 실습 및 사용 환경 (2026년)

| 구분 | 내용 |
| --- | --- |
| **실습 환경** | [Cursor](https://cursor.com/) AI 코드 에디터 (2025년 VS Code → **2026년 Cursor**로 전환) |
| **사용 언어** | **JavaScript**, **Solidity** |
| **기본 브라우저** | Google Chrome (MetaMask·Remix 연동 표준) |
| **스마트 컨트랙트 IDE** | [Remix IDE](https://remix.ethereum.org/) (웹 브라우저, 별도 설치 불필요) |
| **프론트엔드 실습** | Node.js LTS **v20 이상** |
| **블록체인 네트워크** | Ethereum **Sepolia 테스트넷** (실제 ETH 사용 없음) |

---

## 사전 설치 및 가입 (★필수)

### 1. MetaMask (디지털 지갑)

1. Chrome 웹 스토어에서 **MetaMask** 확장 프로그램을 설치합니다.
2. 지갑을 생성하고 계정·비밀번호를 설정합니다.
3. **시드 구문(Seed Phrase)은 절대 타인·AI 채팅·SNS에 노출하지 마세요.** 개인 메모장 등 안전한 곳에만 보관하세요.
4. MetaMask에 **Sepolia 테스트넷**을 추가합니다.
   - 네트워크 이름: `Sepolia`
   - RPC URL: `https://rpc.sepolia.org`
   - Chain ID: `11155111`
   - 통화 기호: `ETH`

### 2. Cursor AI 편집기

1. [cursor.com](https://cursor.com/)에서 Cursor를 다운로드해 노트북에 설치합니다.
2. 회원가입 후 **로그인 상태**로 수업에 참석해 주세요. (무료 계정으로 실습 가능)

### 3. Node.js (프론트 DApp 실습)

1. [nodejs.org](https://nodejs.org/)에서 **LTS v20+** 설치
2. 터미널에서 확인: `node -v` (예: v20.x, v22.x)

### 4. 테스트 가스비 (Faucet)

블록체인 배포 실습에 필요한 **무료 Sepolia ETH**는 당일 현장에서 안내해 드립니다. 사전에 받아 두고 싶다면 아래 Faucet을 이용할 수 있습니다.

- [Alchemy Sepolia Faucet](https://www.alchemy.com/faucets/ethereum-sepolia)
- [Sepolia PoW Faucet](https://sepolia-faucet.pk910.de/)

> Faucet은 일일 한도가 있을 수 있습니다. 수업 **30분 전** 미리 받아 두시면 원활합니다.

---

## 보안·주의사항

- 본 교육은 **Sepolia 테스트넷**만 사용합니다. **메인넷에 실제 ETH를 보내지 마세요.**
- AI(Cursor)가 생성한 스마트 컨트랙트는 **교육·테스트 목적**으로만 사용하세요.
- 메인넷(실서비스) 배포 전 반드시 **전문 스마트 컨트랙트 Audit**이 필요합니다.

---

## (선택) 교육 자료 미리보기

교육 저장소가 제공되면 아래 경로를 참고하세요.

- `docs/student/` — 단계별 실습 가이드
- `docs/prompts/` — Cursor AI 프롬프트 팩

---

## 2025년 → 2026년 변경 요약

| 2025년 (참고) | 2026년 (본 교육) |
| --- | --- |
| Visual Studio Code | **Cursor AI** (Agent/Composer 모드 활용) |
| JavaScript, Solidity | 동일 + **AI 바이브 코딩** 워크플로우 |
| — | **MetaMask**, **Remix IDE**, **Sepolia 테스트넷** 필수 |
| — | **Node.js v20+** (NFT DApp 프론트 실습) |
