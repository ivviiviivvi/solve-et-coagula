## 2025-12-14 - Path Traversal in Habitat Creation
**Vulnerability:** Path traversal vulnerability in `ExperimentalHabitat.spawn_experiment`.
**Learning:** `os.path.join` with user-controlled input allows creating directories outside the intended root if the input contains `../`, `..\`, absolute paths (`/`, `C:\`), or other traversal patterns.
**Prevention:** 
1. Normalize path separators (convert `\` to `/`) to handle cross-platform attacks
2. Check for parent directory references (`..`) anywhere in the path
3. Check for absolute path indicators (leading `/` or `\`)
4. Check for Windows drive letters (`:` in position 1)
5. Use `os.path.abspath` and verify with `os.path.commonpath` that resulting path is within intended root
6. Handle `ValueError` from `commonpath` when paths are on different drives
**Fixed:** 2026-01-03 - Enhanced multi-layer validation prevents all known path traversal vectors

