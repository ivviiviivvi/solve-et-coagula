
#!/usr/bin/env bash
ROOT=${1:-$HOME/GENESIS_ROOT}
STAMP=$(date +%Y%m%d_%H%M%S)
tar -czf "$ROOT/../PREWIPE_$STAMP.tar.gz" "$ROOT"
shasum -a 256 "$ROOT/../PREWIPE_$STAMP.tar.gz" > "$ROOT/../PREWIPE_$STAMP.sha256"
tree -a "$ROOT" > "$ROOT/../SNAPSHOT_tree_$STAMP.txt"
echo "Snapshot complete: $STAMP"
