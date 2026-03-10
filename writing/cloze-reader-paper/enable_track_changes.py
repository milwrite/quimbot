#!/usr/bin/env python3
import zipfile
import os
import sys
from pathlib import Path


def enable_track_changes(src: Path, dst: Path):
    with zipfile.ZipFile(src, 'r') as zin:
        files = {name: zin.read(name) for name in zin.namelist()}

    settings_name = 'word/settings.xml'
    if settings_name not in files:
        raise RuntimeError('No word/settings.xml found in DOCX')

    settings = files[settings_name].decode('utf-8')
    if '<w:trackRevisions' not in settings:
        settings = settings.replace('</w:settings>', '  <w:trackRevisions/>\n</w:settings>')

    files[settings_name] = settings.encode('utf-8')

    dst.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as zout:
        for name, data in files.items():
            zout.writestr(name, data)

    return '<w:trackRevisions' in settings


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: enable_track_changes.py <input.docx> <output.docx>')
        sys.exit(1)

    src = Path(sys.argv[1]).expanduser().resolve()
    dst = Path(sys.argv[2]).expanduser().resolve()
    ok = enable_track_changes(src, dst)
    print(f'Wrote: {dst}')
    print(f'trackRevisions present: {ok}')
