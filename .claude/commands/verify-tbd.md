---
description: Verify all TBD items are tracked in the centralized tracker
---

# Verify TBD Tracking

Ensure all TBD items are tracked in the centralized tracker with appropriate priorities.

**Search Path:** `docs/jeep_lj/` (exclude CLAUDE.md files, tracker itself, and .claude/)

**Tracker Location:** `docs/jeep_lj/08-installation/01-tbd-tracker.md`

## Checks to Perform

### 1. Find all TBD items in source files

Search all .md files in `docs/jeep_lj/` for:
- "TBD" (case insensitive)
- "TODO" outside of Outstanding Items sections
- "UNKNOWN" or "unknown"

### 2. Cross-reference: Source → Tracker

For each TBD found in source files:
- Check if it exists in tracker
- Verify priority level is assigned (Critical/High/Medium/Low/Verify)
- Verify file path in tracker matches actual location

### 3. Cross-reference: Tracker → Source (CRITICAL)

For each entry in the tracker, verify the TBD still exists in the source file:
- Read the referenced file
- Search for corresponding TBD text
- If TBD is resolved (no longer says TBD), mark as stale

### 4. Stale tracker entries

Flag tracker entries where:
- Referenced file no longer exists
- TBD has been resolved but not moved to "Recently Resolved"
- Duplicate entries for same item
- Source file now has actual value instead of TBD

### 5. Priority validation

Flag potential priority mismatches:
- Part numbers marked Medium/Low should be High (blocks ordering)
- Wire gauges marked Low should be Medium (affects installation)
- Mounting locations can stay Medium/Low (determined during build)

## Exclusions

Skip these files when searching:
- `CLAUDE.md` files (navigation guides, reference TBD process)
- `01-tbd-tracker.md` itself (contains TBD as content)
- Any file in `.claude/` directory
- `index.md` files that just reference the tracker

## Output Format

**Untracked TBD Items:**
| File | Line | TBD Text | Suggested Priority |
|------|------|----------|-------------------|

**Stale Tracker Entries (resolved in source):**
| Tracker Entry | Source File | Current Value | Action |
|---------------|-------------|---------------|--------|

**Priority Mismatches:**
| Item | Current | Suggested | Reason |
|------|---------|-----------|--------|

**Count Validation:**
- Verify tracker summary counts match actual table row counts
- Verify Total Open Items matches sum of priorities

## After Audit

1. Move resolved items to "Recently Resolved" with date and resolution
2. Add untracked items to appropriate priority section
3. Update priority levels if needed
4. Update summary counts
5. Run `mkdocs build` to verify no broken links
