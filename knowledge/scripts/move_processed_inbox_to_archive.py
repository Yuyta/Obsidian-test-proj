import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / 'inbox' / 'academic_papers'
ARCHIVE = ROOT / 'archive' / 'academic_papers'
SUMS = ROOT / 'research' / 'auto_summaries'

ARCHIVE.mkdir(parents=True, exist_ok=True)

sum_texts = {p.name: p.read_text(encoding='utf-8') for p in SUMS.glob('*.md')}

moved = []
skipped = []
for f in sorted(INBOX.glob('*.md')):
    found = False
    for text in sum_texts.values():
        if f.name in text:
            found = True
            break
    if found:
        dest = ARCHIVE / f.name
        # if dest exists, append suffix
        if dest.exists():
            dest = ARCHIVE / (f.stem + '_dup.md')
        shutil.move(str(f), str(dest))
        moved.append((f.name, dest.name))
    else:
        skipped.append(f.name)

print('moved_count:', len(moved))
for o,d in moved:
    print(' -', o, '->', d)
print('skipped_count:', len(skipped))
for s in skipped:
    print(' -', s)
