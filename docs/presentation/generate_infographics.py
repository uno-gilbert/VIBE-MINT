#!/usr/bin/env python3
"""Generate VibeMint workshop infographic PNGs for PPT slides."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).parent
IMAGES = ROOT / "images"

# Brand colors (match session1-1-1 style)
NAVY = (15, 23, 42)
BLUE = (37, 99, 235)
LIGHT_BLUE = (219, 234, 254)
GRAY = (107, 114, 128)
DARK = (17, 24, 39)
WHITE = (255, 255, 255)
CARD_BG = (248, 250, 252)
BORDER = (226, 232, 240)
GREEN = (22, 163, 74)

W, H = 1920, 1080


def load_font(size: int, bold: bool = False):
    candidates = [
        "/System/Library/Fonts/AppleSDGothicNeo.ttc",
        "/System/Library/Fonts/Supplemental/AppleGothic.ttf",
        "/Library/Fonts/Arial Unicode.ttf",
        "/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf" if bold else "/usr/share/fonts/truetype/nanum/NanumGothic.ttf",
    ]
    for path in candidates:
        p = Path(path)
        if p.exists():
            try:
                return ImageFont.truetype(str(p), size=size, index=1 if bold and p.suffix == ".ttc" else 0)
            except OSError:
                try:
                    return ImageFont.truetype(str(p), size=size)
                except OSError:
                    continue
    return ImageFont.load_default()


def rounded_rect(draw, xy, radius, fill, outline=None, width=1):
    x0, y0, x1, y1 = xy
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def draw_badge(draw, x, y, num, font):
    r = 22
    draw.ellipse((x - r, y - r, x + r, y + r), fill=BLUE)
    text = str(num)
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text((x - tw / 2, y - th / 2 - 2), text, fill=WHITE, font=font)


def wrap_text(text, font, max_width, draw):
    words = text.replace(" · ", " · ").split(" ")
    lines = []
    current = ""
    for word in words:
        test = f"{current} {word}".strip()
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_timeline_node(draw, x, y, color, label, title, body_lines, icon_fn, fonts):
    title_f, body_f, tag_f = fonts
    r = 18
    draw.line((x, y + r, x, y + 52), fill=BORDER, width=3)
    draw.ellipse((x - r, y - r, x + r, y + r), fill=color, outline=WHITE, width=3)
    icon_fn(draw, x, y, r)
    draw.text((x + 36, y - 22), label, fill=BLUE, font=tag_f)
    draw.text((x + 36, y - 2), title, fill=NAVY, font=title_f)
    by = y + 18
    for line in body_lines:
        draw.text((x + 36, by), line, fill=DARK, font=body_f)
        by += 22


def icon_blizzard(draw, x, y, r):
    draw.rectangle((x - 10, y - 8, x + 10, y + 8), fill=WHITE)
    draw.text((x - 7, y - 10), "BZ", fill=(200, 50, 50), font=load_font(12, bold=True))


def icon_mobile(draw, x, y, r):
    draw.rounded_rectangle((x - 8, y - 12, x + 8, y + 12), radius=3, fill=WHITE)
    draw.ellipse((x - 2, y + 8, x + 2, y + 11), fill=GRAY)


def icon_chain(draw, x, y, r):
    draw.ellipse((x - 12, y - 4, x - 2, y + 6), outline=WHITE, width=2)
    draw.ellipse((x + 2, y - 4, x + 12, y + 6), outline=WHITE, width=2)


def icon_poker(draw, x, y, r):
    draw.ellipse((x - 10, y - 10, x + 10, y + 10), fill=WHITE, outline=(220, 38, 38), width=2)
    draw.text((x - 8, y - 9), "♠", fill=(220, 38, 38), font=load_font(14))


def icon_ai(draw, x, y, r):
    draw.polygon([(x, y - 12), (x + 12, y + 10), (x - 12, y + 10)], fill=WHITE)
    draw.text((x - 5, y - 4), "AI", fill=BLUE, font=load_font(11, bold=True))


def draw_instructor_avatar(draw, cx, cy):
    """Simple instructor illustration — waving developer."""
    # shoulders
    draw.ellipse((cx - 70, cy + 20, cx + 70, cy + 110), fill=LIGHT_BLUE, outline=BLUE, width=2)
    # head
    draw.ellipse((cx - 48, cy - 70, cx + 48, cy + 26), fill=(255, 224, 189), outline=(180, 140, 110), width=2)
    # hair
    draw.arc((cx - 50, cy - 82, cx + 50, cy + 10), start=180, end=360, fill=(30, 30, 30), width=16)
    # eyes
    draw.ellipse((cx - 18, cy - 20, cx - 8, cy - 10), fill=DARK)
    draw.ellipse((cx + 8, cy - 20, cx + 18, cy - 10), fill=DARK)
    # smile
    draw.arc((cx - 16, cy - 8, cx + 16, cy + 14), start=10, end=170, fill=(180, 80, 80), width=2)
    # waving hand
    draw.line((cx + 52, cy + 30, cx + 95, cy - 10), fill=(255, 224, 189), width=10)
    draw.ellipse((cx + 88, cy - 22, cx + 108, cy - 2), fill=(255, 224, 189), outline=(180, 140, 110), width=2)
    # laptop badge
    draw.rounded_rectangle((cx - 34, cy + 48, cx + 34, cy + 78), radius=4, fill=NAVY)
    draw.text((cx - 24, cy + 52), "VibeMint", fill=WHITE, font=load_font(14, bold=True))


def generate_session1_1_1_instructor_env():
    """강사 소개 · GitHub QR (Q&A·로드맵 제거)."""
    out = IMAGES / "session1-1-1-instructor-env.png"
    qr_path = ROOT.parent / "images" / "vibe-mint-github-qr.png"
    if not qr_path.exists():
        raise FileNotFoundError(f"Missing QR: {qr_path}")

    img = Image.new("RGB", (W, H), WHITE)
    draw = ImageDraw.Draw(img)

    title_f = load_font(52, bold=True)
    sub_f = load_font(26)
    card_title_f = load_font(28, bold=True)
    body_f = load_font(20)
    small_f = load_font(18)
    tag_f = load_font(16, bold=True)
    footer_f = load_font(26, bold=True)

    # Header
    draw.text((80, 48), "VibeMint 워크숍 · 1차시-1", fill=GRAY, font=sub_f)
    draw.text((80, 92), "강사 소개 · 수업 환경", fill=NAVY, font=title_f)
    draw.text((80, 168), "강사 경력 · GitHub 실습 저장소", fill=GRAY, font=sub_f)

    # --- Left card: Instructor ---
    left = (80, 230, 920, 960)
    rounded_rect(draw, left, 20, CARD_BG, BORDER, 2)
    draw.text((left[0] + 36, left[1] + 28), "1. 강사 소개", fill=NAVY, font=card_title_f)

    # Avatar illustration area
    avatar_cx = left[0] + 130
    avatar_cy = left[1] + 120
    draw.rounded_rectangle(
        (left[0] + 36, left[1] + 72, left[0] + 280, left[1] + 290),
        radius=14,
        fill=WHITE,
        outline=LIGHT_BLUE,
        width=2,
    )
    draw_instructor_avatar(draw, avatar_cx, avatar_cy)
    draw.text((left[0] + 48, left[1] + 248), "안녕하세요!", fill=NAVY, font=body_f)
    draw.text((left[0] + 48, left[1] + 274), "VibeMint 워크숍 강사", fill=GRAY, font=small_f)

    # Career timeline
    timeline_x = left[0] + 310
    timeline_top = left[1] + 78
    draw.text((timeline_x, timeline_top), "경력 타임라인", fill=BLUE, font=tag_f)

    nodes = [
        ("2000s", "Blizzard · Battle.net", ["디아블로 옥션 하우스 개발", "게임 아이템 경제의 중요성"], (200, 50, 50), icon_blizzard),
        ("2010s", "Smilegate", ["모바일 게임 플랫폼 개발", "대규모 유저 서비스 경험"], (16, 120, 70), icon_mobile),
        ("Blockchain", "Anserslab", ["블록체인 프로젝트 진행", "온체인·오프체인 연동"], (124, 58, 237), icon_chain),
        ("Poker", "온라인 포커 서비스", ["포커칩 충전 → 크립토 에셋", "다수 블록체인 프로젝트 총괄"], (180, 120, 40), icon_poker),
        ("Now", "HelloLive · 개발 이사", ["AI 활용 프로젝트 진행", "Intent → Ship 실무 적용"], BLUE, icon_ai),
    ]

    ny = timeline_top + 34
    for label, title, lines, color, icon in nodes:
        draw_timeline_node(
            draw,
            timeline_x + 14,
            ny,
            color,
            label,
            title,
            lines,
            icon,
            (load_font(19, bold=True), load_font(17), tag_f),
        )
        ny += 108

    # --- Right card: GitHub + QR ---
    right = (980, 230, 1840, 960)
    rounded_rect(draw, right, 20, CARD_BG, BORDER, 2)
    draw.text((right[0] + 36, right[1] + 28), "2. 실습 저장소 · GitHub", fill=NAVY, font=card_title_f)

    qr = Image.open(qr_path).convert("RGB")
    qr_size = 320
    qr = qr.resize((qr_size, qr_size), Image.Resampling.LANCZOS)
    qr_x = right[0] + (right[2] - right[0] - qr_size) // 2
    qr_y = right[1] + 100
    rounded_rect(draw, (qr_x - 16, qr_y - 16, qr_x + qr_size + 16, qr_y + qr_size + 16), 12, WHITE, BLUE, 3)
    img.paste(qr, (qr_x, qr_y))

    draw.text((right[0] + 36, qr_y + qr_size + 36), "github.com/uno-gilbert/VIBE-MINT", fill=BLUE, font=load_font(24, bold=True))
    draw.text((right[0] + 36, qr_y + qr_size + 76), "QR 스캔 또는 git clone", fill=GRAY, font=body_f)

    cmd_y = qr_y + qr_size + 120
    rounded_rect(draw, (right[0] + 36, cmd_y, right[2] - 36, cmd_y + 56), 10, (241, 245, 249), BORDER, 1)
    draw.text(
        (right[0] + 52, cmd_y + 14),
        "git clone https://github.com/uno-gilbert/VIBE-MINT.git",
        fill=DARK,
        font=load_font(19),
    )

    bullets = [
        "Code → Download ZIP 도 가능",
        "Cursor에서 폴더를 열어 실습 시작",
        "NFT 메타데이터: assets/nft/ (HeroGate 영웅 카드)",
    ]
    by = cmd_y + 80
    for line in bullets:
        draw.text((right[0] + 36, by), f"• {line}", fill=DARK, font=body_f)
        by += 32

    # Footer
    draw.rectangle((0, H - 88, W, H), fill=NAVY)
    draw.text(
        (80, H - 62),
        "오늘 6시간으로 Intent → Spec → Generate → Review → Ship 전 구간을 경험합니다",
        fill=WHITE,
        font=footer_f,
    )

    img.save(out, "PNG", optimize=True)
    print(f"Saved: {out}")


def generate_session2_1_3_compile_deploy():
    """Compile·Deploy·Read/Write — Remix screenshot + menu order."""
    out = IMAGES / "session2-1-3-compile-deploy.png"
    screenshot = IMAGES / "remix-vibemint-compile-screenshot.png"
    if not screenshot.exists():
        raise FileNotFoundError(f"Missing screenshot: {screenshot}")

    img = Image.new("RGB", (W, H), WHITE)
    draw = ImageDraw.Draw(img)

    title_f = load_font(52, bold=True)
    sub_f = load_font(26)
    card_title_f = load_font(24, bold=True)
    body_f = load_font(20)
    badge_f = load_font(22, bold=True)
    footer_f = load_font(26, bold=True)
    small_f = load_font(18)

    # Header
    draw.text((80, 48), "VibeMint 워크숍 · 2차시-1", fill=GRAY, font=sub_f)
    draw.text((80, 92), "Compile · Deploy · Read/Write", fill=NAVY, font=title_f)
    draw.text(
        (80, 168),
        "VibeMintNFT.sol · Remix 메뉴별 순서 (Compiler 0.8.31 · EVM osaka)",
        fill=GRAY,
        font=sub_f,
    )

    # Screenshot panel (left)
    shot = Image.open(screenshot).convert("RGB")
    panel_x, panel_y = 80, 230
    panel_w, panel_h = 980, 620
    shot_ratio = shot.width / shot.height
    target_ratio = panel_w / panel_h
    if shot_ratio > target_ratio:
        new_w = panel_w
        new_h = int(new_w / shot_ratio)
    else:
        new_h = panel_h
        new_w = int(new_h * shot_ratio)
    shot_resized = shot.resize((new_w, new_h), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (panel_w, panel_h), CARD_BG)
    ox = (panel_w - new_w) // 2
    oy = (panel_h - new_h) // 2
    canvas.paste(shot_resized, (ox, oy))
    rounded_rect(draw, (panel_x, panel_y, panel_x + panel_w, panel_y + panel_h), 16, CARD_BG, BORDER, 2)
    img.paste(canvas, (panel_x + 2, panel_y + 2))

    # Annotation labels on screenshot area
    labels = [
        (panel_x + 18, panel_y + 18, "② Solidity Compiler", GREEN),
        (panel_x + panel_w - 280, panel_y + 18, "① File Explorer", BLUE),
        (panel_x + 18, panel_y + panel_h - 44, "③ Compile VibeMintNFT.sol", BLUE),
    ]
    for lx, ly, text, color in labels:
        bbox = draw.textbbox((0, 0), text, font=small_f)
        tw = bbox[2] - bbox[0]
        rounded_rect(draw, (lx, ly, lx + tw + 24, ly + 34), 8, color)
        draw.text((lx + 12, ly + 6), text, fill=WHITE, font=small_f)

    # Step cards (right)
    steps = [
        (
            "① File Explorer (📁)",
            [
                "contracts/VibeMintNFT.sol 생성",
                "stage-0-base 코드 전체 붙여넣기",
                "pragma ^0.8.31 · OZ @5.1.0 import",
                "Cmd/Ctrl + S 저장",
            ],
        ),
        (
            "② Solidity Compiler (⚙️)",
            [
                "COMPILER → 0.8.31 선택",
                "Advanced → EVM Version = osaka",
                "Compile VibeMintNFT.sol 클릭",
                "초록 체크 = 성공",
            ],
        ),
        (
            "③ Deploy & Run (🚀)",
            [
                "Environment = Remix VM",
                "Account #0 (owner)",
                "Contract: VibeMintNFT → Deploy",
                "Deployed Contracts에 등장 확인",
            ],
        ),
        (
            "④ Read / Write",
            [
                "파란색 = Read (name, owner, maxSupply)",
                "주황색 = Write (setBaseURI)",
                "Account #1 → setBaseURI revert 확인",
                "mint 버튼 없음 (Stage 0)",
            ],
        ),
    ]

    card_x = 1100
    card_w = 740
    card_h = 138
    gap = 16
    start_y = 230

    for i, (title, bullets) in enumerate(steps):
        cy = start_y + i * (card_h + gap)
        rounded_rect(draw, (card_x, cy, card_x + card_w, cy + card_h), 14, CARD_BG, BORDER, 2)
        draw_badge(draw, card_x + 36, cy + 36, i + 1, badge_f)
        draw.text((card_x + 72, cy + 18), title, fill=NAVY, font=card_title_f)
        bx = card_x + 72
        by = cy + 54
        for j, line in enumerate(bullets):
            draw.text((bx, by + j * 22), f"• {line}", fill=DARK, font=body_f)

    # Footer bar
    draw.rectangle((0, H - 88, W, H), fill=NAVY)
    draw.text(
        (80, H - 62),
        "Stage 0~3 공통: ①파일 → ②컴파일(0.8.31·osaka) → ③Remix VM Deploy → ④Read/Write 테스트",
        fill=WHITE,
        font=footer_f,
    )

    img.save(out, "PNG", optimize=True)
    print(f"Saved: {out}")


def generate_session2_2_1_stage_0_1():
    """Stage 0~1 — Remix Deploy panel with mint (Stage 1 screenshot)."""
    out = IMAGES / "session2-2-1-stage-0-1.png"
    screenshot = IMAGES / "remix-stage1-deploy-mint-screenshot.png"
    if not screenshot.exists():
        raise FileNotFoundError(f"Missing screenshot: {screenshot}")

    img = Image.new("RGB", (W, H), WHITE)
    draw = ImageDraw.Draw(img)

    title_f = load_font(48, bold=True)
    sub_f = load_font(24)
    card_title_f = load_font(22, bold=True)
    body_f = load_font(18)
    badge_f = load_font(20, bold=True)
    footer_f = load_font(24, bold=True)
    small_f = load_font(16)

    draw.text((80, 40), "VibeMint 워크숍 · 2차시-2", fill=GRAY, font=sub_f)
    draw.text((80, 82), "Stage 1 · Public Mint", fill=NAVY, font=title_f)
    draw.text(
        (80, 150),
        "캡처: Remix VM(Osaka) Deploy 후 mint 버튼 · VALUE 0.001 ether",
        fill=GRAY,
        font=sub_f,
    )

    shot = Image.open(screenshot).convert("RGB")
    panel_x, panel_y = 60, 210
    panel_w, panel_h = 1020, 680
    shot_ratio = shot.width / shot.height
    target_ratio = panel_w / panel_h
    if shot_ratio > target_ratio:
        new_w = panel_w
        new_h = int(new_w / shot_ratio)
    else:
        new_h = panel_h
        new_w = int(new_h * shot_ratio)
    shot_resized = shot.resize((new_w, new_h), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (panel_w, panel_h), CARD_BG)
    ox = (panel_w - new_w) // 2
    oy = (panel_h - new_h) // 2
    canvas.paste(shot_resized, (ox, oy))
    rounded_rect(draw, (panel_x, panel_y, panel_x + panel_w, panel_y + panel_h), 16, CARD_BG, BORDER, 2)
    img.paste(canvas, (panel_x + 2, panel_y + 2))

    labels = [
        (panel_x + 14, panel_y + 14, "B Deploy & Run", BLUE),
        (panel_x + 14, panel_y + 56, "C Remix VM · Osaka", GREEN),
        (panel_x + 14, panel_y + panel_h - 90, "F mint (payable)", (220, 38, 38)),
        (panel_x + panel_w - 220, panel_y + 14, "G mint() 코드", BLUE),
    ]
    for lx, ly, text, color in labels:
        bbox = draw.textbbox((0, 0), text, font=small_f)
        tw = bbox[2] - bbox[0]
        rounded_rect(draw, (lx, ly, lx + tw + 20, ly + 30), 8, color)
        draw.text((lx + 10, ly + 5), text, fill=WHITE, font=small_f)

    steps = [
        (
            "A · 초록 체크",
            [
                "Compile 성공 (문법 OK)",
                "아직 Stage 완료는 아님",
            ],
        ),
        (
            "C · Environment",
            [
                "Remix VM (Osaka)",
                "연습용 · MetaMask 불필요",
            ],
        ),
        (
            "E · Deploy",
            [
                "VibeMintNFT · Compiled",
                "Deploy → Deployed에 등장",
            ],
        ),
        (
            "F · mint 테스트",
            [
                "VALUE = 0.001 ether",
                "mint → transact → totalMinted=1",
                "Value 0 / 4번째 → revert",
            ],
        ),
        (
            "Stage 0과 차이",
            [
                "Stage 0: mint 버튼 없음",
                "Stage 1: mint + 가격·한도",
            ],
        ),
    ]

    card_x = 1120
    card_w = 720
    card_h = 112
    gap = 12
    start_y = 210

    for i, (title, bullets) in enumerate(steps):
        cy = start_y + i * (card_h + gap)
        rounded_rect(draw, (card_x, cy, card_x + card_w, cy + card_h), 12, CARD_BG, BORDER, 2)
        draw_badge(draw, card_x + 32, cy + 32, i + 1, badge_f)
        draw.text((card_x + 64, cy + 14), title, fill=NAVY, font=card_title_f)
        for j, line in enumerate(bullets):
            draw.text((card_x + 64, cy + 48 + j * 20), f"• {line}", fill=DARK, font=body_f)

    draw.rectangle((0, H - 80, W, H), fill=NAVY)
    draw.text(
        (80, H - 55),
        "초록 체크 = Compile OK · Stage 1 완료 = Deploy + mint(0.001 ETH) + revert 테스트까지",
        fill=WHITE,
        font=footer_f,
    )

    img.save(out, "PNG", optimize=True)
    print(f"Saved: {out}")


if __name__ == "__main__":
    IMAGES.mkdir(parents=True, exist_ok=True)
    generate_session1_1_1_instructor_env()
    generate_session2_1_3_compile_deploy()
    generate_session2_2_1_stage_0_1()
