# Family Tree v1 Structure - Original ASCII Format

## Overview

The original family tree archive stores each family branch as a markdown page containing a single fenced code block with a free-form ASCII family tree. Person information is embedded in the ASCII art as free text. There are no structured fields, person IDs, or machine-readable relationships in v1.

## Notation

| Marker | Meaning | Example |
|--------|---------|---------|
| `Name` (bare, at line start) | Person; root of a subtree | `James Clarke` |
| `= Name` | Spouse (marriage) | `= Sarah` |
| `=1 Name`, `=2 Name` | First, second spouse (marriage order) | `=1 [Samuel Unwin](../clark_unwin/).` |
| `_Name` or `___Name` | Child of the couple above | `_Hephzibah Clarke B 29 Oct 1816` |
| `|` | Vertical connector; continues a column | `| d of James Clarke & Sarah` |
| `_|`, `|_____|` | Closing line; ends a subtree | `|____________|` |
| `M date place` | Marriage details | `M 21 Mar 1853 St Matthew's Bethnal Green` |
| `B date` | Birth date | `B 29 Oct 1816` |
| `D date` | Death date | `D 30 Aug 1854` |
| `bpt date` | Baptism date | `bpt 21 Mar 1830` |
| `bd place` | Burial place | `bd Highgate Cemetery` |
| `s of`, `d of` | Son of, daughter of | `d of James Clarke & Sarah` |
| `aged N` | Age at death | `aged 25` |
| `gv n sq n` | Grave reference | `gv 36555 sq 117` |
| `YYYY census` | Census record reference | `1861 census, Bird in Hand Court` |
| `[Name](../branch.md#Anchor)` | Cross-branch link | `[Charles John Coles](../coles.md#CharlesJohnColes)` |

## Layout Rules

1. Each person occupies a vertical column below their entry marker.
2. A person's details continue on following lines, aligned under the start of the entry.
3. Spouses are added below the person with `=`; children with `_`.
4. Sibling columns sit side by side on the same physical line, separated by spaces.
5. A closing line (`_|` or `|_____|`) ends the current subtree and returns to the parent column.
6. Blank lines separate top-level persons.
7. Marriage details (`M ...`) belong to the couple above them.

## Example

From the Clark & Unwin branch:

```
James Clarke

 = Sarah
 |             _Hephzibah Clarke B 29 Oct 1816, bpt at the Meeting House,
 |            | d of James Clarke & Sarah of the parish of Gt Waltham, Essex.
 |____________|
               |  =2 [Samuel Unwin](../clark_unwin/).
```

Reading: James Clarke married Sarah. Their daughter Hephzibah Clarke was born 29 Oct 1816 and baptised at the Meeting House; she was the daughter of James Clarke & Sarah of the parish of Gt Waltham, Essex. Sarah's second marriage (marriage order 2) was to Samuel Unwin.

## Parsing Challenges

The ASCII art is hand-drawn, which causes recognition problems when converting to v2:

- **Column drift**: columns shift a few characters between lines because the art was aligned by eye.
- **Multiple entries per line**: several person columns coexist on one physical line.
- **Indentation is not nesting**: siblings can appear at deeper indents after closing lines, so indentation alone cannot determine parentage.
- **Text wrapping**: a person's details wrap across lines at arbitrary widths.
- **Tight spacing**: columns are sometimes separated by only one or two spaces, so entry boundaries are ambiguous.

These challenges are why the ASCII is expanded (spacing widened, lines lengthened, entries separated) before conversion to v2. The expansion pass runs in two horizontal phases and one vertical phase. Phase 1 widens column gaps to a minimum separation and lengthens short horizontal lines (entry bars, corners, branch lines) to the same minimum. Because phase 1 widens by different amounts on different lines, phase 2 realigns the columns: it walks the anchor columns from left to right and adds the missing characters in front of the segment that holds each anchor, so pipes that shared a column in the hand-drawn tree still share a column afterwards, and the child markers of one parent still line up the same way. Where the anchor is a pipe inside a bar, the underscore run in front of it is lengthened so the bar grows to meet its connector; where the anchor is a sibling name behind a marker run, that run is lengthened so the bar grows instead of tearing the marker off its pipe. The vertical phase then inserts a blank line before each person entry unless a connector run links it to the line above, so the hand-drawn connections stay continuous. Original branch pages are not modified. See the family tree v1 to v2 conversion skill for the conversion pipeline.
