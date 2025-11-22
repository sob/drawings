---
hide:
  - toc
---

# 1.2 START battery Distribution (Driver Wheel Well) {#starter-battery-distribution}

/// html | div.product-info
![Odyssey PC1500 Battery Terminals](../../images/odyssey-pc1500.jpg){ loading=lazy }
///

## Overview

The START battery (driver wheel well) provides power for critical engine and safety systems:

1. **Direct high-current** → Starter (no CB), alternator charging input (no CB)
2. **Circuit breaker protected** → PMU (250A CB), BCDC (80A CB)
3. **Direct low-current** → ECM, grid heater (fusible link protection)

See [Circuit Breakers][circuit-breakers] for complete CB specifications. All CBs mounted in wheel well within 7" of battery (code compliant).

!!! info "Single Source of Truth"
    This page is the authoritative source for all START battery wire specs (gauge, distance, voltage drop). Component pages reference here. For battery specs see [Section 1.1][batteries]. For ground bus bars see [Section 1.5][grounding].

## START battery Positive Terminal

### Wheel Well to Engine Bay

| Circuit | Wire Gauge | Distance | Current | Voltage Drop | Protection |
|:--------|:-----------|:---------|:--------|:-------------|:-----------|
| [Alternator][alternator] (charging input) | 2/0 AWG | 8 ft | 270A | 2.81% @ 60°C (13.99V) | None |
| [Starter][starter] | 2/0 AWG | 6 ft | 400-600A | 1.9-3.9% (11.5-11.8V) | None |
| [PMU24][pmu] | 2/0 AWG | ~7 ft | 250A max | 2.4% @ 60°C (14.05V) | 250A CB |
| ECM | Per Cummins | Short | <5A | Negligible | Fusible link |
| [Grid Heater][grid-heater] Relay | Per Cummins | Short | ~80A | Negligible | Fusible link |

### Wheel Well to Wheel Well (Under Vehicle)

| Circuit | Wire Gauge | Distance | Current | Voltage Drop | Protection |
|:--------|:-----------|:---------|:--------|:-------------|:-----------|
| [BCDC Alpha 50][bcdc] | 4 AWG | ~6 ft | 50A | 0.94% (13.89V) | 80A CB |

**Total Positive Connections:** 6 (all active)

!!! info "Circuit Breaker Locations"
    All circuit breakers mounted in wheel well within 7" of battery positive terminal (ABYC/NEC code compliant). See [Circuit Breakers][circuit-breakers] for complete specifications.

## START battery Negative Terminal

### Wheel Well to Engine Bay

| Circuit | Wire Gauge | Distance | Current | Voltage Drop | Notes |
|:--------|:-----------|:---------|:--------|:-------------|:------|
| [Engine Bay Ground Bus][engine-ground-bus] | 2/0 AWG | ~8 ft | 600A+ peak | <0.1V | Primary return path |
| ECM Ground | 12 AWG | Short | <5A | Negligible | Cummins harness |
| [Grid Heater][grid-heater] Ground | Per Cummins | Short | ~80A | Negligible | Cummins harness |

### Wheel Well to Wheel Well (Under Vehicle)

| Circuit | Wire Gauge | Distance | Current | Voltage Drop | Notes |
|:--------|:-----------|:---------|:--------|:-------------|:------|
| [AUX Battery][aux-battery] Ground Reference | 1/0 AWG | 5-6 ft | 75A max | <0.05V | BCDC + fault path |

### Wheel Well to Dashboard (Along Tub)

| Circuit | Wire Gauge | Distance | Current | Voltage Drop | Notes |
|:--------|:-----------|:---------|:--------|:-------------|:------|
| [G1 GMRS Radio][radios] Ground | 10 AWG | ~8 ft | 15A TX | 1.2% (0.17V) | RF ground requirement |
| [STX Intercom][radios] Ground | 10 AWG | ~8 ft | 5A | 0.4% (0.06V) | RF ground requirement |
| [Ham Radio][radios] Ground | 10 AWG | ~8 ft | 13A TX | 1.0% (0.14V) | Future - RF ground |

**Total Negative Connections:** 7 (6 active + 1 future)

### Direct Connection Rationale

**ECM & Grid Heater:** Direct to battery via Cummins harness prevents voltage spikes from starter/alternator from damaging sensitive ECM electronics.

**Radios (G1 GMRS, STX, Ham):** Direct to battery negative minimizes ground loop noise and RF interference. Critical for radio performance.

## Related Documentation

- [Power Generation][power-gen] - Battery and alternator specifications
- [Circuit Breakers][circuit-breakers] - Complete CB specifications
- [Grounding Architecture][grounding] - Ground bus bars
- [PMU24][pmu] - Power management unit
- [BCDC Alpha 50][bcdc] - DC-DC charger to AUX battery
- [Starter System][starter] - Starter specifications
- [Alternator][alternator] - Charging system
- [AUX battery Distribution][aux-battery] - Aux/accessory battery system

[pmu]: ../04-pmu/index.md
[bcdc]: ../01-power-generation/03-bcdc.md
[batteries]: ../01-power-generation/01-batteries.md
[grid-heater]: ../../02-engine-systems/08-grid-heater.md
[grounding]: ../05-grounding/index.md
[engine-ground-bus]: ../05-grounding/01-engine-bay-ground-bus.md
[power-gen]: ../01-power-generation/index.md
[aux-battery]: ../03-aux-battery-distribution/index.md
[starter]: ../../02-engine-systems/01-starter.md
[alternator]: ../01-power-generation/02-alternator.md
[radios]: ../../06-communication-systems/01-communication.md
[circuit-breakers]: 01-circuit-breakers.md
