const fs = require('fs');
const path = require('path');

const files = [];
function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name === 'node_modules' || entry.name.startsWith('.kilo')) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      walk(full);
    } else if (entry.name.endsWith('.md')) {
      files.push(full);
    }
  }
}
walk('.');

function isTableLine(line) {
  const trimmed = line.trim();
  return trimmed.startsWith('|') && trimmed.endsWith('|');
}

function fixMarkdown(content) {
  const lines = content.split('\n');
  const result = [];
  let inCodeBlock = false;
  let hasChanges = false;

  for (let line of lines) {
    const trimmed = line.trim();
    if (trimmed.startsWith('```')) {
      inCodeBlock = !inCodeBlock;
      result.push(line);
      continue;
    }
    if (inCodeBlock) {
      result.push(line);
      continue;
    }

    if (isTableLine(line)) {
      result.push(line);
      continue;
    }

    const segments = [];
    let remaining = line;
    while (remaining.length > 0) {
      const codeStart = remaining.indexOf('`');
      if (codeStart === -1) {
        segments.push({ type: 'text', value: remaining });
        break;
      }
      if (codeStart > 0) {
        segments.push({ type: 'text', value: remaining.slice(0, codeStart) });
      }
      const codeEnd = remaining.indexOf('`', codeStart + 1);
      if (codeEnd === -1) {
        segments.push({ type: 'text', value: remaining.slice(codeStart) });
        break;
      }
      segments.push({ type: 'code', value: remaining.slice(codeStart, codeEnd + 1) });
      remaining = remaining.slice(codeEnd + 1);
    }

    const processed = segments.map(segment => {
      if (segment.type === 'code') return segment.value;

      let text = segment.value;

      text = text.replace(/\*{2,}([^\*\n]+?)\*{2,}/g, (match, content) => {
        return `**${content}**`;
      });

      text = text.replace(/(^|[^a-zA-Z0-9_])_([^_\n]+?)_([^a-zA-Z0-9_]|$)/g, (match, before, content, after) => {
        if (after === '' && before === '') return `*${content}*`;
        if (before === '') return `*${content}*${after}`;
        if (after === '') return `${before}*${content}*`;
        return `${before}*${content}*${after}`;
      });

      text = text.replace(/(^|[^\\*])\*([^\*\n]+?)\*([^*a-zA-Z0-9_]|$)/g, (match, before, content, after) => {
        if ((before === '*' && after === '*') || (before === '*' && after === '') || (before === '' && after === '*')) {
          return match;
        }
        if (after === '' && before === '') return `**${content}**`;
        if (before === '') return `**${content}**${after}`;
        if (after === '') return `${before}**${content}**`;
        return `${before}**${content}**${after}`;
      });

      return text;
    });

    result.push(processed.join(''));
  }

  return { content: result.join('\n'), hasChanges };
}

const checkOnly = process.argv.includes('--check');

let totalChanged = 0;
let totalIssues = 0;
for (const file of files) {
  let content = fs.readFileSync(file, 'utf8');
  const { content: newContent, hasChanges } = fixMarkdown(content);
  if (hasChanges) {
    totalIssues++;
    if (checkOnly) {
      console.log(`ISSUE: ${file}`);
    } else if (newContent !== content) {
      fs.writeFileSync(file, newContent);
      totalChanged++;
      console.log(`Fixed: ${file}`);
    }
  }
}

if (checkOnly) {
  console.log(`\n${totalIssues} files have markdown issues`);
  process.exit(totalIssues > 0 ? 1 : 0);
} else {
  console.log(`\nTotal files fixed: ${totalChanged}`);
}
