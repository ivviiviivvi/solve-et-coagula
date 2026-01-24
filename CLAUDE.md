# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

4_S0VRC3 (read: "A Source") is a hybrid creative/technical system combining an Obsidian knowledge vault with Python automation. It implements RE:GE:OS (Recursive Generative Operating System) - a symbolic operating system using consonant-only UIDs, mythic archetypes, and experimental containment.

**Zero external dependencies** for core functionality - uses only Python standard library.

## Commands

### Setup
```bash
pip install -e .                    # Install package
pip install -e ".[dev]"             # Install with dev dependencies (pytest, black, flake8)
```

### Testing
```bash
pytest tests/                       # Run all tests
pytest tests/test_habitat_system.py # Run specific test file
python -m pytest -v                 # Verbose output
```

### Entry Points (after install)
```bash
habitat-manager      # Experimental Habitat containment system
habitat-interactive  # Interactive habitat interface
habitat-demo         # Simple demonstration
habitat-workflow     # Complete workflow demo
```

### Vault Utilities
```bash
python scripts/vault_utils/generate_uid.py     # Generate symbolic UIDs
python scripts/vault_utils/uid_indexer.py      # Generate master UID index
python scripts/vault_utils/uid_check.py        # Validate UID compliance
python scripts/vault_utils/initialize_vault.py # Bootstrap folder structure
python scripts/vault_utils/vault_freeze.py     # Create archival snapshots
python scripts/vault_utils/sort_router.py      # Route files to domain folders
```

### Validation
```bash
python scripts/validate_containment.py  # Check containment policy compliance
python scripts/metadata_guard.py        # Validate YAML frontmatter
python scripts/check_env_vars.py        # Verify environment variables
```

## Architecture

### Folder Structure

The vault uses a simplified naming convention with 4-letter suffix codes:

| Folder | Purpose |
|--------|---------|
| `REGEOS_RG01/` | Core RE:GE:OS logic, symbolic laws, 22 organizational bodies |
| `ARCHIVE_RK01/` | Long-term archival storage (gitignored) |
| `MIRROR_MR01/` | Shadow self, reflection systems |
| `TEMPLATES_TP01/` | Seed files, note templates |
| `TAGS_TA01/` | Tag and symbol management |
| `SYSTEM_MAP_SM01/` | System architecture maps, experiments |
| `ARCHIVAL_STACK/` | Project thread digests |
| `DOCUMENTATION/` | Vault guides, SOPs, policies, standards |
| `PROJECT_MANAGEMENT/` | Manifests, changelogs, meta-operations |
| `CATALOGS_AND_INDEXES/` | Master indexes, observation logs |
| `Users/` | User-specific content |
| `GATEWAY_GT01/` | External ingestion points |
| `ANOMALIES_FL01/` | Anomaly tracking |
| `FRAGMENTS_FR01/` | Fragment and memory collection |
| `NARRATIVES_NR01/` | Narrative content |
| `GAMEDESIGN_GD01/` | Game design materials |
| `WORKSHOPS_WR01/` | Workshop content |
| `scripts/` | Python automation (CLI entry points) |
| `tests/` | Test suite (pytest integration) |
| `security/` | Recovery keys (sensitive, isolated) |

### Experimental Habitat System

Safe, isolated containment for experimental code with resource limits:

```python
from experimental_habitat_implementation import ExperimentalHabitat, ExperimentalSystem

habitat = ExperimentalHabitat("lab_name", isolation_level=3)
experiment = ExperimentalSystem("test_name", "hypothesis")
habitat.spawn_experiment(experiment, {'resources': {'cpu': '50%'}})
result = habitat.run_experiment("test_name")
habitat.cleanup()
```

**Lifecycle:** Spawn → Run → Graduate (to production) or Compost (extract lessons)

### Key Files

- `experimental_habitat_implementation.py` - Core containment system
- `habitat_manager.py` - CLI management interface
- `SOP_SYSTEM_OVERVIEW.md` - Complete operations manual
- `UIDS_MASTER_INDEX.md` - Master UID lookup
- `DOCUMENTATION/guides/GLOSSARY.md` - Symbolic terminology

## Working with Special Characters

Some older symbolic folder names may contain special characters. Always use quotes:

```bash
ls -la "MIRROR_MR01/"
cat "path/with spaces/file.md"
```

## GitHub Workflows

Active CI/CD in `.github/workflows/`:
- `ai-review.yml` - AI-assisted PR reviews
- `jules-branch-guard.yml` - Branch lifecycle (bolt-*/sentinel-*/palette-* prefixes)
- `codeql.yml` / `semgrep.yml` - Security analysis
- `documentation-quality.yml` - Doc validation

## AI Handoff Protocol

AI-generated documents use envelope notation:
```
<<<AI-Handoff:BEGIN::Agent={Name}::Timestamp={ISO-8601}>>>
...content...
<<<AI-Handoff:END>>>
```
