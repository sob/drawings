---
hide:
  - toc
tags:
  - lighting
  - drl
  - pmu-controlled
---

# DRL & Parking Lights {#drl-parking-lights}

**Control:** Automatic with ignition

**Power Source:** PMU Out 9 (8A capacity, SWITCHED)

**DRL Auto-Off:** PMU programming logic disables when CT4 SW3 activates headlights

## Circuit Components

The DRL/parking circuit (PMU Out 9) powers:

1. LP6 Headlight DRL (Pin 3) - both lights
2. License plate lights - both lights
3. Front 2" LED side markers (parking) - both lights
4. Maxbilt tail light RED wire (marker/parking) - both lights

**Total Load:** ~8A (PMU Out 9 capacity: 15A)

## PMU DRL Auto-Off Logic

**Purpose:** Automatically turns off DRL when headlights activate

**PMU Configuration:**

```text
PMU Input 7 (In 7): CT4 SW3 headlight status signal
PMU Input 6 (In 6): Ignition RUN signal
PMU Output 9 (Out 9): DRL/Parking lights circuit

Programming Logic:
IF (In6_IgnitionRUN == ON) AND (In7_CT4_Headlights == OFF)
  THEN Out9_DRL = ON
ELSE
  Out9_DRL = OFF
END
```

## Operation States

**1. Ignition ON, Headlights OFF:**

- PMU In 6 = ON (ignition RUN)
- PMU In 7 = OFF (CT4 SW3 not active)
- PMU Out 9 = ON
- **Result:** All DRL/parking lights illuminated

**2. Ignition ON, Headlights ON:**

- PMU In 6 = ON (ignition RUN)
- PMU In 7 = ON (CT4 SW3 active)
- PMU Out 9 = OFF
- **Result:** Headlights active, DRL off

**3. Ignition OFF:**

- PMU In 6 = OFF
- PMU Out 9 = OFF (regardless of headlight status)
- **Result:** All DRL/parking lights off

## Wiring

**PMU Input Wiring:**

- **In 6:** Ignition switch RUN output (shared with CT4, SwitchPros)
- **In 7:** CT4 SW3 output (tapped from headlight low beam circuit)

**PMU Output Wiring:**

- **Out 9:** 14 AWG from PMU to DRL junction
- DRL junction distributes to:
  - LP6 Pin 3 (DRL): 16 AWG to each light (0.8A total)
  - License plate lights: 16 AWG to each light
  - Front LED side markers: 16 AWG to each light
  - Maxbilt tail RED wire: 16 AWG to each light

## License Plate Lights

**Type:** Factory or aftermarket LED license plate lights
**Quantity:** 2 (factory locations)
**Control:** DRL/parking circuit (automatic with ignition)
**Wire Gauge:** 16 AWG from DRL junction

## Outstanding Items

- [ ] Determine if factory license plate lights are retained or upgraded to LED
- [ ] Verify wire routing from DRL junction to license plate area
- [ ] Plan wire routing from ignition switch RUN to PMU In 6 (splits to CT4, SwitchPros)
- [ ] Plan wire routing from CT4 SW3 to PMU In 7 (DRL cutoff logic)
- [ ] Create PMU programming configuration with DRL auto-off logic
- [ ] Verify total DRL circuit load does not exceed 8A

## Related Documentation

- [PMU Power Distribution][pmu-power-distribution] - PMU Out 9 circuit and programming
- [Headlights][headlights] - LP6 DRL function (Pin 3)
- [Tail/Brake/Reverse][tail-brake-reverse-lights] - Maxbilt RED wire (marker/parking)
- [Turn Signals][turn-signals] - Front marker parking lights

[pmu-power-distribution]: ../01-power-systems/04-pmu/index.md
[headlights]: 02-headlights.md
[tail-brake-reverse-lights]: 04-tail-brake-reverse.md
[turn-signals]: 03-turn-signals.md
