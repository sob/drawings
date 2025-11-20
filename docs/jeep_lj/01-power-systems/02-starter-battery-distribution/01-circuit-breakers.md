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
| **PMU24** | Mechanical Products<br/>([174-S2-300-2][mp-300]) | 300A | Manual | START battery+<br/>└→ 300A CB<br/>&nbsp;&nbsp;&nbsp;└→ PMU24 | ~220A theoretical (100-140A typical) | 136% of max load (handles motor inrush) |
| **SafetyHub 150** | Mechanical Products<br/>([174-S2-150-2][mp-150]) | 150A | Manual | START battery+<br/>└→ 150A CB<br/>&nbsp;&nbsp;&nbsp;└→ SafetyHub 150 | ~111A (ARB 90A + GMRS 15A + Intercom 5A) | 135% of max load |
| **BCDC Input** | Mechanical Products<br/>([174-S2-040-2][mp-40]) | 40A | Manual | START battery+<br/>└→ 40A CB<br/>&nbsp;&nbsp;&nbsp;└→ BCDC Alpha 25 | 27-29A BCDC input | 138-148% of max load |

**Total Circuit Breakers:** 3 (PMU 300A, SafetyHub 150A, BCDC 40A)

**Eliminated:** Radiator Fan 100A CB (now PMU controlled), Critical Cabin PDU 40A CB (Dakota Digital now PMU controlled)

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
- [SafetyHub 150][safetyhub] - Load details for SafetyHub circuit
- [PMU Outputs][pmu-outputs] - Load details for PMU circuit (radiator fan, Dakota Digital, etc.)
- [BCDC Alpha 25][bcdc] - DC-DC charger specifications

[mp-300]: https://www.waytekwire.com/item/49083/
[mp-150]: https://www.waytekwire.com/item/49079/
[mp-40]: https://www.waytekwire.com/item/48981/
[front-battery]: index.md
[safetyhub]: 04-safetyhub.md
[pmu-outputs]: ../04-pmu/03-pmu-outputs.md
[bcdc]: ../01-power-generation/03-bcdc.md
