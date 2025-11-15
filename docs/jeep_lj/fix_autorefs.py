#!/usr/bin/env python3
"""
Fix malformed autorefs links from [text][# heading {#id}] to [text][id]
"""

import re
from pathlib import Path

def fix_file(file_path: Path) -> int:
    """Fix autorefs links in a file. Returns count of fixes."""
    content = file_path.read_text()
    original_content = content

    # Pattern: [text][# anything {#id}]  ->  [text][id]
    # Captures the ID from within {#...}
    pattern = r'\[([^\]]+)\]\[#[^\{]*\{#([^}]+)\}\]'
    replacement = r'[\1][\2]'

    content = re.sub(pattern, replacement, content)

    fixes = len(re.findall(pattern, original_content))

    if content != original_content:
        file_path.write_text(content)

    return fixes

def main():
    docs_root = Path("/Users/seobrien/work/drawings/docs/jeep_lj")
    total_fixes = 0

    print("Fixing malformed autorefs links...")

    for md_file in docs_root.rglob("*.md"):
        if md_file.name.endswith('.py'):
            continue

        fixes = fix_file(md_file)
        if fixes > 0:
            total_fixes += fixes
            print(f"  ✓ {md_file.relative_to(docs_root)}: fixed {fixes} links")

    print(f"\n✅ Fixed {total_fixes} autorefs links")

if __name__ == "__main__":
    main()
