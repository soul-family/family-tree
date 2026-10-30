# Roberts Family Tree

```mermaid---
config:
  flowchart:
    defaultRenderer: elk
---
flowchart LR
    %% Source: original Roberts family account and explicit user corrections.
    %% Samuel: age 58 in the 1871 census implies 1812–1813.
    %% Death on 19 Apr 1871, aged 57, implies 1813–1814.
    %% Retain the covering interval 1812–1814; the ages conflict.
    1812-1814_samuel_roberts["Samuel Roberts<br/>b. c. 1812–1814<br/>d. 1871"]:::person

    %% Martha: ages 48 in 1861 and 58 in 1871 imply 1812–1813.
    %% Maiden surname recorded as Chiven and Chivin; preserve both spellings.
    1812-1813_martha__chiven["Martha (Chiven / Chivin)<br/>b. c. 1812–1813"]:::person

    %% Roberts children declared by ascending birth year.
    %% Equal birth keys retain source order; this does not establish birth order.
    1839_eliza_roberts["Eliza Roberts<br/>b. 25 Sept 1839"]:::person
    1842_ann_roberts["Ann Maria Roberts<br/>b. 1 Aug 1842"]:::person
    1847_martha_roberts["Martha Roberts<br/>b. 1847 Q4"]:::person
    1847_samuel_roberts["Samuel Roberts<br/>b. 1847 Q4"]:::person

    %% John: age 21 at marriage on 23 Apr 1867 implies 1845–1846.
    %% Usable age evidence takes priority over fallback estimates.
    1845-1846_john_cockin["John Cockin<br/>b. c. 1845–1846"]:::person

    %% George: documented father of John; no birth or usable age evidence.
    %% Parent-from-child fallback assumes parental ages 15–60.
    %% John's age-derived interval gives 1845−60 to 1846−15 = 1785–1831.
    %% This is a provisional modelling estimate, not a documented birth bound.
    %% No other applicable fallback interval is supplied by the source.
    1785-1831_george_cockin["George Cockin<br/>b. est. 1785–1831"]:::person

    %% Source explicitly documents Samuel and Martha as married.
    %% No marriage year is supplied. Samuel is parent1; Martha is parent2.
    1812-1814_samuel_roberts ---|married| 1812-1813_martha__chiven

    %% Only parent2 points to their shared children, in birth-year order.
    1812-1813_martha__chiven --> 1839_eliza_roberts
    1812-1813_martha__chiven --> 1842_ann_roberts
    1812-1813_martha__chiven --> 1847_martha_roberts
    1812-1813_martha__chiven --> 1847_samuel_roberts

    %% Ann Maria Roberts and John Cockin married 23 Apr 1867 at St Mary's, Hull.
    %% Ann Maria is first-listed; John is second-listed.
    %% No children of this marriage are documented in the supplied source.
    1842_ann_roberts ---|1867| 1845-1846_john_cockin

    %% George is John's only documented parent in the supplied source.
    1785-1831_george_cockin --> 1845-1846_john_cockin

    classDef person stroke:#666666;
    linkStyle default stroke:#555
```
