# Verify Ground Connections

Cross-check that all PMU outputs have documented ground paths and ground buses are consistent.

## Checks to Perform

1. **PMU outputs** - Read `01-power-systems/04-pmu/03-pmu-outputs.md` and verify each active output has a Ground column entry

2. **Ground bus cross-references** - For each ground location referenced in PMU outputs:
   - Engine Bay Bus (`05-grounding/01-engine-bay-ground-bus.md`) - verify stud assignments match
   - Firewall Stud Bus (`05-grounding/02-firewall-stud-bus.md`) - verify terminal assignments match
   - SwitchPros Ground Bus (`05-grounding/03-switchpros-ground-bus.md`) - verify terminal assignments match

3. **Direct battery grounds** - Verify loads marked as "Direct battery-" are documented in:
   - `02-starter-battery-distribution/index.md` for START battery
   - `03-aux-battery-distribution/index.md` for AUX battery

4. **Utilization counts** - Verify "X of Y used" counts are accurate on each ground bus

## Output Format

| Output | Documented Ground | Ground Bus Entry | Status |
|--------|-------------------|------------------|--------|
| OUT1   | Engine Bay Stud 7 | Found: iBooster  | OK     |
| OUT5   | Missing           | -                | ISSUE  |

## After Audit

List any:
- PMU outputs missing ground documentation
- Ground bus entries that don't match PMU output references
- Incorrect utilization counts
