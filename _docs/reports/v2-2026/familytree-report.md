# Soul Family Tree Archive - Family Tree Report

## Report: Branch Tree Connections and Data Improvements

**Date:** 2026-10-12  
**Scope:** All 16 family branches, combined tree, Mermaid diagrams, JSON data  
**Status:** Complete (data and diagram work paused; ASCII recognition pending)

**Structure references:** The v1 ASCII structure is documented in [familytree-v1-structure.md](familytree-v1-structure.md) and the v2 JSON and Mermaid structure in [familytree-v2-structure.md](familytree-v2-structure.md).

---

## Executive Summary

This report documents the improvements made to the family tree branch data, JSON schemas, Mermaid diagram generation, and combined tree connections. The work focused on cleaning person IDs, extracting structured data from free-text notes, fixing parent-child relationships, and ensuring all subtrees connect correctly through common persons in the combined view. The v1 structure, v2 structure, and the comparison between them are maintained in dedicated structure documents.

---

## 1. The Journey

### 1.1 Branch JSON Schema Standardization

- Created a branch JSON schema as the single source of truth for all branch person records.
- Normalized all 16 branch JSON files to use the schema.
- Shortened person IDs from `birthday_name_initials` to `birthday_firstname_famname` for readability and cross-file matching.

### 1.2 Info Text Cleanup and Structured Extraction

The `info` fields in branch JSON contained redundant free-text patterns (birth dates, death dates, places, baptisms, burials, census records) that duplicated structured fields.

Cleaning tools were created to:

- Extract `baptism`, `burial`, and `census` records into structured fields
- Parse `s of` and `d of` patterns into the `parents` object
- Remove redundant date/place patterns from the remaining info text

**Example:** a marriage record stating "she was daughter of Samuel Clark tailor" moved into the `parents.father` field, with the free text retained in `original-info`.

### 1.3 Mermaid Diagram Generation

Per-branch diagrams and the combined diagram were generated from the JSON data with standardized syntax, inline node definitions, and parent2 markers. Diagram logic ensures parent1 connects only to parent2, parent2 carries the subtree and produces children, every child has links from both parents via parent2, and parent1 never connects directly to children.

### 1.4 Combined Tree Fixes

The combined tree had missing or incorrect connections between subtrees. Common persons appearing in multiple branches were not properly linked, causing disconnected fragments instead of a unified family network.

Key fixes:

1. **Hannah Clark parentage:** updated to have Samuel Clark tailor as her father, matching the marriage record; removed her from James Clarke & Sarah's children.
2. **Samuel Clark tailor:** ensured he is properly connected as father of Hannah Clark in both JSON data and the combined diagram.
3. **Samuel Clark b. 1834:** verified he has no children or spouses in source data, preventing incorrect tree connections.
4. **Cross-branch links:** verified all references point to valid person IDs in other branch files.
5. **Duplicate ID handling:** the merge logic concatenates info, birthplace, deathplace, and occupation when the same person appears in multiple branches.
6. **Duplicate edge removal (2026-10-09):** fixed 4 duplicate edges (Charles Coles-Hannah Coles; Dorothea Wilson-John/Joan/Elaine Soul). Root cause: edges were emitted from both the spouse loop and the parent-reference loop; an emitted-edge set now prevents duplicates.
7. **Duplicate person merging (2026-10-09):** enhanced merge logic with fuzzy birthday matching (±1 year). Merged the 1906 and 1907 Denis Soul entries (same name, birthdays off by one year). Total persons reduced from 690 to 689.

### 1.5 Birth Year Interval Estimation for Unknown Birth Years

165 persons had `xxxx_` prefix IDs indicating unknown birth years, preventing proper sorting and timeline-based connections.

A tool was created to estimate birth year intervals from family connections (parents, spouses, children), with outlier filtering for modern dates. Results: 41 of 165 persons received estimated intervals (25%); the remaining 124 have no connected relatives with known birth years. All cross-references were updated across the 16 branch JSONs and the combined JSON.

| Old ID | New ID | Interval | Basis |
|--------|--------|----------|-------|
| `xxxx_james_clarke` | `1776_1814__james_clarke` | 1776-1814 | Children born 1798-1834 |
| `xxxx_sarah_clarke` | `1776_1814__sarah_clarke` | 1776-1814 | Same as spouse |
| `xxxx_elizabeth_simmonds` | `1762_1800__elizabeth_simmonds` | 1762-1800 | Children born 1790-1820 |
| `xxxx_joseph_jacobsohn` | `1828_1849__joseph_jacobsohn` | 1828-1849 | Parents born 1838/1839 |

### 1.6 Documentation Restructure and Conversion Preparation (2026-10-12)

- The family tree report was restructured: this report now holds the journey, the comparison, and the report; the v1 and v2 structures moved to dedicated structure documents.
- The v1 ASCII structure was documented, including notation, layout rules, and parsing challenges.
- An ASCII expansion capability was created to widen the space between person columns and insert a blank line before each person entry in v1 trees, producing expanded copies for verification. Original branch pages are not modified.
- The v1 to v2 conversion process was documented as a reusable skill.
- Data and diagram work is paused until the ASCII is recognised properly; the expanded ASCII verification pass comes first.

---

## 2. The Comparison

### v1 vs v2

| Aspect | v1 (ASCII Markdown) | v2 (JSON + Mermaid) |
|--------|---------------|---------------------|
| **Structure** | ASCII art with embedded text | Structured JSON with defined schema |
| **Dates** | Mixed in free text (`D 30 Aug 1854`) | Separate `birth` and `died` fields |
| **Places** | Mixed in free text (`Cheapside. City of London`) | Separate `birthplace`/`place` fields |
| **Relationships** | Implied by ASCII tree | Explicit `spouses`, `children`, `parents` arrays |
| **IDs** | None | `birthday_firstname_famname` or interval format for cross-branch linking |
| **Diagrams** | ASCII art only | Mermaid diagrams with syntax logic |
| **Combined view** | Not possible | Combined JSON and diagram merge all branches |
| **Validation** | Manual review | JSON schema plus scripts |
| **Abbreviations** | `bd`, `bpt`, `s of`, `d of` | Expanded to `buried`, `baptised`, `son of`, `daughter of` |

### Abbreviation Conventions

The original v1 info text used common genealogical abbreviations, identified by surveying all 16 branch files:

| v1 Abbreviation | v2 Expansion | Example |
|-----------------|--------------|---------|
| `bd` | `buried` | `bd London` → `buried London` |
| `bpt` | `baptised` | `bpt 25 Mar 1763` → `baptised 25 Mar 1763` |
| `s of` | `son of` | `s of James Clarke` → `son of James Clarke` |
| `d of` | `daughter of` | `d of Samuel Clark` → `daughter of Samuel Clark` |
| `B` | moved to birth field | `B 15 Jan 1850` → `birth.date` |
| `D` | moved to death field | `D 30 Aug 1854` → `died.date` |
| `M` | moved to marriage field | `M 22 Aug 1852` → `spouses.marriedDate` |

### Before/After Example: Hannah Clark

**v1 (free text in ASCII art):**

```
|______________Hannah (Clark) D 30 Aug 1854, 1 Bird-in-Hand Court, Cheapside. City of London,
               25, wife of Charles John Coles billiard marker, uterine haemorrhage.
```

**v2 (structured record):**

```json
{
  "id": "1829_hannah_clark",
  "name": { "full": "Hannah Clark", "firstname": "Hannah", "surname": "Clark" },
  "birth": { "date": "1829-10-06" },
  "died": { "date": "1854-08-30", "place": "1 Bird-in-Hand Court, Cheapside, City of London" },
  "parents": { "father": "samuel_clark_tailor", "mother": "" },
  "remaining-info": "aged 25, wife of Charles John Coles billiard marker, uterine haemorrhage"
}
```

The v2 format separates structured data (dates, places, relationships) from free-text notes, making the data queryable, combinable, and suitable for generating diagrams automatically.

---

## 3. Report

### Combined Tree Structure

The combined tree includes all 16 branches:

Bailey, Clark & Unwin, Cockin, Coles, Fletcher, Giles, Handley, Hankin, Holt, Hone, Jacobsohn & Cohen, Roberts, Simmonds, Smith, Soul, Wilson

Total persons: ~689 (after duplicate merging)  
Total connections: ~268 edges

### Remaining Issues

1. **Parent conflicts:** some persons have conflicting parent information in the original markdown (e.g., Hannah Clark appears as daughter of both James Clarke & Sarah and Samuel Clark tailor). The current fix uses the marriage record as authoritative, but original birth records should be reviewed.

2. **Missing data:** some persons have empty birth, death, or parent fields due to incomplete original records.

3. **Cross-branch IDs:** some cross-branch references use old IDs (e.g., `CharlesJohnColes`) that don't match the new format. These should be updated.

4. **Samuel Clark b. 1834:** no children or spouses found in source data. If additional research reveals descendants, they should be added.

5. **Data entry errors in birthdays:** fuzzy matching (±1 year) catches some birthday inconsistencies (e.g., Denis Soul 1906 vs 1907). Original records should be verified to confirm correct birth years.

6. **Unknown birth years:** 124 persons retain the `xxxx_` prefix with no estimable birth year interval due to lack of connected relatives with known dates.

7. **ASCII recognition:** the v1 ASCII art is not yet recognised reliably (column drift, tight spacing). Conversion to v2 is paused until the expanded ASCII verification pass completes.

### Recommendations

1. Review all `parents` fields against original marriage and baptism records
2. Update cross-branch IDs to match the new ID format
3. Add missing birth and death data where original records are available
4. Validate combined tree connections by reviewing the combined diagram
5. Complete the ASCII expansion verification pass, then run the v1 to v2 conversion skill
6. Consider adding a visual tree view to the branch pages using the generated Mermaid diagrams

---

## 4. Changelog Entry

```markdown
## [Unreleased]

### Added

- Branch JSON schema for all 16 family branches
- Per-branch Mermaid diagrams with inline node syntax
- Combined branch JSON merging all persons by ID
- Combined family tree diagram connecting all subtrees
- Tools for cleaning, extracting, shortening IDs, and generating diagrams
- Birth year interval estimation for unknown-birth-year persons
- New ID format for estimated persons: `year1_year2__firstname__maiden_name` (females) or `year1_year2__firstname_surname` (males)
- Dedicated v1 and v2 structure documents for the family tree
- ASCII expansion capability for v1 tree verification
- v1 to v2 conversion skill

### Changed

- Person IDs shortened to `birthday_firstname_famname`
- Person IDs for unknown birth years now use interval format
- Mermaid node syntax standardized with parent2 marker only in labels
- Edge syntax standardized
- Parent extraction uses `s of`/`d of` patterns from info text
- Info text cleaned of redundant date/place/baptism/burial/census patterns
- 41 unknown-birth-year persons updated with estimated birth year intervals (1600-1950)
- Cross-references updated across all 16 branch JSONs and combined JSON
- Family tree report split into journey, comparison, and report; structure details moved to dedicated structure documents

### Fixed

- Hannah Clark parentage updated to match marriage record
- Removed Hannah Clark from James Clarke and Sarah's children
- Combined tree now properly connects subtrees through common persons
- Parent fields now reference person IDs instead of empty strings or names
- 4 duplicate edges removed from combined diagram
- Duplicate person entries merged (1906 and 1907 Denis Soul) via fuzzy birthday matching (±1 year)
- Total combined persons reduced from 690 to 689
```
