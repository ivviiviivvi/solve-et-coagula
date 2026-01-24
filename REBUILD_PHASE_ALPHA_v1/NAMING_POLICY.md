---
uid: NP_001
version: 1.0.0
created: 2025-05-14
status: canonical
tags: [naming, policy, symbolic]
linked: [UID_SEED_INDEX, NAME_CANDIDATES_MASTER]
---

# NAMING POLICY
# “Let the symbols obey the system”
## Subtitle: Codified rules for project naming conventions

### SYMBOLIC CONVERSION RULES
- A → 4 (e.g., “ALCHEMY” → “4LCHEMY”)
- U → V (e.g., “FUTURE” → “FVTVRE”)
- No emojis or non-ASCII characters in filenames
- All project names must be assigned a UID before use
- Confirmed system names must be stored in `NAME_CANDIDATES_MASTER.md`

### NAMING APPROVAL PROCESS
1. Propose name in working thread
2. Assign a temporary UID (e.g. `NC_TEMP_01`)
3. Mark usage context: SYSTEM, THREAD, PROTOCOL, WING, etc.
4. Await confirmation in `NAME_CANDIDATES_MASTER.md`
5. Once confirmed, lock to UID and log version tag
