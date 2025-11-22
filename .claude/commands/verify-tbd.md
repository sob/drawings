# Verify TBD Tracking

Ensure all TBD items are tracked in the centralized tracker with appropriate priorities.

## Checks to Perform

1. **Find all TBD items** - Search all .md files for:
   - "TBD" (case insensitive)
   - "TODO" outside of Outstanding Items sections
   - "UNKNOWN" or "unknown"
   - Empty table cells that should have values

2. **Cross-reference tracker** - For each TBD found:
   - Check if it exists in `08-installation/01-tbd-tracker.md`
   - Verify priority level is assigned (Critical/High/Medium/Low)
   - Verify file path in tracker matches actual location

3. **Stale tracker entries** - Find tracker entries where:
   - Referenced file no longer exists
   - TBD has been resolved but not moved to "Recently Resolved"
   - Duplicate entries for same item

4. **Priority validation** - Flag potential priority mismatches:
   - Part numbers marked Medium should be High (blocks ordering)
   - Wire gauges marked Low should be Medium (affects installation)

## Exclusions

Skip these files when searching:
- `CLAUDE.md` files (navigation guides)
- `01-tbd-tracker.md` itself
- Any file in `.claude/` directory

## Output Format

**Untracked TBD Items:**
| File | Line | TBD Text | Suggested Priority |
|------|------|----------|-------------------|

**Stale Tracker Entries:**
| Tracker Entry | Issue |
|---------------|-------|

## After Audit

Provide commands to:
1. Add untracked items to tracker
2. Remove stale entries
3. Update priorities if needed
