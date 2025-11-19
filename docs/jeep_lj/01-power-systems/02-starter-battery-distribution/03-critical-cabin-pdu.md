---
hide:
  - toc
tags:
  - product-details
  - power-distribution
  - fuse-block
---

# 1.2.3 Critical Cabin PDU {#critical-cabin-pdu}

/// html | div.product-info
![Blue Sea 5025 ST Blade Fuse Block](../../images/blue-sea-5025-fuse-block.jpg){ loading=lazy }

**Type:** Fuse Block with Negative Bus

**Model:** Blue Sea 5025

**Manufacturer:** Blue Sea Systems

**Product Page:** [ST Blade Fuse Block - 6 Circuits][product-link]

///

## Overview

Provides fused distribution for critical cabin electronics and Dakota Digital instrumentation modules.

**Location:** Cabin side firewall (near Dakota Digital HDPE panel)

**Power Source:** START battery CONSTANT bus via 40A CB - see [Circuit Breakers][circuit-breakers]

## Specifications

- **Rating:** 100A max combined, 30A per circuit
- **Fuse Types:** 6× ATO/ATC (1-30A per circuit)
- **Negative Bus:** Integrated ground bus
- **Positive Feed:** #10-32 stud (4-6 AWG recommended)
- **Branch Circuits:** #8-32 screws (10-16 AWG)
- **Dimensions:** 3.32" W × 4.9" H × 1.52" D
- **Features:** Cover with spare fuse storage, write-on circuit labels
- **Full Specs:** [Blue Sea 5025][product-link]

## Circuit Configuration

| Slot | Fuse | Circuit | Wire Gauge | Load | Notes |
|:-----|:-----|:--------|:-----------|:-----|:------|
| 1 | 5A | [PAC-2800BT Fan Controller][fan-controller] | 16 AWG ✓ | <1A | Dakota Digital fan controller |
| 2 | TBD | Dakota Digital Gauge Module | TBD | TBD | Gauge cluster control box |
| 3 | - | **[Available]** | - | - | - |
| 4 | - | **[Available]** | - | - | - |
| 5 | - | **[Available]** | - | - | - |
| 6 | - | **[Available]** | - | - | - |

**Slot Utilization:** 2 of 6 used (4 available)

**Total Load:** TBD (currently <10A)

## Wiring

| Connection | Wire Gauge | Source | Destination | Distance | Voltage @ Load | Notes |
|:-----------|:-----------|:-------|:------------|:---------|:---------------|:------|
| **Positive Feed (+)** | 6 AWG ✓ | CONSTANT bus via 40A CB | PDU input stud | ~8 ft | TBD | Through firewall from engine bay |
| **Negative Bus (-)** | 6 AWG ✓ | PDU ground bus | Firewall stud bus | <1 ft | - | Cabin ground bus |

## Outstanding Items

- [ ] Source product image for Blue Sea 5025
- [ ] Determine total Dakota Digital module current draw
- [ ] Assign remaining fuse slots for gauge modules
- [ ] Confirm 40A circuit breaker sizing based on total load
- [ ] Determine exact mounting location on firewall
- [ ] Test voltage at PDU under load

## Related Documentation

**Power Systems:**

- [START battery Distribution Overview][front-battery]
- [Circuit Breakers][circuit-breakers] - 40A CB protection
- [CONSTANT Bus][constant-bus] - Power source
- [Grounding Architecture][grounding] - Firewall stud bus

**Connected Systems:**

- [PAC-2800BT Fan Controller][fan-controller] - Fan controller specifications
- [Dakota Digital Gauge Cluster][gauge-cluster] - Gauge module specifications

[product-link]: https://www.bluesea.com/products/5025/ST_Blade_Fuse_Block_-_6_Circuits_with_Negative_Bus_and_Cover
[circuit-breakers]: 01-circuit-breakers.md
[constant-bus]: 02-constant-bus.md
[front-battery]: index.md
[grounding]: ../05-grounding/index.md
[fan-controller]: ../../02-engine-systems/06-radiator-fan/02-fan-controller.md
[gauge-cluster]: ../../04-control-interfaces/04-gauge-cluster.md
