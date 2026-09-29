#!/usr/bin/env python3
"""Fix parents fields to reference person IDs."""

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
            parents = person.get('parents', {})
            if not parents:
                continue

            father_id = parents.get('father')
            mother_id = parents.get('mother')

            if father_id and father_id in by_id:
                parents['father'] = father_id
            elif father_id:
                parents['father'] = father_id

            if mother_id and mother_id in by_id:
                parents['mother'] = mother_id
            elif mother_id:
                parents['mother'] = mother_id

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f'Fixed parents in {os.path.basename(path)}')


if __name__ == '__main__':
    main()
