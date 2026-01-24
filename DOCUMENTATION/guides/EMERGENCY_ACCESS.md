# Emergency Access Guide

## Purpose
This document provides minimum viable procedures for system recovery and knowledge transfer.

---

## Critical File Locations

| Purpose | Location |
|---------|----------|
| UID Naming Rules | `UID_Constitution_v2.md` |
| System Operations | `SOP_SYSTEM_OVERVIEW.md` |
| Security Learnings | `.Jules/sentinel.md` |
| UID Indexer | `scripts/vault_utils/uid_indexer.py` |
| Vault Initialization | `scripts/vault_utils/initialize_vault.py` |
| Habitat System | `experimental_habitat_implementation.py` |

---

## Token Recovery Procedure

### GitHub Token (`GITHUB_TOKEN`)

1. **Check current status:**
   ```bash
   gh auth status
   ```

2. **If token expired or revoked:**
   - Go to GitHub Settings > Developer settings > Personal access tokens
   - Generate new token with required scopes:
     - `repo` (full control of private repositories)
     - `workflow` (if using GitHub Actions)
   - Update local environment:
   ```bash
   export GITHUB_TOKEN="your_new_token"
   # Or use gh CLI:
   gh auth login
   ```

3. **Update stored credentials:**
   - Check `.env` files (if present)
   - Update CI/CD secrets if applicable

---

## Minimum Viable Rebuild Steps

### From Complete Loss

1. **Clone repository:**
   ```bash
   git clone https://github.com/ivviiviivvi/radix-recursiva-solve-coagula-redi.git
   cd radix-recursiva-solve-coagula-redi
   ```

2. **Verify structure:**
   ```bash
   ls -la
   # Should see: scripts/, docs/, SOP_SYSTEM_OVERVIEW.md, UID_Constitution_v2.md
   ```

3. **Initialize vault (if needed):**
   ```bash
   python3 scripts/vault_utils/initialize_vault.py
   ```

4. **Generate UID index:**
   ```bash
   python3 scripts/vault_utils/uid_indexer.py
   ```

### From Partial Corruption

1. **Check git status:**
   ```bash
   git status
   git diff
   ```

2. **Reset to known good state:**
   ```bash
   # Soft reset (keeps changes):
   git reset --soft HEAD~1

   # Hard reset (discards changes - use carefully):
   git reset --hard origin/main
   ```

3. **Restore specific files:**
   ```bash
   git checkout origin/main -- <file_path>
   ```

---

## Key System Concepts

### UID System
- UIDs use consonant-only codes (21 consonants, no vowels)
- Format: `XX-YY_00-00_description`
- Collision rate: 21^4 = 194,481 possible combinations
- Index regenerated via `uid_indexer.py`

### Habitat System
- Experimental code containment in `experimental_habitat_implementation.py`
- Uses temporary directories for isolation
- Experiments can be "graduated" to production or "composted" on failure

### SOPs
- Daily/Weekly/Monthly checklists in `SOP_*_CHECKLIST.md` files
- Scripts located in `scripts/vault_utils/`

---

## Emergency Contacts / Resources

- Repository: https://github.com/ivviiviivvi/radix-recursiva-solve-coagula-redi
- Security issues: Document in `.Jules/sentinel.md`

---

## Version
Created: 2026-01-24
Last Updated: 2026-01-24
