---
hide:
  - toc
---

# 1.2.1 Circuit Breakers {#front-battery-circuit-breakers}

## Overview

All START battery positive circuits protected by Mechanical Products Series 17 circuit breakers with direct battery connections.

**Location:** Wheel well, within 7" of START battery positive terminal (ABYC/NEC code compliant)

## Circuit Breaker Specifications

| Circuit | Model | Rating | Reset Type | Power Path | Max Load | Sizing |
|:--------|:------|:------:|:-----------|:-----------|:---------|:-------|
| **PMU24** | Mechanical Products<br/>([174-S2-250-2][mp-250]) | 250A | Manual | START battery+<br/>└→ 250A CB<br/>&nbsp;&nbsp;&nbsp;└→ PMU24 | ~253A theoretical peak (140-170A typical) | 99% of max load (with all radios transmitting + full radiator fan) |
| **BCDC Input** | Mechanical Products<br/>([174-S2-080-2][mp-80]) | 80A | Manual | START battery+<br/>└→ 80A CB<br/>&nbsp;&nbsp;&nbsp;└→ BCDC Alpha 50 | 50-55A BCDC input | 145-160% of max load |

**Total Circuit Breakers:** 2 (PMU 250A, BCDC 80A)

**All Circuit Breakers:**

- Manufacturer: Mechanical Products Series 17
- Type: Surface mount
- Reset: Manual (Type III - push to reset)
- Terminals: 3/8"-16 studs (S2 configuration)
- Ratings: 48V DC (20-150A), 30V DC (175-200A), 14V DC (225-300A)
- Standards: Marine-rated (SAE J1171, ABYC E-11, UL1500, IP67, MIL-STD-202)
- Mounting: Wheel well within 7" of battery positive terminal

## Related Documentation

- [START battery Distribution Overview][front-battery]
- [PMU Outputs][pmu-outputs] - Load details for PMU circuit (radiator fan, Dakota Digital, communication systems, etc.)
- [BCDC Alpha 50][bcdc] - DC-DC charger specifications
- [Communication Systems][comms] - Radio and intercom specifications (now PMU powered)

[mp-250]: https://www.waytekwire.com/item/49082/
[mp-80]: https://www.waytekwire.com/item/49015/
[front-battery]: index.md
[pmu-outputs]: ../04-pmu/03-pmu-outputs.md
[bcdc]: ../01-power-generation/03-bcdc.md
[comms]: ../../06-communication-systems/01-communication.md
