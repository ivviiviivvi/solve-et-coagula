## 2025-12-16 - Path Traversal in Experiment Names
**Vulnerability:** Path traversal vulnerability in `spawn_experiment` and `nest_habitat` allowing creation of files outside the temporary directory using names like `../pwned`.
**Learning:** `os.path.join` does not sanitize input paths. Input validation is critical for file operations, especially when user input is used as part of a file path.
**Prevention:** Strictly validate all inputs used in file system operations. Use a strict allowlist (alphanumeric + safe chars) rather than trying to sanitize (blocklist).
## 2025-12-15 - Path Traversal in Experiment Names
**Vulnerability:** The `spawn_experiment` function in `experimental_habitat_implementation.py` used `experiment.name` directly in `os.path.join(self.temp_dir, experiment.name)`. This allowed creating directories outside the temporary habitat directory by providing an absolute path or path using `..`.
**Learning:** `os.path.join` does not prevent path traversal if one of the components is an absolute path. It simply returns the absolute path. Even with `os.makedirs`, this can be exploited to write to arbitrary locations where the user has permissions.
**Prevention:** Always validate user-supplied names that are used for filesystem operations. Ensure they do not contain path separators or resolve to a path outside the intended directory. Using `os.path.basename` or strict character whitelisting is recommended.
