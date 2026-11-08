// The violin case's detective lines (the detective's voice only; the others are still read by the browser's voice):
// every line the detective says aloud, with the file it is saved as, pulled from VIOLIN_CASE in index.html so the
// recordings and the game cannot drift apart. Lines with the same words share one recording (copied per file).
// Run from the project folder: node scripts/violin-detective-lines.js  -> JSON [{ file, en, files:[…] }] on stdout
const fs = require('fs'), path = require('path'), os = require('os');
const html = fs.readFileSync('index.html', 'utf8').replace(/\r\n/g, '\n');
const start = html.indexOf('const VIOLIN_CASE = {');
let depth = 0, end = html.indexOf('{', start);
for(let k = end; k < html.length; k++){
  if(html[k] === '{') depth++;
  else if(html[k] === '}' && !--depth){ end = k; break; }
}
const tmp = path.join(os.tmpdir(), 'violin-case.js');
fs.writeFileSync(tmp, html.slice(start, end + 1).replace('const VIOLIN_CASE =', 'module.exports ='));
const P = require(tmp);

const DIR = 'audio/violin/';
const out = [];
const add = (file, en) => { if(en) out.push({ file:DIR + file + '.mp3', en }); };
const det = l => l?.det && !l.think && add(`detective-${l.key}`, l.en);
for(const [id, p] of Object.entries(P.people)){
  [].concat(p.hello || []).forEach(det);
  (p.questions || []).forEach(q => add(`detective-${id}-${q.id}`, q.en));
  (p.actions || []).forEach(a => { if(a.say !== false) add(`detective-${id}-act-${a.id}`, a.en); (a.lines || []).forEach(det); });
  Object.values(p.after || {}).forEach(b => b.lines.forEach(det));
}
// what the detective says of each thing looked at (clue.audio: detective-<place>-<n>); things picked up say their lines
P.places.forEach(pl => pl.clues.forEach((c, i) => c.take ? c.lines.forEach(l => add(`detective-${l.key}`, l.en)) : add(`detective-${pl.id}-${i}`, c.en)));
P.thoughts.forEach(t => add(`detective-${t.line.key}`, t.line.en));
add(`detective-${P.compare.line.key}`, P.compare.line.en);
// the deduction board, by question number (DEDUCE_RECORDED): question, the reply when right, the hint; one miss
P.deduce.qs.forEach((q, i) => { add(`deduce/q${i + 1}`, q.q); add(`deduce/r${i + 1}`, q.right); add(`deduce/h${i + 1}`, q.hint); });
add('deduce/miss', P.deduce.miss.en);
// the questioning and the return
P.ending.intro.forEach(det);
P.ending.script.forEach(s => { if(s.ask) add(`detective-${s.key}`, s.en); (s.lines || []).forEach(det); (s.hit || []).forEach(det); });
P.ending.handoff.forEach(r => { det(r.open); (r.before || []).forEach(det); (r.lines || []).forEach(det); });
// one recording per sentence
const byText = new Map();
out.forEach(l => { const k = l.en; if(!byText.has(k)) byText.set(k, { file:l.file, en:l.en, files:[] }); byText.get(k).files.push(l.file); });
console.log(JSON.stringify([...byText.values()], null, 1));
