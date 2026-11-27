// Local dev server for 숲속 탐정 — no dependencies.
// --review serves a separate snapshot without reloading; --test serves the working files with live reload; --design serves
// the working files too, for the user to look at UI mockups (design/*.html) apart from the game (user request 2026-11-26).
//   node server.js            → http://localhost:5173
//   node server.js --review   → http://localhost:5176 (run scripts/update-review.js first)
//   node server.js --test     → http://localhost:5177
//   node server.js --design   → http://localhost:5179 (opens on the list of mockups)
const http = require('http');
const fs = require('fs');
const path = require('path');

const REVIEW = process.argv.includes('--review');
const TEST = process.argv.includes('--test');
const DESIGN = process.argv.includes('--design');
if (REVIEW + TEST + DESIGN > 1) throw new Error('Choose one of --review, --test or --design.');
const ROOT = REVIEW ? path.join(__dirname, '.preview', 'review') : __dirname;
const PORT = Number(process.env.PORT) || (REVIEW ? 5176 : TEST ? 5177 : DESIGN ? 5179 : 5173);
if (REVIEW && !fs.existsSync(path.join(ROOT, 'index.html'))) {
  throw new Error('Create the review snapshot first: node scripts/update-review.js');
}
const TYPES = {
  '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8', '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg',
  '.webp': 'image/webp', '.mp3': 'audio/mpeg', '.wav': 'audio/wav', '.ogg': 'audio/ogg', '.woff2': 'font/woff2'
};
const RELOAD_SNIPPET = `<script>new EventSource('/__reload').onmessage = () => location.reload();</script>`;
// the mockup server's way back from a mockup to the list: a small pill fixed at the top left, over everything on the page
const BACK_TO_LIST = `<a href="/" id="__backToList" title="시안 목록으로" style="position:fixed;z-index:2147483647;left:12px;top:12px;display:inline-flex;align-items:center;gap:4px;padding:7px 13px 7px 10px;border-radius:999px;background:#FFF8EC;color:#5B3F2A;border:1.5px solid #C9A77F;box-shadow:0 3px 10px rgba(60,36,10,.18);font:600 13px/1 system-ui,'Malgun Gothic',sans-serif;text-decoration:none">‹ 시안 목록</a>`;

const esc = t => t.replace(/&/g, '&amp;').replace(/</g, '&lt;');
function designList() {
  const dir = path.join(ROOT, 'design'), today = new Date().toDateString();
  const items = fs.readdirSync(dir).filter(n => n.endsWith('.html')).map(n => {
    const html = fs.readFileSync(path.join(dir, n), 'utf8'), t = fs.statSync(path.join(dir, n)).mtime;
    const title = (html.match(/<title>([^<]*)<\/title>/) || [, n])[1].trim();
    // 3: the cast and places overview, a reference of its own, not a case plan (user request 2026-11-27)
    const kind = n === 'cast-and-places.html' ? 3 : /시안/.test(title) ? 0 : /학습|기준표/.test(title) ? 2 : 1;
    return { n, title, t, kind };
  }).sort((a, b) => b.t - a.t);
  const when = t => t.toDateString() === today ? `오늘 ${t.getHours() < 12 ? '오전' : '오후'} ${t.getHours() % 12 || 12}:${String(t.getMinutes()).padStart(2, '0')}`
    : `${t.getMonth() + 1}월 ${t.getDate()}일`;
  const group = (k, h) => { const g = items.filter(i => i.kind === k); return g.length ? `<h2>${h} <small>${g.length}</small></h2><div class="grid">${g.map(i =>
    `<a class="card${i.t.toDateString() === today ? ' new' : ''}" href="/design/${encodeURIComponent(i.n)}"><b>${esc(i.title)}</b><span>${when(i.t)}${i.t.toDateString() === today ? ' · 오늘 고침' : ''}</span><code>${esc(i.n)}</code></a>`).join('')}</div>` : ''; };
  return `<!doctype html><html lang="ko"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>시안 목록</title><style>
@font-face{font-family:"Paperlogy";src:url("/assets/fonts/Paperlogy-4Regular.woff2") format("woff2");font-weight:400}@font-face{font-family:"Paperlogy";src:url("/assets/fonts/Paperlogy-7Bold.woff2") format("woff2");font-weight:700}
body{margin:0;padding:24px 28px 48px;font:15px/1.45 "Paperlogy",system-ui,sans-serif;background:#F3E7CF;color:#4A3628}
h1{margin:0 0 4px;font-size:26px}p{margin:0 0 8px;color:#7D6A58}
h2{margin:28px 0 12px;font-size:19px}h2 small{font-size:14px;color:#9A8670}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:12px}
.card{display:flex;flex-direction:column;gap:4px;padding:14px 16px;border-radius:14px;background:#FFFBF2;border:1.5px solid #D9C4A2;color:inherit;text-decoration:none;box-shadow:0 2px 6px rgba(60,40,20,.08)}
.card:hover{border-color:#C96F86;translate:0 -2px}
.card.new{border-color:#C96F86;background:#FFF4F2}
.card b{font-size:16px;font-weight:700;line-height:1.35}
.card span{font-size:13px;color:#7D6A58}.card.new span{color:#B23C55}
.card code{font-size:11.5px;color:#A8957C}
</style><h1>시안 목록</h1><p>최근에 고친 것이 앞에 와요. 분홍 테두리는 오늘 고친 것이에요.</p>
${group(3, '인물과 장소')}${group(0, 'UI 시안')}${group(1, '사건 기획서')}${group(2, '기준표 · 학습 기획')}${RELOAD_SNIPPET}</html>`;
}

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

  // the mockup server opens on a list of design/*.html by kind (UI mockups, case plans, references), each by its <title>
  // and when it last changed, newest first (user request 2026-11-26: the bare file names were hard to tell apart)
  if (DESIGN && url === '/') { res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'no-store' }).end(designList()); return; }
  let file = path.join(ROOT, url === '/' ? 'index.html' : url);
  if (!file.startsWith(ROOT)) { res.writeHead(403).end('Forbidden'); return; }
  if (fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file, 'index.html');

  fs.readFile(file, (err, data) => {
    if (err) { res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' }).end('Not found: ' + url); return; }
    const ext = path.extname(file).toLowerCase();
    const headers = { 'Content-Type': TYPES[ext] || 'application/octet-stream', 'Cache-Control': 'no-store' };
    if (ext === '.html' && !REVIEW) {
      // a mockup page on the mockup server gets a button back to the list (user request 2026-11-27)
      const back = DESIGN && url.startsWith('/design/') ? BACK_TO_LIST : '';
      let html = data.toString('utf8');
      html = html.includes('</body>') ? html.replace('</body>', back + RELOAD_SNIPPET + '\n</body>') : html + back + RELOAD_SNIPPET;
      data = Buffer.from(html);
    }
    res.writeHead(200, headers).end(data);
  });
}).listen(PORT, () => console.log(`Detective ${REVIEW ? 'review (no auto reload)' : TEST ? 'test' : DESIGN ? 'design (mockups)' : 'dev'} server: http://localhost:${PORT}`));

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
