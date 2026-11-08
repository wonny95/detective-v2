// The violin case's recording script: every line the characters say aloud, by speaker, with the file it will be saved
// as and the face they make (mood), pulled from VIOLIN_CASE in index.html so the script and the game cannot drift apart
// (as scripts/umbrella-recording-script.js). The detective's lines are already recorded (audio/violin/README.md).
// Run from the project folder: node scripts/violin-recording-script.js  -> design/case-04-missing-violin-recording.md
const fs = require('fs'), path = require('path'), os = require('os');
const html = fs.readFileSync('index.html', 'utf8').replace(/\r\n/g, '\n');
const start = html.indexOf('const VIOLIN_CASE = {');
let depth = 0, end = html.indexOf('{', start);
for(let k = end; k < html.length; k++){
  if(html[k] === '{') depth++;
  else if(html[k] === '}' && !--depth){ end = k; break; }
}
const tmp = path.join(os.tmpdir(), 'violin-case-script.js');
fs.writeFileSync(tmp, html.slice(start, end + 1).replace('const VIOLIN_CASE =', 'module.exports ='));
const P = require(tmp);

const DIR = 'audio/violin/';
const NAMES = { tara:'타라', owen:'오웬', ivo:'이보', momo:'모모', pip:'핍', badger:'오소리 경사' };
const lines = Object.fromEntries(Object.keys(NAMES).map(id => [id, []]));
const MOOD = { nervous:'당황', sad:'슬픔(고개 숙임)' };
const add = (who, key, scene, l) => lines[who].push({ file:`${DIR}${who}-${key}.mp3`, scene, en:l.en, ko:l.ko, mood:MOOD[l.mood] || '' });
// a line said in a conversation: theirs unless the detective's (det) or a phone voice (phone: the officer)
const say = (id, scene) => l => { if(!l || l.det || l.think) return; add(l.phone ? 'badger' : l.who || id, l.key, scene + (l.phone ? ' (전화)' : ''), l); };

for(const [id, p] of Object.entries(P.people)){
  [].concat(p.hello || []).forEach(say(id, '첫 인사'));
  (p.questions || []).forEach(q => add(id, q.id, `대답 ${q.id} (질문: ${q.en})`, { en:p.answers[q.id], ko:P.answersKo[id]?.[q.id] || '' }));
  Object.entries(p.after || {}).forEach(([qid, b]) => b.lines.forEach(say(id, `${qid}를 적은 뒤`)));
  (p.actions || []).forEach(a => {
    if(a.answer) add(id, a.id, `행동 (${a.en})`, { en:a.answer, ko:a.answerKo });
    (a.lines || []).forEach(say(id, `행동 (${a.en})`));
  });
}
// the questioning in the waiting room, then the violin back to Tara
P.ending.intro.forEach(say('badger', '심문 시작'));
P.ending.script.forEach(s => {
  const scene = s.claim ? '심문 · 오웬의 주장' : '심문';
  (s.lines || []).forEach(say('owen', scene)); (s.hit || []).forEach(say('owen', '심문 · 모순을 짚은 뒤'));
});
say('owen', '심문 · 틀린 것을 내밀었을 때')(P.ending.miss);
P.ending.handoff.forEach(r => { [r.open, ...(r.before || []), ...(r.lines || [])].forEach(say(r.to, '결말 (바이올린 반환)')); });

const esc = s => String(s).replace(/\|/g, '\\|');
const unique = l => new Set(l.map(x => x.en)).size;
const sentences = en => (en.match(/[^.!?]+[.!?]+/g) || [en]).length;
const all = Object.values(lines).flat();
let out = `# 사라진 음악 대회 바이올린 — 녹음 대본

\`scripts/violin-recording-script.js\`가 게임 데이터(\`index.html\`의 \`VIOLIN_CASE\`)에서 뽑은 목록이다. 대사를 고치면 이 파일도 다시 뽑는다. 파일 이름은 게임이 재생할 녹음 파일이다(\`audio/violin/\`).

- **탐정 줄은 모두 녹음됨**(90문장, MiniMax Grady·감정 없음, 목록과 job은 \`audio/violin/README.md\`). 아래는 아직 브라우저 음성으로 나오는 인물들의 줄이다.
- **목소리는 정할 것**(사용자 결정): 앞 사건처럼 Higgsfield MiniMax 프리셋에서 인물마다 하나. 오소리 경사는 도서관 사건과 같은 목소리(Fraser)를 쓰면 이어진다.
- **감정**: 오웬의 심문 줄 가운데 표정이 바뀌는 줄(당황·슬픔)은 감정을 넣으려면 Higgsfield 웹(\`higgsfield.ai/audio\`)에서 만든다(MCP는 감정을 저장하지 않음). 나머지는 앞 사건 인물처럼 행복 또는 감정 없음.
- 여러 문장 대답(**문장** 칸이 2 이상)은 노트의 문장별 다시 듣기에 문장 구간(\`SENTENCE_TIMES\`)이 필요하다(녹음 뒤 무음 구간으로 잰다).
- 같은 화자의 같은 문장은 한 번만 녹음하고 파일을 함께 쓴다(**같은 녹음**에 처음 나온 번호).

| 화자 | 줄 수 | 녹음할 문장 |
|---|---|---|
${Object.entries(lines).map(([who, l]) => `| ${NAMES[who]} | ${l.length} | ${unique(l)} |`).join('\n')}
| **합계** | **${all.length}** | **${Object.values(lines).reduce((t, l) => t + unique(l), 0)}** |
`;
for(const [who, l] of Object.entries(lines)){
  out += `\n## ${NAMES[who]} (${l.length}줄)\n\n| # | 파일 | 장면 | 영어 | 문장 | 표정 | 해석 |\n|---|---|---|---|---|---|---|\n`;
  l.forEach((x, i) => {
    const first = l.findIndex(y => y.en === x.en), same = first < i ? `<br>**같은 녹음**: ${first + 1}번` : '';
    out += `| ${i + 1} | \`${x.file.replace(DIR, '')}\` | ${esc(x.scene)} | ${esc(x.en)}${same} | ${sentences(x.en)} | ${x.mood} | ${esc(x.ko)} |\n`;
  });
}
fs.writeFileSync('design/case-04-missing-violin-recording.md', out.replace(/\n/g, '\r\n'));
console.log(Object.fromEntries(Object.entries(lines).map(([w, l]) => [w, `${l.length} lines, ${unique(l)} to record`])));
