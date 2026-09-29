#!/usr/bin/env python3
"""Clean branch JSON info fields into structured properties."""

import json
import glob
import os
import re

DATA_DIR = r'C:\_Vicki_documents\online github - familytree petersoul.co.uk\src-content\branch\data'


def extract_birth_info(text):
    birth = {}
    m = re.search(r'\bbpt\s+(\d{1,2}\s+\w+\s+\d{4})', text, re.IGNORECASE)
    if m:
        birth['baptism'] = m.group(1)
    m = re.search(r'\bbapt\b', text, re.IGNORECASE)
    if m:
        birth['baptism'] = 'yes'
    m = re.search(r'\bB\s+(\d{1,2}\s+\w+\s+\d{4}|\w+\s+\d{4}|\d{4})\b', text, re.IGNORECASE)
    if m:
        birth['birthday'] = m.group(1)
    m = re.search(r'\bB\s+([A-Z][a-z]+(?:,\s*[A-Z][a-z]+)*)', text, re.IGNORECASE)
    if m and 'birthday' not in birth:
        birth['birthplace'] = m.group(1)
    return birth


def extract_death_info(text):
    death = {}
    m = re.search(r'\bD\s+(\d{1,2}\s+\w+\s+\d{4}|\w+\s+\d{4}|\d{4})\b', text, re.IGNORECASE)
    if m:
        death['death'] = m.group(1)
    m = re.search(r'\bbd\s+([A-Z][a-z]+(?:,\s*[A-Z][a-z]+)*)', text, re.IGNORECASE)
    if m:
        death['burial'] = m.group(1)
    m = re.search(r'\bD\s+\d{1,2}\s+\w+\s+\d{4}\s+([A-Z][a-z]+(?:,\s*[A-Z][a-z]+)*)', text, re.IGNORECASE)
    if m:
        death['deathplace'] = m.group(1)
    return death


def extract_census_info(text):
    censuses = []
    for m in re.finditer(r'(\d{4})\s+census,?\s+([^;]+)', text, re.IGNORECASE):
        censuses.append({'year': m.group(1), 'details': m.group(2).strip()})
    return censuses


def clean_info_text(person):
    info = person.get('info', '') or ''
    if not info:
        return

    # Remove birth date patterns
    info = re.sub(r'\bB\s+\d{1,2}\s+\w+\s+\d{4}\b', '', info, flags=re.IGNORECASE)
    info = re.sub(r'\bbpt\s+\d{1,2}\s+\w+\s+\d{4}\b', '', info, flags=re.IGNORECASE)
    info = re.sub(r'\bbapt\b', '', info, flags=re.IGNORECASE)
    info = re.sub(r'\bB\s+(?!\d)([A-Z][a-z]+(?:,\s*[A-Z][a-z]+)*)', '', info, flags=re.IGNORECASE)

    # Remove death date patterns
    info = re.sub(r'\bD\s+\d{1,2}\s+\w+\s+\d{4}\b', '', info, flags=re.IGNORECASE)
    info = re.sub(r'\bbd\s+[A-Z][a-z]+(?:,\s*[A-Z][a-z]+)*\b', '', info, flags=re.IGNORECASE)
    info = re.sub(r'\bD\s+\d{1,2}\s+\w+\s+\d{4}\s+[A-Z][a-z]+(?:,\s*[A-Z][a-z]+)*\b', '', info, flags=re.IGNORECASE)

    # Remove marriage patterns
    info = re.sub(r'\bM\s+\d{1,2}\s+\w+\s+\d{4}\s+[A-Z][a-z]+(?:,\s*[A-Z][a-z]+)*\b', '', info, flags=re.IGNORECASE)

    # Remove census patterns
    info = re.sub(r'\d{4}\s+census,?\s+[^;]+', '', info, flags=re.IGNORECASE)

    # Clean up punctuation
    info = re.sub(r'\s+', ' ', info).strip()
    info = re.sub(r';\s*;', ';', info)
    info = re.sub(r';\s*$', '', info)
    info = re.sub(r'\.\s*\.', '.', info)
    info = re.sub(r'^\s*[;,]+\s*', '', info)
    info = re.sub(r'\s*[;,]\s*$', '', info)
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

            birth_info = extract_birth_info(info)
            death_info = extract_death_info(info)
            census_info = extract_census_info(info)

            # Update structured fields if missing
            for key, value in birth_info.items():
                if key not in person or not person[key]:
                    person[key] = value
            for key, value in death_info.items():
                if key not in person or not person[key]:
                    person[key] = value

            # Store censuses in info if present
            if census_info:
                existing = person.get('census', [])
                for c in census_info:
                    if c not in existing:
                        existing.append(c)
                person['census'] = existing

            # Clean up info text
            clean_info_text(person)

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f'Cleaned {os.path.basename(path)}')


if __name__ == '__main__':
    main()
