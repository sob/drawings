---
hide:
  - toc
---

# 1.5.2 AUX battery Ground {#rear-battery-ground}

## Overview

The AUX battery negative terminal has direct connections to the rear frame rail, battery reference from front, and several high-current accessories requiring direct battery ground.

## AUX battery Negative Terminal Connections

| Connection | Wire Gauge | Distance | Max Current | Voltage Drop | Status |
|:-----------|:-----------|:---------|:------------|:-------------|:-------|
| **Rear Frame Rail Ground** | 2/0 AWG ✓ | ~3 ft | 569A peak | <0.05V | Active |
| **Ground Reference to START battery** | 1/0 AWG ✓ | 5-6 ft | 75A max | <0.02V | Active |
| **BCDC Alpha 50** | 4 AWG ✓ | Short | 50A | Negligible | Active |
| **Fusion Apollo Amp** | Per amp spec | <18" | ~15A | Negligible | Active |
| **Warn VR EVO 10-S Winch** | 1/0 AWG ✓ | 13 ft one-way | 400A peak | 0.54V @ 400A | Active |

**Total Connections:** 5 (all active)

## Direct Connection Rationale

**Rear Frame Rail Ground (2/0 AWG):** Primary ground for AUX battery, must handle winch peak (400A) + CONSTANT bus loads (169A) = 569A peak. 2/0 AWG required for high-current capacity.

**Ground Reference to START battery (1/0 AWG):** Critical for BCDC operation - ensures both batteries maintain same ground reference. Handles BCDC charging current (50A) and provides fault current path (100A max). 1/0 AWG rated 325A provides 3.25x safety margin.

**BCDC Alpha 50 (4 AWG):** Manufacturer specification requires direct connection to battery negative for proper DC-DC charging operation and battery sensing. 4 AWG sized for 50A charging current.

**Fusion Apollo Amp:** Direct battery ground minimizes voltage drop and noise. Manufacturer allows chassis ground only if run is less than 18 inches.

**Warn VR EVO 10-S Winch (1/0 AWG):** Direct connection matches winch positive terminal routing. Provides symmetrical power/ground path for high-current loads (250A typical, 400A peak). 1/0 AWG provides adequate capacity with 13 ft routing distance.

## Related Documentation

- [Grounding Architecture Overview](index.md)
- [START battery Ground](01-starter-battery-ground.md)
- [AUX battery Distribution][rear-battery]

[rear-battery]: ../03-aux-battery-distribution/index.md
