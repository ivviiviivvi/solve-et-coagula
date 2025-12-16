## 2025-12-16 - Path Traversal in Experiment Names
**Vulnerability:** Path traversal vulnerability in `spawn_experiment` and `nest_habitat` allowing creation of files outside the temporary directory using names like `../pwned`.
**Learning:** `os.path.join` does not sanitize input paths. Input validation is critical for file operations, especially when user input is used as part of a file path.
**Prevention:** Strictly validate all inputs used in file system operations. Use a strict allowlist (alphanumeric + safe chars) rather than trying to sanitize (blocklist).
