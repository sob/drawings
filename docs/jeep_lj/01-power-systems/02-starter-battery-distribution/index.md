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

!!! info "Battery Specifications"
    For complete battery specifications (capacity, dimensions, terminals, etc.), see [Section 1.1 - Battery System][batteries].

!!! note "Battery Location"
    START battery located in **driver side rear wheel well** for optimal wire routing to critical engine systems. See [Wire Distance Reference][wire-distance] for measured routing distances.

## START battery Positive Terminal

**START battery Positive Terminal Connections:**

| # | Connection | Wire Gauge | Distance | Voltage @ Load | Protection | Destination/Notes | Status |
|:--|:-----------|:-----------|:---------|:---------------|:-----------|:------------------|:-------|
| | **━━━ CHARGING INPUT ━━━** | | | | | | |
| 1 | Alternator | 2/0 AWG ✓ | 8 ft | 13.996V (2.81% @ 60°C) | None | 270A alternator output charges START battery - see [Alternator][alternator] | Active |
| | **━━━ CRITICAL SYSTEMS ━━━** | | | | | | |
| 2 | Cummins R2.8 Starter | 2/0 AWG ✓ | 6 ft | 11.53V (3.9%) | None | 400-600A cranking current - see [Starter][starter] | Active |
| | **━━━ CIRCUIT BREAKER PROTECTED LOADS ━━━** | | | | | | |
| 3 | PMU24 | 2/0 AWG ✓ | ~7 ft | 14.05V (2.4% @ 60°C) | 250A CB (wheel well) | Power management unit - see [PMU][pmu] | Active |
| 4 | BCDC Alpha 50 | 4 AWG ✓ | ~6 ft | 13.89V (0.94%) | 80A CB (wheel well) | DC-DC charger to AUX battery - see [BCDC][bcdc] | Active |
| | **━━━ DIRECT CONNECTIONS ━━━** | | | | | | |
| 6 | Cummins ECM | Per Cummins | Short | ~12V | Fusible link | Engine control module | Active |
| 7 | Grid Heater Relay | Per Cummins | Short | ~12V | Fusible link | Powers grid heater element - see [Grid Heater][grid-heater] | Active |

**Total Connections:** 6 (all active)

!!! info "Circuit Breaker Locations"
    All circuit breakers mounted in wheel well within 7" of battery positive terminal (ABYC/NEC code compliant). See [Circuit Breakers][circuit-breakers] for complete specifications.

## START battery Negative Terminal

!!! info "Complete Grounding Architecture"
    See [Section 1.5 - Grounding Architecture][grounding] for complete grounding system design, wire gauges, and architecture details.

**START battery Negative Terminal Connections:**

| # | Connection | Wire Gauge | Distance | Routing/Notes | Status |
|:--|:-----------|:-----------|:---------|:--------------|:-------|
| 1 | **Engine Bay Ground Bus (NEGATIVE Bus Bar)** | 2/0 AWG ✓ | ~8 ft | Primary infrastructure hub - feeds all engine bay grounds | Active |
| 2 | **AUX battery Ground Reference** | 1/0 AWG ✓ | 5-6 ft | Critical for BCDC operation - see [Wire Distance][wire-distance] | Active |
| 3 | **ECM Ground** | 12 AWG ✓ | Short | Cummins harness - direct connection prevents starter/alternator spike damage | Active |
| 4 | **Grid Heater Ground** | Per Cummins spec | Short | Cummins harness - direct connection | Active |
| 5 | **G1 GMRS Radio Ground** | 10 AWG ✓ | ~8 ft | Cabin along tub side (factory wiring path) → driver wheel well | Active |
| 6 | **STX Intercom Ground** | 10 AWG ✓ | ~8 ft | Cabin along tub side (factory wiring path) → driver wheel well | Active |
| 7 | **Ham Radio Ground** | 10 AWG ✓ | ~8 ft | Cabin along tub side (factory wiring path) → driver wheel well | Future |

**Total Connections:** 7 (6 active + 1 future)

## Related Documentation

- [Power Generation][power-gen] - Battery and alternator specifications
- [Circuit Breakers][circuit-breakers] - Complete CB specifications (PMU, SafetyHub, BCDC)
- [Grounding Architecture][grounding] - Complete grounding system
- [PMU24][pmu] - Power management unit (radiator fan, Dakota Digital, wipers, lights)
- **REMOVED:** SafetyHub relocated to AUX battery distribution - see [1.3 AUX Battery Distribution][aux-battery]
- [BCDC Alpha 50][bcdc] - DC-DC charger to AUX battery
- [Starter System][starter] - Starter specifications and wiring
- [Alternator][alternator] - Charging system
- [AUX battery Distribution][aux-battery] - Aux/accessory battery system
- [Wire Distance Reference][wire-distance] - Measured routing distances

[pmu]: ../04-pmu/index.md
[bcdc]: ../01-power-generation/03-bcdc.md
[batteries]: ../01-power-generation/01-batteries.md
[grid-heater]: ../../02-engine-systems/08-grid-heater.md
[grounding]: ../05-grounding/index.md
[power-gen]: ../01-power-generation/index.md
[aux-battery]: ../03-aux-battery-distribution/index.md
[starter]: ../../02-engine-systems/01-starter.md
[alternator]: ../01-power-generation/02-alternator.md
[wire-distance]: ../01-power-generation/05-wire-distance-reference.md
[circuit-breakers]: 01-circuit-breakers.md
