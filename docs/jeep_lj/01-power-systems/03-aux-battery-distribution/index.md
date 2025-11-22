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

!!! info "Battery Specifications"
    For complete battery specifications (capacity, dimensions, terminals, etc.), see [Section 1.1 - Battery System][batteries].

!!! note "Battery Location"
    AUX battery located in **passenger side rear wheel well** for optimal wire routing to winch and accessory systems. See [Wire Distance Reference][wire-distance] for measured routing distances.

## AUX battery Positive Terminal

**AUX battery Positive Terminal Connections:**

| # | Connection | Wire Gauge | Distance | Voltage @ Load | Protection | Destination/Notes | Status |
|:--|:-----------|:-----------|:---------|:---------------|:-----------|:------------------|:-------|
| | **━━━ CHARGING INPUT ━━━** | | | | | | |
| 1 | BCDC Alpha 50 Output | 4 AWG ✓ | 5-6 ft | 13.89V (0.94%) | None | 50A DC-DC charging from START battery - see [BCDC Alpha 50][bcdc] | Active |
| | **━━━ RECOVERY SYSTEMS ━━━** | | | | | | |
| 2 | Warn VR EVO 10-S Winch | 1/0 AWG ✓ | 13 ft one-way | 13.12V (4.9%) @ 250A<br>12.71V (7.9%) @ 400A | None (see note) | 250A typical, 400A peak (brief) - see [Recovery Systems][recovery] | Active |
| | **━━━ CONSTANT BUS BAR ━━━** | | | | | | |
| 3 | CONSTANT Bus Bar | 1/0 AWG ✓ | ~3 ft | 13.67V (0.9%) | None | Feeds SwitchPros, SafetyHub, BODY PDU (~254A max) | Active |

**Total Connections:** 3 (all active)

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

## CONSTANT Bus Bar

**Type:** Blue Sea 2104 PowerBar (225A BusBar)

**Location:** Passenger wheel well compartment (near battery)

**Capacity:** 225A continuous, 4× 3/8"-16 studs

**Power Source:** Direct from AUX battery positive via 1/0 AWG (~3 ft run)

**CONSTANT Bus Bar Connections:**

| Stud | Connection | Wire Gauge | Protection | Load | Notes |
|:-----|:-----------|:-----------|:-----------|:-----|:------|
| 1 | SwitchPros RCR-Force 12 | 4 AWG | 150A CB | ~100A max | Auxiliary lighting - see [SwitchPros][switchpros] |
| 2 | SafetyHub 150 | 4 AWG | 150A CB | ~100A max | ARB compressor, winch trigger - see [SafetyHub][aux-safetyhub] |
| 3 | BODY PDU | 6 AWG | 100A CB | ~54A max | Cabin circuits - see [BODY PDU][body-rtmr] |
| 4 | **[Available]** | - | - | - | Future expansion (1 stud available) |

**Utilization:** 3 of 4 studs used (1 available)

**Total Load:** ~254A max (SwitchPros 100A + SafetyHub 100A + BODY PDU 54A)

**Wire Sizing:** 1/0 AWG feed rated 325A continuous - 0.9% voltage drop @ 254A max load (13.67V at bus)

**Note:** No circuit breaker between battery and CONSTANT bus - each load has individual CB protection at appropriate rating.

## AUX battery Negative Terminal

!!! info "Complete Grounding Architecture"
    See [Section 1.5 - Grounding Architecture][grounding] for complete grounding system design, wire gauges, and architecture details.

**AUX battery Negative Terminal Connections:**

| # | Connection | Wire Gauge | Distance | Routing/Notes | Status |
|:--|:-----------|:-----------|:---------|:--------------|:-------|
| 1 | **Rear Frame Rail Ground** | 2/0 AWG ✓ | ~3 ft | Primary ground for AUX battery and CONSTANT bus | Active |
| 2 | **START battery Ground Reference** | 1/0 AWG ✓ | 5-6 ft | Critical for BCDC operation and fault current path | Active |
| 3 | **BCDC Alpha 50** | 4 AWG ✓ | Short | Direct connection per manufacturer spec | Active |
| 4 | **Fusion Apollo Amp** | Per amp spec | <18" | Chassis ground OK if <18" run, direct connection preferred | Active |
| 5 | **Warn VR EVO 10-S Winch** | 1/0 AWG ✓ | 13 ft one-way | Winch negative return - see [Recovery Systems][recovery] | Active |

**Total Connections:** 5 (all active)

## System Components

- [SafetyHub 150][aux-safetyhub] - Blue Sea 7748 fused distribution (ARB compressor, winch trigger)
- [CONSTANT Bus Bar][constant-bus] - Blue Sea 2104 PowerBar (225A, 4 studs)
- [Circuit Breakers][circuit-breakers] - Protection for all AUX battery circuits
- [BODY PDU][body-rtmr] - Body relay/fuse panel for cabin convenience circuits

## Related Documentation

- [Power Generation][power-gen] - Battery and BCDC specifications
- [Grounding Architecture][grounding] - Complete grounding system
- [Circuit Breakers][circuit-breakers] - Protection for all CB-protected circuits
- [START battery Distribution][starter-battery] - START battery system (BCDC input source)
- [SwitchPros][switchpros] - Auxiliary lighting controller
- [BODY PDU][body-rtmr] - Cabin convenience circuits
- [Recovery Systems][recovery] - Winch specifications and wiring
- [Wire Distance Reference][wire-distance] - Measured routing distances

[aux-safetyhub]: 04-safetyhub.md
[constant-bus]: 02-constant-bus.md
[switchpros]: ../../04-control-interfaces/02-switchpros-sp1200.md
[body-rtmr]: 03-body-pdu.md
[power-gen]: ../01-power-generation/index.md
[batteries]: ../01-power-generation/01-batteries.md
[bcdc]: ../01-power-generation/03-bcdc.md
[circuit-breakers]: 01-circuit-breakers.md
[grounding]: ../05-grounding/index.md
[starter-battery]: ../02-starter-battery-distribution/index.md
[recovery]: ../../07-exterior-systems/01-recovery-systems.md
[wire-distance]: ../01-power-generation/05-wire-distance-reference.md
[warn-manual]: https://www.warn.com/
[standards-exceptions]: ../STANDARDS-EXCEPTIONS.md
