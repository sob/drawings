---
hide:
  - toc
tags:
  - product-details
  - power-distribution
  - grounding
  - bus-bar
---

# 1.5.3 Engine Bay Ground Bus {#engine-bay-ground-bus}

/// html | div.product-info
![Blue Sea 2107 PowerBar](../../images/blue-sea-2107-powerbar.jpg){ loading=lazy }

**Type:** High-Current Ground Distribution Bus Bar

**Model:** Blue Sea 2107 PowerBar - 600A BusBar

**Manufacturer:** Blue Sea Systems

**Product Page:** [Blue Sea 2107 PowerBar][bluesea-2107]

**Installation Manual:** [Blue Sea BusBar Installation Guide][bluesea-busbar-guide]

///

## Specifications

- **Capacity:** 600A continuous
- **Terminals:** 8x 3/8"-16 studs
- **Location:** Firewall (engine bay side), near PMU
- **Full Specs:** [Blue Sea 2107][bluesea-2107]

## Stud Assignment

| Stud | Connection | Wire Gauge | Distance | Max Current | Notes |
|:-----|:-----------|:-----------|:---------|:------------|:------|
| 1 | START battery- | 2/0 AWG ✓ | ~8 ft | 600A+ peak | Primary power return - starter + alternator |
| 2 | Engine block ground | 2/0 AWG ✓ | ~8 ft | 600A+ peak | Starter/alternator return path |
| 3 | Front frame rail (main chassis) | 2/0 AWG ✓ | ~3 ft | 600A+ peak | Primary infrastructure ground |
| 4 | AUX battery reference | 1/0 AWG ✓ | 5-6 ft | 75A max | Inter-battery reference (BCDC + fault current) |
| 5 | PMU ground reference | Per harness | ~2 ft | <1A | Logic/CAN reference (Pin 25) - loads ground separately |
| 6 | Relay/solenoid coil grounds | 14-18 AWG ✓ | Variable | ~3A total | Starter solenoid (~1.6A), horn relay |
| 7-8 | **[Available]** | - | - | - | Future expansion (2 studs available) |

**Utilization:** 6 of 8 studs used (2 available)

**Direct Battery Connections:** ECM, grid heater, radios, winch, and BCDC connect directly to battery negative - see [START battery Ground][front-battery-ground] and [AUX battery Ground][rear-battery-ground]

## Installation

**Mounting:** Firewall (engine bay side) near PMU

**Torque:** 100-120 in-lb (3/8"-16 studs)

**Critical:** Clean metal-to-metal connections - remove paint/rust before installation, apply dielectric grease after assembly

## Related Documentation

- [Grounding Architecture Overview][grounding-architecture]
- [START battery Ground][front-battery-ground]
- [AUX battery Ground][rear-battery-ground]
- [START battery Distribution][starter-battery-distribution]

[grounding-architecture]: index.md
[front-battery-ground]: 01-starter-battery-ground.md
[rear-battery-ground]: 02-aux-battery-ground.md
[starter-battery-distribution]: ../02-starter-battery-distribution/index.md
[bluesea-2107]: https://www.bluesea.com/products/2107/PowerBar_-_600A_BusBar_-_Eight_3_8in-16_Studs
[bluesea-busbar-guide]: https://www.bluesea.com/resources/108
