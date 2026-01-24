
#!/usr/bin/env bash
# MythOS Environment Bootstrap
ARCH=$(uname -m)
echo "Detected architecture: $ARCH"
# Homebrew
if ! command -v brew >/dev/null; then
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi
brew bundle --file=- <<'BREWFILE'
brew "git"
brew "python"
brew "rclone"
brew "tree"
BREWFILE
echo "Bootstrap complete."
