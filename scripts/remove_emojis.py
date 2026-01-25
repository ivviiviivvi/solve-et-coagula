#!/usr/bin/env python3
"""
Remove emojis from project files, preserving meaning with text alternatives.
Issue #28: Remove emojis from project
"""

import os
import re
from pathlib import Path

# Emoji pattern covering common ranges
EMOJI_PATTERN = re.compile(
    '['
    '\U0001F300-\U0001F9FF'  # Misc Symbols and Pictographs, Emoticons, etc.
    '\U0001FA00-\U0001FAFF'  # Chess, symbols
    '\U00002700-\U000027BF'  # Dingbats
    '\U00002600-\U000026FF'  # Misc symbols
    '\U00002300-\U000023FF'  # Misc Technical
    '\U0001F1E0-\U0001F1FF'  # Flags
    ']+', re.UNICODE)

# Emoji to text replacement map
EMOJI_REPLACEMENTS = {
    # Status indicators
    '\u2705': '[OK]',       # check mark
    '\u274c': '[FAIL]',     # cross mark
    '\u26a0': '[WARN]',     # warning sign (part of combo)
    '\U0001F6A8': '[ALERT]',  # rotating light
    '\U0001F6D1': '[STOP]',   # stop sign

    # Actions
    '\U0001F680': '[LAUNCH]',  # rocket
    '\U0001F9F9': '[CLEANUP]', # broom
    '\U0001F50D': '[SEARCH]',  # magnifying glass
    '\U0001F4CA': '[INFO]',    # bar chart
    '\U0001F4CB': '[LIST]',    # clipboard
    '\U0001F4DD': '[NOTE]',    # memo
    '\U0001F512': '[LOCKED]',  # locked
    '\U0001F513': '[UNLOCKED]',
    '\U0001F510': '[SECURE]',  # locked with key
    '\U0001F511': '[KEY]',     # key

    # Lab/Science
    '\U0001F9EA': '[LAB]',     # test tube
    '\U0001F9EC': '[DNA]',     # DNA
    '\U0001F52C': '[ANALYZE]', # microscope
    '\U0001F9FF': '[EXP]',     # lab coat

    # Progress/Status
    '\U0001F3AF': '[TARGET]',  # bullseye
    '\U0001F389': '[DONE]',    # party popper
    '\U0001F38A': '[CELEBRATE]',
    '\U0001F3C6': '[SUCCESS]', # trophy
    '\U0001F947': '[1ST]',     # first place
    '\U0001F393': '[GRAD]',    # graduation cap
    '\U0001F4C8': '[STATS]',   # chart increasing

    # Navigation/Structure
    '\U0001F4C1': '[DIR]',     # file folder
    '\U0001F4C2': '[FOLDER]',  # open folder
    '\U0001F4E6': '[PACKAGE]', # package
    '\U0001F5C2': '[INDEX]',   # card index dividers
    '\U0001F5C3': '[ARCHIVE]', # card file box
    '\U0001F5C4': '[FILES]',   # file cabinet

    # Misc
    '\U0001F3E0': '[HOME]',    # house
    '\U0001FA86': '[NEST]',    # nesting dolls
    '\U0001F44B': '[BYE]',     # waving hand
    '\U0001F916': '[BOT]',     # robot
    '\U0001F4AC': '[CHAT]',    # speech bubble
    '\U0001F501': '[REFRESH]', # refresh
    '\U0001F504': '[CYCLE]',   # counterclockwise
    '\U0001F517': '[LINK]',    # link
    '\U0001F6E0': '[TOOLS]',   # wrench and hammer
    '\U0001F527': '[WRENCH]',  # wrench
    '\u2728': '',              # sparkles - remove
    '\U0001F31F': '',          # glowing star - remove

    # Symbols
    '\u2714': '[v]',           # check
    '\u2716': '[x]',           # cross
    '\u2795': '[+]',           # plus
    '\u2796': '[-]',           # minus
    '\u2139': '[i]',           # info

    # Special
    '\U0001F3A9': '',          # top hat - just remove
    '\u26a1': '[RUN]',         # lightning bolt
    '\u267b': '[RECYCLE]',     # recycle
    '\U0001F480': '[DEAD]',    # skull
    '\u2753': '[?]',           # question mark
    '\U0001F4CD': '[PIN]',     # pushpin
    '\U0001F5FA': '[MAP]',     # world map
    '\U0001F5D3': '[CAL]',     # calendar

    # Hearts/emotions - just remove
    '\u2764': '',
    '\U0001F496': '',
    '\U0001F497': '',
    '\U0001F498': '',
    '\U0001F499': '',
    '\U0001F49A': '',

    # Phases/moon
    '\U0001F311': '[PHASE-NEW]',
    '\U0001F312': '[PHASE-WAX1]',
    '\U0001F313': '[PHASE-WAX2]',
    '\U0001F314': '[PHASE-WAX3]',
    '\U0001F315': '[PHASE-FULL]',

    # Nature
    '\U0001F331': '[SEED]',     # seedling
    '\U0001F525': '[FIRE]',     # fire
    '\U0001F30D': '[WORLD]',    # globe
    '\U0001F30E': '[WORLD]',
    '\U0001F30F': '[WORLD]',

    # Creative
    '\U0001F3A8': '[ART]',      # palette
    '\U0001F4DA': '[BOOKS]',    # books
    '\U0001F4D6': '[BOOK]',     # open book
    '\U0001F4D7': '[BOOK]',
    '\U0001F4D8': '[BOOK]',
    '\U0001F4D9': '[BOOK]',
    '\U0001F4D2': '[BOOK]',
    '\U0001F4D3': '[BOOK]',
    '\U0001F52E': '[FUTURE]',   # crystal ball
    '\U0001F9ED': '[COMPASS]',  # compass
    '\U0001F9F0': '[TOOLKIT]',  # toolbox

    # Labels
    '\U0001F3F7': '[TAG]',      # label
    '\U0001F4CC': '[PIN]',      # pushpin
    '\U0001F4CE': '[ATTACH]',   # paperclip

    # Misc symbols that should be removed completely
    '\U0001F50A': '',           # speaker high volume
    '\U0001F5E3': '',           # speaking head
    '\U0001F30A': '',           # water wave
    '\u2615': '',               # hot beverage
}

# Directories to skip
SKIP_DIRS = {'.git', 'node_modules', '__pycache__', '.obsidian', 'ARCHIVE_RK01', '.venv', 'venv'}

# File extensions to process
EXTENSIONS = {'.py', '.md', '.yml', '.yaml', '.txt', '.json'}


def remove_emojis_from_text(text: str) -> str:
    """Remove emojis from text, using replacements where available."""
    result = text

    # First apply known replacements
    for emoji, replacement in EMOJI_REPLACEMENTS.items():
        result = result.replace(emoji, replacement)

    # Then remove any remaining emojis
    result = EMOJI_PATTERN.sub('', result)

    # Don't do any aggressive space cleanup - just remove emojis
    # The space cleanup was breaking Python code and ASCII art
    return result


def process_file(file_path: Path) -> bool:
    """Process a single file, removing emojis. Returns True if modified."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            original = f.read()

        # Check if file has emojis
        if not EMOJI_PATTERN.search(original):
            return False

        # Remove emojis
        modified = remove_emojis_from_text(original)

        # Only write if changed
        if modified != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(modified)
            return True

        return False

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def main():
    """Main entry point."""
    repo_root = Path(__file__).parent.parent

    print("Removing emojis from project files...")
    print(f"Repository: {repo_root}")
    print()

    modified_count = 0
    checked_count = 0

    for root, dirs, files in os.walk(repo_root):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]

        for filename in files:
            # Check extension
            ext = Path(filename).suffix.lower()
            if ext not in EXTENSIONS:
                continue

            file_path = Path(root) / filename
            checked_count += 1

            if process_file(file_path):
                rel_path = file_path.relative_to(repo_root)
                print(f"  Modified: {rel_path}")
                modified_count += 1

    print()
    print(f"Checked {checked_count} files")
    print(f"Modified {modified_count} files")
    print()

    if modified_count > 0:
        print("Emoji removal complete.")
    else:
        print("No emojis found.")


if __name__ == "__main__":
    main()
