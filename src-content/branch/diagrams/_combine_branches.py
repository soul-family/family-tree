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
    bday = (person.get('born', {}) or {}).get('date', '') or ''
    if not bday:
        return ''
    if len(str(bday)) == 4 and str(bday).isdigit():
        return str(bday)
    return str(bday)


def person_label(person, parent2=False):
    # Use full-name if available, otherwise fall back to name
    name_obj = person.get('name', {}) or {}
    full_name = name_obj.get('full-name') or name_obj.get('full', '') or person.get('full-name', '') or ''
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
        for p in people:
            if 'name' in p and isinstance(p['name'], dict):
                n = p['name']
                if 'full' in n:
                    n['full-name'] = n.pop('full')
                if 'maiden_name' in n:
                    n['maiden-name'] = n.pop('maiden_name')
            if 'gender' in p:
                g = p.pop('gender')
                p['cisgender'] = 'male' if g == 'M' else 'female' if g == 'F' else g
            rel = {}
            if 'spouses' in p:
                rel['spouses'] = p.pop('spouses')
            if 'children' in p:
                rel['children'] = p.pop('children')
            if 'parents' in p:
                rel['parents'] = p.pop('parents')
            if rel:
                p['relationship'] = rel
            if 'birth' in p:
                b = p.pop('birth')
                born = {}
                if 'date' in b:
                    born['date'] = b['date']
                if 'place' in b:
                    born['location'] = b['place']
                if born:
                    p['born'] = born
            if 'died' in p and isinstance(p['died'], dict):
                d = p['died']
                if 'place' in d:
                    d['location'] = d.pop('place')
                if 'burial' in d:
                    d['date-burried'] = d.pop('burial')
            if 'fix' in p:
                fix = p.pop('fix')
                if isinstance(fix, dict):
                    items = [f'{k}: {v}' for k, v in fix.items() if v]
                    if items:
                        p['todo'] = ', '.join(items)
            if 'sources' in p and isinstance(p['sources'], list):
                new_sources = []
                for s in p['sources']:
                    if isinstance(s, str):
                        if ':' in s:
                            key, val = s.split(':', 1)
                            new_sources.append({key.strip(): val.strip()})
                        else:
                            new_sources.append({'source': s})
                    else:
                        new_sources.append(s)
                p['sources'] = new_sources
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
                    if key in ('info', 'occupation', 'original-info', 'remaining-info'):
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
        rel = person.get('relationship', {}) or {}
        spouses = rel.get('spouses', []) or []
        children = rel.get('children', []) or []

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
