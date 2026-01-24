# UID Constitution (v2)

This document governs the symbolic, structural, and file naming system used across your entire OS—including creative documents, course materials, project files, folders, and internal registries.

## UID Format

### Expanded Format (Visible or Annotated)
**Format:** `AB-CD_12-34`
- `AB`: Two consonants from the first key word (e.g., `PR` for *process*)
- `CD`: Two consonants from the second key word (e.g., `NS` for *analysis*)
- `12`: Unit or version number
- `34`: Item/block number within that unit
- Used in comments, markdown metadata, Obsidian hover-notes, section headers, file maps

### Condensed Format (For File & Folder Names)
**Format:** `ABCD1234`
- Strip all symbols (`-`, `_`) to produce minimal, portable UIDs
- Used in folder names, Obsidian filenames, asset registries, cloud-safe export names

## UID Use Cases
| Context          | Expanded UID     | Condensed | Meaning                                  |
|------------------|------------------|-----------|------------------------------------------|
| Compare Prompt   | `CM-CN_03-04`    | `CMCN0304`| Compare–Contrast, Unit 3, Prompt 4        |
| Process Folder   | `PR-NS_02-00`    | `PRNS0200`| Process–Analysis, Unit 2, Folder 00       |
| Argument Rubric  | `AR-RG_04-RU`    | N/A       | Argument–Rebuttal Ground, Rubric file     |
| Portfolio Meta   | `PF-RT_05-M1`    | N/A       | Portfolio–Reflection Thread, meta entry 1 |

## Placement Protocol
- **Markdown:** Use expanded format as comment block above each section or assignment block:
  ```markdown
  <!-- UID: CM-CN_03-07 -->
  ```

- **Filenames:** Use condensed format, lowercase optional:
  - `CMCN0304_thesis-builder.md`
  - `PFRT0500_final_reflection.docx`

- **Folders:** Use condensed UID as prefix, e.g.:
  - `CMCN0300_compare-contrast/`
  - `ARRG0400_argument-essay/`

## UID System Notes
- Always use consonants only unless needed for clarity
- Avoid UID duplication across namespace
- Use `00` suffixes for general or system-wide docs in each module
- UIDs apply to creative, symbolic, and instructional assets equally

## Tracker Files (Required Per Folder)
- `UID_MAP.md`: Lists all used UIDs in this folder/project
- `REVISION_HISTORY.md`: Documents all UID-level changes and file updates
- `README.md`: High-level overview, purpose, UID prefix explanation