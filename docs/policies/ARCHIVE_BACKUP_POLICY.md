# Archive Backup Policy

## Overview

Archive directories (`RC-VK_*/`) are intentionally excluded from git version control due to their size. This document specifies the backup strategy for these critical archival assets.

---

## Archive Locations

| Directory | Purpose | Priority |
|-----------|---------|----------|
| `RC-VK_00-00_archives/` | Primary vault archives | HIGH |
| `RC-VK_0000_archive/` | Legacy archive snapshots | MEDIUM |

---

## Backup Strategy

### Recommended: Cloud Sync

Configure automatic cloud synchronization for archive directories:

**Option A: iCloud Drive (macOS)**
```bash
# Move archives to iCloud
mv RC-VK_00-00_archives ~/Library/Mobile\ Documents/com~apple~CloudDocs/radix_archives/

# Create symlink back to vault
ln -s ~/Library/Mobile\ Documents/com~apple~CloudDocs/radix_archives/RC-VK_00-00_archives .
```

**Option B: Dropbox**
```bash
# Move archives to Dropbox
mv RC-VK_00-00_archives ~/Dropbox/radix_archives/

# Create symlink back to vault
ln -s ~/Dropbox/radix_archives/RC-VK_00-00_archives .
```

**Option C: Backblaze/rsync**
```bash
# Manual backup to external drive
rsync -avz --progress RC-VK_00-00_archives/ /Volumes/ExternalDrive/radix_backups/

# Or to remote server
rsync -avz --progress RC-VK_00-00_archives/ user@server:/path/to/backup/
```

### Alternative: Periodic ZIP Archives

Create timestamped ZIP archives for offline storage:

```bash
# Create dated archive
zip -r "RC-VK_backup_$(date +%Y-%m-%d).zip" RC-VK_00-00_archives/

# Store in ARCHIVES/ directory (also gitignored but can be moved to external storage)
mv "RC-VK_backup_*.zip" ~/ExternalBackups/
```

---

## Backup Schedule

| Type | Frequency | Retention |
|------|-----------|-----------|
| Cloud sync | Continuous | Latest version |
| ZIP snapshot | Monthly | Last 6 months |
| External drive | Quarterly | Last 4 quarters |

---

## Verification Checklist

Run monthly verification:

- [ ] Cloud sync is active and healthy
- [ ] Last ZIP archive created within 30 days
- [ ] External drive backup completed this quarter
- [ ] Spot-check: Can open and read files from backup

---

## Recovery Procedure

### From Cloud Sync
```bash
# Restore symlink if broken
ln -s ~/Library/Mobile\ Documents/com~apple~CloudDocs/radix_archives/RC-VK_00-00_archives .
```

### From ZIP Archive
```bash
# Restore from backup
unzip RC-VK_backup_YYYY-MM-DD.zip -d /path/to/vault/
```

### From External Drive
```bash
rsync -avz /Volumes/ExternalDrive/radix_backups/ ./RC-VK_00-00_archives/
```

---

## Why Archives Are Not Git-Tracked

1. **Size**: Archive directories contain large file collections that would bloat the git repository
2. **Binary content**: Many archive files are binary (ZIPs, images) which git handles inefficiently
3. **History overhead**: Archive content changes infrequently but in large batches
4. **Restore simplicity**: Cloud sync provides simpler disaster recovery than git history

---

## Version
Created: 2026-01-24
Last Updated: 2026-01-24
