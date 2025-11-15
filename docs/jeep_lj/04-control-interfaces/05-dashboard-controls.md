# Dashboard Physical Controls {#dashboard-physical-controls}
This section documents physical switches mounted in the dashboard area (separate from the SwitchPros control panel).

## Winch Control Switch

!!! info "Winch System Documentation"
    For complete winch specifications, wiring details, and recovery system information, see [Recovery Systems][# Recovery Systems {#recovery-systems}].

**Type:** 3-position dash switch
**Location:** Dashboard (Button 4 on physical switch panel)
**Function:** Controls winch operation mode

### Switch Positions

1. **Position 1 (Off):** Winch completely disconnected
2. **Position 2 (SwitchPros):** TBD - controlled remotely via SwitchPros (need to determine which output)
3. **Position 3 (Manual):** Direct wired remote control
   - Uses Warn factory wireless remote or wired remote
   - Trigger wiring: From dash switch → SafetyHub ATC-1 (10A fuse) → winch contactor

### Wiring

- **Control Trigger:** Dash 3-pos switch → SafetyHub ATC-1 (10A) → winch contactor trigger
- **Wire Gauge:** 14 AWG (trigger circuit only, not main power)
- **Routing:** Dash switch → under dash → through firewall → winch contactor

### Outstanding Items

- [ ] Determine if/how Position 2 (SwitchPros control) will work - which SwitchPros output to use for remote winch control?
- [ ] Verify dash 3-position switch wiring diagram (positions: off/SwitchPros/manual)
- [ ] Confirm winch contactor trigger wiring from SafetyHub ATC-1 to winch contactor

## Rear Seat Switch

**Type:** TBD - momentary or latching switch
**Location:** Rear seat area (for rear passenger control)
**Function:** Controls rear roll bar dome lights (4x KC Cyclone)

### Wiring Options

**Option 1: Parallel with SwitchPros Button 4**
- Wire switch in parallel with OUTPUT-4 circuit
- Allows rear passenger to turn on/off dome lights independently
- Both switches can control the same lights

**Option 2: Connected to TRIGGER input**
- Wire to SwitchPros TRIGGER-1, TRIGGER-2, or TRIGGER-3
- Allows SwitchPros to interpret rear seat switch as a remote trigger
- More complex but allows for programmable behavior

### Outstanding Items

- [ ] Determine rear seat switch type (momentary vs latching)
- [ ] Determine rear seat switch mounting location
- [ ] Decide on wiring method (parallel with Button 4 or TRIGGER input)
- [ ] Determine wire routing from rear seat to SwitchPros location
- [ ] Verify switch rating if wired in parallel (must handle 4A dome light load)

## Related Documentation

- [Control Interfaces Overview][# Control Interfaces - Overview {#control-interfaces-overview}] - Main control interfaces overview
- [SwitchPros SP-1200][# SwitchPros SP-1200 (RCR-Force 12) {#switchpros-sp-1200-rcr-force-12}] - Main lighting controller
- [Recovery Systems][# Recovery Systems {#recovery-systems}] - Winch system complete documentation
