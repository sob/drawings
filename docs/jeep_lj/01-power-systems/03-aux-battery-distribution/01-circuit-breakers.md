---
hide:
  - toc
---

# 1.3.1 Circuit Breakers {#rear-battery-circuit-breakers}

## Overview

All aux battery positive circuits protected by Mechanical Products Series 17 circuit breakers with direct battery connections.

**Location:** Rear wheel well near aux battery

## Circuit Breaker Specifications

| Circuit | Model | Rating | Reset Type | Power Path | Max Load | Sizing |
|:--------|:------|:------:|:-----------|:-----------|:---------|:-------|
| **SwitchPros RCR-Force 12** | Mechanical Products<br/>([174-S2-150-2][mp-150]) | 150A | Manual | Aux Battery+<br/>└→ 150A CB<br/>&nbsp;&nbsp;&nbsp;└→ SwitchPros RCR-Force 12 | ~100A (all lighting outputs on) | 150% of max load |
| **Body RTMR CONSTANT** | Mechanical Products<br/>([174-S2-100-2][mp-100]) | 100A | Manual | Aux Battery+<br/>└→ 100A CB<br/>&nbsp;&nbsp;&nbsp;└→ Body RTMR | ~69A (radio, USB, camera, seats) | 145% of max load |

**All Circuit Breakers:**

- Manufacturer: Mechanical Products Series 17
- Type: Surface mount
- Reset: Manual (Type III - push to reset)
- Terminals: 3/8"-16 studs (S2 configuration)
- Ratings: 48V DC (20-150A), 30V DC (175-200A), 14V DC (225-300A)
- Standards: Marine-rated (SAE J1171, ABYC E-11, UL1500, IP67, MIL-STD-202)
- Mounting: Rear wheel well near battery

## Related Documentation

- [Aux Battery Distribution Overview][rear-battery]
- [SwitchPros][switchpros] - Load details for SwitchPros circuit
- [Body RTMR][body-rtmr] - Load details for Body RTMR circuit

[mp-150]: https://www.waytekwire.com/item/49079/
[mp-100]: https://www.waytekwire.com/item/49077/
[rear-battery]: index.md
[switchpros]: ../../04-control-interfaces/02-switchpros-sp1200.md
[body-rtmr]: 04-body-rtmr.md


