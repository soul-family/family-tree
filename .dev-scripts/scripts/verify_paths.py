import os
import re
from urllib.parse import urlparse

base = r"C:\_Vicki_documents\online github - familytree petersoul.co.uk\src-content"

# Collect all HTML files
html_files = []
for root, dirs, files in os.walk(base):
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

html_files = [f for f in html_files]
html_basenames = {os.path.basename(f) for f in html_files}

def resolve_path(base_dir, href):
    if href.startswith('http://') or href.startswith('https://') or href.startswith('//'):
        return None
    
    href = href.split('#')[0]
    href = href.split('?')[0]
    
    if not href or href == '/':
        return None
    
    if href.startswith('/'):
        return os.path.normpath(os.path.join(base, href.lstrip('/')))
    
    path = os.path.normpath(os.path.join(base_dir, href))
    
    if os.path.isdir(path):
        for candidate in ['index.html', 'default.html']:
            if os.path.exists(os.path.join(path, candidate)):
                return os.path.join(path, candidate)
        return path
    
    if not path.endswith('.html'):
        if os.path.isdir(path):
            for candidate in ['index.html', 'default.html']:
                if os.path.exists(os.path.join(path, candidate)):
                    return os.path.join(path, candidate)
        return path
    
    return path

issues = []

for html_file in html_files:
    base_dir = os.path.dirname(html_file)
    rel_file = os.path.relpath(html_file, base)
    
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    hrefs = re.findall(r'href="([^"]+)"', content)
    hrefs += re.findall(r"href='([^']+)'", content)
    srcs = re.findall(r'src="([^"]+)"', content)
    srcs += re.findall(r"src='([^']+)'", content)
    
    for href in hrefs:
        if href.startswith('#') or href.startswith('mailto:') or href.startswith('tel:'):
            continue
        resolved = resolve_path(base_dir, href)
        if resolved and not resolved.startswith(base):
            issues.append(f"OUTSIDE BASE: {rel_file} -> {href}")
        elif resolved and not os.path.exists(resolved):
            issues.append(f"BROKEN LINK: {rel_file} -> {href} (resolved: {os.path.relpath(resolved, base)})")
    
    for src in srcs:
        if src.startswith('http://') or src.startswith('https://') or src.startswith('//'):
            continue
        resolved = resolve_path(base_dir, src)
        if resolved and not os.path.exists(resolved):
            issues.append(f"BROKEN SRC: {rel_file} -> {src} (resolved: {os.path.relpath(resolved, base)})")

if issues:
    print(f"Found {len(issues)} issues:")
    for issue in issues[:50]:
        print(f"  {issue}")
else:
    print("All URLs and paths are valid")
