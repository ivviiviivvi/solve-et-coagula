# Deleted Branch Intent Audit — 2026-01-19

You asked for an “intelligent, batch-friendly” review of the ~182 (actually **177**) Jules branches that were deleted during cleanup, to ensure nothing important—or at least the *intentions*—were lost.

This audit is based on the **saved deletion list**:

- `reports/branch_cleanup_delete_list_20260119-213841.txt` (**177** deleted branches)

> Important constraint: the deletion list contains **branch names only**, not the branch-tip commit SHAs.
> Once a branch is deleted, we cannot reconstruct its exact diff unless we also preserved either:
> 1) the tip SHA(s) before deletion, or
> 2) PR refs (merged/unmerged), or
> 3) patches/artifacts.
>
> So: we can review **intent** via naming clusters and verify whether that intent is represented in `main` via merged PRs and current code, but we cannot do a byte-for-byte diff review of each deleted branch tip.

## A. Batch clustering (by intention “stem”)

Each branch name was normalized to a “stem” by removing the trailing numeric suffix (e.g., `sentinel-path-traversal-fix-123…` → `sentinel-path-traversal-fix`).

### Prefix totals

- `bolt-*`: 59
- `sentinel-*`: 57
- `palette-*`: 61

### Largest intention clusters (count ≥ 2)

- 24 × `sentinel-path-traversal-fix`
- 13 × `bolt-optimize-containment-path`
- 13 × `bolt-regex-optimization`
- 12 × `sentinel-fix-path-traversal`
- 7 × `bolt-recursion-fix`
- 7 × `palette-ux-cards`
- 7 × `palette-ux-improvements`
- 5 × `palette-cli-cards`
- 5 × `palette-ux-cli-cards`
- 4 × `bolt-optimize-habitat-status`
- 4 × `bolt-recursion-optimization`
- 4 × `palette-ux-improvement-cli-cards`
- 3 × `sentinel-ansi-sanitization`
- 3 × `sentinel-terminal-injection-fix`
- 3 × `palette-ux-colors`
- 3 × `palette-ux-improvement-colors`
- 2 × `sentinel-fix-ansi-injection`
- 2 × `bolt-optimize-list-habitats`
- 2 × `bolt-optimize-status-reporting`
- 2 × `palette-cli-ux-improvements`
- 2 × `palette-ux-cli-colors`

These clusters are exactly what you’d expect from Jules “retry storms”: many branches attempting the same small set of tasks.

## B. Were the big intentions lost?

### 1) Sentinel: Path traversal security fix (HIGH importance)

**Deleted-branch intent signal**
- 24 × `sentinel-path-traversal-fix-*`
- 12 × `sentinel-fix-path-traversal-*`

**Evidence it landed in `main`** (merged PRs)
- PR #66 — ️ Sentinel: [CRITICAL] Fix Path Traversal in ExperimentalHabitat
 - https://github.com/ivviiviivvi/solve-et-coagula/pull/66
- PR #69 — Shield: Fix path traversal vulnerability in experiment spawning
 - https://github.com/ivviiviivvi/solve-et-coagula/pull/69
- PR #73 — Fix path traversal in experiment creation
 - https://github.com/ivviiviivvi/solve-et-coagula/pull/73
- (plus follow-on hardening/docs PRs later: e.g., #78, #81)

**Conclusion**
- The *core security intent* of the sentinel branch swarm is preserved.

### 2) Bolt: ContainmentBoundary path optimization/caching (MED/HIGH importance)

**Deleted-branch intent signal**
- 13 × `bolt-optimize-containment-path-*`

**Evidence it landed in `main`** (merged PRs)
- PR #65 — Optimize ContainmentBoundary.get_full_path with caching
 - https://github.com/ivviiviivvi/solve-et-coagula/pull/65
- PR #68 — [RUN] Bolt: Optimize ContainmentBoundary path generation
 - https://github.com/ivviiviivvi/solve-et-coagula/pull/68
- PR #71 — [RUN] Bolt: Optimize ContainmentBoundary.get_full_path caching
 - https://github.com/ivviiviivvi/solve-et-coagula/pull/71

**Conclusion**
- The bolt optimization intent is preserved.

### 3) Palette: CLI UX (cards/formatting/colors/cleanup confirmation) (MED importance)

**Deleted-branch intent signal**
- 7 × `palette-ux-cards-*`
- 5 × `palette-cli-cards-*`
- 7 × `palette-ux-improvements-*`
- multiple singleton stems (colors/spinner/card-pattern variants)

**Evidence it landed in `main`** (merged PRs)
- PR #67 — feat(cli): enhance habitat manager output with colors…
 - https://github.com/ivviiviivvi/solve-et-coagula/pull/67
- PR #70 — feat(cli): add confirmation to cleanup command
 - https://github.com/ivviiviivvi/solve-et-coagula/pull/70
- PR #72 — feat: improve CLI output formatting for better readability
 - https://github.com/ivviiviivvi/solve-et-coagula/pull/72
- PR #76 — feat(ux): implement CLI Card Pattern for clearer output
 - https://github.com/ivviiviivvi/solve-et-coagula/pull/76

**Conclusion**
- The palette UX intent is preserved.

## C. The “maybe” buckets (intent exists; merge evidence unclear)

These stem clusters appear in the deleted branch list but do **not** clearly map to a merged PR by name/title alone:

- `sentinel-ansi-sanitization-*` / `sentinel-terminal-injection-fix-*` / `sentinel-fix-ansi-injection-*`
 - Potential “ANSI escape injection” hardening.
 - I did not find obvious ANSI sanitization code in `*.py` via search; that *may* mean:
 - the repo doesn’t emit untrusted ANSI sequences (so nothing to fix), or
 - the work never merged.
 - Recommendation: treat as a **security review item**, not an automatic “lost work” item.

- `bolt-regex-optimization-*`, `bolt-recursion-fix-*`
 - Likely performance/refactor experiments.
 - May be redundant with existing optimizations already merged (but without preserved tip SHAs, we cannot confirm).
 - Recommendation: only revisit if you have a performance regression or known hotspot.

## D. Is it illogical to “review all deleted branches”?

It’s *partly illogical* in the strict diff-review sense, because after deletion we no longer have branch tips.

What **is** logical (and what we did here):
- review the **batch-friendly naming clusters**,
- confirm the **major intentions** correspond to merged PRs and current `main` behavior,
- identify any clusters that look like security concerns but have no confirmed merge.

## E. If you want this level of assurance next time

Before deleting branches, capture the branch-tip SHAs:

- `git ls-remote --heads origin 'bolt-*' 'sentinel-*' 'palette-*' > reports/branch_tips_before_cleanup.txt`

With that, even after deletion we can:
- reconstruct each branch’s exact tip,
- generate a diffstat per branch,
- cherry-pick or recreate branches deterministically.
