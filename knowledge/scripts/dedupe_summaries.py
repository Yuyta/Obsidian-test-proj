from pathlib import Path
SUMS = Path(__file__).resolve().parents[1] / 'research' / 'auto_summaries'
removed = []
for p in SUMS.glob('*_1.md'):
    base = p.with_name(p.stem[:-2] + '.md')
    if base.exists():
        p.unlink()
        removed.append(p.name)
print('removed', len(removed), 'files')
for r in removed:
    print(' -', r)
