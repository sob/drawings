---
hide:
  - toc
---

# 1.4.3 PMU Outputs {#pmu-outputs}
Complete configuration of all 24 PMU outputs, load allocations, and combined output configurations.

## PMU24 Output Configuration {#pmu-output-wiring-diagram}

### 25A High-Side Outputs (OUT1-OUT10)

| Output           | Circuit                      | Load      | Control Type                   | Trigger/Input                       | Notes                                             |
|:-----------------|:-----------------------------|:----------|:-------------------------------|:------------------------------------|:--------------------------------------------------|
| **Out 1**        | HVAC Blower Motor            | ~20A      | Auto (ignition ON)             | Constant power when ignition on     | See [HVAC System][hvac-system] - highest single load |
| **Out 2**        | **Radiator Fan (combined)**  | Combined  | Auto (ECM PWM control)         | Combined with OUT3 + OUT4           | GM 84100128 - 30-60A, requires 3x 25A outputs     |
| **Out 3**        | **Radiator Fan (combined)**  | Combined  | Auto (ECM PWM control)         | Combined with OUT2 + OUT4           | GM 84100128 - 30-60A, requires 3x 25A outputs     |
| **Out 4**        | **Radiator Fan (combined)**  | Combined  | Auto (ECM PWM control)         | Combined with OUT2 + OUT3           | GM 84100128 - 30-60A, requires 3x 25A outputs     |
| **Out 5**        | **iBooster Main (combined)** | Combined  | CONSTANT (always on)           | Combined with OUT6 + OUT9           | Bosch iBooster - 40A peak, requires 3x 25A outputs for thermal margin|
| **Out 6**        | **iBooster Main (combined)** | Combined  | CONSTANT (always on)           | Combined with OUT5 + OUT9           | Bosch iBooster - 40A peak, requires 3x 25A outputs for thermal margin|
| **Out 7**        | Oil Cooler Fan               | ~15A      | Auto (CAN temp monitoring)     | ECM J1939 engine oil temp (SPN 175) | Programmable temp thresholds via CAN              |
| **Out 8**        | PS Cooler Fan                | ~15A      | Auto (CAN temp monitoring)     | ECM J1939 coolant temp (SPN 110)    | Programmable temp thresholds via CAN              |
| **Out 9**        | **iBooster Main (combined)** | Combined  | CONSTANT (always on)           | Combined with OUT5 + OUT6           | Bosch iBooster - 40A peak, requires 3x 25A outputs for thermal margin|
| **Out 10**       | **[Available]**              | -         | -                              | -                                   | Future expansion (25A high-current)               |

### 15A High-Side Outputs (OUT11-OUT16)

| Output           | Circuit                      | Load      | Control Type                   | Trigger/Input                       | Notes                                             |
|:-----------------|:-----------------------------|:----------|:-------------------------------|:------------------------------------|:--------------------------------------------------|
| **Out 11**       | WS-51C Wiper Controller      | 15A       | Auto (ignition ON)             | Ignition signal (Pin 7)             | See [Wipers][windshield-wiper-control-system]                        |
| **Out 12**       | Dakota Digital Cluster       | ~15A      | Auto (ignition RUN)            | Ignition signal (Pin 7)             | See [Gauge Cluster][dakota-digital-gauge-cluster]          |
| **Out 13**       | Command Touch CT4            | ~10A      | CONSTANT (always on)           | Works with ignition off (hazards)   | Critical safety system - hazards/turn signals     |
| **Out 14**       | DRL/Parking Lights           | ~8A       | Auto (ignition) with logic     | Ignition ON + headlight status      | See [DRL & Parking Lights][drl-parking-lights]    |
| **Out 15**       | **[Available]**              | -         | -                              | -                                   | Future expansion (15A)                            |
| **Out 16**       | **[Available]**              | -         | -                              | -                                   | Future expansion (15A)                            |

### 7A High-Side Outputs (OUT17-OUT24)

**Note:** OUT17-24 are dual-purpose - configurable as 7A outputs OR 0-20V analog inputs. See [PMU Inputs][pmu-inputs] for analog input configuration.

| Output           | Circuit                      | Load      | Control Type                   | Trigger/Input                       | Notes                                             |
|:-----------------|:-----------------------------|:----------|:-------------------------------|:------------------------------------|:--------------------------------------------------|
| **Out 17**       | A/C Clutch                   | 3-5A      | Auto (A/C request)             | Factory TJ A/C button signal (In 9) | See [HVAC System][hvac-system]                     |
| **Out 18**       | Horn                         | 5.4A      | External input                 | Horn button (steering wheel)        | PIAA horns (2.7A × 2), works with ignition off    |
| **Out 19**       | iBooster Ignition Signal     | ~5A       | Auto (ignition RUN)            | Ignition signal (Pin 7)             | Gen 2 iBooster - See [Brake Booster][brake-booster-system-bosch-ibooster-gen-2] |
| **Out 20**       | **[Available]**              | -         | -                              | -                                   | Gen 2 iBooster doesn't need secondary power       |
| **Out 21**       | Brake Lights                 | ~3A       | External input                 | Brake switch signal (In 2)          | See [Tail, Brake & Reverse][tail-brake-reverse-lights]    |
| **Out 22**       | Reverse Lights               | ~3A       | External input                 | Trans reverse switch (In 3)         | See [Tail, Brake & Reverse][tail-brake-reverse-lights]    |
| **Out 23**       | **[Available]**              | -         | -                              | -                                   | Starter uses direct control - see [Starter System][starter-system-cummins-r28] |
| **Out 24**       | **[Available]**              | -         | -                              | -                                   | Future expansion (7A output)                      |

## Combined Outputs

**Radiator Fan (OUT2+3+4):** GM 84100128, 30-60A peak, 3×25A outputs paralleled

**iBooster Main (OUT5+6+9):** Bosch Gen 2, 40A peak, 3×25A outputs paralleled for thermal margin, CONSTANT power

**Combining Rules:**

- Only same-rated outputs can be combined (25A + 25A ✓, 25A + 15A ✗)
- **Thermal limits:** Two adjacent 2.8 terminals = 38A max @ 23°C, derates at higher temperatures
- **Engine bay operation:** Single 2.8 terminal @ 40°C = 23A max (outputs derate with temperature)
- **Load balancing:** Avoid placing heavily loaded outputs adjacent to each other
- Use proper terminal crimping and wire gauge to maximize current capacity

## Thermal Analysis

**High-Current Outputs (Thermal Concerns):**

| Outputs | Load | Terminal Rating | Utilization @ 40°C | Status | Notes |
|:--------|:-----|:----------------|:-------------------|:-------|:------|
| **OUT5+6+9** | 40A peak | 75A (3×25A @ 40°C) | 53% @ 40°C | ✓ OK | 3 outputs provide adequate thermal margin even at high temps |
| **OUT1** | 20A | 23A (single @ 40°C) | 87% | ⚠️ Acceptable | Close to thermal limit - avoid adjacent to OUT2-4 |
| **OUT2-3-4** | 60A peak | 69A (3×23A @ 40°C) | 87% | ⚠️ Monitor | Requires balanced load across all 3 outputs - verify ECM PWM balancing |
| **OUT11** | 15A | 19A (1.5 terminal) | 79% | ✓ OK | Avoid adjacent to OUT12 if possible |
| **OUT12** | 15A | 19A (1.5 terminal) | 79% | ✓ OK | Avoid adjacent to OUT11 if possible |

**Installation Notes:**

- PMU thermal protection will shut down overloaded outputs
- Monitor output temperatures during initial testing (PMU displays thermal status)
- Verify radiator fan ECM balances load evenly across OUT2-3-4
- iBooster 40A peak is brief (motor inrush) - continuous load should be <30A

!!! warning "Thermal Analysis Pending"
    Complete thermal analysis and output placement verification will be performed during initial installation and testing. Monitor PMU LED indicators and thermal status during first engine runs under various load conditions. Adjust output assignments if thermal issues occur.

**Grounding Architecture:**

- **PMU uses high-side outputs** (switches positive power to loads)
- **Each load grounds separately** (chassis ground, battery ground, or ground bus)
- **Pin 25 is reference ground ONLY** (<100mA logic/CAN reference)
- **Output current does NOT return through Pin 25** - returns through individual load grounds
- See [Grounding Architecture][grounding] for load ground connections

[grounding]: ../05-grounding/index.md

## Related Documentation

- [PMU Overview][pmu-overview] - Product specifications and capacity
- [PMU Inputs][pmu-inputs] - Input configuration and triggers
- [PMU Programming][pmu-programming] - Logic configuration for outputs
- [START battery Distribution][starter-battery-distribution] - PMU power source and circuit breaker

[pmu-overview]: 01-pmu-overview.md
[pmu-inputs]: 02-pmu-inputs.md
[pmu-programming]: 04-pmu-programming.md
[starter-battery-distribution]: ../02-starter-battery-distribution/index.md
[29-grid-heater-system]: ../../02-engine-systems/08-grid-heater.md
