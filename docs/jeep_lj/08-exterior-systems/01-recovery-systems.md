---
hide:
  - toc
tags:
  - product-details
  - exterior-systems
  - winch
  - recovery
---

# Recovery Systems {#recovery-systems}

## System Overview

The recovery systems provide essential off-road and emergency recovery capabilities, centered around the Warn Zeon 10-S winch. These systems are designed for reliable operation in extreme conditions with proper power distribution and control integration.

!!! info "Air System Moved"
    ARB Twin Compressor and Air Lockers documentation has been moved to [Air System][air-system]

---

## Winch

### Warn Zeon 10-S

/// html | div.product-info

**Model:** Warn Zeon 10-S

**Mounting Location:** Front bumper

**Pulling Capacity:** 10,000 lbs (4,536 kg)

**Motor:** 12V DC series wound

///

### Electrical Specifications

- **Peak Amperage Draw:** 400-480A (at full load/stall - brief periods only)
- **Typical Operating Draw:** 80-250A (most recovery operations)
- **Main Power Source:** AUX battery (passenger wheel well - direct connection, no fuse/breaker)
  - See [AUX Battery Distribution][aux-battery] for wire specs (gauge, length, routing, voltage drop calculations)
  - **System Voltage:** 13.8V (alternator charging - engine running during winch operations)
  - **Protection:** None - direct connection (see justification below)

### Circuit Protection - Engineering Justification {#winch-circuit-protection}

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

**This is NOT an oversight** - it is intentional adherence to manufacturer specifications and automotive best practices. See [Standards Exceptions][standards-exceptions] for complete documentation.

### Contactor/Solenoid

- **Type:** Warn Zeon 10-S integrated contactor (included with winch)
- **Location:** Mounted on winch motor housing
- **Rating:** 400A+ switching capability
- **Function:** High-current switching for winch motor direction and power

### Control System

**Dual Control Setup:** Dash rocker switch + handheld remote (both work simultaneously)

**Dash Rocker Switch:**

- **Type:** Center-off momentary rocker switch (SPDT or DPDT)
- **Location:** Dashboard physical switch panel
- **Function:**
  - **UP (momentary):** Winch OUT (let out cable)
  - **CENTER:** Off (spring return to center)
  - **DOWN (momentary):** Winch IN (pull in cable)
- **Power:** BODY PDU (available circuit breaker slot, 10A fuse)
- **Use case:** In-cab winch control (self-recovery, convenient operation from driver seat)

**Handheld Remote:**

- **Type:** Warn factory wireless remote or wired remote
- **Function:** IN/OUT directional control (same as dash rocker)
- **Connection:** Wired in parallel with dash rocker switch
- **Use case:** Outside vehicle spotting (traditional winch operation with visual line of sight)

**Control Architecture:**

```text
BODY PDU (10A CB) → Dash Rocker Switch ⟷ Handheld Remote (parallel) → Winch Contactor IN/OUT
                         ↑                      ↑
                      UP = OUT              Remote OUT button
                      DOWN = IN             Remote IN button
```

**Both controls work simultaneously** - either dash rocker OR remote can trigger winch IN/OUT

### Wiring Details

**Main Power Wiring:**

See [AUX Battery Distribution][aux-battery] for wire specs (gauge, length, routing path).

- **Positive (+):** AUX battery+ → winch contactor → winch motor (direct, no breaker)
- **Negative (-):** AUX battery- → winch motor ground lug

**Control Wiring:**

- **Power Source:** BODY PDU (available CB slot, 10A fuse) - AUX battery powered
- **Dash Rocker:** BODY PDU → Dash rocker switch → Winch contactor IN/OUT signals
- **Remote:** Wired in parallel with dash rocker (IN and OUT signals)
- **Wire Gauge:** 16-18 AWG (low-current control signals only, ~2A max)
- **Routing:** BODY PDU (cabin) → dash switch → through firewall → winch contactor (front bumper)
- **Remote Connection:** Paralleled at winch contactor terminals (IN/OUT)

### Wiring Summary

| Circuit | Source | Protection | Wire Gauge | Destination | Function |
|---------|--------|------------|------------|-------------|----------|
| Main Power (+) | AUX battery+ | None (direct) | See [AUX Battery Distribution][aux-battery] for wire specs | Winch Contactor → Motor | High-current power |
| Main Power (-) | AUX battery- | None | See [AUX Battery Distribution][aux-battery] for wire specs | Winch Motor Ground | High-current return |
| Control Trigger | Dash 3-pos Switch | SafetyHub ATC-1 (10A) | 14 AWG | Winch Contactor | Low-current trigger |
| Remote Control | Warn Remote | Internal to winch | Per Warn specs | Winch Control Pack | Directional control |

### Installation Considerations

**Power Cable Routing:**

See [AUX Battery Distribution][aux-battery] for cable specs and routing path. General considerations:

- Protect cables from sharp edges and heat sources
- Use proper grommets where cables pass through metal panels
- Secure cables with appropriate clamps to prevent chafing
- Keep cables away from exhaust components and moving parts

**Contactor Location:**

- Factory mounted on winch motor housing
- Ensure contactor is protected from direct water spray
- Verify all connections are tight and corrosion-free

**Control Switch Location:**

- Dash-mounted 3-position switch (Button 4 on physical switch panel)
- Easily accessible from driver's seat
- Clear labeling for switch positions (Off/SwitchPros/Manual)

### Safety Considerations

!!! warning "Winch Safety"
    - Never exceed winch rated capacity (10,000 lbs)
    - Always use proper recovery techniques and safety equipment
    - Keep hands and body clear of winch line under tension
    - Use tree savers and recovery equipment rated for load
    - Monitor battery voltage during extended winch operations

!!! warning "Electrical Safety"
    - Winch power cables carry extremely high current (up to 400A)
    - Ensure all connections are tight and properly crimped
    - Never disconnect battery while winch is under load
    - Verify proper fuse sizing for control circuit (10A)
    - Check cable insulation regularly for damage

### Outstanding Items

- [ ] **Determine if/how Position 2 (SwitchPros control) will work** - which SwitchPros output to use for remote winch control?
- [ ] Verify dash 3-position switch wiring diagram (positions: off/SwitchPros/manual)
- [ ] Confirm winch contactor trigger wiring from SafetyHub ATC-1 to winch contactor
- [ ] Determine Warn wireless/wired remote model and integration
- [ ] Verify winch mounting hardware and front bumper compatibility

## Related Documentation

- [AUX battery Distribution][aux-battery] - Winch power source (passenger wheel well)
- [Wire Distance Reference][wire-distance] - Winch to battery routing distance (13 ft one-way, 26 ft circuit)
- [SafetyHub][safetyhub] - Winch contactor trigger circuit protection
- [Air System][air-system] - ARB compressor and air lockers

[aux-battery]: ../01-power-systems/03-aux-battery-distribution/index.md
[wire-distance]: ../01-power-systems/01-power-generation/05-wire-distance-reference.md
[safetyhub]: ../01-power-systems/03-aux-battery-distribution/04-safetyhub.md
[air-system]: 02-air-system.md
[warn-manual]: https://www.warn.com/
[standards-exceptions]: ../01-power-systems/STANDARDS-EXCEPTIONS.md

---

## Future Recovery Expansion

**Potential Additional Recovery Equipment:**

- **Recovery Boards:** MaxTrax or similar traction boards (storage location TBD)
- **Recovery Straps:** Tree savers, kinetic ropes (storage in cargo area)
- **D-Rings/Shackles:** Bow shackles and D-rings (storage in cargo area)
- **Snatch Block:** Pulley block for winch line redirection (storage in cargo area)
- **Hi-Lift Jack:** 48" or 60" high-lift jack (mount location TBD - hood, bumper, or rear swing-out)
- **Portable Jump Starter:** Lithium jump pack for emergency battery assistance
- **Air Down/Up Kit:** ARB E-Z Deflator and tire inflation accessories (integrates with air compressor system)

**Integration Opportunities:**

- **Wireless Winch Control Integration:** Integrate with vehicle's audio/communication system for voice commands
- **Winch Load Monitoring:** Add amp meter or load sensor to monitor winch current draw
- **Remote Battery Monitoring:** Monitor START battery voltage during winch operations from inside cabin
- **Automatic Winch Cut-off:** Integrate with battery voltage monitoring to prevent over-discharge
