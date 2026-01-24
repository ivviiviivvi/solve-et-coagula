
#!/usr/bin/env bash
SRC=$HOME/GENESIS_ROOT
rclone sync $SRC remote_icloud:GENESIS_MIRROR
rclone sync $SRC remote_dropbox:GENESIS_MIRROR
rclone sync $SRC remote_gdrive:GENESIS_MIRROR
echo "Sync complete."
