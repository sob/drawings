---
hide:
  - toc
tags:
  - product-details
  - power-distribution
  - fuse-block
---

# 1.2.2 SafetyHub 150 {#safetyhub-150}

/// html | div.product-info
![Blue Sea SafetyHub 150](../../images/blue-sea-7748-safetyhub.jpg){ loading=lazy }

**Type:** Fuse Block

**Model:** Blue Sea 7748 SafetyHub 150

**Manufacturer:** Blue Sea Systems

**Product Page:** [SafetyHub 150 Fuse Block][bluesea-7748]

///

## Overview

Provides high-current fused distribution for heavy-load accessories.

**Location:** Engine bay

**Power Source:** START battery via 150A CB - see [Circuit Breakers][circuit-breakers]

## Specifications

- **Rating:** 150A max combined (400A bus rating)
- **Fuse Types:** 3x MIDI (AMI/MIDI), 4x ATC (ATO/ATC)
- **Fuse Range:** MIDI: 30-200A, ATC: 1-20A per circuit
- **Features:** Ignition protected, negative ground bus, ISO 8846, SAE J1171, IP66
- **Full Specs:** [Blue Sea 7748][bluesea-7748]

## Circuit Configuration

| Slot | Fuse | Circuit | Wire Gauge | Distance | Voltage @ Load | Load | Notes |
|:-----|:-----|:--------|:-----------|:---------|:---------------|:-----|:------|
| MIDI-1 | 60A | [ARB Compressor][air-system] Motor 1 | 10 AWG ✓ | ~12 ft | 13.53V (2.0%) | 45A | Engine bay → firewall → under passenger seat |
| MIDI-2 | 60A | [ARB Compressor][air-system] Motor 2 | 10 AWG ✓ | ~12 ft | 13.53V (2.0%) | 45A | Engine bay → firewall → under passenger seat |
| MIDI-3 | - | **[Reserved]** | - | - | - | - | **Reserved for Ham Radio** |
| ATC-1 | - | **[Available]** | - | - | - | - | - |
| ATC-2 | 15A | [G1 GMRS Radio][comms] | 14 AWG ✓ | ~3 ft | 13.71V (0.7%) | 15A | Engine bay → firewall → behind dash |
| ATC-3 | 10A | [STX Intercom][comms] | 16 AWG ✓ | ~3 ft | 13.76V (0.3%) | ~5A | Engine bay → firewall → under dash |
| ATC-4 | - | **[Available]** | - | - | - | - | - |

**Slot Utilization:** 4 of 7 used (2 MIDI + 2 ATC, 3 available - MIDI-3 reserved for Ham Radio)

**Total Load:** ~110A maximum (ARB 90A + GMRS 15A + Intercom 5A)

**Utilization:** 110A / 150A = 73% ✓ Adequate headroom

!!! info "Winch Contactor Trigger"
    Winch contactor trigger moved to PMU OUT15 (15A). See [PMU Outputs][pmu-outputs] and [Recovery Systems][recovery-systems] for winch control details. Winch motor draws 400A peak directly from START battery positive (no CB).

## Related Documentation

**Power Systems:**

- [START battery Distribution Overview][front-battery]
- [Circuit Breakers][circuit-breakers] - 150A CB protection

**Connected Systems:**

- [Air System][air-system] - ARB twin compressor specifications
- [Communication Systems][comms] - GMRS, Ham, Intercom specifications
- [Recovery Systems][recovery-systems] - Winch main power (direct battery connection, no fuse)
- [PMU Outputs][pmu-outputs] - Winch contactor trigger (PMU OUT15)

[bluesea-7748]: https://www.bluesea.com/products/7748/SafetyHub_150_Fuse_Block
[circuit-breakers]: 01-circuit-breakers.md
[air-system]: ../../07-exterior-systems/02-air-system.md
[recovery-systems]: ../../07-exterior-systems/01-recovery-systems.md
[comms]: ../../06-communication-systems/01-communication.md
[front-battery]: index.md
[pmu-outputs]: ../04-pmu/03-pmu-outputs.md
