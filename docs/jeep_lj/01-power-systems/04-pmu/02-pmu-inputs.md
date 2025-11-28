---
hide:
  - toc
---

# 1.4.2 PMU Inputs {#pmu-inputs}

PMU input configuration including digital inputs, analog inputs, CAN bus integration, and ignition signal distribution.

## 12V Switched Input (Pin 7)

**Source:** Dedicated 18 AWG wire from ignition switch RUN terminal

**Function:** Provides switched power reference for PMU logic

**Implementation:** Dedicated wire through firewall (Grommet 2) direct to PMU Pin 7 - NOT from ignition signal bus bar

**Load:** ~50mA

See [Ignition Signal Distribution](#ignition-signal-distribution) for complete wiring architecture.

## Digital Inputs (Trigger Sources)

**Note:** Pin 7 (physical 12V switched input above) is separate from In 7 (digital input channel below). Use "Pin7" in programming for ignition sense, "In7" for headlight status.

| Input    | Function             | Source                       | Connected to Output     | Notes                                    |
| :------- | :------------------- | :--------------------------- | :---------------------- | :--------------------------------------- |
| **In 1** | Horn Button          | Steering wheel button        | Out 18 (Horn)           | Normally open, closes when pressed       |
| **In 2** | Brake Switch         | Brake pedal switch           | Out 21 (Brake Lights)   | Normally open, closes when pedal pressed |
| **In 3** | Reverse Switch       | AX15 trans switch            | Out 22 (Reverse Lights) | Normally open, closes in reverse gear    |
| **In 4** | **[Available]**      | -                            | -                       | Available for future expansion           |
| **In 5** | **[Available]**      | -                            | -                       | Available for future expansion           |
| **In 6** | **[Available]**      | -                            | -                       | Available for future expansion           |
| **In 7** | CT4 SW3 (Headlights) | CT4 lever pull               | Out 14 (DRL) logic      | 12V when headlights active, disables DRL |
| **In 8** | **[Available]**      | -                            | -                       | Available for future expansion           |
| **In 9** | A/C Request          | Factory TJ A/C button signal | Out 17 (A/C Clutch)     | 12V when factory dash A/C button pressed |

**Note:** Starter system uses traditional direct control (keyswitch → clutch switch → relay) independent of PMU. See [Starter System][starter].

[starter]: ../../02-engine-systems/01-starter.md

## Analog Inputs

| Input       | Physical Pin | Range | Function                    | Notes                                          |
| :---------- | :----------- | :---- | :-------------------------- | :--------------------------------------------- |
| **An 1-4**  | Dedicated    | 0-5V  | **[Available]**             | Future expansion                               |
| **An 5**    | Dedicated    | 0-5V  | Boost Pressure              | 0-5V transducer, displayed on ADU7             |
| **An 6**    | Dedicated    | 0-5V  | EGT (Exhaust Gas Temp)      | Thermocouple + amplifier, displayed on ADU7    |
| **An 7**    | Dedicated    | 0-5V  | AUX Battery Voltage         | Voltage divider circuit, displayed on ADU7     |
| **An 8**    | Dedicated    | 0-5V  | **[Available]**             | Future expansion                               |
| **An 9-16** | OUT17-24     | 0-20V | **[Configured as outputs]** | Dual-purpose pins - currently used as OUT17-24 |

**Current Configuration:** An 9-16 configured as outputs (OUT17-24). See [PMU Outputs][pmu-outputs] for output assignments.

**J1939 Data:** Engine oil temperature and coolant temperature are monitored via J1939 CAN bus from ECM (no analog inputs needed).

**ADU7 Integration:** Analog inputs An 5-8 feed data to [ADU7 Display][adu7-display] via ECUMaster CAN bus.

## CAN Bus Integration (J1939)

PMU24 taps into existing J1939 CAN bus as stub connection (no termination).

### Bus Topology

```text
[ECM 120Ω] ←--+--+--→ [Cummins Body Harness End 120Ω]
               |  |
               |  [PMU24 - stub tap]
               |
          [Dakota Digital - stub tap]
```

### Physical Connection

- **Tap Location:** Cummins body harness (same as Dakota Digital tap)
- **Wire Gauge:** 18-20 AWG twisted pair
- **Stub Length:** <12" from tap to PMU (keep as short as possible, ideally <6")
- **Termination:** None - bus already terminated at ECM + harness end
- **PMU Setting:** Disable internal CAN termination in software

### J1939 Data Used

|   SPN   | Parameter           | PMU Use                        |
| :-----: | :------------------ | :----------------------------- |
| **175** | Engine Oil Temp     | Oil cooler fan control (OUT 7) |
| **110** | Engine Coolant Temp | PS cooler fan control (OUT 8)  |
| **190** | Engine Speed (RPM)  | Data logging                   |
| **100** | Engine Oil Pressure | Data logging                   |

See [PMU Programming][pmu-programming] for CAN-based logic examples.

## Ignition Signal Distribution

**PMU Pin 7:** Dedicated 18 AWG wire directly from keyswitch RUN terminal (NOT from ignition signal bus bar)

**Routing:** Through firewall (Grommet 2) to PMU Pin 7

**Purpose:** Critical PMU functions have guaranteed power independent of other devices

**Non-critical devices** (CT4, SwitchPros, radio, BCDC, camera) use shared ignition signal bus bar - see [Ignition Signal][ignition-signal] for details.

## Related Documentation

- [PMU Overview][pmu-overview] - Product specifications and capacity
- [PMU Outputs][pmu-outputs] - Output configuration and load details
- [PMU Programming][pmu-programming] - Logic examples using inputs and CAN data
- [Firewall Ingress][firewall-ingress] - Grommet 2 routing
- [Gauge Cluster][gauge-cluster] - Dakota Digital J1939 integration

[pmu-overview]: 01-pmu-overview.md
[pmu-outputs]: 03-pmu-outputs.md
[pmu-programming]: 04-pmu-programming.md
[firewall-ingress]: ../07-wire-routing/02-firewall-ingress.md
[gauge-cluster]: ../../02-engine-systems/09-gauge-cluster/index.md
[ignition-signal]: ../06-ignition-signal/index.md
[adu7-display]: ../../02-engine-systems/10-adu7-display/index.md
