import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

const dir = path.dirname(fileURLToPath(import.meta.url));
const nftImagesDir = path.resolve(dir, "../../assets/nft/images");

function nftImagesPlugin() {
  return {
    name: "nft-images",
    configureServer(server) {
      server.middlewares.use("/nft-images", (req, res, next) => {
        const name = path.basename(req.url ?? "");
        if (!/^\d+\.(webp|png|jpg|jpeg)$/.test(name)) {
          next();
          return;
        }
        const filePath = path.join(nftImagesDir, name);
        if (!fs.existsSync(filePath)) {
          res.statusCode = 404;
          res.end("Not found");
          return;
        }
        const ext = path.extname(name).toLowerCase();
        const types = {
          ".webp": "image/webp",
          ".png": "image/png",
          ".jpg": "image/jpeg",
          ".jpeg": "image/jpeg",
        };
        res.setHeader("Content-Type", types[ext] ?? "application/octet-stream");
        fs.createReadStream(filePath).pipe(res);
      });
    },
  };
}

export default defineConfig({
  plugins: [react(), nftImagesPlugin()],
  server: {
    fs: { allow: [path.resolve(dir, "../..")] },
  },
});
