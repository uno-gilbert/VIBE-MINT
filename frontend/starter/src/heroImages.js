/** Hero card JPEG base URL — dev serves repo assets via vite plugin. Etherscan 호환용. */
const GITHUB_BASE =
  "https://raw.githubusercontent.com/uno-gilbert/VIBE-MINT/main/assets/nft/images";

export const HERO_IMAGE_BASE =
  import.meta.env.VITE_NFT_IMAGE_BASE ??
  (import.meta.env.DEV ? "/nft-images" : GITHUB_BASE);

export const HERO_COUNT = 53;

export function heroImageUrl(heroIndex) {
  return `${HERO_IMAGE_BASE}/${heroIndex % HERO_COUNT}.jpg`;
}
