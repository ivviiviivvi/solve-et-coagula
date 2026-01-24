# SOP_SYSTEM_OVERVIEW.md

Complete protocol for managing, duplicating, maintaining, and growing the 4_S0VRC3 symbolic operating system.

## CORE PHASES

### PHASE 0: GENESIS
- Run `scripts/vault_utils/initialize_vault.py` to build the symbolic folder structure.
- Use `scripts/vault_utils/generate_uid.py` to name everything legally.

### PHASE 1: ACTIVE USE
- Drop threads or ideas into `FL-TR` or `XP-PR`.
- Use `scripts/vault_utils/sort_router.py` to route, `scripts/vault_utils/tag_suggestor.py` to label.
- Use `scripts/vault_utils/rename_uid.py` after dumping files.

### PHASE 2: MAINTENANCE
- Use `scripts/vault_utils/uid_check.py` and `scripts/vault_utils/uid_indexer.py` weekly.
- Update local `UID_MAP.md` and `UIDS_MASTER_INDEX.md`.

### PHASE 3: ARCHIVING
- Run `scripts/vault_utils/vault_freeze.py` monthly or after a major build.
- Save output to `RC-VK_00-00_archives/fossils/`.

### PHASE 4: CLONING / FORKING
- Use `CLONE_PROTOCOL.md` to duplicate the system or fork for new use.
- Rename all folders/files using UID law.
- Begin again from `scripts/vault_utils/initialize_vault.py` if needed.

## EXPERIMENTAL HABITAT SYSTEM

The Habitat System (`experimental_habitat_implementation.py`) provides containment for experimental code:

- **Spawn**: Create isolated experiments with resource limits
- **Run**: Execute experiments within containment boundaries
- **Graduate**: Promote successful experiments to production (Code Forge)
- **Compost**: Safely retire failed experiments, extracting lessons learned

### Usage
```python
from experimental_habitat_implementation import ExperimentalHabitat, ExperimentalSystem

habitat = ExperimentalHabitat("my_lab", isolation_level=3)
experiment = ExperimentalSystem("test_experiment", "hypothesis here")
habitat.spawn_experiment(experiment, {'resources': {'cpu': '50%'}})
result = habitat.run_experiment("test_experiment")
habitat.cleanup()
```

See `.Jules/sentinel.md` for security learnings related to this system.

## SCRIPT INDEX

All vault utility scripts are located in `scripts/vault_utils/`:
- `generate_uid.py` - Generate valid UIDs
- `initialize_vault.py` - Set up folder structure
- `rename_uid.py` - Rename files with UIDs
- `sort_router.py` - Route files to correct locations
- `tag_suggestor.py` - Suggest tags for content
- `uid_check.py` - Validate UID compliance
- `uid_indexer.py` - Generate master UID index
- `vault_freeze.py` - Create archival snapshots

See `SOP_INDEX.md` for all maintenance and naming guides.

## DAILY / WEEKLY / MONTHLY
- Daily: use `SOP_DAILY_CHECKLIST.md`
- Weekly: use `SOP_WEEKLY_CHECKLIST.md` + freeze if needed
- Monthly: review `SOP_MONTHLY_CHECKLIST.md` + Git tag

## OBSIDIAN & GIT INTEGRATION
- See `SOP_OBSIDIAN_SYNC.md` and `SOP_GITHUB_VERSIONING.md`.

## SYMBOLIC CONSIDERATIONS
- UID = meaning + memory + function
- Every folder is a story. Every script is a turn.
