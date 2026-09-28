# GEDCOM

## Description

GEDCOM (Genealogical Data Communications) is the standard file format for uploading and downloading family trees. GEDCOM is a text-only, universally accepted format that allows different genealogy software programs to exchange data. GEDCOM 5.5.1 does not include photos or media; GEDCOM 7.0 supports multimedia via GEDZip.

## Links

- https://gedcom.io/
- https://en.wikipedia.org/wiki/GEDCOM

## Why

- Text-only format ensures long-term portability and avoids vendor lock-in.

- Universal adoption means family tree data can be moved between tools without loss.

- Version-control friendly: line-based structure produces clean diffs and merges.

- Human-readable without special software for basic inspection.

- Standardized format for backup and transfer between genealogy software and websites.


## GEDCOM 5.5 vs 7.0

GEDCOM 5.5.1 final (released November 2019) remains the de facto industry standard for exchanging genealogical data. GEDCOM 7.0 (released May 2021, latest 7.0.18 as of February 2026) is the most recent specification, but adoption is still in progress.

Key differences:

- **Character encoding:** 5.5.1 allows UTF-8 but older tools often use ANSEL. 7.0 requires UTF-8 throughout.
- **Multimedia:** 7.0 introduces GEDZip, a ZIP-based format (`.gdz`) that carries the GEDCOM file alongside photos and media. Earlier versions could only link media externally; embedded media support was dropped in the 5.5.1 draft.
- **Ambiguity:** 7.0 clarifies ambiguities in 5.5.1, particularly around sources and extensions.
- **Semantic versioning:** 7.0 is the first version to use semantic versioning; 5.5.1 does not.
- **Nonexistent events:** 7.0 allows explicitly marking an event as nonexistent (e.g., documenting that someone never married).
- **Extensions:** 7.0 provides a standard way to identify proprietary extensions; 5.5.1 has no such mechanism.
- **Unicode:** 7.0 fully embraces Unicode for international names and places; 5.5.1 support varies by software.

## Importing GEDCOM into Ancestry

Ancestry accepts GEDCOM uploads up to 500MB. Only the tree owner can import a GEDCOM file; contributors and guests cannot.

Steps:

1. Sign in to Ancestry on a computer (the website, not the mobile app).
2. Click the Trees tab and select the destination tree, or create a new one.
3. In the left toolbar, click More (three dots) and choose Tree Settings.
4. Under Manage your tree, click Upload GEDCOM file.
5. Choose your `.ged` file and click Open.
6. Enter a name for the tree. Uncheck Make my family tree public if you want it private.
7. Click Upload.

Notes:

- GEDCOM files created on Ancestry before November 2022 do not include photos or media. Files created after that date preserve media location references, so if you re-upload the same GEDCOM later, Ancestry will relink the media if it is still available.
- Ancestry exports GEDCOM 5.5.1, which is readable by all major genealogy programs.

## Photos and Media in GEDCOM

Standard GEDCOM 5.5.1 does not include photos or media files in the `.ged` file itself. The file is text-only and contains names, dates, relationships, and source citations. Photos must be managed separately through the genealogy software or website.

GEDCOM 7.0 changes this with GEDZip (`.gdz`), a ZIP archive that bundles the `.ged` file with linked multimedia objects for sharing and archiving. Until GEDCOM 7.0 is widely supported, the practical approach is:

- Export the GEDCOM for data exchange.
- Export or sync media separately through your genealogy software (e.g., Family Tree Maker, RootsMagic).
- When uploading to Ancestry, note that media is not transferred via GEDCOM; it remains in your Ancestry media gallery.

## Syntax

Date format: DD MMM YYYY (e.g., 15 Jan 1850).

### Simple

```gedcom
0 HEAD
1 SOUR FamilyTreeJS
1 GEDC
2 VERS 5.5.1
2 FORM LINEAGE-LINKED

0 @I1@ INDI
1 NAME Grandfather /Smith/
1 SEX M

0 @I2@ INDI
1 NAME Grandmother /Smith/
1 SEX F

0 @I3@ INDI
1 NAME Father /Smith/
1 SEX M

0 @F1@ FAM
1 HUSB @I1@
1 WIFE @I2@
1 CHIL @I3@

0 TRLR
```

### Detailed

```gedcom
0 HEAD
1 SOUR FamilyTreeJS
1 GEDC
2 VERS 5.5.1
2 FORM LINEAGE-LINKED

0 @I1@ INDI
1 NAME Grandfather /Smith/
2 GIVN Grandfather
2 SURN Smith
1 SEX M
1 BIRT
2 DATE 15 Jan 1850
2 PLAC London, England

0 @I2@ INDI
1 NAME Grandmother /Smith/
2 GIVN Grandmother
2 SURN Smith
1 SEX F
1 BIRT
2 DATE ABT 1852
2 PLAC London, England

0 @I3@ INDI
1 NAME Father /Smith/
2 GIVN Father
2 SURN Smith
1 SEX M
1 BIRT
2 DATE ABT 1880
2 PLAC London, England

0 @I4@ INDI
1 NAME Uncle /Smith/
2 GIVN Uncle
2 SURN Smith
1 SEX M
1 BIRT
2 DATE ABT 1883
2 PLAC London, England

0 @F1@ FAM
1 HUSB @I1@
1 WIFE @I2@
1 CHIL @I3@
1 CHIL @I4@

0 TRLR
```

Approximate dates use Abt, Bef, or Aft. Women are recorded by maiden names. Nicknames go in quotation marks.
