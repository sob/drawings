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

## AUX battery Positive Terminal

### Wheel Well Local

| Circuit | Wire Gauge | Distance | Current | Voltage Drop | Protection |
|:--------|:-----------|:---------|:--------|:-------------|:-----------|
| [BCDC Alpha 50][bcdc] (charging input) | 4 AWG | Short | 50A | Negligible | None |
| [CONSTANT Bus Bar][constant-bus] | 1/0 AWG | ~3 ft | 254A max | 0.9% (13.67V) | None |

### Wheel Well to Front Bumper

| Circuit | Wire Gauge | Distance | Current | Voltage Drop | Protection |
|:--------|:-----------|:---------|:--------|:-------------|:-----------|
| [Winch][recovery] Positive | 1/0 AWG | 13 ft | 250-400A | 4.9-7.9% @ peak | None (see note) |

**Total Positive Connections:** 3 (all active)

!!! note "Winch Circuit Protection - Engineering Justification"
    **Design Decision:** No external circuit breaker per WARN manufacturer specifications

    **Manufacturer Specification:**

    - WARN Part: VR EVO 10-S Winch
    - Installation Manual: [WARN VR EVO Installation Guide][warn-manual]
    - Specification: "No external fuse or circuit breaker required"

    **Protection Strategy:**

    1. **Internal Thermal Protection:** Winch motor has integrated thermal cutoff
    2. **Contactor Disconnect:** Provides isolation when not in use
    3. **Cable Sizing:** 1/0 AWG rated 325A continuous, adequate for 400A brief peaks
    4. **Duty Cycle:** Winch operations are brief (10-30 seconds typical recovery)

    **Automotive Industry Standard:**

    - Factory vehicle winch installations do NOT use external circuit breakers
    - Winch internal protection is designed for automotive fault scenarios
    - This differs from marine practice (ABYC E-11) which requires all circuits fused

    **Fault Scenarios Covered:**

    - **Motor Stall:** Internal thermal protection trips before fire hazard
    - **Cable Short:** 1/0 AWG fuses open at ~800A+ (well above 400A operating current)
    - **Contactor Weld:** Manual disconnect at battery terminal provides emergency shutoff

    **Standards Applied:** SAE J1128 (automotive), WARN manufacturer specifications

    **This is NOT an oversight** - it is intentional adherence to manufacturer specifications and automotive best practices.

    See [Standards Exceptions][standards-exceptions] for complete documentation of intentional design decisions that differ from general marine electrical standards.

## AUX battery Negative Terminal

### Wheel Well Local

| Circuit | Wire Gauge | Distance | Current | Voltage Drop | Notes |
|:--------|:-----------|:---------|:--------|:-------------|:------|
| Rear Frame Rail Ground | 2/0 AWG | ~3 ft | 654A peak | <0.1V | Primary chassis ground |
| [BCDC Alpha 50][bcdc] | 4 AWG | Short | 50A | Negligible | Direct per manufacturer spec |
| [Fusion Apollo Amp][audio] | Per amp spec | <18" | Per spec | Negligible | Direct battery or chassis |

### Wheel Well to Wheel Well (Under Vehicle)

| Circuit | Wire Gauge | Distance | Current | Voltage Drop | Notes |
|:--------|:-----------|:---------|:--------|:-------------|:------|
| [START Battery][starter-battery] Ground Reference | 1/0 AWG | 5-6 ft | 75A max | <0.05V | BCDC + fault path |

### Wheel Well to Front Bumper

| Circuit | Wire Gauge | Distance | Current | Voltage Drop | Notes |
|:--------|:-----------|:---------|:--------|:-------------|:------|
| [Winch][recovery] Negative | 1/0 AWG | 13 ft | 250-400A | 4.9-7.9% @ peak | Matches positive run |

**Total Negative Connections:** 5 (all active)

### Direct Connection Rationale

**Rear Frame Rail Ground (2/0 AWG):** Primary ground for AUX battery, must handle winch peak (400A) + CONSTANT bus loads (~254A) = 654A peak. 2/0 AWG required for high-current capacity.

**Ground Reference to START Battery (1/0 AWG):** Critical for BCDC operation - ensures both batteries maintain same ground reference. Handles BCDC charging current (50A) and provides fault current path. 1/0 AWG rated 325A provides adequate safety margin.

**BCDC Alpha 50 (4 AWG):** Manufacturer specification requires direct connection to battery negative for proper DC-DC charging operation and battery sensing.

**Fusion Apollo Amp:** Direct battery ground minimizes voltage drop and noise. Manufacturer allows chassis ground only if run is less than 18 inches.

**Winch (1/0 AWG):** Direct connection matches winch positive terminal routing. Provides symmetrical power/ground path for high-current loads (250A typical, 400A peak).

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
[audio]: ../../05-audio-systems/index.md
[warn-manual]: https://www.warn.com/
[standards-exceptions]: ../STANDARDS-EXCEPTIONS.md
