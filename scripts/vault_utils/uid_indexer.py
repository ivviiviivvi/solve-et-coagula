import os
import re
from collections import defaultdict
from datetime import datetime
import pandas as pd

UID_PATTERN = re.compile(r"[A-Z]{2}-[A-Z]{2}_\d{2}-\d{2}", re.IGNORECASE)

CATEGORY_TAGS = {
    "script": ["launch", "init", "run", "script"],
    "template": ["template", "spawn"],
    "symbol": ["symbol", "glyph", "mark", "sigil"],
    "instruction": ["readme", "manual", "guide"],
    "devtool": ["tool", "dev", "bundle", "system"],
    "archive": ["archive", "legacy", "fossil"],
}

def guess_category_and_tags(filepath):
    name = filepath.lower()
    tags = []
    category = "misc"

    for cat, keywords in CATEGORY_TAGS.items():
        for word in keywords:
            if word in name:
                tags.append(f"#{cat}")
                category = cat
                break
    return category, " ".join(tags)

def determine_status(uid):
    if "archive" in uid.lower() or "legacy" in uid.lower():
        return "archived"
    if "draft" in uid.lower():
        return "draft"
    return "active"

def build_uid_index(root_dir):
    uid_map = defaultdict(list)
    placeholder_log = []

    for root, dirs, files in os.walk(root_dir):
        # Check files
        for file in files:
            filepath = os.path.join(root, file)
            if file.startswith('.') or 'DS_Store' in file:
                continue
            # UID in filename
            matches = UID_PATTERN.findall(file)
            for uid in matches:
                if uid.upper().startswith("XX-XX") or "00-00" in uid:
                    placeholder_log.append((filepath, uid))
                    continue
                if not re.search(r"_v\d+[a-z]$", file):
                    uid = f"{uid}_v1a"
                uid_map[uid].append(filepath)
            # UID in file content
            if file.endswith(".md"):
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        matches = UID_PATTERN.findall(content)
                        for uid in matches:
                            if uid.upper().startswith("XX-XX") or "00-00" in uid:
                                placeholder_log.append((filepath, uid))
                                continue
                            if not re.search(r"_v\d+[a-z]$", file):
                                uid = f"{uid}_v1a"
                            uid_map[uid].append(filepath)
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")
        # Check folder names
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            matches = UID_PATTERN.findall(folder)
            for uid in matches:
                if uid.upper().startswith("XX-XX") or "00-00" in uid:
                    placeholder_log.append((folder_path, uid))
                    continue
                uid_map[uid].append(folder_path)

    return uid_map, placeholder_log

def suggest_uid_replacements(placeholder_log):
    suggestions = {}
    used_uids = set()
    def increment_suffix(suffix):
        # suffix format: _v{number}{letter}
        match = re.match(r"_v(\d+)([a-z])", suffix)
        if not match:
            return "_v1a"
        num, letter = int(match.group(1)), match.group(2)
        if letter == 'z':
            return f"_v{num+1}a"
        else:
            return f"_v{num}{chr(ord(letter)+1)}"

    for path, _ in placeholder_log:
        parts = os.path.basename(path).split("_")
        if len(parts) >= 3:
            base = parts[2] if parts[2] else parts[0]
            base_clean = re.sub(r'[^a-zA-Z]', '', base).lower()
            consonants = [c for c in base_clean if c not in 'aeiou']
            while len(consonants) < 4:
                consonants.append(consonants[0] if consonants else 'x')
            prefix = ''.join(consonants[:2]).upper() + '-' + ''.join(consonants[2:4]).upper()
            suffix = "01-01"
            base_uid = f"{prefix}_{suffix}"
            # Ensure uniqueness with suffixes
            candidate_uid = f"{base_uid}_v1a"
            while candidate_uid in used_uids:
                # increment suffix
                if re.search(r"_v\d+[a-z]$", candidate_uid):
                    suffix_part = candidate_uid[-3:]
                    new_suffix = increment_suffix(suffix_part)
                    candidate_uid = candidate_uid[:-3] + new_suffix
                else:
                    candidate_uid += "_v1a"
            used_uids.add(candidate_uid)
            suggestions[path] = candidate_uid
        else:
            suggestions[path] = "UNABLE_TO_GENERATE"
    return suggestions

def apply_uid_replacements(index_path, suggestion_path, output_path):
    if not os.path.exists(index_path) or not os.path.exists(suggestion_path):
        print("Missing index or suggestion file.")
        return

    replacement_map = {}
    with open(suggestion_path, "r", encoding="utf-8") as sugg_file:
        lines = sugg_file.readlines()[4:]  # Skip header
        for line in lines:
            if "|" in line:
                parts = [part.strip() for part in line.strip().split("|")[1:-1]]
                if len(parts) == 2:
                    path, suggested_uid = parts
                    replacement_map[path] = suggested_uid

    updated_lines = []
    with open(index_path, "r", encoding="utf-8") as idx_file:
        lines = idx_file.readlines()

    for line in lines:
        if line.startswith("|") and not line.startswith("| UID"):
            parts = [p.strip() for p in line.strip().split("|")[1:-1]]
            if len(parts) >= 9:
                path = parts[1]
                if path in replacement_map:
                    parts[0] = replacement_map[path]
                    line = "| " + " | ".join(parts) + " |\n"
        updated_lines.append(line)

    with open(output_path, "w", encoding="utf-8") as out:
        out.writelines(updated_lines)

def deduplicate_uid_entries(uid_map):
    """Generate suffix-based deduplications like _v1a → _v1b, _v1c, _v2a if duplicates exist"""
    deduped = {}
    for uid, paths in uid_map.items():
        if len(paths) == 1:
            deduped[uid] = [(uid, paths[0])]
        else:
            base_uid = re.sub(r'_v\d+[a-z]$', '', uid)
            deduped[uid] = []
            for i, path in enumerate(sorted(paths)):
                # Calculate suffix index: cycle letters a-z, increment version number as needed
                version_num = 1 + (i // 26)
                letter_idx = i % 26
                suffix = f"_v{version_num}{chr(ord('a') + letter_idx)}"
                new_uid = normalize_uid_suffix_format(f"{base_uid}{suffix}")
                # Avoid collisions by checking if new_uid already used for this base_uid
                while any(new_uid == existing_uid for existing_uid, _ in deduped[uid]):
                    # increment suffix
                    letter_idx += 1
                    if letter_idx >= 26:
                        letter_idx = 0
                        version_num += 1
                    suffix = f"_v{version_num}{chr(ord('a') + letter_idx)}"
                    new_uid = normalize_uid_suffix_format(f"{base_uid}{suffix}")
                deduped[uid].append((new_uid, path))
    return deduped

def normalize_uid_suffix_format(uid):
    """Ensure UID suffixes conform to expected pattern: _v1a, _v2b, etc."""
    match = re.match(r"(.+)_v(\d+)([a-z])$", uid, re.IGNORECASE)
    if match:
        base, num, letter = match.groups()
        return f"{base}_v{int(num)}{letter.lower()}"
    else:
        return uid  # return as-is if it doesn't match

if __name__ == "__main__":
    uid_map, placeholder_log = build_uid_index(".")

    # Optional: Run deduplication suggestion pass
    deduped_uid_map = deduplicate_uid_entries(uid_map)
    with open("UIDS_DUPLICATE_PATCH.md", "w", encoding="utf-8") as dup_out:
        dup_out.write("# UIDS_DUPLICATE_PATCH (Generated)\n")
        dup_out.write("Suggested UID suffix changes for duplicates.\n\n")
        dup_out.write("| Original UID | Suggested UID | Path |\n")
        dup_out.write("|--------------|----------------|------|\n")
        for original_uid, items in deduped_uid_map.items():
            for suggested_uid, path in items:
                if original_uid != suggested_uid:
                    dup_out.write(f"| {original_uid} | {suggested_uid} | {path} |\n")

    output_file = "UIDS_MASTER_INDEX_generated.md"
    with open(output_file, "w", encoding="utf-8") as out:
        out.write("# UIDS_MASTER_INDEX (Generated)\n")
        out.write(f"**Last updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        out.write("| UID | File | Modified | Count | Duplicate? | Category | Tags | Status | Notes |\n")
        out.write("|-----|------|----------|--------|-------------|----------|------|--------|-------|\n")

        for uid in sorted(uid_map.keys()):
            file_paths = sorted(set(uid_map[uid]))
            count = len(uid_map[uid])
            duplicate = "Yes" if count > 1 else ""
            status = determine_status(uid)

            for path in file_paths:
                try:
                    mod_time = datetime.fromtimestamp(os.path.getmtime(path)).strftime('%Y-%m-%d %H:%M')
                except:
                    mod_time = "unknown"
                category, tags = guess_category_and_tags(path)
                out.write(f"| {uid} | {path} | {mod_time} | {count} | {duplicate} | {category} | {tags} | {status} | |\n")

    # Write placeholder audit file
    audit_file = "UIDS_PLACEHOLDER_AUDIT.md"
    with open(audit_file, "w", encoding="utf-8") as audit_out:
        audit_out.write("# UIDS_PLACEHOLDER_AUDIT (Generated)\n")
        audit_out.write("This file logs all skipped UIDs due to placeholder patterns like \"XX-XX\" or \"00-00\".\n\n")
        audit_out.write("| Path | UID |\n")
        audit_out.write("|------|-----|\n")
        for path, uid in placeholder_log:
            audit_out.write(f"| {path} | {uid} |\n")

    print(f"Generated: {output_file}, {audit_file}, UIDS_DUPLICATE_PATCH.md")
