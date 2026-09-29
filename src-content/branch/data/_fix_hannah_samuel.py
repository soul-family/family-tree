#!/usr/bin/env python3
"""Fix Hannah Clark and Samuel Clark parentage based on original source analysis."""

import json
import glob
import os

DATA_DIR = r'C:\_Vicki_documents\online github - familytree petersoul.co.uk\src-content\branch\data'


def fix_hannah_and_samuel(data):
    """Fix Hannah Clark to have James Clarke as father, not Samuel Clark tailor."""
    by_id = {p['id']: p for p in data}
    
    # Fix 1829_hannah_clark: father is james_clarke, not samuel_clark_tailor
    if '1829_hannah_clark' in by_id:
        hannah = by_id['1829_hannah_clark']
        hannah['parents'] = {
            'father': 'james_clarke',
            'mother': 'sarah_clarke'
        }
        
        # Remove from james_clarke's children if not already there
        if 'james_clarke' in by_id:
            james = by_id['james_clarke']
            if 'children' in james and '1829_hannah_clark' not in james['children']:
                james['children'].append('1829_hannah_clark')
        
        # Remove from sarah_clarke's children if not already there
        if 'sarah_clarke' in by_id:
            sarah = by_id['sarah_clarke']
            if 'children' in sarah and '1829_hannah_clark' not in sarah['children']:
                sarah['children'].append('1829_hannah_clark')
    
    # Fix samuel_clark_tailor: remove 1829_hannah_clark from his children
    if 'samuel_clark_tailor' in by_id:
        tailor = by_id['samuel_clark_tailor']
        if 'children' in tailor and '1829_hannah_clark' in tailor['children']:
            tailor['children'].remove('1829_hannah_clark')
        # If no children left, keep empty array
        if not tailor.get('children'):
            tailor['children'] = []
    
    # Ensure 1834_samuel_clark is child of james_clarke and sarah_clarke
    if '1834_samuel_clark' in by_id:
        samuel = by_id['1834_samuel_clark']
        samuel['parents'] = {
            'father': 'james_clarke',
            'mother': 'sarah_clarke'
        }
        if 'james_clarke' in by_id:
            james = by_id['james_clarke']
            if 'children' in james and '1834_samuel_clark' not in james['children']:
                james['children'].append('1834_samuel_clark')
        if 'sarah_clarke' in by_id:
            sarah = by_id['sarah_clarke']
            if 'children' in sarah and '1834_samuel_clark' not in sarah['children']:
                sarah['children'].append('1834_samuel_clark')
    
    return True


def main():
    files = sorted(glob.glob(os.path.join(DATA_DIR, '*.json')))
    for path in files:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if fix_hannah_and_samuel(data):
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f'Fixed Hannah/Samuel Clark in {os.path.basename(path)}')
        else:
            print(f'No Hannah/Samuel Clark entries in {os.path.basename(path)}')


if __name__ == '__main__':
    main()
