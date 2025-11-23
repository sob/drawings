---
description: Check wire gauge, length, and rating consistency
---

# Verify Wire Specifications

Check wire gauge, length, and rating consistency across all documentation.

## Checks to Perform

### 1. Temperature Derating

For engine bay circuits (>50A continuous):

- Verify voltage drop calculations include 60°C derating (1.2x factor)
- Flag any high-current engine bay circuit missing temperature annotation

### 2. Wire Gauge vs Load

For each circuit:

- Calculate minimum wire gauge for stated load and distance
- Flag any undersized wiring (>3% voltage drop at rated load)

### 3. Distance Consistency

Compare wire distances stated in:

- Battery distribution pages (`02-starter-battery-distribution/index.md`, `03-aux-battery-distribution/index.md`)
- Load documentation (component pages)
- Wire distance reference (`01-power-generation/05-wire-distance-reference.md`)

### 4. Circuit Breaker Sizing

Verify CB is 125-160% of max load for each protected circuit

### 5. CB vs Wire Rating (Critical Safety)

- CB must be ≤ wire ampacity (CB protects wire, not load)
- Flag any circuit where CB rating exceeds wire continuous rating
- Wire ratings at temperature: engine bay @ 60°C, wheel well @ 20°C
- Common wire ratings @ 20°C: 2 AWG=130A, 4 AWG=95A, 6 AWG=75A

### 6. Ground Wire Analysis

Check all ground bus inputs and connections:

- Engine Bay Ground Bus (`05-grounding/01-engine-bay-ground-bus.md`)
- Firewall Stud Bus (`05-grounding/02-firewall-stud-bus.md`)
- SwitchPros Ground Bus (`05-grounding/03-switchpros-ground-bus.md`)

For each bus:

- Verify input wire gauge supports total load
- Verify individual connection wire gauges support their loads
- Note: Brief peak loads (starter, winch) don't require continuous wire rating

### 7. Cross-Reference Consistency

Compare specs between authoritative source and downstream pages. Flag any mismatches:

| Authoritative Source | Cross-Reference With |
|---------------------|----------------------|
| `02-starter-battery-distribution/index.md` | `01-power-generation/02-alternator.md`, `02-engine-systems/01-starter.md`, `04-pmu/01-pmu-overview.md` |
| `03-aux-battery-distribution/index.md` | `07-exterior-systems/01-recovery-systems.md`, `04-control-interfaces/02-switchpros-sp1200.md` |
| `03-aux-battery-distribution/02-constant-bus.md` | `03-aux-battery-distribution/01-circuit-breakers.md`, `03-body-pdu.md`, `04-safetyhub.md` |
| `05-grounding/*.md` | Component pages referencing ground connections |
| `01-power-generation/05-wire-distance-reference.md` | All battery distribution and component pages |

Check for consistency in:

- Wire gauge
- Distance
- Current rating
- Circuit breaker size
- Voltage drop calculations

## Reference Tables

Use these for calculations:

- 12V system, copper wire
- 3% max voltage drop for critical circuits
- 5% max for non-critical circuits

**Wire Ampacity @ 20°C (chassis/wheel well):**

| Gauge | Ampacity |
|-------|----------|
| 1/0 AWG | 150A |
| 2 AWG | 130A |
| 4 AWG | 95A |
| 6 AWG | 75A |
| 10 AWG | 55A |
| 12 AWG | 30A |
| 14 AWG | 25A |
| 16 AWG | 18A |

**Wire Ampacity @ 60°C (engine bay) - derate by ~15%:**

| Gauge | Ampacity |
|-------|----------|
| 2/0 AWG | 265A |
| 1/0 AWG | 125A |
| 2 AWG | 110A |

## Output Format

### Power Circuits

| Circuit | Load | Distance | Gauge | Wire Rating | V-Drop | CB | CB % of Wire | Status |
|---------|------|----------|-------|-------------|--------|-----|--------------|--------|
| PMU main | 220A | 7ft | 2/0 AWG | 265A @60C | 2.4% | 250A | 94% | ✅ OK |
| SwitchPros | 100A | 2ft | 2 AWG | 130A @20C | 0.4% | 150A | 115% | ✅ OK |
| Example bad | 50A | 2ft | 4 AWG | 95A @20C | 0.3% | 150A | 158% | ❌ CB > wire |

### Ground Circuits

| Ground Bus | Input Wire | Wire Rating | Total Load | Status |
|------------|------------|-------------|------------|--------|
| Engine Bay | 2/0 AWG | 265A @60C | 600A+ peak | ✅ OK (brief peaks) |
| Firewall Stud | 4 AWG | 95A @20C | ~50A | ✅ OK |
| SwitchPros | 1/0 AWG | 150A @20C | ~100A | ✅ OK |

### Cross-Reference Mismatches

| Circuit | Spec | Source Value | Downstream File | Downstream Value | Status |
|---------|------|--------------|-----------------|------------------|--------|
| BCDC | Distance | 6 ft | `03-bcdc.md` | 6 ft | ✅ Match |
| Example | Wire | 2 AWG | `component.md` | 4 AWG | ❌ Mismatch |

## After Audit

List circuits needing attention, prioritized by:

1. **Safety critical:** CB rating exceeds wire ampacity (wire could overheat before CB trips)
2. **Safety critical:** Ground wire undersized for load
3. Undersized power wire for load
4. Cross-reference mismatches between files
5. Missing temperature derating
