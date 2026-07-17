import manifest from "./nft-manifest.json";

const GOLD_CONDITIONS = [
  "①",
  "①①",
  "①①①①",
  "③③",
  "②",
  "③④⑤",
  "≡≡",
  "Σ9",
  "④³|⑤³",
];

const ABILITIES = ["🃟1", "🃟2", "🃟3∞", "⚔", "🛡", "—"];

/** Deterministic pseudo-random from tokenId (same token → same traits in UI). */
function mulberry32(seed) {
  let a = seed >>> 0;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = Math.imul(a ^ (a >>> 15), a | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

/** @param {number} tokenId */
export function getHeroTraits(tokenId) {
  const id = Math.max(0, Math.floor(tokenId));
  const rng = mulberry32(id * 2654435761 + 1013904223);
  const heroIndex = id % manifest.length;
  const hero = manifest[heroIndex]?.hero ?? `Hero #${heroIndex}`;

  return {
    tokenId: id,
    heroIndex,
    hero,
    score: Math.floor(rng() * 6),
    gold: GOLD_CONDITIONS[Math.floor(rng() * GOLD_CONDITIONS.length)],
    ability: ABILITIES[Math.floor(rng() * ABILITIES.length)],
  };
}
