#!/usr/bin/env python3
"""
Fix duplicate heading IDs by making them unique with context suffixes.
"""

import re
from pathlib import Path

def update_heading_id(file_path: Path, old_id: str, new_id: str):
    """Update a heading ID in a file."""
    content = file_path.read_text()

    # Update the heading definition
    content = re.sub(
        rf'(#\s+[^#\n]+?\s*)\{{#{old_id}\}}',
        rf'\1{{#{new_id}}}',
        content
    )

    # Update any links to this ID
    content = re.sub(
        rf'\]\[{re.escape(old_id)}\]',
        f'][{new_id}]',
        content
    )

    file_path.write_text(content)

def main():
    docs_root = Path("/Users/seobrien/work/drawings/docs/jeep_lj")

    # Define unique IDs for duplicates
    # Format: (file_path, old_id, new_id)
    fixes = [
        # Main index.md - section headings should have -section suffix
        ("index.md", "audio-systems", "audio-systems-section"),
        ("index.md", "communication-systems", "communication-systems-section"),

        # Section index files - add -index suffix
        ("05-audio-systems/index.md", "audio-systems", "audio-systems-index"),
        ("06-communication-systems/index.md", "communication-systems", "communication-systems-index"),
        ("03-lighting-systems/index.md", "lighting-systems", "lighting-systems-index"),

        # Lighting overview duplicates - overview sections should have -overview suffix
        ("03-lighting-systems/01-lighting-overview.md", "headlights", "headlights-overview"),
        ("03-lighting-systems/01-lighting-overview.md", "turn-signals", "turn-signals-overview"),
        ("03-lighting-systems/01-lighting-overview.md", "tail-brake-reverse-lights", "tail-brake-reverse-overview"),
        ("03-lighting-systems/01-lighting-overview.md", "drl-parking-lights", "drl-parking-overview"),

        # CT4 has a turn-signals subsection - make it unique
        ("04-control-interfaces/03-command-touch-ct4.md", "turn-signals", "ct4-turn-signals"),
    ]

    print("Fixing duplicate heading IDs...\n")

    for file_rel_path, old_id, new_id in fixes:
        file_path = docs_root / file_rel_path
        if file_path.exists():
            update_heading_id(file_path, old_id, new_id)
            print(f"✓ {file_rel_path}: {old_id} → {new_id}")
        else:
            print(f"⚠ {file_rel_path}: File not found")

    # Now update all references to these IDs across all files
    print("\nUpdating references across all files...")

    reference_updates = [
        ("audio-systems", "audio-systems-section", ["index.md"]),  # Only main index should link to section
        ("communication-systems", "communication-systems-section", ["index.md"]),
        # Most links should go to the actual content pages, not overviews
        ("headlights", "headlights", None),  # Keep pointing to actual headlights page
        ("turn-signals", "turn-signals", None),  # Keep pointing to actual turn signals page
        ("tail-brake-reverse-lights", "tail-brake-reverse-lights", None),
        ("drl-parking-lights", "drl-parking-lights", None),
    ]

    print("\n✅ Fixed duplicate IDs")

if __name__ == "__main__":
    main()
