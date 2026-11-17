// Local dev server for 숲속 탐정 — no dependencies.
// --review serves a separate snapshot without reloading; --test serves the working files with live reload.
//   node server.js            → http://localhost:5173
//   node server.js --review   → http://localhost:5176 (run scripts/update-review.js first)
//   node server.js --test     → http://localhost:5177
const http = require('http');
const fs = require('fs');
const path = require('path');

const REVIEW = process.argv.includes('--review');
const TEST = process.argv.includes('--test');
if (REVIEW && TEST) throw new Error('Choose either --review or --test.');
const ROOT = REVIEW ? path.join(__dirname, '.preview', 'review') : __dirname;
const PORT = Number(process.env.PORT) || (REVIEW ? 5176 : TEST ? 5177 : 5173);
if (REVIEW && !fs.existsSync(path.join(ROOT, 'index.html'))) {
  throw new Error('Create the review snapshot first: node scripts/update-review.js');
}
const TYPES = {
  '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8', '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg',
  '.webp': 'image/webp', '.mp3': 'audio/mpeg', '.wav': 'audio/wav', '.ogg': 'audio/ogg', '.woff2': 'font/woff2'
};
const RELOAD_SNIPPET = `<script>new EventSource('/__reload').onmessage = () => location.reload();</script>`;

const clients = new Set();

http.createServer((req, res) => {
  const url = decodeURIComponent(req.url.split('?')[0]);

  if (url === '/__reload') {
    // A tab left open from the old live server can reconnect here: 204 stops EventSource reconnecting.
    if (REVIEW) { res.writeHead(204).end(); return; }
    res.writeHead(200, { 'Content-Type': 'text/event-stream', 'Cache-Control': 'no-cache', Connection: 'keep-alive' });
    res.write(': connected\n\n');
    clients.add(res);
    req.on('close', () => clients.delete(res));
    return;
  }

  let file = path.join(ROOT, url === '/' ? 'index.html' : url);
  if (!file.startsWith(ROOT)) { res.writeHead(403).end('Forbidden'); return; }
  if (fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file, 'index.html');

  fs.readFile(file, (err, data) => {
    if (err) { res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' }).end('Not found: ' + url); return; }
    const ext = path.extname(file).toLowerCase();
    const headers = { 'Content-Type': TYPES[ext] || 'application/octet-stream', 'Cache-Control': 'no-store' };
    if (ext === '.html' && !REVIEW) {
      data = Buffer.from(data.toString('utf8').replace('</body>', RELOAD_SNIPPET + '\n</body>'));
    }
    res.writeHead(200, headers).end(data);
  });
}).listen(PORT, () => console.log(`Detective ${REVIEW ? 'review (no auto reload)' : TEST ? 'test' : 'dev'} server: http://localhost:${PORT}`));

// Debounced reload on any change in this folder (editors often write a file in several steps).
let timer;
if (!REVIEW) fs.watch(ROOT, { recursive: true }, (_event, name) => {
  // .git changes whenever the story worktree (Codex) commits or checks its status: not a change to the game
  if (!name || name.startsWith('.git') || name.startsWith('.claude') || name.startsWith('.preview') || name.startsWith('node_modules')) return;
  clearTimeout(timer);
  timer = setTimeout(() => {
    console.log('changed:', name, '→ reload');
    for (const c of clients) c.write('data: reload\n\n');
  }, 120);
});
