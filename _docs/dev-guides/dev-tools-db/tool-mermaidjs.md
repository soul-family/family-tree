# Mermaid.js

## Description

Mermaid.js is the free, open-source diagramming library that powers text-to-diagram rendering. Mermaid is built on top of it, adding collaboration features, a visual editor, AI assistance, team workspaces, plugins, and enterprise support. It was founded by the creators behind Mermaid.js to bring professional tooling to the Mermaid ecosystem.

Mermaid.js does not natively support responsive family trees with horizontal relationships links as a dedicated diagram type, often resulting in cluttered vertical flowcharts. Users typically create family trees using graph TD (Top-Down) or graph LR (Left-Right) syntax, but this lacks specific pedigree features like connecting spouses horizontally.

## Links

- https://mermaid.ai/open-source/
- https://github.com/mermaid-js/mermaid
- https://github.com/mermaid-js/mermaid/issues/1747
- https://github.com/mermaid-js/mermaid/issues/1589
- Made by: https://mermaid.ai

## Why 

- Diagrams are text-based and live alongside your code, making them easy to version control and integrate into your development workflow.

- Teams can collaborate to maintain consistency across docs, and tool actions create the diagrams.

- Flowchart top to bottom syntax closest to family tree.


### Simple example

```mermaid
flowchart TD
    grandmother === +grandfather
    +grandfather === father
    +grandfather === mother2

    father === +mother
    +mother === child1
    +mother === child2

    mother2 === +father2
    +father2 === child3

    linkStyle default stroke:#555
```

### Detailed example

```mermaid
flowchart TD

    great-grandfather(
        great-grandfather
        b.1800
        )
        === great-grandmother(
                +great-grandmother
                b.1805
                )

    great-grandmother 
        === grandfather1(
            grandfather1<br/>b.1825
            )
    great-grandmother 
        === grandmother2(
            grandmother2<br/>b.1830
            )
    
    grandfather1 
        === grandmother1(
            +grandmother1<br/>b.1838
            )
    grandmother2(
            grandmother2<br/>b.1832
            ) 
        === grandfather2(
    +grandfather2<br/>b.1828
    )

    grandfather2 
        === mother2(
            mother2<br/>b.1852
            )
    grandmother1 
        === father1(
            father1<br/>b.1828
            )
    
    father1 
        === mother1(
            +mother1
            )

    mother1 
        === child1

    mother1 
        === child2(
            child2<br/>b.1883
            )
    
    mother2 
        === father2(
            +father2
            )
    father2
        ===
     child3(
            child3<br/>b.1885
            )

    linkStyle default stroke:#555,stroke-width:2px
```

### Syntax logic

- `+` prefix marks parent 2, the incoming parent who carries the subtree.
- Parent 1 connects to parent 2 with exactly one direct link.
- Parent 2 produces the next generation: children or further subtrees.
- Every child receives links from both parents.
- Node IDs are person IDs from branch JSON files:
  - Known birth year: `birthday_firstname_famname` (e.g., `1845_thomas_dickerson_smith`)
  - Unknown birth year (estimated interval): `year1_year2__firstname__maiden_name` (females) or `year1_year2__firstname_surname` (males) (e.g., `1776_1814__james_clarke`)
- Nodes use plain parenthesis () with markdown label text displaying name and birthday on a new line using `<br/>`.
- Edges use `===` and `linkStyle default stroke:#555`.

#### Example with real branch IDs

Using `smith.json` as an example:

| Person | ID | Role |
|--------|----|------|
| Thomas Dickerson Smith | `1845_thomas_dickerson_smith` | parent 1 to Elizabeth Simmonds Soul |
| Elizabeth Simmonds Soul | `+1841_elizabeth_simmonds_soul` | parent 2, carries subtree |
| Joseph Soul Smith | `1875_joseph_soul_smith` | child of both parents |
| Leslie Joseph Soul Smith | `1905_leslie_joseph_soul_smith` | child, later parent 1 to Hilda Harmer |
| Hilda Elizabeth Harmer | `+1904_hilda_elizabeth_harmer` | parent 2, carries subtree to Ethel |
| Ethel Margaret Smith | `1908_ethel_margaret_smith` | child of both parents |

#### Example with estimated birth year intervals

For persons with unknown birth years, intervals are estimated from family connections:

| Person | Old ID | New ID | Interval Basis |
|--------|--------|--------|----------------|
| James Clarke | `xxxx_james_clarke` | `1776_1814__james_clarke` | Children born 1798-1834 |
| Sarah Clarke | `xxxx_sarah_clarke` | `1776_1814__sarah_clarke` | Same as spouse |
| Elizabeth Simmonds | `xxxx_elizabeth_simmonds` | `1762_1800__elizabeth_simmonds` | Children born 1790-1820 |
