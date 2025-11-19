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
  - **Cable:** Dual 1/0 AWG (positive and negative) - optimized for 26 ft total circuit length
  - **Length:** 13 ft one-way from AUX battery to winch (26 ft total circuit - see [Wire Distance Reference][wire-distance])
  - **System Voltage:** 13.8V (alternator charging - engine running during winch operations)
  - **Voltage Drop @ 250A typical:** 4.92% (0.68V drop, 13.12V at winch) - excellent for normal recovery
  - **Voltage Drop @ 400A peak:** 7.87% (1.09V drop, 12.71V at winch) - acceptable for brief stall/heavy load
  - **Protection:** None - direct connection (winch-rated contactor handles switching)
  - **Route:** Passenger wheel well → along frame rail → through bumper → winch motor

### Contactor/Solenoid

- **Type:** Warn Zeon 10-S integrated contactor (included with winch)
- **Location:** Mounted on winch motor housing
- **Rating:** 400A+ switching capability
- **Function:** High-current switching for winch motor direction and power

### Control System

**Primary Control:** 3-position dash switch (Button 4 on physical switch panel)

**Switch Positions:**
1. **Position 1 (Off):** Winch completely disconnected
   - No power to contactor
   - Winch is completely de-energized

2. **Position 2 (SwitchPros):** TBD - controlled remotely via SwitchPros
   - **Outstanding:** Need to determine which SwitchPros output to use for remote winch control
   - Allows winch operation from inside cabin via SwitchPros app or button

3. **Position 3 (Manual):** Direct wired remote control
   - Uses Warn factory wireless remote or wired remote
   - **Trigger wiring:** From dash switch → SafetyHub ATC-1 (10A fuse) → winch contactor
   - Allows traditional remote control operation

### Wiring Details

**Main Power Wiring:**
- **Positive (+):** AUX battery+ (passenger wheel well) → 1/0 AWG red wire (direct, no breaker) → winch contactor → winch motor
- **Negative (-):** AUX battery- (passenger wheel well) → 1/0 AWG black wire → winch motor ground lug
- **Cable Run:** 13 ft one-way (26 ft total circuit length - see [Wire Distance Reference][wire-distance])
- **Routing:** Passenger wheel well → along frame rail → through bumper passage → front bumper winch mount

**Control Wiring:**
- **Trigger Circuit:** Dash 3-position switch → SafetyHub ATC-1 (10A fuse) → winch contactor trigger input
- **Wire Gauge:** 14 AWG (trigger circuit only, not main power)
- **Fuse:** SafetyHub ATC-1 (10A) protects control circuit
- **Routing:** Dash switch → under dash → through firewall → winch contactor

**Remote Control:**
- **Warn Wireless/Wired Remote:** Connects to winch control pack (when manual mode selected)
- **Function:** Provides directional control (in/out) when in Position 3

### Wiring Summary

| Circuit | Source | Distance | Protection | Wire Gauge | Destination | Function |
|---------|--------|----------|------------|------------|-------------|----------|
| Main Power (+) | AUX battery+ (passenger wheel well) | 13 ft one-way | None (direct) | 1/0 AWG | Winch Contactor → Motor | High-current power |
| Main Power (-) | AUX battery- (passenger wheel well) | 13 ft one-way | None | 1/0 AWG | Winch Motor Ground | High-current return |
| Control Trigger | Dash 3-pos Switch | Short | SafetyHub ATC-1 (10A) | 14 AWG | Winch Contactor | Low-current trigger |
| Remote Control | Warn Remote | N/A | Internal to winch | Per Warn specs | Winch Control Pack | Directional control |

### Installation Considerations

**Power Cable Routing:**
- Route 1/0 AWG cables from AUX battery (passenger wheel well) along frame rail to front bumper
- 13 ft one-way routing distance (26 ft total circuit - see [Wire Distance Reference][wire-distance])
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
    - 1/0 AWG cables carry extremely high current (up to 400A)
    - Ensure all connections are tight and properly crimped
    - Never disconnect battery while winch is under load
    - Verify proper fuse sizing for control circuit (10A)
    - Check cable insulation regularly for damage

### Outstanding Items

- [ ] **Determine if/how Position 2 (SwitchPros control) will work** - which SwitchPros output to use for remote winch control?
- [ ] Confirm exact routing path for 1/0 AWG cables from passenger wheel well along frame rail
- [ ] Verify dash 3-position switch wiring diagram (positions: off/SwitchPros/manual)
- [ ] Confirm winch contactor trigger wiring from SafetyHub ATC-1 to winch contactor
- [ ] Determine Warn wireless/wired remote model and integration
- [ ] Verify proper crimp connectors for 1/0 AWG cable terminations (battery lugs, winch terminals)
- [ ] Plan cable protection method along frame rail and through bumper area
- [ ] Verify winch mounting hardware and front bumper compatibility
- [ ] Confirm battery terminal lugs are rated for 1/0 AWG cable

## Related Documentation

- [AUX battery Distribution][aux-battery] - Winch power source (passenger wheel well)
- [Wire Distance Reference][wire-distance] - Winch to battery routing distance (13 ft one-way, 26 ft circuit)
- [SafetyHub][safetyhub] - Winch contactor trigger circuit protection
- [Air System][air-system] - ARB compressor and air lockers

[aux-battery]: ../01-power-systems/03-aux-battery-distribution/index.md
[wire-distance]: ../01-power-systems/01-power-generation/05-wire-distance-reference.md
[safetyhub]: ../01-power-systems/02-starter-battery-distribution/04-safetyhub.md
[air-system]: 02-air-system.md

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
