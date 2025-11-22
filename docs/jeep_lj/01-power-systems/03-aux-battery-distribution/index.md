---
hide:
  - toc
---

# 1.3 AUX battery Distribution (Passenger Wheel Well) {#aux-battery-distribution}

/// html | div.product-info
![Odyssey PC1500 Battery Terminals](../../images/odyssey-pc1500.jpg){ loading=lazy }
///

## Overview

The AUX battery (passenger wheel well) provides power for high-current accessories and cabin systems:

1. **Direct high-current** → Winch (recovery system, no CB per manufacturer spec)
2. **CONSTANT Bus Bar** (Blue Sea 2104 PowerBar, 225A) - Feeds SwitchPros, SafetyHub 150, BODY PDU
3. **Direct charging input** → BCDC Alpha 50 output

See [CONSTANT Bus Bar][constant-bus] for complete bus bar specifications, [SafetyHub][aux-safetyhub] for fused distribution, and [Circuit Breakers][circuit-breakers] for CB details.

!!! info "Single Source of Truth"
    This page is the authoritative source for all AUX battery wire specs (gauge, distance, voltage drop). Component pages reference here. For battery specs see [Section 1.1][batteries]. For ground bus bars see [Section 1.5][grounding].

## AUX battery Positive Terminal (3 connections)

| Circuit | Destination | Wire Gauge | Distance | Current | Voltage Drop | Protection |
|:--------|:------------|:-----------|:---------|:--------|:-------------|:-----------|
| [BCDC Alpha 50][bcdc] | Local | 4 AWG | Short | 50A | Negligible | None |
| [CONSTANT Bus Bar][constant-bus] | Local | 1/0 AWG | ~3 ft | 254A max | 0.9% @ 20°C | None |
| [Winch][recovery] | Front bumper | 1/0 AWG | 13 ft | 250-400A | 4.9-7.9% @ 20°C | [None][winch-protection] |

## AUX battery Negative Terminal (5 connections)

| Circuit | Destination | Wire Gauge | Distance | Current | Voltage Drop |
|:--------|:------------|:-----------|:---------|:--------|:-------------|
| Rear Frame Rail | Local (chassis) | 2/0 AWG | ~3 ft | 654A peak | <0.1V @ 20°C |
| [BCDC Alpha 50][bcdc] | Local | 4 AWG | Short | 50A | Negligible |
| [Fusion Apollo Amp][audio] | Local | Per spec | <18" | Per spec | Negligible |
| [START Battery][starter-battery] | Driver wheel well | 1/0 AWG | 5-6 ft | 75A max | <0.05V @ 20°C |
| [Winch][recovery] | Front bumper | 1/0 AWG | 13 ft | 250-400A | 4.9-7.9% @ 20°C |

## Related Documentation

- [CONSTANT Bus Bar][constant-bus] - Stud assignments and loads
- [SafetyHub 150][aux-safetyhub] - ARB compressor, winch trigger
- [BODY PDU][body-rtmr] - Cabin convenience circuits
- [Circuit Breakers][circuit-breakers] - CB specifications
- [Grounding Architecture][grounding] - Ground bus bars
- [START battery Distribution][starter-battery] - BCDC input source
- [Recovery Systems][recovery] - Winch specifications

[aux-safetyhub]: 04-safetyhub.md
[constant-bus]: 02-constant-bus.md
[body-rtmr]: 03-body-pdu.md
[batteries]: ../01-power-generation/01-batteries.md
[bcdc]: ../01-power-generation/03-bcdc.md
[circuit-breakers]: 01-circuit-breakers.md
[grounding]: ../05-grounding/index.md
[starter-battery]: ../02-starter-battery-distribution/index.md
[recovery]: ../../07-exterior-systems/01-recovery-systems.md
[winch-protection]: ../../07-exterior-systems/01-recovery-systems.md#winch-circuit-protection
[audio]: ../../05-audio-systems/index.md
