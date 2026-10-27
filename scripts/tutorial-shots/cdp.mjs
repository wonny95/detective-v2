// Drive the headless Chrome on :9333 (one page kept between runs).
// usage: node cdp.mjs steps.json   steps: [{nav:url}|{eval:js}|{wait:ms}|{shot:file}]
import fs from 'node:fs';
const steps = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const list = await (await fetch('http://127.0.0.1:9333/json/list')).json();
let page = list.find(t => t.type === 'page');
if(!page) page = await (await fetch('http://127.0.0.1:9333/json/new?about:blank', { method:'PUT' })).json();
const ws = new WebSocket(page.webSocketDebuggerUrl);
await new Promise(r => ws.onopen = r);
let id = 0; const wait = new Map();
ws.onmessage = e => { const m = JSON.parse(e.data); if(m.id && wait.has(m.id)){ wait.get(m.id)(m); wait.delete(m.id); } };
const send = (method, params = {}) => new Promise(r => { const i = ++id; wait.set(i, r); ws.send(JSON.stringify({ id:i, method, params })); });
await send('Emulation.setDeviceMetricsOverride', { width:390, height:844, deviceScaleFactor:3, mobile:true });
await send('Emulation.setTouchEmulationEnabled', { enabled:true });
for(const s of steps){
  if(s.nav){ await send('Page.navigate', { url:s.nav }); await new Promise(r => setTimeout(r, s.after ?? 2500)); }
  if(s.eval){ const r = await send('Runtime.evaluate', { expression:`(async()=>{${s.eval}})()`, awaitPromise:true, returnByValue:true }); console.log(JSON.stringify(r.result?.result?.value ?? r.result?.exceptionDetails?.exception?.description ?? r)); }
  if(s.wait) await new Promise(r => setTimeout(r, s.wait));
  if(s.shot){ const r = await send('Page.captureScreenshot', { format:'png' }); fs.writeFileSync(s.shot, Buffer.from(r.result.data, 'base64')); console.log('shot', s.shot); }
}
ws.close();
