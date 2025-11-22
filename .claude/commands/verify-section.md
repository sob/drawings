---
description: Audit a documentation section for quality and consistency
argument-hint: <section-path>
---

# Verify Documentation Section

Audit the specified documentation section for quality and consistency issues.

**Section path:** $ARGUMENTS (e.g., `01-power-systems` or `01-power-systems/04-pmu`)

## Checks to Perform

1. **Duplicate content** - Find repeated tables, specs, or text across files in the section
2. **Broken links** - Verify all reference-style links resolve to existing files
3. **Inline links** - Flag any inline markdown links (should be reference-style per CLAUDE.md)
4. **TBD tracking** - Find any TBD items not tracked in `08-installation/01-tbd-tracker.md`
5. **Outstanding items** - Verify checkbox items are specific and actionable
6. **Image paths** - Confirm images exist in `docs/jeep_lj/images/`

## Output Format

Report findings grouped by issue type. For each issue:
- File path and line number
- Description of the problem
- Suggested fix (if applicable)

## After Audit

Summarize:
- Total issues found by category
- Files with most issues
- Recommended priority for fixes
