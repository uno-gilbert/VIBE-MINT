# 06. Pinata(IPFS)로 NFT 메타데이터 관리하기

수업 기본은 [04-deploy-sepolia.md](04-deploy-sepolia.md)의 **GitHub Raw**입니다.  
이 문서는 **지정 서비스 [Pinata Cloud](https://pinata.cloud/)** 만 써서, 같은 VibeMint 에셋을 IPFS에 올리고 Remix `setBaseURI`까지 **클릭 순서대로** 따라 합니다.

> **지정 서비스**: [Pinata](https://app.pinata.cloud/) (웹 앱)  
> **CLI / API 키 / 다른 서비스(nft.storage 등)는 이 실습에서 쓰지 않습니다.**

```text
1) Pinata 가입
2) images 폴더 업로드 → IMAGES_CID
3) Dedicated Gateway로 이미지 확인
4) metadata image URL 수정 (스크립트)
5) metadata 폴더 업로드 → METADATA_CID
6) Remix setBaseURI(게이트웨이 + METADATA_CID + /)
7) 브라우저·Etherscan 확인
```

---

## 실습 참고 값 (이 워크숍에서 확정)

아래는 **images 폴더 pin + Dedicated Gateway**까지 완료한 실제 값입니다.  
따라하기·복습 시 그대로 쓰거나, 본인 Pinata 계정으로 다시 올려 같은 순서를 연습하세요.

| 항목 | 값 |
| --- | --- |
| **DEDICATED_GATEWAY** | `https://magenta-key-quokka-912.mypinata.cloud` |
| **IMAGES_CID** | `bafybeibzqlnvhkviwqytx2lx7pxk65yzjap3uunoeth2wknylzg6z4pm7e` |
| **METADATA_CID** | *(Step 6에서 metadata 폴더 업로드 후 기입)* |
| **이미지 확인 URL** | [0.jpg 열기](https://magenta-key-quokka-912.mypinata.cloud/ipfs/bafybeibzqlnvhkviwqytx2lx7pxk65yzjap3uunoeth2wknylzg6z4pm7e/0.jpg) |

메모장 템플릿 (현재까지 채운 상태):

```text
DEDICATED_GATEWAY = https://magenta-key-quokka-912.mypinata.cloud
IMAGES_CID        = bafybeibzqlnvhkviwqytx2lx7pxk65yzjap3uunoeth2wknylzg6z4pm7e
METADATA_CID      = (Step 6 업로드 후)
BASE_URI          = https://magenta-key-quokka-912.mypinata.cloud/ipfs/{METADATA_CID}/
```

> **지금 할 일**: Step 5는 이미 적용됨(`assets/nft/metadata`의 `image`가 위 gateway·CID를 가리킴).  
> → **[Step 6](#step-6--pinata에-metadata-폴더-업로드)** 부터 이어서 metadata 폴더를 Pinata에 올리고, 나온 CID로 Remix `setBaseURI`를 호출하세요.

---

## 학습 목표

- [ ] Pinata에 가입하고 **Files**에서 폴더를 올린다
- [ ] 본인 **Dedicated Gateway** 주소를 복사한다
- [ ] Images CID · Metadata CID를 메모한다
- [ ] Remix `setBaseURI`를 Pinata gateway URL로 설정한다

**전제**: 로컬에 `assets/nft/images/0.jpg`…`52.jpg`, `assets/nft/metadata/0`…`52`  
**시간**: 약 25~40분  
**네트워크**: Sepolia 컨트랙트가 이미 있으면 Step 7 Remix만 하면 됨. 없으면 → [04-deploy-sepolia.md](04-deploy-sepolia.md)

---

## 왜 Pinata인가? (한 줄)

| | GitHub Raw (수업 기본) | **Pinata = IPFS 핀 서비스** |
| --- | --- | --- |
| 하는 일 | GitHub에 올린 파일 링크 | 파일을 IPFS에 올리고 **계속 보관(pin)** |
| 주소 | `raw.githubusercontent.com/…` | `https://{내게이트웨이}.mypinata.cloud/ipfs/{CID}/` |
| 수업에서 | 빠름 | **이 문서의 지정 실습** |

**CID** = 파일(폴더) 내용의 지문. 내용이 바뀌면 CID도 바뀝니다.

---

## 준비물 체크

| # | 준비 | 확인 |
| --- | --- | --- |
| 1 | Chrome | |
| 2 | 이메일 (Pinata 가입) | |
| 3 | 이 저장소 로컬 클론 + `assets/nft/` | |
| 4 | Node.js (스크립트용, `node -v`) | |
| 5 | (Step 7) Sepolia 배포 컨트랙트 + owner MetaMask | |

---

## Step 1 — Pinata 가입 · 로그인

1. Chrome에서 **https://app.pinata.cloud/** 접속  
2. **Sign up** (처음) 또는 **Log in**  
   - Google / GitHub / email 중 편한 방식  
3. 로그인 후 대시보드가 보이면 OK  

> 요금제 안내가 떠도 **Free** 로 실습하면 됩니다. (폴더 2개 + JPEG 수십 장이면 보통 충분)

- [ ] https://app.pinata.cloud/ 로그인됨

---

## Step 2 — Dedicated Gateway 주소 복사 (필수)

Pinata 계정마다 **전용 게이트웨이**가 있습니다. NFT URL은 이 주소를 씁니다.

1. 왼쪽 메뉴에서 **Gateways** 클릭  
   (없으면 상단/설정에서 **Gateway** 검색)
2. 목록에 나오는 게이트웨이 이름 확인  
3. 주소 형태: `https://{게이트웨이이름}.mypinata.cloud`

**이 워크숍 참고 값:**

```text
https://magenta-key-quokka-912.mypinata.cloud
```

4. 메모장 **DEDICATED_GATEWAY**에 붙여넣기  
   - 끝에 `/` **넣지 마세요** (나중에 `/ipfs/...`를 붙입니다)

> **공개 공용** `https://gateway.pinata.cloud` 은 쓰지 마세요.  
> 본인 계정이면 Gateways에 나온 **본인** 주소를 씁니다. (위 값은 실습 참고용)

- [ ] DEDICATED_GATEWAY 저장

---

## Step 3 — 로컬 폴더 확인

Finder / Explorer에서 프로젝트의 `assets/nft`를 엽니다.

```text
assets/nft/
  images/
    0.jpg
    1.jpg
    …
    52.jpg
  metadata/
    0          ← 확장자 없음 (0.json 아님!)
    1
    …
    52
```

| 확인 | OK 기준 |
| --- | --- |
| 이미지 | `0.jpg` ~ `52.jpg` |
| metadata | 파일명 `0` … `52` (**`.json` 없음**) |

- [ ] 폴더 구조 OK

---

## Step 4 — Pinata에 **images** 폴더 업로드

### 4-1. Files 화면

1. 왼쪽 메뉴 **Files** 클릭  
2. 오른쪽 위 **+ Add** (또는 **Add Files**) 클릭  
3. **Folder** 선택  
   - File / Folder / CID 중 **Folder**

### 4-2. 폴더 선택

1. 로컬에서 **`assets/nft/images`** 폴더를 고릅니다  
   - `nft` 전체가 아니라 **`images`만**  
2. Name(이름)이 비어 있으면 `vibemint-images` 정도로 입력 (선택)  
3. **Upload** / **Pin** 진행 → 완료될 때까지 대기

### 4-3. CID 복사

1. Files 목록에서 방금 올린 항목의 **CID** 복사  
2. 메모장 **IMAGES_CID**에 붙여넣기  

**이 워크숍에서 확정된 IMAGES_CID** (동일 `images` 폴더를 pin하면 같은 CID가 나옵니다):

```text
bafybeibzqlnvhkviwqytx2lx7pxk65yzjap3uunoeth2wknylzg6z4pm7e
```

### 4-4. 브라우저로 이미지 확인

```text
https://magenta-key-quokka-912.mypinata.cloud/ipfs/bafybeibzqlnvhkviwqytx2lx7pxk65yzjap3uunoeth2wknylzg6z4pm7e/0.jpg
```

**Hero 카드 JPEG가 보이면** Step 4 성공입니다.

| 안 보일 때 | 할 일 |
| --- | --- |
| 404 | CID·게이트웨이 오타, 또는 폴더를 한 겹 잘못 올림 |
| 빈 화면 | 1~2분 후 새로고침 |
| `images/0.jpg` 경로가 필요해 보임 | 상위 `nft`를 올린 것 → **삭제 후 `images`만** 다시 업로드 |

올바른 구조: `{CID}/0.jpg` (바로 아래 jpg)  
잘못된 구조: `{CID}/images/0.jpg` (한 겹 더)

- [ ] IMAGES_CID 저장
- [ ] `/0.jpg` 이미지 표시 OK

---

## Step 5 — metadata의 `image` URL을 Pinata로 바꾸기

목표 `image` 예 (`metadata/0`):

```json
"image": "https://magenta-key-quokka-912.mypinata.cloud/ipfs/bafybeibzqlnvhkviwqytx2lx7pxk65yzjap3uunoeth2wknylzg6z4pm7e/0.jpg"
```

> 저장소의 `assets/nft/metadata/0`…`52`는 **이미 위 형식으로 갱신된 상태**일 수 있습니다.  
> 다시 돌리려면 아래 명령을 실행하세요.

### 5-1. 스크립트 실행 (0~52 일괄)

프로젝트에서:

```bash
cd assets/nft

IMAGES_CID="bafybeibzqlnvhkviwqytx2lx7pxk65yzjap3uunoeth2wknylzg6z4pm7e" \
GATEWAY="https://magenta-key-quokka-912.mypinata.cloud/ipfs" \
node scripts/rewrite-image-urls.mjs
```

| 환경변수 | 이 워크숍 값 |
| --- | --- |
| `IMAGES_CID` | `bafybeibzqlnvhkviwqytx2lx7pxk65yzjap3uunoeth2wknylzg6z4pm7e` |
| `GATEWAY` | `https://magenta-key-quokka-912.mypinata.cloud/ipfs` |

성공 메시지 예:

```text
Updated 53/53 metadata files.
image pattern: https://magenta-key-quokka-912.mypinata.cloud/ipfs/bafybeibzqlnvhkviwqytx2lx7pxk65yzjap3uunoeth2wknylzg6z4pm7e/{id}.jpg
```

확인:

```bash
head -n 5 metadata/0
```

`image`에 `magenta-key-quokka-912.mypinata.cloud` 와 위 CID가 보이면 OK.

### 5-2. (대안) tokenId 0만 손으로

시간 부족 시 `metadata/0`만 수정해도 `tokenURI(0)` 테스트는 가능합니다.  
전체 컬렉션이면 **5-1 스크립트**를 쓰세요.

- [ ] metadata `image`가 Dedicated Gateway + IMAGES_CID

---

## Step 6 — Pinata에 **metadata** 폴더 업로드 ← **지금 할 단계**

1. Pinata **Files** → **+ Add** → **Folder**  
2. 로컬 폴더 선택 (절대 경로 예):

```text
/Users/gilbert-mac/projects/dev/vibe-mint/assets/nft/metadata
```

   또는 저장소 기준 `assets/nft/metadata`  
   - Step 5에서 **이미 수정한** 폴더  
3. 이름 예: `vibemint-metadata` → Upload  
4. 완료 후 **CID** 복사 → 메모장 **METADATA_CID**

### 브라우저로 JSON 확인

```text
https://magenta-key-quokka-912.mypinata.cloud/ipfs/{METADATA_CID}/0
```

| 확인 | 기대 |
| --- | --- |
| 페이지 | JSON (`name`, `image`, `attributes`) |
| `image` URL | Step 4 이미지 URL과 동일 패턴 |
| 파일명 | URL 끝이 `/0` (`.json` 아님) |

업로드 후 나온 **METADATA_CID**를 메모하고, 아래 Step 7 BASE_URI에 넣습니다.

- [ ] METADATA_CID 저장
- [ ] `/0` JSON + image 링크 OK

---

## Step 7 — Remix `setBaseURI` (Pinata URL)

### 7-1. BASE_URI 만들기

끝 **`/`** 필수:

```text
https://magenta-key-quokka-912.mypinata.cloud/ipfs/{METADATA_CID}/
```

예 (METADATA_CID를 `bafy…META` 라고 가정):

```text
https://magenta-key-quokka-912.mypinata.cloud/ipfs/bafy…META/
```

| 끝 | + tokenId `1` | 결과 |
| --- | --- | --- |
| `…/CID/` ✅ | `1` | `…/CID/1` |
| `…/CID` ❌ | `1` | `…/CID1` → 깨짐 |

### 7-2. Remix에서 실행

1. [remix.ethereum.org](https://remix.ethereum.org)  
2. Environment: **WalletConnect / Injected Provider** → MetaMask **Sepolia**  
3. 배포해 둔 `VibeMintNFT` (Deployed Contracts)  
4. Account = **배포한 owner**  
5. 주황색 **`setBaseURI`**  
6. 입력칸에 위 BASE_URI **전체** 붙여넣기 (따옴표 없이)  
7. **transact** → MetaMask **Confirm**

### 7-3. 확인

**A. 브라우저 (mint 전에도 가능)**

```text
https://magenta-key-quokka-912.mypinata.cloud/ipfs/{METADATA_CID}/0
```

**B. Remix Read `tokenURI`**

| 조건 | 동작 |
| --- | --- |
| 이미 tokenId `0`을 mint함 | `tokenURI`에 `0` → BASE_URI + `0` |
| 아직 mint 안 함 | `tokenURI`가 **revert**할 수 있음 → **A**로 확인 후 mint |

- [ ] `setBaseURI` 트랜잭션 성공
- [ ] `{BASE_URI}0` JSON 확인

---

## Step 8 — Etherscan에서 NFT 보기 (선택)

mint한 뒤:

```text
https://sepolia.etherscan.io/nft/{CONTRACT_ADDRESS}/0
```

1. Metadata / Image가 `magenta-key-quokka-912.mypinata.cloud` 를 가리키는지 확인  
2. 안 보이면 **Refresh Metadata**(로그인) 또는 수 분 대기  
3. Pinata **Files**에서 해당 항목이 목록에 남아 있는지(pin) 확인

- [ ] (선택) Etherscan에 이미지 표시

---

## 완료 체크리스트

- [ ] 서비스 = **Pinata** (app.pinata.cloud)만 사용  
- [ ] Dedicated Gateway = `magenta-key-quokka-912.mypinata.cloud` (또는 본인 gateway)  
- [ ] IMAGES_CID = `bafybeibzqlnvhkviwqytx2lx7pxk65yzjap3uunoeth2wknylzg6z4pm7e`  
- [ ] 스크립트로 metadata `image` 갱신  
- [ ] metadata 폴더 → METADATA_CID → `/0` JSON 확인  
- [ ] `setBaseURI` = `https://magenta-key-quokka-912.mypinata.cloud/ipfs/{METADATA_CID}/`  
- [ ] (선택) Etherscan Refresh  

**통과** → [05-frontend-mint.md](05-frontend-mint.md)

---

## 자주 막히는 곳 (Pinata 기준)

| 증상 | 원인 | 해결 |
| --- | --- | --- |
| Gateways 메뉴가 안 보임 | UI 위치 변경 | 앱 검색창에 `Gateway` · [Pinata Docs – Gateways](https://docs.pinata.cloud/) |
| 업로드에 Folder가 없음 | File만 선택함 | **+ Add → Folder** |
| `/0.jpg` 404 | `nft` 전체를 올림 | Files에서 삭제 → **`images`만** 재업로드 |
| JSON은 되는데 그림 X | `image`가 GitHub이거나 옛 CID | Step 5 → metadata **재업로드** → **새** METADATA_CID로 `setBaseURI` |
| `setBaseURI` 후 404 | 끝 `/` 없음 | `…/CID/` 로 다시 transact |
| Free 한도 | 용량·핀 수 | 불필요 파일 Unpin/Delete 후 재시도 |
| 다른 사람 gateway만 복사 | Dedicated는 계정마다 다름 | 본인 Gateways 값 사용 (참고 값은 위 표) |

### metadata를 다시 고쳤을 때 (순서 고정)

```text
1. image URL 수정 (스크립트)
2. Pinata에 metadata 폴더 다시 Upload → 새 METADATA_CID
3. Remix setBaseURI(새 URL)
4. Etherscan Refresh Metadata
```

이미지만 바꿔도 JSON의 `image`가 바뀌면 **metadata를 다시 올려야** CID가 맞습니다.

---

## GitHub Raw로 되돌리기

Pinata 대신 다시 GitHub을 쓰려면 owner가 `setBaseURI`만 다시 호출:

```text
https://raw.githubusercontent.com/uno-gilbert/VIBE-MINT/main/assets/nft/metadata/
```

상세: [04-deploy-sepolia.md](04-deploy-sepolia.md)

---

## 관련 링크

| 구분 | URL / 경로 |
| --- | --- |
| Pinata 앱 | https://app.pinata.cloud/ |
| 이미지 확인 (실습) | https://magenta-key-quokka-912.mypinata.cloud/ipfs/bafybeibzqlnvhkviwqytx2lx7pxk65yzjap3uunoeth2wknylzg6z4pm7e/0.jpg |
| 업로드 공식 문서 | https://docs.pinata.cloud/files/uploading-files |
| 에셋 README | [assets/nft/README.md](../../assets/nft/README.md) |
| image URL 스크립트 | `assets/nft/scripts/rewrite-image-urls.mjs` |

---

Sepolia 교육용 실습입니다. 메인넷에서는 pin 유지·백업·전문 Audit을 검토하세요.
