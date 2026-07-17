# Stage 3: Whitelist Mint — 따라하기

Stage 2까지 만든 컨트랙트에 **VIP 창구(`whitelistMint`)** 를 추가합니다.

> **한 줄**: 명단에 있는 주소만 mint. public 창구를 꺼도 VIP는 가능. pause면 둘 다 중지.

이전: [Stage 2](../stage-2-access/README.md) · 목록: [../README.md](../README.md)

⏱ 시간 부족 → [solution](../../solution/VibeMintNFT.sol) 써도 OK. **Audit은 필수.**

---

## 이 Stage 목표

- [ ] whitelist + setWhitelist + whitelistMint 추가
- [ ] 내 주소 등록 후 public OFF여도 whitelistMint 성공
- [ ] 미등록(#1) whitelistMint는 revert
- [ ] pause면 whitelistMint도 revert

---

## 따라하기 (순서대로)

### Step 3-1. Intent

> “whitelist mapping + whitelistMint 추가. publicMintEnabled와 무관.”

### Step 3-2. Cursor로 diff 받기

1. `@VibeMintNFT.sol` + [00-rules](../../../docs/prompts/00-rules.md)  
2. [stage-3.md](../../../docs/prompts/03-stage-build/stage-3.md) 복붙용 프롬프트  
3. Stage 2 기능(pause/withdraw) **삭제되지 않았는지** 확인  

막히면: [VibeMintNFT.sol](./VibeMintNFT.sol)

- [ ] Stage 3 diff 반영

### Step 3-3. Remix 재Compile · 재Deploy

1. 코드 저장 → Compiler **0.8.31** · EVM **osaka** Compile  
2. Remix VM → **Deploy**

- [ ] `setWhitelist`, `whitelistMint` 버튼 보임

### Step 3-4. 명단 등록

1. Account **#0** (owner)  
2. `setWhitelist` 펼치기  

**`accounts` 칸 — 아래를 통째로 복사해서 붙여넣기** (한 글자도 빼지 마세요)

```text
["0x4B20993Bc481177ec7E8f571ceCaE8A9e22C02db"]
```

| 넣으면 안 됨 ❌ | 결과 |
| --- | --- |
| `0x4B20...` | 주소만 → `expected array value` |
| `"0x4B20..."` | 따옴표만 → **같은 에러** (배열 아님) |
| `[0x4B20...]` | 대괄호만, 따옴표 없음 → 종종 실패 |

| 넣어야 함 ✅ | 구성 |
| --- | --- |
| `["0x4B20..."]` | `[` + `"` + 주소 + `"` + `]` |

체크: `accounts` 칸 **맨 앞이 `[`**, **맨 뒤가 `]`** 인지 확인.

3. `allowed` 칸 = `true` (**여기는 주소 넣지 말 것**)  
4. **transact**  
5. 파란 `whitelist`에는 주소만 (`0x4B20...`, 대괄호 없이) → `true`

- [ ] whitelist 등록 확인

> Remix가 입력을 지우면: accounts 칸을 비우고 위 한 줄을 **다시 붙여넣기**한 뒤 바로 transact.
### Step 3-5. public 끄고 VIP mint

1. `setPublicMintEnabled(false)` → transact  
2. Value `0.001` ether → `mint` → **revert** (일반 창구 닫힘)  
3. 같은 Value → `whitelistMint` → **성공**

- [ ] public off + whitelistMint OK

### Step 3-6. 미등록 차단

1. Account를 **#1**로 변경  
2. Value 0.001 → `whitelistMint` → **revert**

- [ ] 비화이트리스트 revert

### Step 3-7. pause 공통

1. Account #0 → `pause`  
2. `whitelistMint` → **revert**  
3. (선택) `unpause`로 복구

- [ ] pause 시 VIP도 중지

### Step 3-8. Stage 2 기능 유지 확인 (짧게)

- [ ] `withdraw` 또는 `ownerMint` 아직 동작?

### Step 3-9. Stage 3 완료 체크

- [ ] 미등록 whitelistMint revert?  
- [ ] setWhitelist batch 길이 제한 있는가?  
- [ ] 가격·지갑 cap이 public과 동일한가?

---

## Stage 0→3 끝났으면 (필수)

기능 확인과 **보안 Audit**은 다릅니다. 배포 전에:

1. [04-security-audit.md](../../../docs/prompts/04-security-audit.md) 실행  
2. Critical / High **0건**까지 수정  
3. Remix 재Compile · 짧은 mint 재테스트  
4. → [04-deploy-sepolia.md](../../../docs/student/04-deploy-sepolia.md)

정답 전체: [solution/VibeMintNFT.sol](../../solution/VibeMintNFT.sol)

---

## 막히면

| 증상 | 해결 |
| --- | --- |
| `expected array value` | accounts에 **주소만** 넣음 → `["0x..."]` 로 |
| public 끄고 mint만 누름 | VIP는 **`whitelistMint`** |
| #1이 성공함 | 그 주소를 명단에 넣지 않았는지 확인 |

---

## 읽어 두면 좋은 설명

```text
[일반 문] mint              ← publicMintEnabled로 개폐
[VIP 문]  whitelistMint     ← 명단 필수, public과 무관
[비상등]  pause             ← 두 문 모두 잠금
[한도]    mintedCount       ← 두 문 합산 지갑당 3개
```

| 용어 | 의미 |
| --- | --- |
| whitelist | 초대 명단 (`주소 → true/false`) |
| setWhitelist | owner가 명단 일괄 수정 |
| event | 명단 변경 로그 |

프롬프트: [stage-3.md](../../../docs/prompts/03-stage-build/stage-3.md)
