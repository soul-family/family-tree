# SchemaTex

## Description


Schematex is open-source rendering and editing engine for the diagrams professionals actually use: medical, electrical, legal, production, and analytical. 52 diagram families spanning medicine, engineering, law, live production, and analysis.

For the family tree the relashipship pedigree diagram is the closest.

## Links

- https://schematex.js.org
- https://github.com/SchemaTex/SchemaTex
- https://schematex.js.org/playground
- https://schematex.js.org/docs/pedigree
- https://en.wikipedia.org/wiki/Pedigree_chart
- Made by: https://MyMap.ai

## Why 

- Diagrams are text-based and live alongside your code, making them easy to version control and integrate into your development workflow.

- Teams can collaborate to maintain consistency across docs, and tool actions create the diagrams.

- Diagrams rendered as a deterministic SVG.

- SVG is the best export when the drawing will be printed, embedded in a document, or edited later because lines and text remain sharp at any size. 

## Syntax

A pedigree chart uses standardized shapes, fills, and descent lines to show the tree structure.

### Simple

```text
pedigree "Family Tree"
  grandfather [male]
  grandmother [female]
  grandfather -- grandmother
    father [male]
    uncle [male]
```

### Detailed

```text
pedigree "Family Tree"
  grandfather [male, label: "grandfather (b.1850)"]
  grandmother [female, label: "grandmother (b.1852)"]

  grandfather -- grandmother
    father [male, label: "father (b.1880)"]
    uncle [male, label: "uncle (b.1883)"]
```

Individuals are declared with an ID and optional attributes. Couples are connected with `--` and children are indented under the couple line.
