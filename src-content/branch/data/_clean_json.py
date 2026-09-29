#!/usr/bin/env python3
"""Clean branch JSON: extract structured fields from info text."""

import json
import glob
import os
import re

DATA_DIR = r'C:\_Vicki_documents\online github - familytree petersoul.co.uk\src-content\branch\data'

# Patterns for extracting structured data from info text
DATE_PATTERNS = [
    r'\bB\s+(\d{1,2}\s+\w+\s+\d{4}|\w+\s+\d{4}|\d{4})\b',
    r'\bbpt\s+(\d{1,2}\s+\w+\s+\d{4})\b',
    r'\bbapt\b',
    r'\bD\s+(\d{1,2}\s+\w+\s+\d{4}|\w+\s+\d{4}|\d{4})\b',
    r'\bbd\b',
    r'\bM\s+(\d{1,2}\s+\w+\s+\d{4}|\w+\s+\d{4}|\d{4})\b',
    r'\bmarried\s+(\d{1,2}\s+\w+\s+\d{4}|\w+\s+\d{4}|\d{4})\b',
]

PLACE_PATTERNS = [
    r'\bof\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
    r'\bfrom\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
    r'\bat\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
    r'\bin\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
    r'\bB\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
]


def extract_dates(text):
    dates = []
    for pattern in DATE_PATTERNS:
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        dates.extend(matches)
    return dates


def extract_places(text):
    places = []
    for pattern in PLACE_PATTERNS:
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        places.extend(matches)
    return places


def clean_info(person):
    info = person.get('info', '') or ''
    if not info:
        return

    # Remove date references from info if they're already in structured fields
    birthday = person.get('birthday', '') or ''
    death = person.get('death', '') or ''
    birthplace = person.get('birthplace', '') or ''
    deathplace = person.get('deathplace', '') or ''

    # Remove common date patterns from info if they match structured fields
    if birthday:
        pattern = re.compile(r'\bB\s+' + re.escape(birthday) + r'\b', re.IGNORECASE)
        info = pattern.sub('', info)

    if death:
        pattern = re.compile(r'\bD\s+' + re.escape(death) + r'\b', re.IGNORECASE)
        info = pattern.sub('', info)

    # Clean up extra whitespace
    info = re.sub(r'\s+', ' ', info).strip()
    info = re.sub(r';\s*$', '', info).strip()
    info = re.sub(r'\.\s*$', '.', info).strip()

    person['info'] = info


def resolve_death_and_birthplace(person):
    info = person.get('info', '') or ''

    # Try to extract death date if missing
    if not person.get('death'):
        death_match = re.search(r'\bD\s+(\d{1,2}\s+\w+\s+\d{4}|\w+\s+\d{4}|\d{4})\b', info, re.IGNORECASE)
        if death_match:
            person['death'] = death_match.group(1)

    # Try to extract birthplace if missing
    if not person.get('birthplace'):
        birth_match = re.search(r'\bB\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)', info, re.IGNORECASE)
        if birth_match:
            person['birthplace'] = birth_match.group(1)

    # Try to extract deathplace if missing
    if not person.get('deathplace'):
        death_place_match = re.search(r'\bD\s+\d{1,2}\s+\w+\s+\d{4}\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)', info, re.IGNORECASE)
        if death_place_match:
            person['deathplace'] = death_place_match.group(1)


def main():
    files = sorted(glob.glob(os.path.join(DATA_DIR, '*.json')))
    for path in files:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for person in data:
            resolve_death_and_birthplace(person)
            clean_info(person)

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f'Cleaned {os.path.basename(path)}')


if __name__ == '__main__':
    main()
