---
hide:
  - toc
---

# 1.3.1 Circuit Breakers {#rear-battery-circuit-breakers}

## Overview

All CONSTANT bus loads protected by Mechanical Products Series 17 circuit breakers.

**Location:** Rear wheel well near CONSTANT bus bar

## Circuit Breaker Specifications

| Circuit                      | Model                                             | Rating | Reset Type | Power Path                                                                   | Max Load                                                  | Sizing                                   |
| :--------------------------- | :------------------------------------------------ | :----: | :--------- | :--------------------------------------------------------------------------- | :-------------------------------------------------------- | :--------------------------------------- |
| **SwitchPros RCR-Force 12**  | Mechanical Products<br/>([174-S2-150-2][mp-150])  |  150A  | Manual     | CONSTANT bus<br/>└→ 150A CB<br/>&nbsp;&nbsp;&nbsp;└→ SwitchPros RCR-Force 12 | ~100A (all lighting outputs on)                           | 150% of max load                         |
| **SafetyHub 150 (Recovery)** | Mechanical Products<br/>([174-S2-150-2][mp-150b]) |  150A  | Manual     | CONSTANT bus<br/>└→ 150A CB<br/>&nbsp;&nbsp;&nbsp;└→ SafetyHub 150           | ~100A (ARB 90A + Winch Trigger 10A)                       | Future-proofed to SafetyHub max capacity |
| **BODY PDU**                 | Mechanical Products<br/>([174-S2-100-2][mp-100])  |  100A  | Manual     | CONSTANT bus<br/>└→ 100A CB<br/>&nbsp;&nbsp;&nbsp;└→ BODY PDU                | ~54A max (radio 16A, USB 13A, camera 10A, seats 10A peak) | 185% of max load (future expansion)      |

!!! info "Wire Sizing for CB Protection"
All CONSTANT bus outputs use 2 AWG (130A @ 20°C) for consistency and future expansion capacity.

**All Circuit Breakers:**

- Manufacturer: Mechanical Products Series 17
- Type: Surface mount
- Reset: Manual (Type III - push to reset)
- Terminals: 3/8"-16 studs (S2 configuration)
- Ratings: 48V DC (20-150A), 30V DC (175-200A), 14V DC (225-300A)
- Standards: Marine-rated (SAE J1171, ABYC E-11, UL1500, IP67, MIL-STD-202)
- Mounting: Rear wheel well near battery

## Related Documentation

- [AUX battery Distribution Overview][rear-battery]
- [SwitchPros][switchpros] - Load details for SwitchPros circuit
- [SafetyHub 150][safetyhub] - Load details for SafetyHub circuit (ARB compressor, winch trigger)
- [BODY PDU][body-rtmr] - Load details for BODY PDU circuit

[mp-150]: https://www.waytekwire.com/item/49079/
[mp-150b]: https://www.waytekwire.com/item/49079/
[mp-100]: https://www.waytekwire.com/item/49077/
[rear-battery]: index.md
[switchpros]: ../../05-control-interfaces/02-switchpros-sp1200.md
[safetyhub]: 04-safetyhub.md
[body-rtmr]: 03-body-pdu.md
