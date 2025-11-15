#!/usr/bin/env python3
"""
Convert Jeep LJ documentation to use mkdocs-autorefs.

This script:
1. Adds stable heading identifiers to all H1 headings
2. Converts internal markdown links to autorefs syntax
3. Preserves external links and image links
"""

import re
import os
from pathlib import Path
from typing import Dict, List, Tuple, Set
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


class AutorefsConverter:
    """Convert markdown documentation to use mkdocs-autorefs."""

    def __init__(self, docs_root: str):
        self.docs_root = Path(docs_root)
        self.file_to_heading_id: Dict[str, str] = {}
        self.stats = {
            'files_processed': 0,
            'headings_added': 0,
            'links_converted': 0,
            'errors': []
        }

    def generate_identifier(self, heading_text: str) -> str:
        """
        Generate a stable identifier from heading text.

        Rules:
        - Remove section numbers (e.g., "1.4 -" or "Section 1:")
        - Convert to lowercase
        - Replace spaces with hyphens
        - Remove special characters except hyphens
        - Strip leading/trailing hyphens

        Examples:
        - "1.4 - PMU Power Distribution" → "pmu-power-distribution"
        - "Section 1: Power Systems" → "power-systems"
        - "2.1 Starter System" → "starter-system"
        """
        # Remove section numbering patterns
        text = re.sub(r'^(\d+\.)*\d+\s*[-:]\s*', '', heading_text.strip())
        text = re.sub(r'^Section\s+\d+:\s*', '', text, flags=re.IGNORECASE)

        # Convert to lowercase and replace spaces with hyphens
        text = text.lower()
        text = re.sub(r'\s+', '-', text)

        # Remove special characters except hyphens
        text = re.sub(r'[^a-z0-9-]', '', text)

        # Remove multiple consecutive hyphens
        text = re.sub(r'-+', '-', text)

        # Strip leading/trailing hyphens
        text = text.strip('-')

        return text

    def extract_h1_heading(self, content: str) -> Tuple[str, str, str, bool]:
        """
        Extract the first H1 heading from markdown content.

        Returns:
            (heading_text, identifier, heading_with_id, has_existing_id)
        """
        # Match H1 heading with optional existing identifier
        pattern = r'^#\s+(.+?)(?:\s+\{#([a-z0-9-]+)\})?\s*$'

        for line in content.split('\n'):
            match = re.match(pattern, line.strip())
            if match:
                heading_text = match.group(1).strip()
                existing_id = match.group(2)
                has_id = existing_id is not None

                # Use existing ID if present, otherwise generate one
                identifier = existing_id if has_id else self.generate_identifier(heading_text)
                heading_with_id = f"# {heading_text} {{#{identifier}}}"

                return heading_text, identifier, heading_with_id, has_id

        return "", "", "", False

    def add_heading_identifier(self, content: str) -> Tuple[str, str, bool]:
        """
        Add identifier to the first H1 heading if not present.

        Returns:
            (modified_content, identifier, was_added)
        """
        heading_text, identifier, heading_with_id, has_id = self.extract_h1_heading(content)

        if not heading_text:
            return content, "", False

        if has_id:
            # Already has identifier
            return content, identifier, False

        # Add identifier to heading - match H1 without identifier
        pattern = r'^(#\s+' + re.escape(heading_text) + r')\s*$'
        modified_content = re.sub(
            pattern,
            f"# {heading_text} {{#{identifier}}}",
            content,
            count=1,
            flags=re.MULTILINE
        )

        return modified_content, identifier, True

    def build_file_mapping(self) -> None:
        """Build mapping of file paths to their heading identifiers."""
        logger.info("Building file-to-heading mapping...")

        md_files = list(self.docs_root.rglob('*.md'))
        # Skip meta files
        md_files = [f for f in md_files if f.name not in ['CLAUDE.md', 'MIGRATION_COMPLETE.md']]

        for md_file in md_files:
            try:
                content = md_file.read_text(encoding='utf-8')
                _, identifier, _, _ = self.extract_h1_heading(content)

                if identifier:
                    # Store relative path from docs root
                    rel_path = md_file.relative_to(self.docs_root)
                    self.file_to_heading_id[str(rel_path)] = identifier
                    logger.debug(f"Mapped {rel_path} → {identifier}")
                else:
                    logger.warning(f"No H1 heading found in {md_file}")
            except Exception as e:
                logger.error(f"Error processing {md_file}: {e}")
                self.stats['errors'].append(f"Mapping {md_file}: {e}")

        logger.info(f"Built mapping for {len(self.file_to_heading_id)} files")

    def resolve_link_path(self, current_file: Path, link_path: str) -> str:
        """
        Resolve a relative link path to absolute path from docs root.

        Args:
            current_file: Path to the current markdown file
            link_path: Relative link path (e.g., "../01-power-systems/index.md")

        Returns:
            Path relative to docs root (e.g., "01-power-systems/index.md")
        """
        # Get directory containing current file
        current_dir = current_file.parent

        # Resolve the link path relative to current directory
        target_path = (current_dir / link_path).resolve()

        # Return path relative to docs root
        try:
            rel_path = target_path.relative_to(self.docs_root)
            return str(rel_path)
        except ValueError:
            # Path is outside docs root
            return ""

    def convert_links(self, content: str, current_file: Path) -> Tuple[str, int]:
        """
        Convert internal markdown links to autorefs syntax.

        Args:
            content: Markdown file content
            current_file: Path to current file

        Returns:
            (modified_content, number_of_conversions)
        """
        conversions = 0

        # Pattern to match markdown links: [text](path.md) or [text](path.md#anchor)
        # Excludes external links (http/https) and image links (images/)
        link_pattern = r'\[([^\]]+)\]\(([^)]+\.md(?:#[^)]*)?)\)'

        def replace_link(match):
            nonlocal conversions

            link_text = match.group(1)
            link_path = match.group(2)

            # Skip external links
            if link_path.startswith(('http://', 'https://')):
                return match.group(0)

            # Skip image links
            if 'images/' in link_path:
                return match.group(0)

            # Remove anchor if present (we'll use heading ID instead)
            link_path_clean = re.sub(r'#.*$', '', link_path)

            # Resolve to path relative to docs root
            resolved_path = self.resolve_link_path(current_file, link_path_clean)

            if not resolved_path:
                logger.warning(f"Could not resolve link: {link_path} in {current_file}")
                return match.group(0)

            # Look up heading identifier
            heading_id = self.file_to_heading_id.get(resolved_path)

            if not heading_id:
                logger.warning(f"No heading ID found for: {resolved_path} (from {current_file})")
                return match.group(0)

            # Convert to autorefs syntax
            conversions += 1
            return f"[{link_text}][{heading_id}]"

        modified_content = re.sub(link_pattern, replace_link, content)
        return modified_content, conversions

    def process_file(self, md_file: Path) -> None:
        """Process a single markdown file."""
        try:
            content = md_file.read_text(encoding='utf-8')
            original_content = content

            # Add heading identifier if needed
            content, identifier, heading_added = self.add_heading_identifier(content)
            if heading_added:
                self.stats['headings_added'] += 1
                logger.debug(f"Added heading ID '{identifier}' to {md_file}")

            # Convert links
            content, links_converted = self.convert_links(content, md_file)
            if links_converted > 0:
                self.stats['links_converted'] += links_converted
                logger.debug(f"Converted {links_converted} links in {md_file}")

            # Write back if modified
            if content != original_content:
                md_file.write_text(content, encoding='utf-8')
                self.stats['files_processed'] += 1
                logger.info(f"Updated: {md_file.relative_to(self.docs_root)}")

        except Exception as e:
            logger.error(f"Error processing {md_file}: {e}")
            self.stats['errors'].append(f"Processing {md_file}: {e}")

    def process_all_files(self) -> None:
        """Process all markdown files in the docs directory."""
        logger.info("Processing markdown files...")

        md_files = sorted(self.docs_root.rglob('*.md'))

        # Skip CLAUDE.md and MIGRATION_COMPLETE.md (meta files)
        md_files = [f for f in md_files if f.name not in ['CLAUDE.md', 'MIGRATION_COMPLETE.md']]

        for md_file in md_files:
            self.process_file(md_file)

        logger.info("Processing complete!")

    def print_summary(self) -> None:
        """Print conversion summary."""
        print("\n" + "=" * 70)
        print("CONVERSION SUMMARY")
        print("=" * 70)
        print(f"Files updated:           {self.stats['files_processed']}")
        print(f"Heading IDs added:       {self.stats['headings_added']}")
        print(f"Links converted:         {self.stats['links_converted']}")
        print(f"Errors:                  {len(self.stats['errors'])}")

        if self.stats['errors']:
            print("\nErrors encountered:")
            for error in self.stats['errors']:
                print(f"  - {error}")

        print("=" * 70)

    def run(self) -> None:
        """Run the complete conversion process."""
        logger.info(f"Starting conversion in: {self.docs_root}")

        # Step 1: Build file mapping (first pass to get all identifiers)
        self.build_file_mapping()

        # Step 2: Process all files (add IDs and convert links)
        self.process_all_files()

        # Step 3: Print summary
        self.print_summary()


def main():
    """Main entry point."""
    docs_root = "/Users/seobrien/work/drawings/docs/jeep_lj"

    converter = AutorefsConverter(docs_root)
    converter.run()


if __name__ == "__main__":
    main()
