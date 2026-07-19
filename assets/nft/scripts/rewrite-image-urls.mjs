#!/usr/bin/env node
/**
 * Rewrite metadata/*.image for Pinata Dedicated Gateway (VibeMint workshop).
 *
 * Usage (from assets/nft/):
 *   IMAGES_CID="bafy..." \
 *   GATEWAY="https://YOUR_GATEWAY.mypinata.cloud/ipfs" \
 *   node scripts/rewrite-image-urls.mjs
 *
 * GATEWAY must be your Pinata Dedicated Gateway + "/ipfs" (no trailing slash required).
 * Do not use https://gateway.pinata.cloud — use your own *.mypinata.cloud host.
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const nftRoot = path.resolve(__dirname, "..");
const metadataDir = path.join(nftRoot, "metadata");

const imagesCid = (process.env.IMAGES_CID || "").trim();
const gatewayRaw = (process.env.GATEWAY || "").trim();

if (!imagesCid || !gatewayRaw) {
  console.error("IMAGES_CID and GATEWAY are required (Pinata Dedicated Gateway).");
  console.error("");
  console.error("Example:");
  console.error(
    '  IMAGES_CID="bafy..." GATEWAY="https://coral-xxx.mypinata.cloud/ipfs" node scripts/rewrite-image-urls.mjs',
  );
  console.error("");
  console.error("Copy GATEWAY from Pinata → Gateways (https://app.pinata.cloud/), then append /ipfs.");
  process.exit(1);
}

const gateway = gatewayRaw.replace(/\/$/, "");

if (!gateway.includes("mypinata.cloud") && !gateway.includes("/ipfs")) {
  console.warn(
    "Warning: GATEWAY usually looks like https://YOUR_NAME.mypinata.cloud/ipfs",
  );
}

const files = fs
  .readdirSync(metadataDir)
  .filter((name) => /^\d+$/.test(name))
  .sort((a, b) => Number(a) - Number(b));

if (files.length === 0) {
  console.error(`No metadata files found in ${metadataDir}`);
  process.exit(1);
}

let updated = 0;
for (const name of files) {
  const filePath = path.join(metadataDir, name);
  const raw = fs.readFileSync(filePath, "utf8");
  const json = JSON.parse(raw);
  const nextImage = `${gateway}/${imagesCid}/${name}.jpg`;
  if (json.image === nextImage) continue;
  json.image = nextImage;
  fs.writeFileSync(filePath, `${JSON.stringify(json, null, 2)}\n`);
  updated += 1;
}

console.log(`Updated ${updated}/${files.length} metadata files.`);
console.log(`image pattern: ${gateway}/${imagesCid}/{id}.jpg`);
