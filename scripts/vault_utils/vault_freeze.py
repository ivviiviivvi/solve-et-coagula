import os
import zipfile
from datetime import datetime

def freeze_vault(source_dir="4_S0VRC3_vault", output_dir="."):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    zip_name = f"{output_dir}/4_S0VRC3_FREEZE_{timestamp}.zip"
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(source_dir):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, source_dir)
                zipf.write(full_path, arcname)
    print(f"Vault frozen to: {zip_name}")

if __name__ == "__main__":
    freeze_vault()
