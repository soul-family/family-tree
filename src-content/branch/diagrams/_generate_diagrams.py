#!/usr/bin/env python3
"""Generate simplified Mermaid family tree diagrams from branch JSON data using dev-guide syntax logic."""

import json
import os
import re

DATA_DIR = r'C:\_Vicki_documents\online github - familytree petersoul.co.uk\src-content\branch\data'
OUT_DIR = r'C:\_Vicki_documents\online github - familytree petersoul.co.uk\src-content\branch\diagrams'
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


def build_diagram(branch_name, people):
    by_id = {p['id']: p for p in people}
    lines = ['flowchart TD']
    emitted_couples = set()
    seen_nodes = set()

    def format_node(pid, parent2=False):
        person = by_id.get(pid)
        if not person:
            return pid
        label = person_label(person, parent2=parent2).replace('"', "'")
        return f'{pid}({label})'

    for person in people:
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

            # Inline node definitions on first edge
            p1_node = format_node(pid, parent2=False)
            p2_node = format_node(sid, parent2=True)

            if pid not in seen_nodes:
                lines.append(f'    {p1_node} === {p2_node}')
                seen_nodes.add(pid)
            else:
                lines.append(f'    {pid} === {p2_node}')

            seen_nodes.add(sid)

            # parent2 produces children with inline nodes
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
    return '\n'.join(lines)


def title_case_branch(branch):
    return branch.replace('_', ' ').title().replace('Clk', 'Clark')


def main():
    files = sorted(f for f in os.listdir(DATA_DIR) if f.endswith('.json'))
    for filename in files:
        branch = filename[:-5]
        path = os.path.join(DATA_DIR, filename)
        with open(path, 'r', encoding='utf-8') as fh:
            people = json.load(fh)
        diagram = build_diagram(branch, people)
        title = f'{title_case_branch(branch)} Family Tree - Simplified Diagram'
        content = f'# {title}\n\n```mermaid\n{diagram}\n```\n'
        out_path = os.path.join(OUT_DIR, f'{branch}.md')
        with open(out_path, 'w', encoding='utf-8') as fh:
            fh.write(content)
        print(f'Wrote {out_path}')


if __name__ == '__main__':
    main()
