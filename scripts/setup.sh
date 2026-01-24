#!/bin/bash

# Define vault path
VAULT_PATH="$HOME/Documents/4_S0VRC3"

# Change to vault directory
cd "$VAULT_PATH" || { echo "Vault path not found."; exit 1; }

# Run the Python reset script
echo "Running vault_reset.py..."
python3 vault_reset.py

# Optional: Open in Finder or Obsidian (comment out if not needed)
open "$VAULT_PATH"
