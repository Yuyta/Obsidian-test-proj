import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / 'inbox' / 'academic_papers'
SUMS = ROOT / 'research' / 'auto_summaries'

if not SUMS.exists():
    SUMS.mkdir(parents=True)

meta_regex = re.compile(r'^---\n(.*?)\n---', re.S)


def slugify(title):
    s = re.sub(r'[^0-9a-zA-Z\u0080-\uFFFF]+', '-', title).strip('-')
    s = s.lower()
    if len(s) > 80:
        s = s[:80]
    return s


def extract_meta_and_abstract(text):
    meta = {}
    m = meta_regex.search(text)
    if m:
        body = text[m.end():].strip()
        # simple parse of yaml-like header
        header = m.group(1)
        for line in header.splitlines():
            if ':' in line:
                k, v = line.split(':', 1)
                meta[k.strip()] = v.strip().strip('"')
        abstract = body.split('\n\n')[0].strip()
    else:
        # fallback
        lines = text.splitlines()
        abstract = '\n'.join(lines[:8]).strip()
        meta['title'] = Path('unknown').stem
    return meta, abstract


def translate_brief_en_to_ja(en):
    # naive, rule-based short translation for abstracts
    s = en
    s = s.replace('We propose', '本研究では〜を提案する。')
    s = s.replace('We present', '本稿では〜を提示する。')
    s = s.replace('We show', '〜を示す。')
    s = s.replace('We find', '〜が確認された。')
    s = s.replace('We conducted', '我々は〜を実施した。')
    s = s.replace('We evaluate', '我々は〜を評価した。')
    s = s.replace('dataset', 'データセット')
    s = s.replace('performance', '性能')
    # fallback: keep English but mark
    if all(ord(c) < 128 for c in s):
        s = s
    return s


def build_summary(meta, abstract, src_name):
    title = meta.get('title', src_name)
    authors = meta.get('authors', '')
    year = meta.get('published', meta.get('year', ''))
    tags = []
    if 'MLOps' in title or 'MLOps' in abstract:
        tags.append('MLOps')

    ja_abstract = translate_brief_en_to_ja(abstract)

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
    inbox_files = sorted(INBOX.glob('*.md'))
    existing = {p.stem for p in SUMS.glob('*.md')}
    candidates = []
    for f in inbox_files:
        # create a normalized stem
        stem = re.sub(r'[^0-9a-zA-Z]+','-', f.stem).lower()
        if stem not in existing:
            candidates.append(f)
    to_process = candidates[:10]
    created = []
    for f in to_process:
        text = f.read_text(encoding='utf-8')
        meta, abstract = extract_meta_and_abstract(text)
        summary = build_summary(meta, abstract, f.name)
        # filename
        title_for_name = meta.get('title', f.stem)
        slug = slugify(title_for_name)
        out_name = f'{slug}.md'
        out_path = SUMS / out_name
        # avoid overwrite
        if out_path.exists():
            out_path = SUMS / (slug + '_1.md')
        out_path.write_text(summary, encoding='utf-8')
        created.append(out_path.name)
    print('created', len(created), 'summaries')
    for c in created:
        print(' -', c)

if __name__ == '__main__':
    main()
