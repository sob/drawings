---
hide:
  - toc
---

# Dashboard Physical Controls {#dashboard-physical-controls}

This section documents physical switches mounted in the dashboard area (separate from the SwitchPros control panel).

## Winch Control Rocker Switch

!!! info "Winch System Documentation"
For complete winch specifications, wiring details, and recovery system information, see [Recovery Systems][recovery-systems].

**Type:** Center-off momentary rocker switch (SPDT or DPDT)
**Location:** Dashboard physical switch panel
**Function:** In-cab winch control (works in parallel with handheld remote)

### Switch Positions

- **UP (momentary):** Winch OUT (let out cable)
- **CENTER:** Off (spring return to center)
- **DOWN (momentary):** Winch IN (pull in cable)

**Dual Control:** Dash rocker switch + handheld remote work simultaneously in parallel

### Wiring

**Power Source:**

- **BODY PDU:** Available circuit breaker slot (10A fuse)
- **System:** AUX battery powered (matches winch main power source)

**Control Circuit:**

- **Power:** BODY PDU (10A CB) → Dash rocker switch
- **Outputs:** Rocker UP/DOWN → Winch contactor IN/OUT signals
- **Wire Gauge:** 16-18 AWG (low-current control signals, ~2A max)
- **Routing:** BODY PDU (cabin) → dash rocker → through firewall → winch contactor (front bumper)

**Parallel Remote:**

- Handheld remote (wireless or wired) connects in parallel at winch contactor
- Both dash rocker AND remote can trigger IN/OUT independently

### Winch Control Outstanding Items

- [ ] Source center-off momentary rocker switch (SPDT or DPDT, 10A rated)
- [ ] Assign BODY PDU circuit breaker slot for winch control (10A)
- [ ] Determine firewall grommet routing for control wires
- [ ] Verify winch contactor IN/OUT terminal connections for parallel wiring

## Rear Seat Switch

**Type:** TBD - momentary or latching switch
**Location:** Rear seat area (for rear passenger control)
**Function:** Controls rear roll bar dome lights (4x KC Cyclone)

### Wiring Options

**Option 1 - Parallel with SwitchPros Button 4:**

- Wire switch in parallel with OUTPUT-4 circuit
- Allows rear passenger to turn on/off dome lights independently
- Both switches can control the same lights

**Option 2 - Connected to TRIGGER input:**

- Wire to SwitchPros TRIGGER-1, TRIGGER-2, or TRIGGER-3
- Allows SwitchPros to interpret rear seat switch as a remote trigger
- More complex but allows for programmable behavior

### Rear Seat Switch Outstanding Items

- [ ] Determine rear seat switch type (momentary vs latching)
- [ ] Determine rear seat switch mounting location
- [ ] Decide on wiring method (parallel with Button 4 or TRIGGER input)
- [ ] Determine wire routing from rear seat to SwitchPros location
- [ ] Verify switch rating if wired in parallel (must handle 4A dome light load)

## Related Documentation

- [Control Interfaces Overview][control-interfaces-overview] - Main control interfaces overview
- [SwitchPros SP-1200][switchpros-sp-1200-rcr-force-12] - Main lighting controller
- [Recovery Systems][recovery-systems] - Winch system complete documentation

[recovery-systems]: ../08-exterior-systems/01-recovery-systems.md
[control-interfaces-overview]: 01-overview.md
[switchpros-sp-1200-rcr-force-12]: 02-switchpros-sp1200.md
