---
hide:
  - toc
tags:
  - product-details
  - exterior-systems
  - winch
  - recovery
---

# 8.1 Winch {#winch}

/// html | div.product-info

**Model:** Warn Zeon 10-S

**Mounting Location:** Front bumper (verified compatible)

**Pulling Capacity:** 10,000 lbs (4,536 kg)

**Motor:** 12V DC series wound

///

## Electrical Specifications

- **Peak Amperage Draw:** 450A (at full load/stall - brief periods only)
- **Typical Operating Draw:** 80-250A (most recovery operations)
- **Main Power Source:** AUX battery (passenger wheel well - direct connection, no fuse/breaker)
  - See [AUX Battery Distribution][aux-battery] for wire specs (gauge, length, routing, voltage drop calculations)
  - **System Voltage:** 13.8V (alternator charging - engine running during winch operations)
  - **Protection:** None - direct connection (see justification below)

## Circuit Protection - Engineering Justification {#winch-circuit-protection}

**Design Decision:** No external circuit breaker per WARN manufacturer specifications

**Manufacturer Specification:**

- WARN Part: VR EVO 10-S Winch
- Installation Manual: [WARN VR EVO Installation Guide][warn-manual]
- Specification: "No external fuse or circuit breaker required"

**Protection Strategy:**

1. **Internal Thermal Protection:** Winch motor has integrated thermal cutoff
2. **Contactor Disconnect:** Provides isolation when not in use
3. **Cable Sizing:** 1/0 AWG rated 325A continuous, adequate for 450A brief peaks
4. **Duty Cycle:** Winch operations are brief (10-30 seconds typical recovery)

**Automotive Industry Standard:**

- Factory vehicle winch installations do NOT use external circuit breakers
- Winch internal protection is designed for automotive fault scenarios
- This differs from marine practice (ABYC E-11) which requires all circuits fused

**Fault Scenarios Covered:**

- **Motor Stall:** Internal thermal protection trips before fire hazard
- **Cable Short:** 1/0 AWG fuses open at ~800A+ (well above 450A peak current)
- **Contactor Weld:** Manual disconnect at battery terminal provides emergency shutoff

**Standards Applied:** SAE J1128 (automotive), WARN manufacturer specifications

**This is NOT an oversight** - it is intentional adherence to manufacturer specifications and automotive best practices. See [Standards Exceptions][standards-exceptions] for complete documentation.

## Contactor/Solenoid

- **Type:** Warn Zeon 10-S integrated contactor (included with winch)
- **Location:** Mounted on winch motor housing
- **Rating:** 450A+ switching capability
- **Function:** High-current switching for winch motor direction and power

## Control System

**Dual Control Setup:** Dash rocker switch + handheld remote (both work simultaneously)

**Dash Rocker Switch:**

- **Type:** Center-off momentary rocker switch (SPDT or DPDT)
- **Location:** Dashboard physical switch panel
- **Function:**
  - **UP (momentary):** Winch OUT (let out cable)
  - **CENTER:** Off (spring return to center)
  - **DOWN (momentary):** Winch IN (pull in cable)
- **Power:** SafetyHub ATC-1 (15A fuse)
- **Use case:** In-cab winch control (self-recovery, convenient operation from driver seat)

**Handheld Remote:**

- **Type:** Warn factory wired remote (included with Zeon 10-S)
- **Function:** IN/OUT directional control (same as dash rocker)
- **Connection:** Plugs into winch control pack
- **Use case:** Outside vehicle spotting (traditional winch operation with visual line of sight)

**Control Architecture:**

```text
SafetyHub ATC-1 (15A) → Dash Rocker Switch ⟷ Handheld Remote (parallel) → Winch Contactor IN/OUT
                              ↑                      ↑
                           UP = OUT              Remote OUT button
                           DOWN = IN             Remote IN button
```

**Both controls work simultaneously** - either dash rocker OR remote can trigger winch IN/OUT

## Wiring

**Main Power Wiring:**

See [AUX Battery Distribution][aux-battery] for wire specs (gauge, length, routing path).

- **Positive (+):** AUX battery+ → winch contactor → winch motor (direct, no breaker)
- **Negative (-):** AUX battery- → winch motor ground lug

**Control Wiring:**

- **Power Source:** SafetyHub ATC-1 (15A fuse) - AUX battery powered
- **Dash Rocker:** SafetyHub ATC-1 → Dash rocker switch → Winch contactor IN/OUT signals
- **Remote:** Wired in parallel with dash rocker (IN and OUT signals)
- **Wire Gauge:** 14 AWG (low-current control signals only, ~2A max)
- **Routing:** SafetyHub (wheel well) → dash switch → through firewall → winch contactor (front bumper)
- **Remote Connection:** Paralleled at winch contactor terminals (IN/OUT)

| Circuit         | Source             | Protection            | Wire Gauge                                                 | Destination             | Function            |
| --------------- | ------------------ | --------------------- | ---------------------------------------------------------- | ----------------------- | ------------------- |
| Main Power (+)  | AUX battery+       | None (direct)         | See [AUX Battery Distribution][aux-battery] for wire specs | Winch Contactor → Motor | High-current power  |
| Main Power (-)  | AUX battery-       | None                  | See [AUX Battery Distribution][aux-battery] for wire specs | Winch Motor Ground      | High-current return |
| Control Trigger | Dash Rocker Switch | SafetyHub ATC-1 (15A) | 14 AWG                                                     | Winch Contactor         | Low-current trigger |
| Remote Control  | Warn Remote        | Internal to winch     | Per Warn specs                                             | Winch Control Pack      | Directional control |

## Installation

**Power Cable Routing:**

See [AUX Battery Distribution][aux-battery] for cable specs and routing path.

- **Route:** Passenger wheel well → along frame rail → front bumper (13 ft)
- **Protection:** Split loom over entire run
- **Securing:** P-clamps every 18" along frame rail
- **Grommets:** Rubber grommets with sealant at body penetrations
- **Heat:** Route away from exhaust components (minimum 6" clearance)

**Winch Mounting:**

- Zeon 10-S fits front bumper (verified compatible)
- Factory contactor mounted on winch motor housing
- Ensure contactor is protected from direct water spray
- Verify all connections are tight and corrosion-free

**Control Switch Location:**

- Dash-mounted center-off momentary rocker switch
- Easily accessible from driver's seat
- Clear labeling: UP = OUT, DOWN = IN

## Safety Considerations

!!! warning "Winch Safety"
    - Never exceed winch rated capacity (10,000 lbs)
    - Always use proper recovery techniques and safety equipment
    - Keep hands and body clear of winch line under tension
    - Use tree savers and recovery equipment rated for load
    - Monitor battery voltage during extended winch operations

!!! warning "Electrical Safety"
    - Winch power cables carry extremely high current (up to 450A)
    - Ensure all connections are tight and properly crimped
    - Never disconnect battery while winch is under load
    - Check cable insulation regularly for damage

## Outstanding Items

None - all specifications determined.

## Related Documentation

- [AUX Battery Distribution][aux-battery] - Winch power source (passenger wheel well)
- [Wire Distance Reference][wire-distance] - Winch to battery routing distance (13 ft one-way, 26 ft circuit)
- [SafetyHub][safetyhub] - Winch contactor trigger circuit protection
- [Air Compressor][air-compressor] - ARB compressor for tire inflation

[aux-battery]: ../01-power-systems/03-aux-battery-distribution/index.md
[wire-distance]: ../01-power-systems/01-power-generation/05-wire-distance-reference.md
[safetyhub]: ../01-power-systems/03-aux-battery-distribution/04-safetyhub.md
[air-compressor]: 02-air-compressor.md
[warn-manual]: https://www.warn.com/
[standards-exceptions]: ../01-power-systems/STANDARDS-EXCEPTIONS.md
