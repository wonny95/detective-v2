// The umbrella case's recording script (phase 3): every line the game says aloud, by speaker, with the file it will be
// saved as, pulled from UMBRELLA_CASE in index.html so the script and the game cannot drift apart.
// Run from the project folder: node scripts/umbrella-recording-script.js  -> design/case-02-unclaimed-umbrella-recording.md
const fs = require('fs'), path = require('path'), os = require('os');
const html = fs.readFileSync('index.html', 'utf8');
const start = html.indexOf('const UMBRELLA_CASE = {');
let depth = 0, end = html.indexOf('{', start);
for(let k = end; k < html.length; k++){
  if(html[k] === '{') depth++;
  else if(html[k] === '}' && !--depth){ end = k; break; }
}
const tmp = path.join(os.tmpdir(), 'umbrella-case.js');
fs.writeFileSync(tmp, html.slice(start, end + 1).replace('const UMBRELLA_CASE =', 'module.exports ='));
const P = require(tmp);

const DIR = 'audio/umbrella/';
const NAMES = { ella:'엘라', tess:'테스', ruby:'루비', finn:'핀', detective:'탐정' };
const lines = { ella:[], tess:[], ruby:[], finn:[], detective:[] };
const add = (who, file, scene, en, ko) => lines[who].push({ file:DIR + file + '.mp3', scene, en, ko });
// what the voice reads where the screen's words would be read oddly (dates)
const spoken = en => en.replace(/October 24/g, 'October twenty-fourth');

// greetings, questions and answers, the close-look action
for(const [id, p] of Object.entries(P.people)){
  [].concat(p.hello).forEach(l => l.det
    ? add('detective', `detective-${l.key}`, `${NAMES[id]} 첫 인사`, l.en, l.ko)
    : add(id, `${id}-${l.key}`, '첫 인사', l.en, l.ko));
  p.questions.forEach(q => {
    add('detective', `detective-${id}-${q.id}`, `${NAMES[id]}에게 질문 ${q.id}`, q.en, q.ko);
    add(id, `${id}-${q.id}`, `대답 ${q.id}`, p.answers[q.id], P.answersKo[id][q.id]);
  });
  (p.actions || []).forEach(a => {
    add('detective', `detective-${id}-act-${a.id}`, `${NAMES[id]}에게 행동(우산 조사)`, a.en, a.ko);
    add(id, `${id}-${a.id}`, '행동의 대답', a.answer, a.answerKo);
  });
}
// the detective's thought after the banner and the notice
P.together.forEach((t, i) => add('detective', `detective-together${i + 1}`, '현수막·안내문을 찍은 뒤 생각', t.line.en, t.line.ko));
// photos and things looked at: the detective reads each one's sentence
P.places.forEach(pl => pl.clues.forEach((c, i) =>
  add('detective', `detective-${pl.id}-${i}`, `${pl.label} · ${c.label}${c.prop ? ' (소품)' : ''}`, c.en, c.ko)));
Object.entries(P.items).forEach(([id, it]) => add('detective', `detective-item-${id}`, `소지품 · ${it.label}`, it.en, it.ko));
// the deduction board: question, the right answer's reply, the hint; one common miss
P.deduce.qs.forEach(q => {
  const card = q.card.replace(/\{\w+:([^}]+)\}/g, '$1');
  add('detective', `deduce/q${q.step}`, `추리 Q${q.step} 질문`, q.q, q.qKo);
  add('detective', `deduce/r${q.step}`, `추리 Q${q.step} 맞았을 때 (완성 문장: ${card})`, q.right, q.rightKo);
  add('detective', `deduce/h${q.step}`, `추리 Q${q.step} 힌트`, q.hint, q.hintKo);
});
add('detective', 'deduce/miss', '추리 오답(공통)', P.deduce.miss.en, P.deduce.miss.ko);
// the ending: three rounds; a line is the round's person's unless it is the detective's or names someone (who)
P.ending.handoff.forEach((round, r) => {
  const say = (l, part) => {
    if(!l || l.think) return;
    const who = l.det ? 'detective' : l.who || round.to;
    add(who, who === 'detective' ? `detective-${l.key}` : `${who}-${l.key}`, `결말 ${r + 1} (${NAMES[round.to]})${part ? ' ' + part : ''}`, l.en, l.ko);
  };
  say(round.open, '시작'); (round.before || []).forEach(l => say(l, '건네기 전')); (round.lines || []).forEach(l => say(l, ''));
});

const esc = s => String(s).replace(/\|/g, '\\|');
const unique = l => new Set(l.map(x => x.en)).size;
let out = `# 주인 없는 우산 — 녹음 대본

\`scripts/umbrella-recording-script.js\`가 게임 데이터(\`index.html\`의 \`UMBRELLA_CASE\`)에서 뽑은 목록이다. 대사를 고치면 이 파일도 다시 뽑는다. 파일 이름은 녹음해 넣을 자리다(지금은 모두 브라우저 음성).

- 인물 4명(엘라·테스·루비·핀)은 새 목소리, 탐정은 소풍·도서관 사건과 같은 목소리(Grady).
- 읽기용 문장이 따로 있는 줄은 **읽기**에 적었다(화면 글은 그대로).
- 같은 화자의 같은 문장은 한 번만 녹음하고 파일을 함께 쓴다(**같은 녹음**에 처음 나온 번호).

| 화자 | 줄 수 | 녹음할 문장 |
|---|---|---|
${Object.entries(lines).map(([who, l]) => `| ${NAMES[who]} | ${l.length} | ${unique(l)} |`).join('\n')}
| **합계** | **${Object.values(lines).reduce((t, l) => t + l.length, 0)}** | **${Object.values(lines).reduce((t, l) => t + unique(l), 0)}** |
`;
for(const [who, l] of Object.entries(lines)){
  out += `\n## ${NAMES[who]} (${l.length}줄)\n\n| # | 파일 | 장면 | 영어 | 해석 |\n|---|---|---|---|---|\n`;
  l.forEach((x, i) => {
    const read = spoken(x.en) !== x.en ? `<br>**읽기**: ${esc(spoken(x.en))}` : '';
    const first = l.findIndex(y => y.en === x.en), same = first < i ? `<br>**같은 녹음**: ${first + 1}번` : '';
    out += `| ${i + 1} | \`${x.file.replace(DIR, '')}\` | ${esc(x.scene)} | ${esc(x.en)}${read}${same} | ${esc(x.ko)} |\n`;
  });
}
fs.writeFileSync('design/case-02-unclaimed-umbrella-recording.md', out.replace(/\n/g, '\r\n'));
console.log(Object.fromEntries(Object.entries(lines).map(([w, l]) => [w, `${l.length} lines, ${unique(l)} to record`])));
