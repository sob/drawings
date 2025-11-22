---
description: Aggregate and report all Outstanding Items (checkbox tasks) across documentation
---

# Verify Outstanding Tasks

Aggregate all `- [ ]` checkbox items from source files and report them grouped by section and file.

**Argument:** `$ARGUMENTS` (optional section name or number, e.g., "01" or "power-systems" or "01-power-systems")

**Search Path:**
- If argument provided: `docs/jeep_lj/<section>/` (match by number prefix or name)
- If no argument: `docs/jeep_lj/` (all sections)

**Note:** Unlike TBD items, Outstanding Items are NOT centrally tracked. They live in source files near their context. This command aggregates them for review.

## What to Search

Find all uncompleted checkbox items:
```
- [ ] Task description
```

Skip completed items:
```
- [x] Completed task
```

## Exclusions

Skip these files:
- `CLAUDE.md` files
- Any file in `.claude/` directory
- `installation-checklist.md` files (these are comprehensive build checklists, not design tasks)

## Output Format

Group by section, then by file, showing line number and full task text:

**Section 01: Power Systems**

### installation-checklist.md
| Line | Task |
|------|------|
| 20 | Identify rear frame rail ground point location |
| 21 | Install 2/0 AWG: START battery- → Front Frame Rail |

### 03-body-pdu.md
| Line | Task |
|------|------|
| 80 | Verify all circuit breakers and relays are functional |

(etc. for each file with tasks)

**Section 02: Engine Systems**

### 01-starter.md
| Line | Task |
|------|------|
| 108 | Determine ignition START wire routing through firewall |

(etc.)

---

**Summary:**
| Section | Files | Open Tasks |
|---------|-------|------------|
| 01-power-systems | X | X |
| 02-engine-systems | X | X |
| ... | ... | ... |
| **TOTAL** | **X** | **X** |

## Task Categories (informational)

When reviewing, tasks generally fall into:
- **Design decisions** - choices that need to be made (which output, which location)
- **Verification** - specs to confirm (current draw, compatibility)
- **Ordering** - parts to purchase
- **Installation** - physical work during build

No need to tag these in source files - just useful context when reviewing the list.

## After Review

Tasks stay in their source files. This command is read-only reporting.

To mark a task complete, edit the source file:
```
- [x] Completed task description
```
