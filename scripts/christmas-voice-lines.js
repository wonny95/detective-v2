// The Christmas star case's recorded lines: the detective (Higgsfield MiniMax Grady), Sgt. Badger (Fraser) and Ella
// (Petra, no emotion); the others are still read by the browser's voice. Pulled from CHRISTMAS_CASE in index.html so the recordings and the
// game cannot drift apart. Lines with the same words share one recording (copied per file).
// Run from the project folder: node scripts/christmas-voice-lines.js  -> JSON [{ voice, file, en, files:[…] }] on stdout
const fs = require('fs'), path = require('path'), os = require('os');
const html = fs.readFileSync('index.html', 'utf8').replace(/\r\n/g, '\n');
const start = html.indexOf('const CHRISTMAS_CASE = {');
let depth = 0, end = html.indexOf('{', start);
for(let k = end; k < html.length; k++){
  if(html[k] === '{') depth++;
  else if(html[k] === '}' && !--depth){ end = k; break; }
}
const tmp = path.join(os.tmpdir(), 'christmas-case.js');
fs.writeFileSync(tmp, html.slice(start, end + 1).replace('const CHRISTMAS_CASE =', 'module.exports ='));
const P = require(tmp);

const DIR = 'audio/christmas/';
const out = [];
const add = (voice, file, en) => { if(en && /[a-z]/i.test(en)) out.push({ voice, file:DIR + file + '.mp3', en }); };
// the people recorded so far and their voices (people[].audio: <id>-<key>.mp3)
const VOICES = { badger:'Fraser', ella:'Petra' };
// a line in a list: the detective's (det), or a recorded person's (who, else the list's own speaker)
const line = (l, own) => {
  if(!l || l.think) return;
  const who = l.who || own;
  if(l.det) add('Grady', `detective-${l.key}`, l.en);
  else if(VOICES[who]) add(VOICES[who], `${who}-${l.key}`, l.en);
};
for(const [id, p] of Object.entries(P.people)){
  [].concat(p.hello || []).forEach(l => line(l, id));
  (p.questions || []).forEach(q => add('Grady', `detective-${id}-${q.id}`, q.en));
  (p.actions || []).forEach(a => {
    if(a.say !== false) add('Grady', `detective-${id}-act-${a.id}`, a.en);
    if(VOICES[id] && !a.lines) add(VOICES[id], `${id}-${a.id}`, a.answer);
    (a.lines || []).forEach(l => line(l, id));
  });
  Object.values(p.after || {}).forEach(b => b.lines.forEach(l => line(l, id)));
  if(VOICES[id]) Object.entries(p.answers || {}).forEach(([q, en]) => add(VOICES[id], `${id}-${q}`, en));
}
// what the detective says of each thing looked at or picked up (clue.audio: detective-<place>-<n>)
P.places.forEach(pl => pl.clues.forEach((c, i) => c.take ? (c.lines || []).forEach(l => line(l)) : add('Grady', `detective-${pl.id}-${i}`, c.en)));
Object.entries(P.items).forEach(([id, it]) => add('Grady', `detective-item-${id}`, it.en));
P.thoughts.forEach(t => line({ det:true, ...t.line }));
// the deduction board, by question number (DEDUCE_RECORDED): question, the reply when right, the hint; one miss
P.deduce.qs.forEach((q, i) => { add('Grady', `deduce/q${i + 1}`, q.q); add('Grady', `deduce/r${i + 1}`, q.right); add('Grady', `deduce/h${i + 1}`, q.hint); });
add('Grady', 'deduce/miss', P.deduce.miss.en);
// the questioning and the return
(P.ending.intro || []).forEach(l => line(l));
P.ending.script.forEach(s => {
  if(s.ask) add('Grady', `detective-${s.key}`, s.en);
  [s.miss, ...(s.lines || []), ...(s.hit || [])].forEach(l => line(l));
});
P.ending.handoff.forEach(r => [r.go, r.open, ...(r.before || []), ...(r.lines || [])].forEach(l => line(l, r.to)));
// one recording per voice and sentence
const byText = new Map();
out.forEach(l => { const k = l.voice + '|' + l.en; if(!byText.has(k)) byText.set(k, { voice:l.voice, file:l.file, en:l.en, files:[] }); byText.get(k).files.push(l.file); });
console.log(JSON.stringify([...byText.values()], null, 1));
