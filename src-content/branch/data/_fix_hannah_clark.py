#!/usr/bin/env python3
"""Fix duplicate Hannah Clark entries and update references."""

import json
import glob
import os

DATA_DIR = r'C:\_Vicki_documents\online github - familytree petersoul.co.uk\src-content\branch\data'


def fix_hannah_clark(data):
    """Fix duplicate Hannah Clark entries."""
    by_id = {p['id']: p for p in data}
    
    # Remove duplicate hannah_clark if 1829_hannah_clark exists
    if 'hannah_clark' in by_id and '1829_hannah_clark' in by_id:
        duplicate = by_id['hannah_clark']
        canonical = by_id['1829_hannah_clark']
        
        # Update references in other persons
        for person in data:
            # Fix spouse references
            for spouse in person.get('spouses', []):
                if spouse.get('id') == 'hannah_clark':
                    spouse['id'] = '1829_hannah_clark'
            
            # Fix children references
            if 'children' in person:
                person['children'] = [
                    '1829_hannah_clark' if cid == 'hannah_clark' else cid 
                    for cid in person['children']
                ]
            
            # Fix parents references
            parents = person.get('parents', {})
            if parents:
                if parents.get('father') == 'hannah_clark':
                    parents['father'] = '1829_hannah_clark'
                if parents.get('mother') == 'hannah_clark':
                    parents['mother'] = '1829_hannah_clark'
        
        # Merge any unique info from duplicate into canonical
        if duplicate.get('info') and not canonical.get('info'):
            canonical['info'] = duplicate['info']
        elif duplicate.get('info') and canonical.get('info'):
            canonical['info'] = canonical['info'] + '; ' + duplicate['info']
        
        # Remove duplicate
        data[:] = [p for p in data if p['id'] != 'hannah_clark']
        
        return True
    return False


def main():
    files = sorted(glob.glob(os.path.join(DATA_DIR, '*.json')))
    for path in files:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if fix_hannah_clark(data):
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f'Fixed Hannah Clark duplicate in {os.path.basename(path)}')
        else:
            print(f'No Hannah Clark duplicate in {os.path.basename(path)}')


if __name__ == '__main__':
    main()
