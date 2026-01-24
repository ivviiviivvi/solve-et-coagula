import os
import re

UID_PATTERN = re.compile(r"[A-Z]{2}-[A-Z]{2}_\d{2}-\d{2}")

def scan_uids(base_dir):
    print(f"Scanning UIDs in: {base_dir}")
    bad_uids = []

    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".md"):
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    for line in f:
                        matches = UID_PATTERN.findall(line)
                        for uid in matches:
                            if not UID_PATTERN.fullmatch(uid):
                                bad_uids.append((file, uid))

    if bad_uids:
        print("Found malformed UIDs:")
        for file, uid in bad_uids:
            print(f"  {file}: {uid}")
    else:
        print("All UIDs valid.")

if __name__ == "__main__":
    scan_uids("4_S0VRC3_vault")
