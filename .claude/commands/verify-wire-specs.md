# Verify Wire Specifications

Check wire gauge, length, and rating consistency across all documentation.

## Checks to Perform

1. **Temperature derating** - For engine bay circuits (>50A continuous):
   - Verify voltage drop calculations include 60C derating (1.2x factor)
   - Flag any high-current engine bay circuit missing temperature annotation

2. **Wire gauge vs load** - For each circuit:
   - Calculate minimum wire gauge for stated load and distance
   - Flag any undersized wiring (>3% voltage drop at rated load)

3. **Distance consistency** - Compare wire distances stated in:
   - Battery distribution pages
   - Load documentation
   - Installation checklist
   - Wire distance reference (`01-power-generation/05-wire-distance-reference.md`)

4. **Circuit breaker sizing** - Verify CB is 125-160% of max load for each protected circuit

## Reference Tables

Use these for calculations:
- 12V system, copper wire
- 3% max voltage drop for critical circuits
- 5% max for non-critical circuits

## Output Format

| Circuit | Load | Distance | Gauge | V-Drop | CB | Status |
|---------|------|----------|-------|--------|-----|--------|
| PMU main | 220A | 7ft | 1 AWG | 2.8% @60C | 250A | OK |
| BCDC input | 50A | 8ft | 4 AWG | 3.2% | 40A | WARN |

## After Audit

List circuits needing attention, prioritized by:
1. Safety issues (undersized wire for load)
2. Inconsistent specs across files
3. Missing temperature derating
