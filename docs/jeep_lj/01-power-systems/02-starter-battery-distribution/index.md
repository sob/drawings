---
hide:
  - toc
---

# 1.2 Starter Battery Distribution (Driver Wheel Well) {#starter-battery-distribution}

/// html | div.product-info
![Odyssey PC1500 Battery Terminals](../../images/odyssey-pc1500.jpg){ loading=lazy }
///

## Overview

The starter battery (driver wheel well) provides power for critical engine and safety systems:

1. **Direct high-current** → Starter, alternator, PMU (critical systems)
2. **Direct low-current** → ECM, grid heater (no circuit breaker - fusible link)

See [CONSTANT Bus Bar][constant-bus] for complete bus bar specifications and [Circuit Breakers][circuit-breakers] for CB details.

!!! info "Battery Specifications"
    For complete battery specifications (capacity, dimensions, terminals, etc.), see [Section 1.1 - Battery System][batteries].

!!! note "Battery Location"
    Starter battery located in **driver side rear wheel well** for optimal wire routing to critical engine systems. See [Wire Distance Reference][wire-distance] for measured routing distances.

## Starter Battery Positive Terminal

**Starter Battery Positive Terminal Connections:**

| # | Connection | Wire Gauge | Distance | Voltage @ Load | Protection | Destination/Notes | Status |
|:--|:-----------|:-----------|:---------|:---------------|:-----------|:------------------|:-------|
| | **━━━ CHARGING INPUT ━━━** | | | | | | |
| 1 | Alternator | 2/0 AWG ✓ | 8 ft | 13.996V (2.81% @ 60°C) | None | 270A alternator output charges starter battery - see [Alternator][alternator] | Active |
| | **━━━ CRITICAL SYSTEMS ━━━** | | | | | | |
| 2 | Cummins R2.8 Starter | 2/0 AWG ✓ | 6 ft | 11.53V (3.9%) | None | 400-600A cranking current - see [Starter][starter] | Active |
| | **━━━ CONSTANT BUS BAR ━━━** | | | | | | |
| 3 | CONSTANT Bus Bar | 2×1/0 AWG ✓ | ~5 ft | 13.82V (1.26% @ 60°C) | None | Feeds PMU, SafetyHub, BCDC (~356A max) - see [CONSTANT Bus][constant-bus] | Active |
| | **━━━ DIRECT CONNECTIONS ━━━** | | | | | | |
| 4 | Cummins ECM | Per Cummins | Short | ~12V | Fusible link | Engine control module | Active |
| 5 | Grid Heater Relay | Per Cummins | Short | ~12V | Fusible link | Powers grid heater element - see [Grid Heater][grid-heater] | Active |

**Total Connections:** 5 (all active)

## Starter Battery Negative Terminal

!!! info "Complete Grounding Architecture"
    See [Section 1.5 - Grounding Architecture][grounding] for complete grounding system design, wire gauges, and architecture details.

**Starter Battery Negative Terminal Connections:**

| # | Connection | Wire Gauge | Distance | Routing/Notes | Status |
|:--|:-----------|:-----------|:---------|:--------------|:-------|
| 1 | **Engine Bay Ground Bus (NEGATIVE Bus Bar)** | 2/0 AWG ✓ | ~8 ft | Primary infrastructure hub - feeds all engine bay grounds | Active |
| 2 | **Aux Battery Ground Reference** | 1/0 AWG ✓ | 5-6 ft | Critical for BCDC operation - see [Wire Distance][wire-distance] | Active |
| 3 | **ECM Ground** | 12 AWG ✓ | Short | Cummins harness - direct connection prevents starter/alternator spike damage | Active |
| 4 | **Grid Heater Ground** | Per Cummins spec | Short | Cummins harness - direct connection | Active |
| 5 | **G1 GMRS Radio** | 14 AWG ✓ | Via firewall | Direct connection minimizes RF noise | Active |
| 6 | **STX Intercom** | 14 AWG ✓ | Via firewall | Direct connection minimizes RF noise | Active |
| 7 | **Ham Radio** | 10 AWG ✓ | Via firewall | Direct connection minimizes RF noise | Future |

**Total Connections:** 7 (6 active + 1 future)

## Related Documentation

- [Power Generation][power-gen] - Battery and alternator specifications
- [Grounding Architecture][grounding] - Complete grounding system
- [PMU24][pmu] - Power management unit (critical systems)
- [Starter System][starter] - Starter specifications and wiring
- [Alternator][alternator] - Charging system
- [Aux Battery Distribution][aux-battery] - Aux/accessory battery system
- [Wire Distance Reference][wire-distance] - Measured routing distances

[pmu]: ../04-pmu/index.md
[batteries]: ../01-power-generation/01-batteries.md
[grid-heater]: ../../02-engine-systems/08-grid-heater.md
[grounding]: ../05-grounding/index.md
[power-gen]: ../01-power-generation/index.md
[aux-battery]: ../03-aux-battery-distribution/index.md
[starter]: ../../02-engine-systems/01-starter.md
[alternator]: ../01-power-generation/02-alternator.md
[wire-distance]: ../01-power-generation/05-wire-distance-reference.md
[constant-bus]: 02-constant-bus.md
[circuit-breakers]: 01-circuit-breakers.md
