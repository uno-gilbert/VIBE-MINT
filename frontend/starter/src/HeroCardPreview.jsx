import { useEffect, useMemo, useRef, useState } from "react";
import { getHeroTraits } from "./heroCardTraits.js";
import { heroImageUrl } from "./heroImages.js";

const CARD_W = 772;
const CARD_H = 1200;

const INK = "#2a1e12";
const GOLD = "#8a6228";
const HIGHLIGHT = "#d8c498";

function drawEngravedText(ctx, text, x, y, fontSize, align = "left") {
  ctx.font = `700 ${fontSize}px Georgia, "Times New Roman", serif`;
  ctx.textAlign = align;
  ctx.textBaseline = "middle";

  const offsets = [
    [2, 0],
    [-2, 0],
    [0, 2],
    [0, -2],
  ];
  for (const [ox, oy] of offsets) {
    ctx.fillStyle = INK;
    ctx.fillText(text, x + ox, y + oy);
  }
  ctx.fillStyle = GOLD;
  ctx.fillText(text, x, y);
  ctx.fillStyle = HIGHLIGHT;
  ctx.globalAlpha = 0.35;
  ctx.fillText(text, x - 1, y - 1);
  ctx.globalAlpha = 1;
}

function composeCard(ctx, img, traits) {
  ctx.clearRect(0, 0, CARD_W, CARD_H);
  ctx.drawImage(img, 0, 0, CARD_W, CARD_H);

  drawEngravedText(ctx, String(traits.score), 88, 72, 52, "center");
  drawEngravedText(ctx, traits.gold, CARD_W / 2, 68, 40, "center");
  drawEngravedText(ctx, traits.ability, CARD_W / 2, CARD_H - 92, 44, "center");
}

export function HeroCardPreview({ tokenId, compact = false }) {
  const canvasRef = useRef(null);
  const [status, setStatus] = useState("loading");
  const traits = useMemo(() => getHeroTraits(tokenId), [tokenId]);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas || tokenId === undefined || tokenId === null) return;

    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    setStatus("loading");
    const img = new Image();
    img.crossOrigin = "anonymous";
    img.onload = () => {
      composeCard(ctx, img, traits);
      setStatus("ready");
    };
    img.onerror = () => setStatus("error");
    img.src = heroImageUrl(traits.heroIndex);

    return () => {
      img.onload = null;
      img.onerror = null;
    };
  }, [tokenId, traits.heroIndex, traits.score, traits.gold, traits.ability]);

  return (
    <div className={`hero-card${compact ? " hero-card--compact" : ""}`}>
      <canvas
        ref={canvasRef}
        width={CARD_W}
        height={CARD_H}
        className="hero-card__canvas"
        aria-label={`VibeMint Hero #${traits.tokenId} — ${traits.hero}`}
      />
      {status === "loading" && <p className="hero-card__hint">카드 불러오는 중…</p>}
      {status === "error" && (
        <p className="hero-card__hint error">
          이미지를 불러오지 못했습니다. 네트워크 또는 VITE_NFT_IMAGE_BASE를 확인하세요.
        </p>
      )}
      <div className="hero-card__meta">
        <strong>
          #{traits.tokenId} — {traits.hero}
        </strong>
        <ul className="hero-card__traits">
          <li>
            <span>점수</span> {traits.score}
          </li>
          <li>
            <span>골드 조건</span> {traits.gold}
          </li>
          <li>
            <span>능력</span> {traits.ability}
          </li>
        </ul>
        <p className="hero-card__note">
          DApp UI 미리보기 — Etherscan·MetaMask에는 기본 카드 이미지가 표시됩니다.
        </p>
      </div>
    </div>
  );
}
