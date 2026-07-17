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


def cover_crop_image(source: Image.Image, target_w: int, target_h: int) -> Image.Image:
    src = source.convert("RGB")
    src_ratio = src.width / src.height
    target_ratio = target_w / target_h
    if src_ratio > target_ratio:
        new_h = target_h
        new_w = int(new_h * src_ratio)
    else:
        new_w = target_w
        new_h = int(new_w / src_ratio)
    resized = src.resize((new_w, new_h), Image.Resampling.LANCZOS)
    left = (new_w - target_w) // 2
    top = (new_h - target_h) // 2
    return resized.crop((left, top, left + target_w, top + target_h))


def paste_site_tile(img, draw, photo_path, box, period, title, lines, fonts):
    title_f, body_f, tag_f = fonts
    x0, y0, x1, y1 = box
    thumb_h = 140
    rounded_rect(draw, box, 12, WHITE, BORDER, 2)
    if photo_path.exists():
        shot = cover_crop_image(Image.open(photo_path), x1 - x0 - 4, thumb_h)
        img.paste(shot, (x0 + 2, y0 + 2))
        draw.rectangle((x0 + 2, y0 + 2, x1 - 2, y0 + 2 + thumb_h), outline=BORDER, width=1)
    text_y = y0 + thumb_h + 10
    draw.text((x0 + 10, text_y), period, fill=BLUE, font=tag_f)
    draw.text((x0 + 10, text_y + 18), title, fill=NAVY, font=title_f)
    line_y = text_y + 42
    for line in lines:
        draw.text((x0 + 10, line_y), line, fill=DARK, font=body_f)
        line_y += 18


def generate_session1_1_1_instructor_env():
    """강사 소개 · GitHub QR — 경력별 공식 사이트 캡처."""
    out = IMAGES / "session1-1-1-instructor-env.png"
    qr_path = ROOT.parent / "images" / "vibe-mint-github-qr.png"
    logos = IMAGES / "career-logos"
    if not qr_path.exists():
        raise FileNotFoundError(f"Missing QR: {qr_path}")

    img = Image.new("RGB", (W, H), WHITE)
    draw = ImageDraw.Draw(img)

    title_f = load_font(52, bold=True)
    sub_f = load_font(26)
    card_title_f = load_font(28, bold=True)
    body_f = load_font(16)
    small_f = load_font(18)
    tag_f = load_font(14, bold=True)
    node_title_f = load_font(17, bold=True)
    footer_f = load_font(26, bold=True)

    draw.text((80, 48), "VibeMint 워크숍 · 1차시-1", fill=GRAY, font=sub_f)
    draw.text((80, 92), "강사 소개 · 수업 환경", fill=NAVY, font=title_f)
    draw.text((80, 168), "강사 경력 · GitHub 실습 저장소", fill=GRAY, font=sub_f)

    left = (80, 230, 920, 960)
    rounded_rect(draw, left, 20, CARD_BG, BORDER, 2)
    draw.text((left[0] + 36, left[1] + 28), "1. 강사 소개", fill=NAVY, font=card_title_f)
    draw.text((left[0] + 36, left[1] + 68), "경력 하이라이트 (공식 사이트)", fill=GRAY, font=small_f)

    careers = [
        (logos / "01-blizzard-site.png", "2000s", "Blizzard · Battle.net", ["디아블로 옥션 하우스", "게임 아이템 경제"]),
        (logos / "02-smilegate-site.png", "2010s", "Smilegate", ["모바일 게임 플랫폼", "대규모 유저 서비스"]),
        (logos / "03-nsuslab-site.png", "Blockchain", "NSUSLAB · Anserslab", ["블록체인 프로젝트", "iGaming 개발"]),
        (logos / "04-poker-site.png", "Poker", "GGPoker · WSOP", ["포커칩 → 크립토 충전", "블록체인 PM 총괄"]),
        (logos / "05-hellolive-site.png", "Now", "HelloLive · 개발 이사", ["AI 활용 프로젝트", "Intent → Ship"]),
    ]

    tile_w = 246
    tile_h = 230
    gap = 14
    start_x = left[0] + 36
    start_y = left[1] + 108
    fonts = (node_title_f, body_f, tag_f)

    # 1행: Blizzard · Smilegate · NSUSLAB
    for col, idx in enumerate([0, 1, 2]):
        photo, period, title, lines = careers[idx]
        x = start_x + col * (tile_w + gap)
        y = start_y
        paste_site_tile(img, draw, photo, (x, y, x + tile_w, y + tile_h), period, title, lines, fonts)

    # 2행: Poker · HelloLive (가운데 정렬)
    row2_y = start_y + tile_h + gap
    row2_width = 2 * tile_w + gap
    row2_x = start_x + (3 * (tile_w + gap) - row2_width) // 2
    for col, idx in enumerate([3, 4]):
        photo, period, title, lines = careers[idx]
        x = row2_x + col * (tile_w + gap)
        paste_site_tile(
            img, draw, photo, (x, row2_y, x + tile_w, row2_y + tile_h), period, title, lines, fonts
        )

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
