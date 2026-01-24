import os
import shutil
import zipfile
from datetime import datetime

# CONFIGURATION
VAULT_PATH = os.path.expanduser("~/Documents/4_S0VRC3")
ARCHIVE_PATH = os.path.join(VAULT_PATH, "RC-VK_0000_archive")
SEED_PATH = os.path.join(VAULT_PATH, "4_S0VRC3_v2a_FINAL_WITH_SKELETONS")
BACKUP_FILENAME = f"vault_backup_{datetime.now().strftime('%Y-%m-%d_%H%M')}.zip"
BACKUP_PATH = os.path.join(ARCHIVE_PATH, BACKUP_FILENAME)

# Step 1: Ensure archive folder exists
os.makedirs(ARCHIVE_PATH, exist_ok=True)

# Step 2: Zip everything inside VAULT_PATH except the folder itself
def zip_vault_contents():
    with zipfile.ZipFile(BACKUP_PATH, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
        for root, dirs, files in os.walk(VAULT_PATH):
            if ARCHIVE_PATH in root or SEED_PATH in root:
                continue  # Skip archive and seed folders
            for file in files:
                filepath = os.path.join(root, file)
                arcname = os.path.relpath(filepath, VAULT_PATH)
                backup_zip.write(filepath, arcname)

# Step 3: Clear the vault contents (except the vault folder itself)
def clear_vault():
    for item in os.listdir(VAULT_PATH):
        item_path = os.path.join(VAULT_PATH, item)
        if item_path in [ARCHIVE_PATH, SEED_PATH]:
            continue
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)

# Step 4: Copy seed contents into vault
def copy_seed():
    for item in os.listdir(SEED_PATH):
        s = os.path.join(SEED_PATH, item)
        d = os.path.join(VAULT_PATH, item)
        if os.path.isdir(s):
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)

# Step 5: Write log
def write_log():
    log_path = os.path.join(VAULT_PATH, "vault_recovery_log.md")
    with open(log_path, "w") as f:
        f.write("# Vault Recovery Log\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"**Backed up to:** {BACKUP_PATH}\n")
        f.write(f"**Seeded from:** {SEED_PATH}\n")
        f.write("Vault successfully reset.\n")

if __name__ == "__main__":
    print("Zipping current vault...")
    zip_vault_contents()
    print(f"Backup created at {BACKUP_PATH}")

    print("Clearing vault contents...")
    clear_vault()

    print("Copying seed contents...")
    copy_seed()

    print("Writing recovery log...")
    write_log()

    print("Vault reset complete.")
