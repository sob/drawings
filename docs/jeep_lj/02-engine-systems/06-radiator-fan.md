# Radiator Fan System {#radiator-fan-system}
**Fan:** Camaro electric radiator fan
**Control:** Cummins R2.8 ECM via PWM signal
**Power:** TBD - Battery+ or SWITCHED bus (30-60A protection)

## System Overview

Camaro electric radiator fan controlled by R2.8 ECM via PWM signal. Provides variable speed based on coolant temperature.

**Note:** Main radiator fan only. Oil cooler fan (PMU Out 7) and PS cooler fan (PMU Out 8) are separate, triggered via J1939 CAN bus temperature monitoring.

## Components

### Fan Motor

- **Type:** Camaro electric radiator fan (dual-speed or variable speed)
- **Location:** Mounted to radiator (front of engine bay)
- **Power Source:** Direct to battery positive or SWITCHED bus (high current)
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

1. **Fan Power:** Battery+ or SWITCHED bus → TBD breaker/fuse (30-60A) → fan controller module → Camaro fan motor → chassis ground
2. **Fan Control Signal:** ECM Pin 33 → 18-20 AWG wire → fan controller PWM input (Pin 34 unused)
3. **Controller Ground:** Fan controller ground terminal → engine bay chassis ground

## Outstanding Items

- [x] Confirm ECM pins 33/34: Pin 33 PWM output (used), Pin 34 return (unused)
- [ ] Determine Camaro fan model/part number and amperage (low/high speed)
- [ ] Determine fan controller module part number/specs
- [ ] Determine wire size for fan power (based on amperage)
- [ ] Determine fuse/breaker size (30A/40A/50A/60A)
- [ ] Decide fan power source (battery+ or SWITCHED bus)
- [ ] Confirm fan controller mounting location
- [ ] Plan wire routing: ECM Pin 33 → fan controller
- [ ] Test fan operation at various coolant temperatures

## Related Documentation

- [Engine Systems][# 1.4 - PMU Power Distribution {#pmu-power-distribution}] - PMU and ECM specifications
- [Auxiliary Engine Systems][# 7.3 - Auxiliary Systems {#auxiliary-systems}] - Oil cooler and PS cooler fan circuits
