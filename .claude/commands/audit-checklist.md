# Audit Installation Checklist

Review and improve installation checklist tasks for a specific section.

**Argument:** Section number or name (e.g., "01", "02", "engine-systems")

**Search Path:** `docs/jeep_lj/<section>/installation-checklist.md`

## Audit Goals

1. **Rephrase as confirmations** - Tasks should read as verification steps for an amateur mechanic
   - Before: "Wire PMU Out 11 → WS-51C"
   - After: "Confirm PMU Out 11 is wired to WS-51C power input (14 AWG red)"

2. **Include specific specs** - Torque values, wire gauges, pin numbers
   - "Ensure iBooster mounting bolts are torqued to 25 ft-lb"
   - "Confirm 10 AWG wire from PMU OUT1+10 to iBooster"

3. **Group logically** - Tasks should flow in installation order

4. **Be specific** - Reference exact pins, outputs, wire colors, torque specs when known

## Task Phrasing Guide

| Type | Pattern | Example |
|------|---------|---------|
| Wiring | "Confirm [source] is connected to [destination] ([gauge] [color])" | "Confirm PMU OUT1+10 connected to iBooster main power (10 AWG red)" |
| Mounting | "Ensure [component] is mounted at [location], torqued to [spec]" | "Ensure iBooster mounted at factory location, bolts torqued to 25 ft-lb" |
| Testing | "Verify [condition] ([expected value])" | "Verify 12V present at iBooster with ignition OFF and ON" |
| Configuration | "Confirm [setting] is configured in [system]" | "Confirm PMU output combining configured for OUT1+10" |
| Fasteners | "Ensure [fastener] torqued to [spec]" | "Ensure ground stud nut torqued to 15 ft-lb" |

## Output Format

Show the revised checklist with:
1. Tasks rephrased as confirmations with specs
2. Missing specs flagged as TBD if not in design docs
3. Any tasks that need clarification noted

Present as replacement text ready to apply after user approval.

## After Review

Apply changes to the installation-checklist.md file after user approval.
