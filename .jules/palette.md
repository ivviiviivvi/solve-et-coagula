## 2025-12-15 - [Safety Confirmation]
**Learning:** Destructive CLI actions like `cleanup` should always require explicit confirmation to prevent accidental data loss.
**Action:** Implement `input()` check before proceeding with `cleanup_all`, and add a `--force` flag for scripts.
