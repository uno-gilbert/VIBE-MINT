#!/usr/bin/env python3
"""Generate VibeMint workshop PowerPoint."""

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt

OUTPUT = Path(__file__).parent / "VibeMint-Workshop-2026.pptx"

ACCENT = RGBColor(37, 99, 235)
DARK = RGBColor(17, 24, 39)
GRAY = RGBColor(107, 114, 128)
WHITE = RGBColor(255, 255, 255)


def set_slide_bg(slide, r, g, b):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(r, g, b)


def add_title_slide(prs, title, subtitle=""):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, 15, 23, 42)
    box = slide.shapes.add_textbox(Inches(0.8), Inches(2.2), Inches(11.5), Inches(1.5))
    tf = box.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.LEFT
    if subtitle:
        box2 = slide.shapes.add_textbox(Inches(0.8), Inches(3.8), Inches(11.5), Inches(1.2))
        tf2 = box2.text_frame
        p2 = tf2.paragraphs[0]
        p2.text = subtitle
        p2.font.size = Pt(20)
        p2.font.color.rgb = RGBColor(191, 219, 254)


def add_section_slide(prs, time_range, title):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, 37, 99, 235)
    t1 = slide.shapes.add_textbox(Inches(0.8), Inches(2.5), Inches(11), Inches(0.8))
    t1.text_frame.paragraphs[0].text = time_range
    t1.text_frame.paragraphs[0].font.size = Pt(22)
    t1.text_frame.paragraphs[0].font.color.rgb = RGBColor(219, 234, 254)
    t2 = slide.shapes.add_textbox(Inches(0.8), Inches(3.2), Inches(11), Inches(1.5))
    t2.text_frame.paragraphs[0].text = title
    t2.text_frame.paragraphs[0].font.size = Pt(36)
    t2.text_frame.paragraphs[0].font.bold = True
    t2.text_frame.paragraphs[0].font.color.rgb = WHITE


def add_content_slide(prs, title, bullets, note=""):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, 255, 255, 255)
    # title bar
    bar = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(13.33), Inches(1.1))
    bar.fill.solid()
    bar.fill.fore_color.rgb = ACCENT
    bar.line.fill.background()
    tb = slide.shapes.add_textbox(Inches(0.6), Inches(0.25), Inches(12), Inches(0.7))
    tb.text_frame.paragraphs[0].text = title
    tb.text_frame.paragraphs[0].font.size = Pt(26)
    tb.text_frame.paragraphs[0].font.bold = True
    tb.text_frame.paragraphs[0].font.color.rgb = WHITE
    # body
    body = slide.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(11.8), Inches(5.5))
    tf = body.text_frame
    tf.word_wrap = True
    for i, item in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = item
        p.font.size = Pt(22)
        p.font.color.rgb = DARK
        p.space_after = Pt(14)
        p.level = 0
    if note:
        nb = slide.shapes.add_textbox(Inches(0.8), Inches(6.8), Inches(11.8), Inches(0.5))
        np = nb.text_frame.paragraphs[0]
        np.text = note
        np.font.size = Pt(14)
        np.font.color.rgb = GRAY


def add_table_slide(prs, title, headers, rows):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, 255, 255, 255)
    bar = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(13.33), Inches(1.1))
    bar.fill.solid()
    bar.fill.fore_color.rgb = ACCENT
    bar.line.fill.background()
    tb = slide.shapes.add_textbox(Inches(0.6), Inches(0.25), Inches(12), Inches(0.7))
    tb.text_frame.paragraphs[0].text = title
    tb.text_frame.paragraphs[0].font.size = Pt(26)
    tb.text_frame.paragraphs[0].font.bold = True
    tb.text_frame.paragraphs[0].font.color.rgb = WHITE
    cols = len(headers)
    table_shape = slide.shapes.add_table(
        len(rows) + 1, cols, Inches(0.6), Inches(1.6), Inches(12.1), Inches(0.45 * (len(rows) + 2))
    )
    table = table_shape.table
    for c, h in enumerate(headers):
        cell = table.cell(0, c)
        cell.text = h
        for p in cell.text_frame.paragraphs:
            p.font.bold = True
            p.font.size = Pt(14)
            p.font.color.rgb = WHITE
        cell.fill.solid()
        cell.fill.fore_color.rgb = ACCENT
    for r, row in enumerate(rows, start=1):
        for c, val in enumerate(row):
            cell = table.cell(r, c)
            cell.text = val
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(13)


def build():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Cover
    add_title_slide(
        prs,
        "쉽게 이해하고 빠르게\nAI 바이브 코딩으로 만들어 보는 NFT",
        "VibeMint 워크숍 · 2026 · Sepolia 테스트넷",
    )

    # === 10:00-10:30 ===
    add_section_slide(prs, "10:00 ~ 10:30", "강사 소개 및 AI 바이브 코딩 오리엔테이션")

    add_content_slide(
        prs,
        "강사 소개",
        [
            "이름 / 소속 / 연락처 (강사님 정보로 수정)",
            "블록체인 · Web3 · AI 코딩 경력 요약",
            "오늘 함께 만들 것: Sepolia NFT DApp 「VibeMint」",
        ],
    )

    add_table_slide(
        prs,
        "오늘의 로드맵 (6시간)",
        ["시간", "주제"],
        [
            ("10:00~10:30", "오리엔테이션"),
            ("10:30~11:30", "NFT 스마트 컨트랙트 이해"),
            ("11:30~12:30", "유명 NFT 프로젝트 분석"),
            ("13:30~15:00", "AI 바이브 코딩 NFT 개발"),
            ("15:00~16:30", "Sepolia 배포 · mint"),
            ("16:30~18:00", "DApp · OpenSea"),
        ],
    )

    add_content_slide(
        prs,
        "AI 바이브 코딩(Vibe Coding)이란?",
        [
            "자연어(의도)로 원하는 기능을 설명하면 AI가 코드를 생성하는 개발 방식",
            "Cursor, Composer, Agent 모드 등 AI 코딩 도구 활용",
            "2026년 Web3 해커톤·실무에서 표준 워크플로우로 자리 잡는 중",
            "핵심: 빠른 프로토타이핑 + 사람의 검토(Review)",
        ],
    )

    add_content_slide(
        prs,
        "실무 워크플로우: Intent → Spec → Generate → Review → Ship",
        [
            "Intent — 무엇을 만들지 한 문장으로 정의",
            "Spec — 함수·조건·에러를 구체적 명세로 작성",
            "Generate — AI에게 Stage별 diff만 요청 (한 번에 전체 X)",
            "Review — 배포 전 AI + 사람 보안 Audit",
            "Ship — Sepolia 배포 → DApp 연결",
        ],
        note="★ AI에게 「전체 코드 짜줘」라고 하면 꼬이기 쉽습니다",
    )

    add_content_slide(
        prs,
        "오늘의 목표",
        [
            "ERC-721 NFT 스마트 컨트랙트 이해 및 직접 빌드",
            "Cursor + Remix + MetaMask로 Sepolia 테스트넷 배포",
            "MetaMask 연동 민팅 DApp 완성",
            "OpenSea 테스트넷에서 NFT 확인",
        ],
    )

    add_content_slide(
        prs,
        "사전 준비 체크",
        [
            "✓ Chrome 브라우저",
            "✓ MetaMask + Sepolia(세폴리아) 네트워크",
            "✓ Cursor AI 설치 · 로그인",
            "✓ Node.js v20+ (프론트 실습)",
            "⚠ 시드 구문 절대 공유 금지 · 테스트넷만 사용",
        ],
    )

    # === 10:30-11:30 ===
    add_section_slide(prs, "10:30 ~ 11:30", "NFT 스마트 컨트랙트의 이해")

    add_content_slide(
        prs,
        "NFT란?",
        [
            "Non-Fungible Token — 대체 불가능한 디지털 자산",
            "블록체인에 소유권·거래 기록이 저장됨",
            "대표 사용: PFP, 아트, 게임 아이템, 멤버십",
            "오늘 실습: ERC-721 기반 「VibeMint」 컬렉션",
        ],
    )

    add_table_slide(
        prs,
        "ERC-721 vs ERC-1155",
        ["", "ERC-721", "ERC-1155"],
        [
            ("단위", "토큰마다 고유 ID", "한 컨트랙트에 여러 종류"),
            ("용도", "1/1 또는 시리즈 NFT", "게임 아이템·다종 에셋"),
            ("전송", "tokenId 단위", "batch 전송 가능"),
            ("오늘", "★ 사용", "개념만"),
        ],
    )

    add_content_slide(
        prs,
        "OpenZeppelin ERC-721 구조",
        [
            "ERC721 — NFT 표준 (transfer, approve, tokenURI)",
            "Ownable — owner(관리자) 권한",
            "Pausable — 긴급 pause / unpause",
            "ReentrancyGuard — withdraw 시 재진입 공격 방지",
            "→ 검증된 라이브러리를 AI와 함께 사용",
        ],
    )

    add_content_slide(
        prs,
        "핵심 함수 이해",
        [
            "mint() — NFT 발행 (payable)",
            "ownerOf(tokenId) — 소유자 조회",
            "tokenURI(tokenId) — 메타데이터 URL",
            "totalMinted / maxSupply — 발행량 관리",
            "pause() — 모든 mint 일시 중지",
        ],
    )

    add_content_slide(
        prs,
        "실습: Cursor AI 역분석",
        [
            "1. contracts/solution/VibeMintNFT.sol 열기",
            "2. Cursor 채팅에 @VibeMintNFT.sol 멘션",
            "3. 「이 컨트랙트를 역분석해줘」 프롬프트 실행",
            "4. mint / whitelist / pause 흐름을 자연어로 정리",
        ],
        note="코드를 수정하지 않고 읽기만 — Spec 작성 예습",
    )

    # === 11:30-12:30 ===
    add_section_slide(prs, "11:30 ~ 12:30", "유명 NFT 프로젝트 분석")

    add_content_slide(
        prs,
        "대표 NFT 프로젝트 벤치마킹",
        [
            "BAYC (Bored Ape Yacht Club) — PFP, 커뮤니티, 상업 이용권",
            "Azuki — 아트 스타일, 화이트리스트 민팅",
            "공통 요소: maxSupply, mintPrice, whitelist, reveal",
            "→ 비즈니스 로직이 컨트랙트에 어떻게 담기는지 분석",
        ],
    )

    add_content_slide(
        prs,
        "민팅 구조 분석 포인트",
        [
            "누가 mint할 수 있는가? (public / whitelist / owner)",
            "얼마를 내야 하는가? (mintPrice)",
            "최대 몇 개까지? (maxSupply, per-wallet cap)",
            "언제 중지할 수 있는가? (pause)",
            "수익은 어디로? (withdraw)",
        ],
    )

    add_content_slide(
        prs,
        "Spec(명세)이란?",
        [
            "AI에게 「주문서」를 주는 문서",
            "함수명, 접근 권한, revert 조건, ETH 금액을 표/YAML로 명시",
            "Spec 없이 「NFT 만들어줘」→ AI가 추측 → 버그·보안 누락",
            "오후 실습 전 VibeMint Spec을 반드시 확정",
        ],
    )

    add_table_slide(
        prs,
        "VibeMint Spec (교육용)",
        ["항목", "값"],
        [
            ("표준", "ERC-721"),
            ("이름 / 심볼", "VibeMint / VMINT"),
            ("maxSupply", "100"),
            ("mintPrice", "0.001 ETH"),
            ("지갑당 cap", "3"),
            ("체인", "Sepolia 테스트넷"),
        ],
    )

    add_content_slide(
        prs,
        "실습: Spec 작성",
        [
            "1. docs/prompts/02-spec-generator.md 프롬프트 실행",
            "2. YAML Spec 출력 확인 · 수정",
            "3. 옆 사람과 diff — 누락된 revert 조건 찾기",
            "4. 확정 Spec → 점심 후 Stage 빌드에 사용",
        ],
    )

    # === Lunch ===
    add_section_slide(prs, "12:30 ~ 13:30", "점심 식사")

    add_content_slide(
        prs,
        "점심 후 Preview",
        [
            "Stage 0 → 3 점진적 컨트랙트 빌드",
            "AI 보안 Audit (배포 전 필수)",
            "Sepolia 배포 + mint",
            "MetaMask DApp + OpenSea",
        ],
        note="점심 전 MetaMask Sepolia + Cursor 로그인 재확인",
    )

    # === 13:30-15:00 ===
    add_section_slide(prs, "13:30 ~ 15:00", "AI 바이브 코딩 NFT 개발 및 배포 과정 학습")

    add_content_slide(
        prs,
        "점진적 빌드 (Incremental Build)",
        [
            "Stage 0 — ERC-721 뼈대 (mint 없음)",
            "Stage 1 — public mint + supply cap",
            "Stage 2 — pause, ownerMint, withdraw",
            "Stage 3 — whitelist mint",
            "★ 매 Stage마다 Remix Compile 확인",
        ],
    )

    add_content_slide(
        prs,
        "AI 공통 규칙 (00-rules)",
        [
            "한 번에 전체 파일 재작성 금지",
            "OpenZeppelin (@openzeppelin/contracts)만 사용",
            "요청한 Stage diff만 추가",
            "Solidity ^0.8.20, Remix 호환 import",
            "Sepolia 테스트넷 교육용 — 메인넷 X",
        ],
    )

    add_content_slide(
        prs,
        "Stage별 Cursor 프롬프트",
        [
            "Stage 0: docs/prompts/03-stage-build/stage-0.md",
            "Stage 1: stage-1.md — mint() + mintPrice",
            "Stage 2: stage-2.md — Pausable + withdraw",
            "Stage 3: stage-3.md — whitelist",
            "막히면 contracts/stages/ 폴더 참고",
        ],
    )

    add_content_slide(
        prs,
        "AI 보안 Audit (필수 · Review)",
        [
            "배포 전 docs/prompts/04-security-audit.md 실행",
            "Access control — onlyOwner, whenNotPaused",
            "Reentrancy — withdraw CEI 패턴",
            "Mint economics — maxSupply, msg.value, per-wallet cap",
            "Critical / High 0건 → 배포 진행",
        ],
        note="★ AI 생성 코드 상당 비율 취약점 보고 — Audit 생략 금지",
    )

    # === 15:00-16:30 ===
    add_section_slide(prs, "15:00 ~ 16:30", "NFT 컨트랙트 작성 및 배포")

    add_content_slide(
        prs,
        "Sepolia(세폴리아) 테스트넷",
        [
            "Ethereum 연습용 네트워크 — 실제 돈 없음",
            "MetaMask Chain ID: 11155111",
            "메인넷 ETH 보내지 마세요",
            "배포·mint·DApp 연동 모두 Sepolia에서",
        ],
    )

    add_content_slide(
        prs,
        "Faucet(파우셋) — 테스트 ETH 받기",
        [
            "Alchemy Sepolia Faucet",
            "Sepolia PoW Faucet",
            "지갑 주소 입력 → 무료 Sepolia ETH 수령",
            "0.05 ETH 이상 권장",
        ],
    )

    add_content_slide(
        prs,
        "Remix 배포 단계",
        [
            "1. Compile VibeMintNFT.sol (0.8.20)",
            "2. Deploy → Injected Provider - MetaMask",
            "3. Sepolia 선택 → Deploy 승인",
            "4. Contract Address 복사 저장",
            "5. setBaseURI() 호출 (owner)",
        ],
    )

    add_content_slide(
        prs,
        "테스트 Mint",
        [
            "mint() — Value: 0.001 ETH → transact",
            "MetaMask 승인",
            "totalMinted Read → 1",
            "ownerOf(0) → 내 지갑 주소",
            "Etherscan Sepolia에서 tx 확인",
        ],
    )

    # === 16:30-18:00 ===
    add_section_slide(prs, "16:30 ~ 18:00", "AI 바이브 코딩 NFT DApp 개발 및 오픈씨 거래")

    add_content_slide(
        prs,
        "프론트 DApp 구조",
        [
            "frontend/starter — Vite + React + wagmi",
            ".env → VITE_CONTRACT_ADDRESS=배포주소",
            "npm install && npm run dev",
            "localhost:5173 → Connect Wallet → Mint",
        ],
    )

    add_content_slide(
        prs,
        "MetaMask 연동 Mint UI",
        [
            "Connect Wallet — MetaMask Sepolia",
            "Mint (0.001 ETH) — 컨트랙트 mint() 호출",
            "트랜잭션 pending → success",
            "Etherscan 링크로 tx 확인",
        ],
    )

    add_content_slide(
        prs,
        "OpenSea 테스트넷",
        [
            "testnets.opensea.io 접속",
            "MetaMask 연결 → Profile → NFT 확인",
            "인덱싱 5~30분 지연 가능",
            "Token URL: testnets.opensea.io/assets/sepolia/{주소}/{tokenId}",
        ],
    )

    add_content_slide(
        prs,
        "마무리",
        [
            "✓ Intent → Spec → Generate → Review → Ship 완주",
            "오늘 코드 = Sepolia 교육용",
            "메인넷 배포 전 반드시 전문 Smart Contract Audit",
            "AI는 주니어 개발자 — Review(Audit)는 생략하지 마세요",
            "실습 가이드: docs/student/00-walkthrough.md",
        ],
    )

    add_title_slide(
        prs,
        "감사합니다",
        "Q & A",
    )

    prs.save(OUTPUT)
    print(f"Saved: {OUTPUT}")


if __name__ == "__main__":
    build()
