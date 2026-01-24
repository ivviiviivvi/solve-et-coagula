# SOP_GITHUB_VERSIONING.md

Use GitHub to version and sync symbolic vaults.

## Daily Push:

1. Commit new files with short summary:
   `git add .`
   `git commit -m "added new UID content to XP-PR"`
   `git push`

## Weekly:

- Tag a stable commit with:
  `git tag -a v2a-stable -m "Weekly sync point"`
  `git push origin --tags`

## Monthly:

- Create zip via `vault_freeze.py`.
- Upload freeze and tag release via GitHub release.

## Note:

- Keep `.gitignore` updated to exclude system junk or OS metadata.
