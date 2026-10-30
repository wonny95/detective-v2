import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const destination = path.join(root, 'sites', 'detective-demo', 'source');
const html = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
const assets = [...new Set([...html.matchAll(/(?:assets|audio)\/[A-Za-z0-9_./-]+\.(?:png|jpg|webp|mp3)/g)].map(match => match[0]))];
for (const asset of assets) {
  if (!fs.statSync(path.join(root, asset)).isFile()) throw new Error(`Missing source asset: ${asset}`);
}
fs.mkdirSync(destination, { recursive: true });
fs.writeFileSync(path.join(destination, 'index.html'), html);
for (const asset of assets) {
  const target = path.join(destination, asset);
  fs.mkdirSync(path.dirname(target), { recursive: true });
  fs.copyFileSync(path.join(root, asset), target);
}
console.log(`Copied the current game and ${assets.length} referenced assets into the demo source.`);
