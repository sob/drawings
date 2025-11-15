# 1.4.4 PMU Programming {#144-pmu-programming}
PMU configuration examples, logic sequences, and implementation checklist.

## Programming Examples

### DRL Auto-Off Logic (Output 14)

```
IF (In6_IgnitionRUN == ON) AND (In7_CT4_Headlights == OFF)
  THEN Out14_DRL = ON
ELSE Out14_DRL = OFF
```

DRL on with ignition, off when headlights active.

### Starter Safety Logic (Output 23)

```
IF (In5_IgnitionSTART == ON) AND (In4_ClutchSwitch == CLOSED)
  THEN Out23_StarterRelay = ON
ELSE Out23_StarterRelay = OFF
```

Starter requires ignition START + clutch depressed.

### A/C Clutch Logic (Output 17)

```
IF (In9_AC_Request == ON) AND (BatteryVoltage > 11.5V)
  THEN Out17_AC_Clutch = ON
ELSE Out17_AC_Clutch = OFF
```

A/C engages when requested and voltage adequate.

### Oil Cooler Fan Control (Output 7) - CAN-based

```
IF (J1939_SPN175_OilTemp > 230°F) THEN Out7_OilFan = ON
ELSEIF (J1939_SPN175_OilTemp < 220°F) THEN Out7_OilFan = OFF
```

10°F hysteresis prevents rapid cycling. Uses J1939 engine oil temperature from ECM (SPN 175).

### PS Cooler Fan Control (Output 8) - CAN-based

```
IF (J1939_SPN110_CoolantTemp > 220°F) THEN Out8_PSFan = ON
ELSEIF (J1939_SPN110_CoolantTemp < 210°F) THEN Out8_PSFan = OFF
```

10°F hysteresis prevents rapid cycling. Uses J1939 coolant temperature from ECM (SPN 110) as proxy for PS fluid temp.

### Sequential Load Startup

```
DELAY Out3_HVAC = 0.5s
DELAY Out7_OilFan = 1.0s
DELAY Out8_PSFan = 1.5s
```

Prevents voltage sag during ignition-on by staggering high-current load activation.

## Configuration Software

**Software:** ECUMaster PMU Configuration Software

**Connection:** USB to PMU (PC configuration)

**Configuration File:** Export and backup PMU configuration file (.pmu format)

**Features:**
- Visual output state monitoring
- Real-time data logging
- Logic programming interface
- CAN bus configuration
- Output combining setup
- Diagnostic LED configuration

## Outstanding Items

### PMU Installation
- [ ] Determine PMU mounting location (firewall vs inner fender)
- [ ] Verify PMU ground to Front Battery- via Pin 25 (10 AWG)

### CAN Bus Integration
- [ ] Tap J1939 CAN bus from Cummins body harness (same tap location as Dakota Digital):
  - CAN High: T-tap → PMU Pin 23 or 24 (18-20 AWG twisted pair stub, <12" length)
  - CAN Low: T-tap → PMU Pin 36 or 37 (18-20 AWG twisted pair stub, <12" length)
- [ ] Verify PMU internal CAN termination is DISABLED (bus already terminated at both ends)
- [ ] Verify 60Ω resistance across CAN High/Low with ignition off (confirms proper termination)
- [ ] Configure PMU to read J1939 data (SPN 100, 110, 175, 190, etc.)
- [ ] Program OUT 7 (oil cooler fan) to trigger based on J1939 SPN 175 (oil temp)
- [ ] Program OUT 8 (PS cooler fan) to trigger based on J1939 SPN 110 (coolant temp)
- [ ] Test J1939 communication and verify data accuracy with all devices connected

### PMU Output Wiring
- [ ] Route ignition switch RUN wire to PMU Pin 7 and In 6 (18 AWG)
- [ ] Split ignition signal to CT4, SwitchPros, Fusion Radio, BCDC (18 AWG branches)
- [ ] Route CT4 SW3 to PMU In 7 (DRL cutoff)
- [ ] Wire radiator fan (GM 84100128) to PMU outputs OUT2+OUT3+OUT4 (3x 25A paralleled for 75A capacity)
- [ ] Configure PMU24 to control radiator fan via ECM PWM signal (or temperature-based logic)
- [ ] Determine radiator fan control strategy (ECM-controlled vs PMU24 temperature sensor)
- [ ] Wire iBooster main power to PMU outputs OUT5+OUT6 (2x 25A paralleled for 50A capacity)
- [ ] Wire iBooster ignition signal to PMU OUT19 (7A output, 5A load)

### PMU Programming
- [ ] Create PMU configuration file with all logic sequences
- [ ] Test sequential load startup timing
- [ ] Export and backup PMU configuration file
- [ ] Verify all outputs operate correctly with programmed logic
- [ ] Test DRL auto-off when headlights activated
- [ ] Test starter safety (clutch + ignition START required)
- [ ] Test A/C clutch engagement logic
- [ ] Test CAN-based fan controls (oil cooler, PS cooler)
- [ ] Verify voltage-based load shedding if implemented

## Related Documentation

- [PMU Overview][# 1.4.1 PMU Overview {#141-pmu-overview}] - Product specifications and capacity
- [PMU Outputs][# 1.4.2 PMU Outputs {#142-pmu-outputs}] - Output configuration and load details
- [PMU Inputs][# 1.4.3 PMU Inputs {#143-pmu-inputs}] - Input configuration and CAN bus integration
- [Front Battery Distribution][# 1.2 Front Battery Distribution (Engine Bay) {#zone-1-front-battery-tray--primary-distribution-engine-bay}] - Power architecture and bus bars
- [Gauge Cluster][# Dakota Digital Gauge Cluster {#dakota-digital-gauge-cluster}] - Dakota Digital J1939 CAN bus tap location
