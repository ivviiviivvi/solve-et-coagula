# MACOS_OVERLAY_GUIDE.md

How the 4_S0VRC3 symbolic operating system cleanly and powerfully overlays your macOS environment.

---

## CORE PRINCIPLE

Use **aesthetic symbolic names for top-level macOS folders**, and apply **UID structure *within***.

This keeps Finder human-readable while maintaining recursive system law inside your vault.

---

## VAULT PLACEMENT

**Recommended Vault Root Folder:**  
`~/Documents/4_S0VRC3/`  
(*This is symbolic, not UID-bound — ideal for daily use*)

All UID folders (e.g., `SS-TM_00-00_system-core/`) live *inside* this vault root.

---

## SYSTEM LAYER MAPPING

| macOS Location            | 4_S0VRC3 Overlay                  | UID Required? | Notes |
|---------------------------|-----------------------------------|---------------|-------|
| `/Users/yourname/`        | Start here                        | ❌            | Leave OS structure untouched  
| `~/Documents/`            | `4_S0VRC3/`                        | ❌ (symbolic) | Vault lives here  
| `~/Desktop/`              | `INBOX/` for file routing         | ❌ (scripted) | Use `sort_router.py` or Hazel  
| `~/Downloads/`            | `downloads_pending/` if needed    | ❌            | Can be used as input cache  
| `~/Documents/Projects/`   | Route select items into `CR-TV/`  | ✅ (internal) | UID them as you migrate  
| `~/Documents/notes_icloud/`| `RC-VK/legacy/notes_archive/`    | ✅ (fossils)  | Archive exports here

---

## AUTOMATION TIPS

- Use Apple Shortcuts or Hazel to route files from `INBOX/` into `FL-TR/`, `PD-GG/`, etc.
- Example: if a filename contains "feedback", route to `PD-GG/feedback/`
- Use `rename_uid.py` and `sort_router.py` for automation logic

---

## FREEZING + ARCHIVING

- Freeze old Finder folders as ZIPs
- Move to: `RC-VK_00-00_archives/fossils/`
- Name with UID and version if possible:
  Example: `FR-GM_01-03_old_poems_archive.zip`

---

## SYMBOLIC RULE

Use UID law **inside your creative and teaching folders**.  
Let the outer structure remain aesthetic, human-readable, and OS-friendly.

---

## FUTURE CONSIDERATIONS

- Sync `4_S0VRC3/` via iCloud Drive if desired  
- Backup via Time Machine, external disk, or Git  
- Mirror vault structure to a second machine or collaborator

