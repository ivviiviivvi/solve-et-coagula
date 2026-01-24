# CLONE_PROTOCOL.md

This protocol explains how to clone a complete instance of the 4_S0VRC3 symbolic OS for a new project, course, or persona.

## Step-by-Step:

### 1. Run the Genesis Script
- Use `initialize_vault.py` to create the full folder structure.

### 2. Duplicate and Rename for New Context
- For example: `PD-GG_00-00_guidance-protocols/courses/ENG101_AMP_24FA`
- Rename to `ENG201_AMP_24SP` and update internal README.md

### 3. Modify UID Prefixes if Needed
- Maintain consonant-only UID logic.
- Use `uid_indexer.py` to regenerate your master index.

### 4. Add Local `UID_MAP.md` in Each Folder
- Use the format: `| UID | Subfolder | Notes |`

### 5. Regenerate Exports if Needed
- Run `vault_freeze.py` to zip the cloned structure.

## Notes
- All UIDs must be consonant-only, 4-letter prefix.
- Each new persona or project should have its own thread log.
- Add `README.md` and `index.md` in each new folder.