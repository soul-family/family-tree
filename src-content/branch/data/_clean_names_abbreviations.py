#!/usr/bin/env python3
"""Clean branch JSON: remove Jr/Sr from names and expand common abbreviations in info text."""

import json
import glob
import os
import re

DATA_DIR = r'C:\_Vicki_documents\online github - familytree petersoul.co.uk\src-content\branch\data'

ABBREVIATIONS = {
    r'\bbd\b': 'buried',
    r'\bbpt\b': 'baptised',
    r'\bbapt\b': 'baptised',
    r'\bmar\b': 'married',
    r'\bcem\b': 'cemetery',
    r'\bdecd\b': 'deceased',
    r'\brev\b': 'reverend',
    r'\best\.?\b': 'estate',
     r'(?<!& )\bco\.?\b': 'county',
    r'\bpar\.?\b': 'parish',
    r'\bdis\.?\b': 'district',
    r'\bs\s+of\b': 'son of',
    r'\bd\s+of\b': 'daughter of',
    r'\bson\s+of\b': 'son of',
    r'\bdaughter\s+of\b': 'daughter of',
}

NAME_SUFFIXES = [
    r'\s+Jr\.?$',
    r'\s+Sr\.?$',
    r'\s+II$',
    r'\s+III$',
    r'\s+IV$',
    r'\s+V$',
]


def clean_name(raw):
    if not raw:
        return 'Unknown'
    name = str(raw).strip()
    # Remove Jr/Sr/II/III/IV/V suffixes
    for suffix in NAME_SUFFIXES:
        name = re.sub(suffix, '', name, flags=re.IGNORECASE)
    # Remove maiden name in parentheses
    name = re.sub(r'\s*\([^)]*\)', '', name).strip()
    return name


def expand_abbreviations(text):
    if not text:
        return text
    for pattern, replacement in ABBREVIATIONS.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    # Clean up double spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def main():
    files = sorted(glob.glob(os.path.join(DATA_DIR, '*.json')))
    for path in files:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for person in data:
            # Clean name
            if 'name' in person:
                person['name'] = clean_name(person['name'])
            
            # Expand abbreviations in info
            if 'info' in person and person['info']:
                person['info'] = expand_abbreviations(person['info'])

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f'Updated {os.path.basename(path)}')


if __name__ == '__main__':
    main()
