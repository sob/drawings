---
hide:
  - toc
---

# 2.6 Radiator Fan System {#radiator-fan-system}

## System Overview

Electric radiator fan with automatic PWM temperature control via PMU24.

**Components:**

- GM 84100128 Camaro electric radiator fan (brushless PWM-capable, 53A @ full speed)
- PMU24 outputs OUT2+3+4 combined (3×25A = 75A capacity)

**Operation:**

- ECM broadcasts coolant temp on J1939 CAN bus (SPN 110)
- PMU reads temperature and adjusts fan speed via PWM:
  - <185°F: Fan OFF (0%)
  - 185-195°F: Low speed (30% = ~16A)
  - 195-205°F: Medium speed (60% = ~32A)
  - ≥205°F: Full speed (100% = 53A)

**Power:**

- **PMU OUT2+3+4** (75A capacity) → Fan motor via PWM control (4 AWG)
- **PMU power source:** START battery via 300A CB (wheel well)

**Benefits:**

- Variable speed control reduces electrical load and noise
- Integrated into PMU programming (no separate controller)
- No external relay or circuit breaker needed
- Quieter operation (low speed sufficient for most conditions)

**Note:** Main radiator fan only. Oil cooler and PS cooler fans controlled separately via PMU OUT7+8.

## Programming

**Via PMU Setup Software:**

Temperature-based PWM control curve (see [PMU Programming][pmu-programming] for complete logic):

```
IF (J1939_SPN110_CoolantTemp < 185°F) THEN Out234_RadiatorFan_PWM = 0%
ELSEIF (J1939_SPN110_CoolantTemp < 195°F) THEN Out234_RadiatorFan_PWM = 30%
ELSEIF (J1939_SPN110_CoolantTemp < 205°F) THEN Out234_RadiatorFan_PWM = 60%
ELSEIF (J1939_SPN110_CoolantTemp >= 205°F) THEN Out234_RadiatorFan_PWM = 100%
```

Setpoints can be adjusted based on testing and climate conditions.

## Installation

**Mounting:**

- Fan motor: Radiator shroud (factory location or custom mount)
- All control via PMU24 (engine bay mounted - see [PMU Overview][pmu-overview])

**Power Wiring:**

- **PMU OUT2+3+4** → Fan motor (+) via 4 AWG
- **Fan ground:** Fan motor (-) → Engine bay ground bus (4 AWG)
- **Distance:** PMU to fan motor ~TBD ft
- **Wire gauge:** 4 AWG minimum for 53A @ full speed

**Testing:**

- Program PMU temperature logic via PMU Setup software
- Monitor PMU LED indicators for output status
- Verify fan activation at temperature setpoints
- Check voltage at fan motor under various PWM speeds
- Adjust temperature setpoints if needed

## Wire Sizing

**Fan Motor Circuit (PMU to Fan):**
- **Wire gauge:** 4 AWG minimum
- **Full speed:** 53A @ 100% PWM, 4 AWG @ ~TBD ft, 60°C: TBD% drop
- **Medium speed:** 32A @ 60% PWM
- **Low speed:** 16A @ 30% PWM
- **Average load:** Much lower than 53A due to variable speed operation

**Note:** Fan is brushless PWM-capable, now fully utilized with PMU PWM control.

## Components

- **[2.6.1 Fan Motor][fan-motor]** - Camaro electric fan specifications

## Outstanding Items

- [ ] Determine optimal temperature setpoints for R2.8 (adjust PWM curve)
- [ ] Measure exact PMU to fan motor distance for wire sizing
- [ ] Test voltage drop under load at fan terminals (all PWM speeds)
- [ ] Verify PMU PWM frequency compatibility with Camaro fan motor
- [ ] Tune PWM curve based on real-world operating conditions

## Related Documentation

- [PMU Overview][pmu-overview] - PMU24 specifications and mounting
- [PMU Outputs][pmu-outputs] - OUT2+3+4 radiator fan assignment, OUT7+8 aux fans
- [PMU Programming][pmu-programming] - Radiator fan PWM control logic
- [START battery Distribution][front-battery] - PMU power source (300A CB)
- [Engine Bay Ground Bus][ground-bus] - Fan motor ground connection
- [Dakota Digital Gauge Cluster][gauge-cluster] - J1939 CAN bus source (SPN 110)

[fan-motor]: 01-fan-motor.md
[pmu-overview]: ../../01-power-systems/04-pmu/01-pmu-overview.md
[pmu-outputs]: ../../01-power-systems/04-pmu/03-pmu-outputs.md
[pmu-programming]: ../../01-power-systems/04-pmu/04-pmu-programming.md
[front-battery]: ../../01-power-systems/02-starter-battery-distribution/index.md
[gauge-cluster]: ../../04-control-interfaces/04-gauge-cluster/index.md
[ground-bus]: ../../01-power-systems/05-grounding/03-engine-bay-ground-bus.md
