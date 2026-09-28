# FamilyTreeJS

## Description

FamilyTreeJS is an interactive family tree visualization library by BALKANGraph that renders pedigree diagrams from structured JSON data. It supports both family and pedigree views, making it the closest out-of-the-box match for the family tree archive's diagramming needs.

For the archive it provides a ready-made pedigree renderer with pan, zoom, and drag interactions without hand-rolling SVG layout.

## Links

- https://balkangraph.com/family-tree-js/
- https://github.com/BALKANGraph/OrgChartJS
- https://balkangraph.com/family-tree-js/demo/
- https://balkangraph.com/family-tree-js/docs/
- Made by: https://balkangraph.com

## Why

- Diagrams are JSON-driven and deterministic, making them easy to version control and regenerate from source data.

- Pedigree and family view modes are built in, reducing the amount of custom layout work required.

- Interactive rendering with pan, zoom, expand/collapse, and touch support.

- Deterministic SVG output keeps lines and text sharp at any size, suitable for print or embedding.

## Syntax

Input is JSON with nested person nodes and relationship links.

### Simple

```json
{
  "treeStructure": {
    "name": "grandfather",
    "spouses": [
      { "name": "grandmother" }
    ],
    "children": [
      {
        "name": "father",
        "children": [
          { "name": "child1" },
          { "name": "child2" }
        ]
      },
      {
        "name": "uncle",
        "children": [
          { "name": "cousin1" }
        ]
      }
    ]
  }
}
```

### Detailed

```json
{
  "treeStructure": {
    "name": "grandfather",
    "birthDate": "1850-01-15",
    "birthPlace": "London, England",
    "spouses": [
      {
        "name": "grandmother",
        "birthDate": "1852-01-01",
        "birthPlace": "London, England"
      }
    ],
    "children": [
      {
        "name": "father",
        "birthDate": "1880-05-20",
        "birthPlace": "London, England",
        "children": [
          {
            "name": "child1",
            "birthDate": "1910-03-10",
            "birthPlace": "London, England"
          },
          {
            "name": "child2",
            "birthDate": "1912-07-04",
            "birthPlace": "London, England"
          }
        ]
      },
      {
        "name": "uncle",
        "birthDate": "1883-11-30",
        "birthPlace": "London, England",
        "children": [
          {
            "name": "cousin1",
            "birthDate": "1915-09-01",
            "birthPlace": "London, England"
          }
        ]
      }
    ]
  }
}
```
