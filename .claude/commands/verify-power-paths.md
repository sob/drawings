# Verify Power Distribution Paths

Trace power from batteries through distribution to loads, checking for consistency.

## Checks to Perform

1. **START battery paths** - For each load in `02-starter-battery-distribution/index.md`:
   - Verify circuit breaker exists in `01-circuit-breakers.md`
   - Verify wire gauge matches between source and load documentation
   - Check load's own documentation references correct power source

2. **AUX battery paths** - For each load in `03-aux-battery-distribution/index.md`:
   - Verify circuit breaker exists in `01-circuit-breakers.md`
   - Verify CONSTANT bus connection in `02-constant-bus.md` if applicable
   - Check load's own documentation references correct power source

3. **PMU power source** - Verify PMU main power documented consistently:
   - START battery distribution page
   - Circuit breaker page (250A CB)
   - PMU overview page

4. **Wire gauge consistency** - Flag any circuit where wire gauge differs between:
   - Battery distribution page
   - Circuit breaker page
   - Load's own documentation

## Output Format

For each inconsistency:
```
Circuit: [name]
  Source says: 4 AWG, 40A CB
  Load doc says: 6 AWG, 50A CB
  Files: [list of files with conflicting info]
```

## After Audit

Identify the authoritative source for each inconsistency and recommend which files need updating.
