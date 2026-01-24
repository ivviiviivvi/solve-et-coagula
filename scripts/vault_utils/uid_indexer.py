import os
import re

UID_PATTERN = re.compile(r"[A-Z]{2}-[A-Z]{2}_\d{2}-\d{2}")

def build_index(base_dir):
    uid_index = []

    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    for line in f:
                        matches = UID_PATTERN.findall(line)
                        for uid in matches:
                            uid_index.append((uid, path))

    with open("UIDS_MASTER_INDEX_generated.md", "w", encoding="utf-8") as out:
        out.write("# UIDS_MASTER_INDEX (Generated)

")
        out.write("| UID | File |
|-----|------|
")
        for uid, path in sorted(uid_index):
            out.write(f"| {uid} | {path} |
")

if __name__ == "__main__":
    build_index("4_S0VRC3_vault")
