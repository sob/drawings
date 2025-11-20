---
hide:
  - toc
---

# 1.2.1 Circuit Breakers {#front-battery-circuit-breakers}

## Overview

All START battery positive circuits protected by Mechanical Products Series 17 circuit breakers with direct battery connections.

**Location:** Engine bay near START battery

## Circuit Breaker Specifications

| Circuit | Model | Rating | Reset Type | Power Path | Max Load | Sizing |
|:--------|:------|:------:|:-----------|:-----------|:---------|:-------|
| **PMU24** | Mechanical Products<br/>([174-S2-300-2][mp-300]) | 300A | Manual | START battery+<br/>└→ 300A CB<br/>&nbsp;&nbsp;&nbsp;└→ PMU24 | ~220A theoretical (100-140A typical) | 136% of max load (handles motor inrush) |
| **SafetyHub 150** | Mechanical Products<br/>([174-S2-150-2][mp-150]) | 150A | Manual | START battery+<br/>└→ 150A CB<br/>&nbsp;&nbsp;&nbsp;└→ SafetyHub 150 | ~111A (ARB 90A + GMRS 15A + Intercom 5A + winch 1A) | 135% of max load |
| **Radiator Fan Relay** | Mechanical Products<br/>([174-S2-100-2][mp-100]) | 100A | Manual | START battery+<br/>└→ 100A CB<br/>&nbsp;&nbsp;&nbsp;└→ Radiator Fan Relay | 53A (GM Camaro fan motor) | 189% of max load |
| **BCDC Input** | Mechanical Products<br/>([174-S2-040-2][mp-40]) | 40A | Manual | START battery+<br/>└→ 40A CB<br/>&nbsp;&nbsp;&nbsp;└→ BCDC Alpha 25 | 25A BCDC output | 160% of max load |
| **Critical Cabin PDU** | Mechanical Products<br/>([174-S2-040-2][mp-40]) | 40A | Manual | START battery+<br/>└→ 40A CB<br/>&nbsp;&nbsp;&nbsp;└→ Critical Cabin PDU | <10A (Dakota Digital modules) | 400% of max load |

**All Circuit Breakers:**

- Manufacturer: Mechanical Products Series 17
- Type: Surface mount
- Reset: Manual (Type III - push to reset)
- Terminals: 3/8"-16 studs (S2 configuration)
- Ratings: 48V DC (20-150A), 30V DC (175-200A), 14V DC (225-300A)
- Standards: Marine-rated (SAE J1171, ABYC E-11, UL1500, IP67, MIL-STD-202)
- Mounting: Engine bay near battery

## Related Documentation

- [START battery Distribution Overview][front-battery]
- [SafetyHub 150][safetyhub] - Load details for SafetyHub circuit
- [PMU Outputs][pmu-outputs] - Load details for PMU circuit
- [Critical Cabin PDU][cabin-pdu] - Load details for Critical Cabin PDU circuit
- [Radiator Fan System][radiator-fan] - Load details for radiator fan circuit

[mp-300]: https://www.waytekwire.com/item/49083/
[mp-150]: https://www.waytekwire.com/item/49079/
[mp-100]: https://www.waytekwire.com/item/49077/
[mp-40]: https://www.waytekwire.com/item/48981/
[front-battery]: index.md
[safetyhub]: 04-safetyhub.md
[pmu-outputs]: ../04-pmu/03-pmu-outputs.md
[cabin-pdu]: 03-critical-cabin-pdu.md
[radiator-fan]: ../../02-engine-systems/06-radiator-fan/index.md
