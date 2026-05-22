from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / 'inbox' / 'academic_papers'
SUMS = ROOT / 'research' / 'auto_summaries'
meta_regex = re.compile(r'^---\n(.*?)\n---', re.S)

def extract_title(text):
    m = meta_regex.search(text)
    if not m:
        return None
    header = m.group(1)
    for line in header.splitlines():
        if ':' in line:
            k, v = line.split(':',1)
            if k.strip().lower() in ('title','titre','タイトル'):
                return v.strip().strip('"')
    return None

def slugify(title):
    s = re.sub(r'[^0-9a-zA-Z\u0080-\uFFFF]+', '-', title).strip('-')
    s = s.lower()
    if len(s) > 80:
        s = s[:80]
    return s

inbox_files = sorted(INBOX.glob('*.md'))
summary_stems = [p.stem for p in SUMS.glob('*.md')]

unprocessed = []
for f in inbox_files:
    text = f.read_text(encoding='utf-8')
    title = extract_title(text)
    if title:
        stem = slugify(title)
    else:
        stem = re.sub(r'[^0-9a-zA-Z]+','-', f.stem).lower()
    # relaxed match: any summary stem contains stem
    matched = any(stem in s for s in summary_stems)
    if not matched:
        unprocessed.append((f.name, stem))

print('inbox count:', len(inbox_files))
print('summaries count:', len(summary_stems))
print('unprocessed count:', len(unprocessed))
for u in unprocessed:
    print(' -', u[0], '-> expected summary stem:', u[1])
