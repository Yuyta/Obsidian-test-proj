import os
import shutil
from pathlib import Path

root = Path(r"c:\Users\tacta\OneDrive\デスクトップ\MyBrain\knowledge\archive\academic_papers")
preview = root / "_to_delete_preview"
preview.mkdir(exist_ok=True)

# Broader AI/robotics keywords (if present together with physical terms, keep)
ai_keywords = [
    'autonom', 'driv', 'adas', 'vehicle', 'vla', 'vision-language', 'vision_language', 'vln',
    'mlops', 'mlo', 'agent', 'agentic', 'ai', 'llm', 'machine', 'learning', 'robot', 'robotics',
    'sensor', 'fleet', 'provision', 'cloud',
]

# Physical / embodiment specific terms. Presence of these + AI keywords indicates Physical-AI relevance.
physical_terms = [
    'physical-ai', 'physical_ai', 'physical', 'embodiment', 'robotic', 'manipulation', 'grasp',
    'end-effector', 'end effector', 'kinematics', 'actuator', 'real-robot', 'robotic-arm', 'manipulator', 'tactile'
]

# Normalise
ai_keywords = [k.lower() for k in ai_keywords]
physical_terms = [k.lower() for k in physical_terms]

moved = []
kept = []

for p in root.glob('*.md'):
    if p.name.startswith('_'):
        kept.append(p.name)
        continue
    name = p.name.lower()
    try:
        text = p.read_text(encoding='utf-8', errors='ignore').lower()
    except Exception:
        text = ''
    keep = False
    # If explicit Physical-AI tag or phrase appears, keep
    for k in ['physical-ai', 'physical_ai']:
        if k in name or k in text:
            keep = True
            break
    # If any physical term appears, require also an AI/robotics term to consider relevant
    if not keep:
        phys_found = any(k in name or k in text for k in physical_terms)
        if phys_found:
            ai_found = any(k in name or k in text for k in ai_keywords)
            if ai_found:
                keep = True
    # Otherwise, if file clearly about AI/robotics (even without explicit 'physical'), keep
    if not keep:
        if any(k in name or k in text for k in ai_keywords):
            keep = True
    if keep:
        kept.append(p.name)
    else:
        shutil.move(str(p), str(preview / p.name))
        moved.append(p.name)

print('Moved to preview (candidate deletions):')
for m in moved:
    print(m)

print('\nKept files:')
for k in kept[:200]:
    print(k)

print(f'\nSummary: moved {len(moved)} files, kept {len(kept)} files. Preview folder: {preview}')
