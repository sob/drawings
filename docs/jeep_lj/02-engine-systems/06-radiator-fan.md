---
hide:
  - toc
---

# Radiator Fan System {#radiator-fan-system}
**Fan:** Camaro electric radiator fan
**Control:** Cummins R2.8 ECM via PWM signal
**Power:** CONSTANT power via PMU combined outputs (OUT2+3+4, 60A capacity)

## System Overview

Camaro electric radiator fan controlled by R2.8 ECM via PWM signal. Provides variable speed based on coolant temperature.

**Note:** Main radiator fan only. Oil cooler fan (PMU Out 7) and PS cooler fan (PMU Out 8) are separate, triggered via J1939 CAN bus temperature monitoring.

## Components

### Fan Motor

- **Type:** Camaro electric radiator fan (dual-speed or variable speed)
- **Location:** Mounted to radiator (front of engine bay)
- **Power Source:** CONSTANT power via PMU combined outputs (OUT2+3+4)
- **Control:** ECM PWM signal via fan controller module
- **Load:** TBD - verify actual amperage (typically 20-40A depending on speed)
- **Protection:** TBD - inline fuse or breaker (30A to 60A depending on fan specs)

### Fan Controller Module

- **Function:** Receives ECM PWM signal and controls fan motor speed
- **Trigger Input:** ECM Pin 33 (PWM signal - Pin 34 is return, unused)
- **Output:** High-current switched power to fan motor
- **Mounting Location:** TBD - near radiator or on radiator shroud
- **Ground:** Engine bay chassis ground

### ECM Integration

- **ECM Output:** Pin 33 provides PWM signal (0-100% duty cycle)
- **Pin 34:** Return (unused - not connected to fan controller)
- **Signal Type:** Ground-switched PWM (verify with Cummins documentation)
- **Wire Gauge:** 18-20 AWG for signal wire (low current)

## Power Flow

1. **Fan Power:** CONSTANT power (START battery) → PMU combined outputs (OUT2+3+4, 60A) → Junction → Camaro fan motor → chassis ground
   - OUT2, OUT3, OUT4 each use 10 AWG wire from PMU to junction point
   - Junction method: Terminal block or bus bar (near PMU preferred)
   - Junction to fan: 6 AWG minimum (handles combined 60A load)
   - **Critical:** Keep all three PMU wires equal length for balanced current distribution
2. **Fan Control Signal:** ECM Pin 33 → 18-20 AWG wire → fan controller PWM input (Pin 34 unused)
3. **Controller Ground:** Fan controller ground terminal → engine bay chassis ground

## Outstanding Items

- [x] Confirm ECM pins 33/34: Pin 33 PWM output (used), Pin 34 return (unused)
- [ ] Determine Camaro fan model/part number and amperage (low/high speed)
- [ ] Determine fan controller module part number/specs
- [ ] Determine wire size for fan power (based on amperage)
- [ ] Verify PMU combined outputs (OUT2+3+4) configured for fan control
- [ ] **Specify junction method for combining OUT2+3+4** (terminal block, bus bar, or splice)
- [ ] **Verify load balancing during testing** (measure current on each wire with clamp meter)
- [ ] Confirm fan controller mounting location
- [ ] Plan wire routing: ECM Pin 33 → fan controller
- [ ] Test fan operation at various coolant temperatures

## Related Documentation

- [Engine Systems][pmu-power-distribution] - PMU and ECM specifications
- [Auxiliary Engine Systems][auxiliary-systems] - Oil cooler and PS cooler fan circuits
