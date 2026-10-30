# Family Tree v1 to v2 Conversion Skill

## Goal

Convert the v1 ASCII family tree structure (free-form ASCII art in branch pages) into the v2 structured format (per-branch JSON person records and Mermaid diagrams), with every relationship traceable to the v1 source.

## When to Use

- Converting a v1 branch page to v2 structured data
- Re-syncing v2 data after v1 source corrections
- Verifying v2 output against the original v1 source
- Adding a new family branch from an ASCII source

## Prerequisites

- v1 branch page with the family tree in a fenced code block
- ASCII expansion capability (widens the space between person columns)
- v1 structure reference (notation, layout rules, parsing challenges)
- v2 structure reference (JSON fields, ID conventions, Mermaid syntax, edge constraints)

## Workflow

### Step 1: Expand the ASCII (verification pass)

The v1 ASCII is hand-drawn: columns are separated by as little as one or two spaces, and horizontal branch lines are drawn with as few as one underscore, so entry and column boundaries are ambiguous. Expand the tree in both dimensions before any conversion:

1. Run the expansion tool over the branch page.
2. Horizontal, phase 1: gaps of 2 to (minimum gap - 1) spaces between segments become the minimum gap (8 by default); single-space gaps between structural segments (made only of `|`, `_`, `=`) are also widened; short underscore runs in structural positions (a leading `|` or `=` followed by underscores, or a segment made only of `|`, `_`, `=`) are lengthened to the minimum gap, so entry bars, corners and short branch lines all reach the same length; single spaces between words are preserved; larger gaps and longer underscore runs are preserved; a gap in front of a segment containing `|` is never widened, because that would move the pipe off its column.
3. Horizontal, phase 2 (column realignment): phase 1 widens by different amounts on different lines, because a column can be reached through leading indentation on one line and through a widened gap or a lengthened bar on another, which misaligns the vertical connectors. Phase 2 walks the anchor columns from left to right and adds the missing characters in front of the segment that holds each anchor, so every line puts the same anchor on the same expanded column. Spaces are only added, never removed. The anchors are the pipe characters and the columns where sibling names start, so the child markers of one parent line up the same way they did in the hand-drawn tree, and a bar keeps the same distance from its parent pipe. Two refinements matter: when the anchor is a pipe inside a bar or corner, the underscore run in front of it is lengthened, so the bar grows to meet its connector instead of being split; and when the anchor is a sibling name behind a marker run, that run is lengthened, so the bar grows instead of tearing the marker off its pipe.
4. Horizontal, phase 1 details worth remembering: a gap in front of a segment that starts with `|`, `_` or `=` is never widened, because that would move a pipe or a child marker off its column. An underscore run only counts as structural, and is only lengthened, when it starts a segment or follows a `|` or `=`; runs inside words, links and URLs follow a letter and are never touched.
4. Vertical: a blank line is inserted before every person entry (spouse, child, or bare-name entry start), except when the previous line is a connector run (`|` and `| |` lines) that shares a pipe column with the entry; that connection is continuous in the original, so no blank line is inserted and connector runs stay attached to the entries they lead into. Closing lines stay attached to the entry above; marriage detail lines stay attached to the couple above; a closing line that carries text is continued on the next line, so that text is not a new entry; existing blank lines are never doubled.
5. Expanded copies are written to the expanded ASCII output folder; original branch pages are never modified.
6. Verify the expanded copy: columns separated by the minimum gap, no short underscore runs remain in structural positions, all text segments match the original exactly, pipe columns that were aligned in the original are still aligned, connector runs stay continuous, and person entries are separated by blank lines unless a vertical connector links them to the line above.

### Step 2: Identify person entries

Read the expanded tree line by line. Entry markers:

- `= Name`, `=1 Name`, `=2 Name` - spouse (marriage order from the number)
- `_Name`, `___Name` - child of the couple above
- bare `Name` at line start - person; root of a subtree
- `M date place` lines - marriage details belonging to the couple above

### Step 3: Extract fields

- `B date` to birth date; `D date` to death date
- `bpt date` to sources (baptism); `bd place` to burial
- `s of` / `d of` phrases to parents
- `[Name](../branch.md#Anchor)` links to cross-branch references
- census, directory, and probate references to sources
- everything else to remaining info; original info keeps the raw v1 text

### Step 4: Assign person IDs

- known birth year: `{year}_{firstname}_{surname}`
- female with maiden name: `{year}_{firstname}__{maiden_name}`
- estimated interval: `{year1}_{year2}__{firstname}__{maiden_name}` (or `{year1}_{year2}__{firstname}_{surname}` for males)
- unknown birth year: `xxxx_` prefix; estimate intervals later from relatives (parents 20-40 years earlier, spouses similar, children 20-40 years later)

### Step 5: Build relationships

- spouse edges: person to each spouse, in marriage order
- parent-child: child entries (`_`) belong to the couple in whose column they appear
- each child links to both parents; the parent2 column carries the subtree

### Step 6: Generate the Mermaid diagram

- branch diagrams use `flowchart TD`; the combined diagram uses `flowchart LR`
- spouse edge: `parent1 ==o +parent2` (the `+` marks parent2 on the right/incoming side)
- parent-child edge: `parent ==o child` (no `+`)
- end every diagram with `linkStyle default stroke:#555`
- check the edge constraints: every node has at least one edge; each node appears on the right side at most once; non-root and non-leaf nodes have at least two edges

### Step 7: Verify against the v1 source

- every person in the ASCII appears in the JSON
- every spouse and child relationship appears in the diagram
- no invented connections: every edge traces to a v1 marker or column position
- gaps are recorded in the fix object (missing birthday, death, parents)

## Output Format

- per-branch JSON: array of person records
- per-branch Mermaid diagram
- combined JSON and diagram: merge all branches by person ID, concatenating info text and places when a person appears in multiple branches

## Verification

- [ ] expanded copy passes the segment-preservation check (all words identical, only spacing changed)
- [ ] every ASCII entry has a JSON record
- [ ] every relationship traces to a v1 marker or column
- [ ] diagram satisfies all edge constraints
- [ ] fix object lists all known gaps
- [ ] original branch page unchanged

## Notes

- The ASCII art is hand-drawn: columns drift a few characters between lines. Use the expanded copy for reading, but treat the original as the source of truth.
- Never invent connections that are not visible in the v1 source.
- Indentation alone cannot determine nesting; use entry markers and column position together.
- Closing lines (`_|`, `|_____|`) end a subtree; siblings can appear at deeper indents after a closing line.
- Text wraps within a column at arbitrary widths; continuation lines align under the start of the entry.
