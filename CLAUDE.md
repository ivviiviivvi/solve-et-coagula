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

### Core System: RE:GE:OS

The vault uses **4-letter consonant-only UID prefixes** to organize content into domains:

| Prefix | Domain | Purpose |
|--------|--------|---------|
| `SS-TM` | system-core | Core OS, symbolic laws, 22 organizational bodies |
| `XP-PR` | experiments-live | Experimental Habitat containment |
| `CR-TV` | creative-systems | Mythic, visual, sonic infrastructure |
| `GT-WK` | gateway-inputs | External ingestion points |
| `RC-VK` | archives | Backups and frozen states (gitignored) |
| `PD-GG` | guidance-protocols | SOPs and feedback systems |
| `PB-RC` | public-records | Publications and essays |

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
- `docs/guides/GLOSSARY.md` - Symbolic terminology

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
