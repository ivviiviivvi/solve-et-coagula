
#!/usr/bin/env bash
echo "Running filename linter..."
python $HOME/GENESIS_ROOT/SYS/lint_filename.py $HOME/GENESIS_ROOT
echo "Listing root tree..."
tree -a $HOME/GENESIS_ROOT | head -n 50
