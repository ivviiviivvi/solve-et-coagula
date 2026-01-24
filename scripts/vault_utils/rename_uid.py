import os
import re

def rename_files(base_path):
    for root, _, files in os.walk(base_path):
        for name in files:
            if name.endswith(".md") and not name.startswith("README"):
                new_name = name.replace(" ", "-").lower()
                os.rename(os.path.join(root, name), os.path.join(root, new_name))
                print(f"Renamed: {name} -> {new_name}")

if __name__ == "__main__":
    rename_files("4_S0VRC3_vault")
