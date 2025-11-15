#!/usr/bin/env python3
"""
Convert all markdown internal links to mkdocs-autorefs format.
- Adds stable {#id} identifiers to h1 headings
- Converts [text](path.md) to [text][heading-id]
"""

import os
import re
from pathlib import Path
from typing import Dict, Tuple

def slugify(text: str) -> str:
    """Convert heading text to slug identifier (without section numbers)."""
    # Remove section numbers like "1.4 -" or "Section 2:"
    text = re.sub(r'^\d+\.?\d*\.?\d*\.?\s*-?\s*', '', text)
    text = re.sub(r'^Section\s+\d+:\s*', '', text, flags=re.IGNORECASE)

    # Convert to lowercase and replace spaces/special chars with hyphens
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    text = text.strip('-')

    return text

def process_file(file_path: Path) -> Tuple[str, Dict[str, str]]:
    """
    Process a markdown file:
    - Extract h1 heading and add {#id} if missing
    - Return the heading ID and updated content
    """
    content = file_path.read_text()
    heading_id = None

    # Find h1 heading (first line starting with #, not ##)
    h1_match = re.search(r'^#\s+([^#\n]+?)(\s*\{#([^}]+)\})?\s*$', content, re.MULTILINE)

    if h1_match:
        heading_text = h1_match.group(1).strip()
        existing_id = h1_match.group(3)

        if existing_id:
            heading_id = existing_id
        else:
            # Generate new ID from heading text
            heading_id = slugify(heading_text)

            # Replace the heading with one that includes the ID
            old_heading = h1_match.group(0)
            new_heading = f"# {heading_text} {{#{heading_id}}}"
            content = content.replace(old_heading, new_heading, 1)

    return content, {str(file_path): heading_id} if heading_id else {}

def main():
    docs_root = Path("/Users/seobrien/work/drawings/docs/jeep_lj")

    # Step 1: Process all markdown files and build heading ID map
    print("Step 1: Adding heading IDs...")
    file_to_id = {}

    for md_file in docs_root.rglob("*.md"):
        if md_file.name == "convert_links.py":
            continue

        content, ids = process_file(md_file)

        if ids:
            file_to_id.update(ids)
            md_file.write_text(content)
            print(f"  ✓ {md_file.relative_to(docs_root)}: {list(ids.values())[0]}")

    print(f"\nProcessed {len(file_to_id)} files with h1 headings")

    # Step 2: Convert all internal markdown links
    print("\nStep 2: Converting internal links...")
    link_count = 0

    for md_file in docs_root.rglob("*.md"):
        if md_file.name == "convert_links.py":
            continue

        content = md_file.read_text()
        original_content = content

        # Find all markdown links: [text](path)
        # Exclude: http/https URLs, image links, and anchor-only links
        def replace_link(match):
            nonlocal link_count
            link_text = match.group(1)
            link_path = match.group(2)

            # Skip external links
            if link_path.startswith(('http://', 'https://')):
                return match.group(0)

            # Skip image links
            if 'images/' in link_path or link_path.endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg')):
                return match.group(0)

            # Skip anchor-only links (#something)
            if link_path.startswith('#'):
                return match.group(0)

            # Skip PDF links
            if link_path.endswith('.pdf'):
                return match.group(0)

            # Resolve the target file path
            target_path = (md_file.parent / link_path).resolve()

            # Find the heading ID for this target
            target_id = file_to_id.get(str(target_path))

            if target_id:
                link_count += 1
                # Convert to autorefs format: [text][id]
                return f"[{link_text}][{target_id}]"
            else:
                print(f"  ⚠ Warning: No heading ID found for {link_path} in {md_file.name}")
                return match.group(0)

        # Replace all internal markdown links
        content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_link, content)

        if content != original_content:
            md_file.write_text(content)

    print(f"\nConverted {link_count} internal links to autorefs format")
    print("\n✅ Done! All files updated.")

if __name__ == "__main__":
    main()
