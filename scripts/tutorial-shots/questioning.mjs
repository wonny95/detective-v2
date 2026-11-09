// The 심문해요 tutorial picture (tut-7): the motion mockup's own questioning (a made-up claim, the lamp photo picked, the whole screen), shot
// at 3x from the headless Chrome on :9333 with the dev server on 5173. usage: node questioning.mjs <out.png> (then questioning.py)
import fs from 'node:fs';
const out = process.argv[2];
const list = await (await fetch('http://127.0.0.1:9333/json/list')).json();
let page = list.find(t => t.type === 'page');
const ws = new WebSocket(page.webSocketDebuggerUrl);
await new Promise(r => ws.onopen = r);
let id = 0; const wait = new Map();
ws.onmessage = e => { const m = JSON.parse(e.data); if(m.id && wait.has(m.id)){ wait.get(m.id)(m); wait.delete(m.id); } };
const send = (method, params = {}) => new Promise(r => { const i = ++id; wait.set(i, r); ws.send(JSON.stringify({ id:i, method, params })); });
await send('Emulation.setDeviceMetricsOverride', { width:1000, height:900, deviceScaleFactor:3, mobile:false });
await send('Page.navigate', { url:'http://127.0.0.1:5173/design/tutorial-motion.html' });
await new Promise(r => setTimeout(r, 4000));
const js = `(async () => {
  const wait = ms => new Promise(r => setTimeout(r, ms));
  const f = document.getElementById('game'), d = f.contentDocument;
  for(let i = 0; i < 6; i++){ [...d.querySelectorAll('button')].find(b => b.textContent.trim() === '다음' && b.offsetParent)?.click(); await wait(500); }
  // the moment a photo is picked, the whole screen at once: the gauge, the claim, the person, the drawer with the lamp
  // photo and 내밀기 (the camera stepped back so far that the full phone screen fits; the room fills the sides)
  for(let i = 0; i < 400; i++){ const p = d.querySelector('.tdemo .drawer-pick'); if(p && !p.hidden) break; await wait(25); }
  await wait(450);
  const box = d.querySelector('.tdemo'), stage = box.querySelector('.tdemo-stage'), z = box.clientHeight / 844, w = box.clientWidth / z;
  stage.style.transition = 'none'; stage.style.transform = 'scale(' + z + ') translate(' + (w - 390) / 2 + 'px, 0px)';
  await wait(120);
  const fr = f.getBoundingClientRect(), b = d.querySelector('.tdemo').getBoundingClientRect();
  return [d.querySelector('#tutTitle').textContent, fr.left + b.left, fr.top + b.top, fr.left + b.right, fr.top + b.bottom];
})()`;
const r = await send('Runtime.evaluate', { expression:js, awaitPromise:true, returnByValue:true });
const v = r.result?.result?.value; console.log(JSON.stringify(v ?? r));
const shot = await send('Page.captureScreenshot', { format:'png' });
fs.writeFileSync(out, Buffer.from(shot.result.data, 'base64'));
fs.writeFileSync(out + '.json', JSON.stringify(v));
ws.close();
