#!/usr/bin/env python3
"""Shorten branch JSON IDs to birthday_firstname_famname."""

import json
import glob
import os
import re

DATA_DIR = r'C:\_Vicki_documents\online github - familytree petersoul.co.uk\src-content\branch\data'


def shorten_id(old_id):
    if '_' not in old_id:
        return old_id
    parts = old_id.split('_')
    birthday = parts[0]
    # first name is second part
    first = parts[1] if len(parts) > 1 else 'unknown'
    # last name/family name is the last part that is longer than 3 chars
    last = 'unknown'
    for part in reversed(parts[1:]):
        if len(part) > 3:
            last = part
            break
    return f'{birthday}_{first}_{last}'


def remap_person(person):
    old_id = person.get('id')
    if not old_id:
        return
    person['id'] = shorten_id(old_id)

    for spouse in person.get('spouses', []) or []:
        if 'id' in spouse:
            spouse['id'] = shorten_id(spouse['id'])

    if 'children' in person:
        person['children'] = [shorten_id(c) for c in (person['children'] or [])]

    if 'parents' in person:
        if person['parents'].get('father'):
            person['parents']['father'] = shorten_id(person['parents']['father'])
        if person['parents'].get('mother'):
            person['parents']['mother'] = shorten_id(person['parents']['mother'])

    if 'crossBranch' in person:
        for cb in person.get('crossBranch', []) or []:
            if 'id' in cb:
                cb['id'] = shorten_id(cb['id'])


def main():
    files = sorted(glob.glob(os.path.join(DATA_DIR, '*.json')))
    for path in files:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for person in data:
            remap_person(person)

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f'Shortened IDs in {os.path.basename(path)}')


if __name__ == '__main__':
    main()
