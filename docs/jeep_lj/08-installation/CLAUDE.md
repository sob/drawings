# Installation Section - Navigation Guide

## What's Here

Project planning, installation tracking, and outstanding item management.

## Files

### `index.md` - Installation Overview

**Contains:** Links to installation resources across all sections

**Use when:** Finding installation checklists, wire routing, or firewall planning docs

### `01-tbd-tracker.md` - TBD Tracker

**Contains:** Central tracking of all To-Be-Determined items with priorities

**Use when:** Checking outstanding items, tracking progress, or planning next steps

## Cross-Section References

**To Power Systems (1):**
- Installation checklist (01-power-systems/installation-checklist.md)
- Wire routing (01-power-systems/07-wire-routing/index.md)

**To Engine Systems (2):**
- Firewall ingress (02-engine-systems/07-firewall-ingress.md)

## TBD Tracker Maintenance

### When Adding a TBD

1. Add the TBD item in the relevant .md file
2. Immediately add to TBD Tracker (01-tbd-tracker.md)
3. Include file reference with link
4. Assign priority: Critical, High, Medium, Low

### When Resolving a TBD

1. Update the relevant .md file with actual specification
2. Move item to "Recently Resolved" section in TBD Tracker with date
3. Update "Total Open Items" count
4. Update "Last Updated" date

### Finding All TBDs

```bash
# Search for all TBD items in documentation
grep -r "TBD" docs/jeep_lj --include="*.md" -n | grep -v "PHASE1-ANALYSIS" | grep -v "PROMPT.md" | grep -v "01-tbd-tracker"

# Count total TBD items
grep -r "TBD" docs/jeep_lj --include="*.md" | grep -v "PHASE1-ANALYSIS" | grep -v "PROMPT.md" | grep -v "01-tbd-tracker" | wc -l
```

### Priority Definitions

- **🔴 CRITICAL:** Installation blockers - must have before build starts
- **⚠️ HIGH PRIORITY:** Needed for final design - get before ordering parts
- **📋 MEDIUM PRIORITY:** Design optimization - can determine during build
- **🔍 VERIFICATION NEEDED:** Estimated values - verify with actual product specs

### Review Schedule

- **Weekly:** Review Critical and High Priority items
- **Monthly:** Review Medium Priority items
- **Before Parts Order:** Verify all High Priority items resolved
- **Before Installation:** Verify all Critical items resolved

## When Updating

**Adding installation documentation:**

1. Add to appropriate section (not here - installation docs live with their systems)
2. Link from 08-installation/index.md if it's a major installation resource
3. Keep this section focused on tracking and project management only

**Updating TBD Tracker:**

1. Always update "Last Updated" date
2. Keep "Recently Resolved" to last 10 items
3. Archive older resolved items if needed
4. Update summary table at bottom

## Success Criteria

✅ All TBD items are tracked with priorities
✅ Recently resolved items documented with dates
✅ Summary table matches actual counts
✅ Links point to correct files
✅ Last Updated date is current
