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

**Power Source:** PMU Out 23 (7A capacity, ~2A load)

**DRL Auto-Off:** PMU programming logic disables when CT4 SW3 activates headlights

## Circuit Components

The DRL/parking circuit (PMU Out 23) powers:

1. LP6 Headlight DRL (Pin 3) - both lights (0.8A total)
2. Maxbilt Round Trail Tail RED wire (marker/parking) - both lights (~1A total)

**Total Load:** ~2A (PMU Out 23 capacity: 7A, 29% utilization)

## PMU DRL Auto-Off Logic

**Purpose:** Automatically turns off DRL when headlights activate

**PMU Configuration:**

```text
PMU Input 7 (In 7): CT4 SW3 headlight status signal
PMU Input 6 (In 6): Ignition RUN signal
PMU Output 23 (Out 23): DRL/Parking lights circuit

Programming Logic:
IF (In6_IgnitionRUN == ON) AND (In7_CT4_Headlights == OFF)
  THEN Out23_DRL = ON
ELSE
  Out23_DRL = OFF
END
```

## Operation States

**1. Ignition ON, Headlights OFF:**

- PMU In 6 = ON (ignition RUN)
- PMU In 7 = OFF (CT4 SW3 not active)
- PMU Out 23 = ON
- **Result:** All DRL/parking lights illuminated

**2. Ignition ON, Headlights ON:**

- PMU In 6 = ON (ignition RUN)
- PMU In 7 = ON (CT4 SW3 active)
- PMU Out 23 = OFF
- **Result:** Headlights active, DRL off

**3. Ignition OFF:**

- PMU In 6 = OFF
- PMU Out 23 = OFF (regardless of headlight status)
- **Result:** All DRL/parking lights off

## Wiring

**PMU Input Wiring:**

- **In 6:** Ignition switch RUN output (shared with CT4, SwitchPros)
- **In 7:** CT4 SW3 output (tapped from headlight low beam circuit)

**PMU Output Wiring:**

- **Out 23:** 16 AWG from PMU (engine bay) splits to:
  - LP6 Pin 3 (DRL): 16 AWG to each headlight (0.8A total)
  - Maxbilt Round Trail Tail RED wire: 16 AWG to each tail light (~1A total)

**Wiring Method:** Simple inline splice or parallel connection at PMU output. No junction box required for ~2A load.

## Outstanding Items

- [ ] Plan wire routing from ignition switch RUN to PMU In 6 (splits to CT4, SwitchPros)
- [ ] Plan wire routing from CT4 SW3 to PMU In 7 (DRL cutoff logic)
- [ ] Create PMU programming configuration with DRL auto-off logic

## Related Documentation

- [PMU Power Distribution][pmu-power-distribution] - PMU Out 23 circuit and programming
- [Headlights][headlights] - LP6 DRL function (Pin 3)
- [Tail/Brake/Reverse][tail-brake-reverse-lights] - Maxbilt RED wire (marker/parking)

[pmu-power-distribution]: ../01-power-systems/04-pmu/index.md
[headlights]: 02-headlights.md
[tail-brake-reverse-lights]: 04-tail-brake-reverse.md
