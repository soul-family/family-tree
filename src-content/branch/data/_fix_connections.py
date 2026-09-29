#!/usr/bin/env python3
"""Fix branch tree connections: update parent references to match marriage records and common persons."""

import json
import glob
import os

DATA_DIR = r'C:\_Vicki_documents\online github - familytree petersoul.co.uk\src-content\branch\data'


def main():
    files = sorted(glob.glob(os.path.join(DATA_DIR, '*.json')))
    for path in files:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        by_id = {p['id']: p for p in data}

        for person in data:
            pid = person.get('id')
            if not pid:
                continue

            # Fix Hannah Clark: marriage record says "d of Samuel Clark tailor"
            if pid == '1829_hannah_clark':
                # Update father to Samuel Clark tailor based on marriage record
                person['parents'] = {
                    'father': 'samuel_clark_tailor',
                    'mother': ''
                }
                # Remove from James Clarke & Sarah's children
                if 'james_clarke' in by_id:
                    james = by_id['james_clarke']
                    if 'children' in james and pid in james['children']:
                        james['children'].remove(pid)
                if 'sarah_clarke' in by_id:
                    sarah = by_id['sarah_clarke']
                    if 'children' in sarah and pid in sarah['children']:
                        sarah['children'].remove(pid)

            # Fix 1834_samuel_clark: no children or spouses in source, remove empty entries
            if pid == '1834_samuel_clark':
                person['spouses'] = []
                person['children'] = []

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f'Fixed connections in {os.path.basename(path)}')


if __name__ == '__main__':
    main()
