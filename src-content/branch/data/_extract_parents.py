#!/usr/bin/env python3
"""Move parent details from info text into structured parents fields, handling 's of' and 'd of' patterns."""

import json
import glob
import os
import re

DATA_DIR = r'C:\_Vicki_documents\online github - familytree petersoul.co.uk\src-content\branch\data'


def extract_parent_details(text):
    """Extract parent details from info text using 's of' and 'd of' patterns."""
    details = {}
    
    # Pattern: "s of John Smith" or "d of John and Mary Smith"
    son_match = re.search(r'\bs\s+of\s+([A-Z][a-z]+(?:\.?\s+[A-Z][a-z]+)*)', text, re.IGNORECASE)
    if son_match:
        details['father'] = son_match.group(1).strip()
    
    daughter_match = re.search(r'\bd\s+of\s+([A-Z][a-z]+(?:\.?\s+[A-Z][a-z]+)*)', text, re.IGNORECASE)
    if daughter_match:
        details['mother'] = daughter_match.group(1).strip()
    
    # Also handle "son of" and "daughter of"
    son_full_match = re.search(r'\bson\s+of\s+([A-Z][a-z]+(?:\.?\s+[A-Z][a-z]+)*)', text, re.IGNORECASE)
    if son_full_match and 'father' not in details:
        details['father'] = son_full_match.group(1).strip()
    
    daughter_full_match = re.search(r'\bdaughter\s+of\s+([A-Z][a-z]+(?:\.?\s+[A-Z][a-z]+)*)', text, re.IGNORECASE)
    if daughter_full_match and 'mother' not in details:
        details['mother'] = daughter_full_match.group(1).strip()
    
    return details


def clean_info_text(person):
    """Remove parent details from info text."""
    info = person.get('info', '') or ''
    if not info:
        return
    
    # Remove 's of' and 'd of' patterns
    info = re.sub(r'\bs\s+of\s+[A-Z][a-z]+(?:\.?\s+[A-Z][a-z]+)*', '', info, flags=re.IGNORECASE)
    info = re.sub(r'\bd\s+of\s+[A-Z][a-z]+(?:\.?\s+[A-Z][a-z]+)*', '', info, flags=re.IGNORECASE)
    info = re.sub(r'\bson\s+of\s+[A-Z][a-z]+(?:\.?\s+[A-Z][a-z]+)*', '', info, flags=re.IGNORECASE)
    info = re.sub(r'\bdaughter\s+of\s+[A-Z][a-z]+(?:\.?\s+[A-Z][a-z]+)*', '', info, flags=re.IGNORECASE)
    
    # Clean up
    info = re.sub(r'\s+', ' ', info).strip()
    info = re.sub(r';\s*;', ';', info)
    info = re.sub(r';\s*$', '', info)
    info = info.strip(' ;.,')
    
    person['info'] = info


def main():
    files = sorted(glob.glob(os.path.join(DATA_DIR, '*.json')))
    for path in files:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for person in data:
            info = person.get('info', '') or ''
            if not info:
                continue
            
            parent_details = extract_parent_details(info)
            
            # Update parents field if details found
            parents = person.get('parents', {})
            if not parents:
                parents = {}
            
            if 'father' in parent_details and not parents.get('father'):
                parents['father'] = parent_details['father']
            if 'mother' in parent_details and not parents.get('mother'):
                parents['mother'] = parent_details['mother']
            
            if parents:
                person['parents'] = parents
            
            # Clean info text
            clean_info_text(person)

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f'Updated parents in {os.path.basename(path)}')


if __name__ == '__main__':
    main()
