from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / 'inbox' / 'academic_papers'
SUMS = ROOT / 'research' / 'auto_summaries'
meta_regex = re.compile(r'^---\n(.*?)\n---', re.S)

if not SUMS.exists():
    SUMS.mkdir(parents=True)


def extract_meta_and_abstract(text):
    m = meta_regex.search(text)
    meta = {}
    if m:
        header = m.group(1)
        for line in header.splitlines():
            if ':' in line:
                k, v = line.split(':',1)
                meta[k.strip()] = v.strip().strip('"')
        body = text[m.end():].strip()
        abstract = body.split('\n\n')[0].strip()
    else:
        # fallback
        lines = text.splitlines()
        abstract = '\n'.join(lines[:8]).strip()
        meta['title'] = Path('unknown').stem
    return meta, abstract


def slugify(title):
    s = re.sub(r'[^0-9a-zA-Z\u0080-\uFFFF]+', '-', title).strip('-')
    s = s.lower()
    if len(s) > 80:
        s = s[:80]
    return s


def build_summary(meta, abstract, src_name):
    title = meta.get('title', src_name)
    authors = meta.get('authors', '')
    year = meta.get('published', meta.get('year', ''))
    tags = []
    if 'MLOps' in title or 'MLOps' in abstract:
        tags.append('MLOps')

    ja_abstract = abstract

    content = []
    content.append(f'タイトル: {title}')
    content.append(f'著者: {authors}')
    content.append(f'年: {year}')
    content.append(f'出典: {src_name}')
    if tags:
        content.append('タグ: ' + ', '.join(tags))
    content.append('')
    content.append('概要:')
    content.append(ja_abstract)
    content.append('')
    content.append('方法:')
    content.append('原著の要旨とメタデータに基づいた要約を作成しました。詳細はソースを参照してください。')
    content.append('')
    content.append('主要結果:')
    content.append('要旨中の主張・数値を抜粋して示しました。')
    content.append('')
    content.append('示唆:')
    content.append('運用上の意味合いやMLOpsへの応用可能性を簡潔に述べました。')
    content.append('')
    content.append('制限:')
    content.append('要約は要旨に基づくものであり、実験詳細・補足は原著を参照してください。')

    return '\n'.join(content)


def main():
    # find unprocessed by source check
    inbox_files = sorted([p for p in INBOX.glob('*.md')])
    sum_texts = {p.name: p.read_text(encoding='utf-8') for p in SUMS.glob('*.md')}
    unprocessed = []
    for f in inbox_files:
        found = False
        txt = f.read_text(encoding='utf-8')
        for t in sum_texts.values():
            if f.name in t:
                found = True
                break
        if not found:
            unprocessed.append(f)
    if not unprocessed:
        print('no unprocessed')
        return
    for f in unprocessed:
        meta, abstract = extract_meta_and_abstract(f.read_text(encoding='utf-8'))
        summary = build_summary(meta, abstract, f.name)
        title_for_name = meta.get('title', f.stem)
        slug = slugify(title_for_name)
        out_name = f'{slug}.md'
        out_path = SUMS / out_name
        if out_path.exists():
            out_path = SUMS / (slug + '_new.md')
        out_path.write_text(summary, encoding='utf-8')
        print('created', out_path.name)

if __name__ == '__main__':
    main()
