---
hide:
  - toc
---

# 1.5.1 Starter Battery Ground {#front-battery-ground}

## Overview

The starter battery negative terminal has direct connections to the negative bus bar and several components requiring direct battery ground (ECM, grid heater, radios).

## Starter Battery Negative Terminal Connections

| Connection | Wire Gauge | Distance | Max Current | Voltage Drop | Status |
|:-----------|:-----------|:---------|:------------|:-------------|:-------|
| **Engine Bay Ground Bus (NEGATIVE Bus Bar)** | 2/0 AWG ✓ | ~8 ft | 600A+ peak | <0.1V | Active |
| **ECM Ground** | 12 AWG ✓ | Short | <5A | Negligible | Active |
| **Grid Heater Ground** | Per Cummins spec | Short | Variable | Negligible | Active |
| **G1 GMRS Radio** | 14 AWG ✓ | Via Grommet 6 | 15A | <0.1V | Active |
| **STX Intercom** | 14 AWG ✓ | Via Grommet 6 | 5A | <0.1V | Active |
| **Ham Radio** | 10 AWG ✓ | Via Grommet 6 | 15A | <0.1V | Future |

**Total Connections:** 6 (5 active + 1 future)

## Infrastructure Grounds (via Negative Bus Bar)

See [Engine Bay Ground Bus](03-engine-bay-ground-bus.md) for complete bus bar configuration.

**Primary Infrastructure:**
- Front frame rail ground (2/0 AWG) - handles starter + 270A alternator return
- Engine block ground (2/0 AWG) - starter/alternator return path
- Aux battery reference (2/0 AWG) - critical for BCDC operation

## Direct Connection Rationale

**ECM & Grid Heater:** Direct to battery via Cummins harness prevents voltage spikes from starter/alternator from damaging sensitive ECM electronics.

**Radios (G1 GMRS, STX, Ham):** Direct to battery negative minimizes ground loop noise and RF interference. Critical for radio performance.

## Related Documentation

- [Grounding Architecture Overview](index.md)
- [Engine Bay Ground Bus](03-engine-bay-ground-bus.md)
- [Starter Battery Distribution][front-battery]

[front-battery]: ../02-starter-battery-distribution/index.md
