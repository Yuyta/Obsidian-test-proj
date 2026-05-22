import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUM_DIR = ROOT / 'research' / 'auto_summaries'
ARCHIVE_DIR = ROOT / 'archive' / 'academic_papers'

meta_regex = re.compile(r'^(タイトル|著者|年|出典|タグ):\s*(.*)$', re.MULTILINE)

def extract_meta(text):
    meta = {}
    for m in meta_regex.finditer(text):
        key = m.group(1)
        val = m.group(2).strip()
        meta[key] = val
    return meta


def make_frontmatter(meta, file_name):
    fm = {
        'title': meta.get('タイトル', file_name.replace('.md','')),
        'authors': meta.get('著者', ''),
        'year': meta.get('年', ''),
        'source': meta.get('出典', ''),
        'tags': [t.strip() for t in meta.get('タグ', '').split(',') if t.strip()]
    }
    lines = ['---']
    for k, v in fm.items():
        if isinstance(v, list):
            if v:
                lines.append(f"{k}: [{', '.join(v)}]")
        else:
            lines.append(f"{k}: " + (v if v is not None else ''))
    lines.append('---\n')
    return '\n'.join(lines), fm


def build_wiki_links(fm):
    source = fm.get('source','')
    links = []
    if source:
        basename = os.path.basename(source)
        note_name = os.path.splitext(basename)[0]
        # Wiki link by filename
        links.append(f'[[{note_name}]]')
        # Relative path link
        rel_path = os.path.join('..','archive','academic_papers', basename).replace('\\','/')
        links.append(f'[ソースファイル]({rel_path})')
    return links


def clean_original(text):
    # remove lines that are meta fields to avoid duplication
    cleaned = meta_regex.sub('', text)
    # strip leading/trailing blank lines
    return cleaned.strip() + '\n'


def process_file(path: Path):
    text = path.read_text(encoding='utf-8')
    meta = extract_meta(text)
    front, fm = make_frontmatter(meta, path.name)
    body = clean_original(text)
    links = build_wiki_links(fm)

    new = front + '\n' + body
    if links:
        new += '\n## 関連ファイル\n' + '\n'.join(['- ' + l for l in links]) + '\n'

    path.write_text(new, encoding='utf-8')
    return path.name


def main():
    if not SUM_DIR.exists():
        print('summary dir not found:', SUM_DIR)
        return
    files = sorted(SUM_DIR.glob('*.md'))
    updated = []
    for f in files:
        try:
            updated.append(process_file(f))
        except Exception as e:
            print('failed', f, e)
    print('updated', len(updated), 'files')
    for u in updated:
        print(' -', u)

if __name__ == '__main__':
    main()
