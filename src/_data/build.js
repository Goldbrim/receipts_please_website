import { createHash } from "node:crypto";
import { readFileSync } from "node:fs";

const assetHash = createHash("sha256");
for (const path of [
  "../styles.css",
  "../assets/screenshots/home.webp",
  "../assets/screenshots/receipt-search.webp",
  "../assets/screenshots/spending-categories.webp",
  "../assets/screenshots/item-prices.webp",
]) {
  assetHash.update(readFileSync(new URL(path, import.meta.url)));
}

export default {
  year: new Date().getFullYear(),
  assetVersion: assetHash.digest("hex").slice(0, 12),
};
