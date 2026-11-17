// Promote a completed game build to the user's independent review server. No browser reload or save changes.
// Run: node scripts/update-review.js
const fs = require('fs');
const path = require('path');

const SOURCE = path.resolve(__dirname, '..');
const DESTINATION = path.join(SOURCE, '.preview', 'review');
let copied = 0;

function copy(relative) {
  const source = path.join(SOURCE, relative);
  const destination = path.join(DESTINATION, relative);
  const stat = fs.statSync(source);
  if (stat.isDirectory()) {
    fs.mkdirSync(destination, { recursive: true });
    for (const name of fs.readdirSync(source)) copy(path.join(relative, name));
    return;
  }
  if (fs.existsSync(destination)) {
    const previous = fs.statSync(destination);
    if (previous.size === stat.size && Math.abs(previous.mtimeMs - stat.mtimeMs) < 1) return;
  }
  fs.copyFileSync(source, destination);
  fs.utimesSync(destination, stat.atime, stat.mtime);
  copied++;
}

// These are real copies: editing an image or audio file in the working folder cannot alter the review copy.
// Old unused files are left alone; nothing in the review folder or browser storage is deleted.
fs.mkdirSync(DESTINATION, { recursive: true });
for (const relative of ['assets', 'audio', 'index.html']) copy(relative);
fs.writeFileSync(path.join(DESTINATION, 'snapshot.json'), JSON.stringify({ updatedAt: new Date().toISOString() }, null, 2) + '\n');
console.log(`Review snapshot ready: ${copied} files copied. http://localhost:5176/`);
console.log('The review tab stays where it is. Refresh it when ready to see this version.');
