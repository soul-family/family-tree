#!/usr/bin/env python3
"""Create combined branch JSON and combined mermaid diagram."""

import json
import os
import re
from collections import defaultdict

DATA_DIR = r'C:\_Vicki_documents\online github - familytree petersoul.co.uk\src-content\branch\data'
OUT_DIR = r'C:\_Vicki_documents\online github - familytree petersoul.co.uk\src-content\branch'
os.makedirs(OUT_DIR, exist_ok=True)


def format_birthday(person):
    bday = person.get('birthday') or ''
    if not bday:
        return ''
    if len(str(bday)) == 4 and str(bday).isdigit():
        return str(bday)
    return str(bday)


def person_label(person, parent2=False):
    # Use full-name if available, otherwise fall back to name
    full_name = person.get('full-name') or person.get('name') or ''
    name = full_name.strip()
    bday = format_birthday(person)
    label = name
    if parent2:
        label = f'+{label}'
    if bday:
        label += f'<br/>{bday}'
    return label


def merge_field(existing, new_value):
    if not new_value:
        return existing
    if not existing:
        return new_value
    if existing == new_value:
        return existing
    return f'{existing}; {new_value}'


def main():
    # Load all branch data
    files = sorted(f for f in os.listdir(DATA_DIR) if f.endswith('.json'))
    all_people = []
    for filename in files:
        path = os.path.join(DATA_DIR, filename)
        with open(path, 'r', encoding='utf-8') as fh:
            people = json.load(fh)
            all_people.extend(people)

    # Merge by ID
    by_id = defaultdict(list)
    for p in all_people:
        pid = p.get('id')
        if pid:
            by_id[pid].append(p)

    merged_people = []
    for pid, persons in by_id.items():
        if len(persons) == 1:
            merged_people.append(persons[0])
        else:
            # Merge multiple occurrences
            merged = dict(persons[0])
            for p in persons[1:]:
                for key, value in p.items():
                    if key in ('spouses', 'children', 'parents', 'crossBranch', 'sources', 'census'):
                        continue
                    if key in ('info', 'occupation', 'birthplace', 'deathplace'):
                        merged[key] = merge_field(merged.get(key, ''), value)
                    elif key in ('birthday', 'death', 'gender'):
                        if not merged.get(key):
                            merged[key] = value
            merged_people.append(merged)

    # Write combined JSON
    combined_json_path = os.path.join(OUT_DIR, 'combined.json')
    with open(combined_json_path, 'w', encoding='utf-8') as fh:
        json.dump(merged_people, fh, indent=2, ensure_ascii=False)
    print(f'Wrote {combined_json_path}')

    # Build combined mermaid diagram
    by_id = {p['id']: p for p in merged_people}
    lines = ['flowchart TD']
    emitted_couples = set()
    seen_nodes = set()

    def format_node(pid, parent2=False):
        person = by_id.get(pid)
        if not person:
            return pid
        label = person_label(person, parent2=parent2).replace('"', "'")
        return f'{pid}({label})'

    for person in merged_people:
        pid = person.get('id')
        if not pid:
            continue
        spouses = person.get('spouses', []) or []
        children = person.get('children', []) or []

        for spouse in spouses:
            sid = spouse.get('id')
            if not sid or sid not in by_id:
                continue

            couple_key = tuple(sorted([pid, sid]))
            if couple_key in emitted_couples:
                continue
            emitted_couples.add(couple_key)

            p1_node = format_node(pid, parent2=False)
            p2_node = format_node(sid, parent2=True)

            if pid not in seen_nodes:
                lines.append(f'    {p1_node} === {p2_node}')
                seen_nodes.add(pid)
            else:
                lines.append(f'    {pid} === {p2_node}')

            seen_nodes.add(sid)

            for cid in children:
                if cid and cid in by_id:
                    c_node = format_node(cid, parent2=False)
                    if cid not in seen_nodes:
                        lines.append(f'    {sid} === {c_node}')
                        seen_nodes.add(cid)
                    else:
                        lines.append(f'    {sid} === {cid}')

        if not spouses and children:
            p_node = format_node(pid, parent2=False)
            if pid not in seen_nodes:
                lines.append(f'    {p_node} === {format_node(children[0], parent2=False)}')
                seen_nodes.add(pid)
                for cid in children[1:]:
                    if cid and cid in by_id:
                        c_node = format_node(cid, parent2=False)
                        if cid not in seen_nodes:
                            lines.append(f'    {pid} === {c_node}')
                            seen_nodes.add(cid)
                        else:
                            lines.append(f'    {pid} === {cid}')

    lines.append('')
    lines.append('    linkStyle default stroke:#555')

    diagram = '\n'.join(lines)
    combined_md_path = os.path.join(OUT_DIR, 'combined.md')
    with open(combined_md_path, 'w', encoding='utf-8') as fh:
        fh.write('# Combined Family Tree\n\n```mermaid\n')
        fh.write(diagram)
        fh.write('\n```\n')
    print(f'Wrote {combined_md_path}')


if __name__ == '__main__':
    main()
