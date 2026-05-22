from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / 'inbox' / 'academic_papers'
SUMS = ROOT / 'research' / 'auto_summaries'

inbox_files = sorted([p.name for p in INBOX.glob('*.md')])
sum_texts = {p.name: p.read_text(encoding='utf-8') for p in SUMS.glob('*.md')}

unprocessed = []
for inbox in inbox_files:
    found = False
    for sname, text in sum_texts.items():
        if inbox in text:
            found = True
            break
    if not found:
        unprocessed.append(inbox)

print('inbox count:', len(inbox_files))
print('summaries count:', len(sum_texts))
print('unprocessed count:', len(unprocessed))
for u in unprocessed:
    print(' -', u)
