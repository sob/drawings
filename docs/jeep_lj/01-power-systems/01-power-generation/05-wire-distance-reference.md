---
hide:
  - toc
---

# 1.1.5 Wire Distance Reference {#wire-distance-reference}

Measured wire routing distances between major electrical components for voltage drop calculations and wire sizing.

!!! note "Measurement Method"
    These distances represent actual measured cable routing paths (not straight-line distances) following frame rails, firewall passages, and avoiding obstacles. All measurements are one-way cable length.

!!! info "Dual Wheel Well Battery Configuration"
    Both batteries located in rear wheel wells for optimal wire routing:

    - **Driver Wheel Well** = START battery (critical systems)
    - **Passenger Wheel Well** = AUX battery (accessories)

## Component Distance Matrix

| From | To | Distance | Notes |
|:-----|:---|:---------|:------|
| **Alternator** | **START battery** (driver wheel well) | 8 ft | Primary charging path |
| **Starter** | **START battery** (driver wheel well) | 6 ft | Cranking power |
| **PMU24** | **START battery** (driver wheel well) | 8 ft | Critical systems power |
| **BCDC Alpha 25** | START battery ↔ AUX battery | 5-6 ft | Inter-battery charging |
| **Winch** (front bumper) | **AUX battery** (passenger wheel well) | 13 ft | Recovery system power |
| **OEM Battery** (engine bay) | **Starter** | 4 ft | Reference: original configuration |
| **OEM Battery** (engine bay) | **Winch** (front bumper) | 5 ft | Reference: original configuration |
| **OEM Battery** (engine bay) | **Alternator** | 4 ft | Reference: original configuration |

## Optimized Wire Gauge Specifications

Wire gauges optimized for performance at measured routing distances:

| Circuit | Distance | Wire Gauge | Max Current | Voltage Drop @ Temp | Notes |
|:--------|:---------|:-----------|:------------|:--------------------|:------|
| **Alternator → START battery** | 8 ft | 2/0 AWG | 270A | 2.81% @ 60°C | Charging system - temp derating applied |
| **PMU24 Power Feed** | 8 ft | 1 AWG | 220A | 5.27% @ 60°C | Via CONSTANT bus - see routing notes |
| **Starter Motor** | 6 ft | 2/0 AWG | 400-600A | <3% @ 20°C | Brief cranking load - minimal temp effect |
| **BCDC Inter-Battery** | 5-6 ft | 6 AWG | 25A | 0.75% @ 20°C | Under-vehicle routing, lower ambient temp |
| **Winch → AUX battery** | 13 ft one-way (26 ft circuit) | 1/0 AWG | 250A typical, 400A peak | 6.3% @ 250A, 10.1% @ 400A @ 20°C | Wheel well routing, system voltage 13.8V (engine running) |

**Temperature Derating Notes:**

- Engine bay circuits (alternator, PMU) calculated @ 60°C ambient
- Wheel well circuits (starter, winch) calculated @ 20°C ambient
- Voltage drop percentages shown at maximum rated current

## Related Documentation

- [Batteries][batteries] - Battery specifications and mounting locations
- [BCDC Alpha 25][bcdc] - Inter-battery charging system
- [Alternator][alternator] - Charging system specifications
- [PMU24][pmu] - Power management unit
- [Starter System][starter] - Starter power requirements
- [Recovery Systems][recovery] - Winch specifications
- [START battery Distribution][starter-battery] - Driver wheel well battery terminal connections
- [AUX battery Distribution][aux-battery] - Passenger wheel well battery terminal connections

[batteries]: 01-batteries.md
[bcdc]: 03-bcdc.md
[alternator]: 02-alternator.md
[pmu]: ../04-pmu/index.md
[starter]: ../../02-engine-systems/01-starter.md
[recovery]: ../../07-exterior-systems/01-recovery-systems.md
[starter-battery]: ../02-starter-battery-distribution/index.md
[aux-battery]: ../03-aux-battery-distribution/index.md
