# 1.4 - PMU Power Distribution {#pmu-power-distribution}
Engine bay power distribution is handled by the ECUMaster PMU24, a programmable power management unit replacing traditional relay/fuse panels.

## System Architecture

**PMU24 replaces:**
- Traditional relay/fuse panel
- DRL relay
- Horn relay
- Fan controllers
- TIPM (Totally Integrated Power Module) functions

**Power source:** Front Battery CONSTANT bus (all outputs powered from CONSTANT)

**Ground:** Front battery negative bus via PMU Pin 25 (10 AWG)

**Control:** Programmable logic via PC software, ignition-aware outputs, CAN bus integration

## Why PMU24 Instead of RTMR

**Advantages over traditional relay/timer modules:**
- Single integrated unit vs scattered relays
- Programmable logic (complex conditional triggers)
- Built-in overcurrent protection per output
- Data logging (256MB memory, up to 500 Hz)
- CAN bus integration for engine data
- Diagnostic LED indicators for all outputs
- Eliminates wiring complexity of individual relays

**Engine RTMR eliminated:** PMU provides all engine bay power distribution with superior diagnostics and flexibility.

## System Components

### Direct Battery Connections (Bypass PMU)

Critical systems with direct Front Battery+ connections:
1. **Cummins ECM Power** - Direct to Front Battery+
2. **Grid Heater Fusible Link** - Direct to Front Battery+ (40-80A) - See [Grid Heater][# 2.9 Grid Heater System {#29-grid-heater-system}]
3. **Starter Main Solenoid** - Direct to Front Battery+ via 2/0 AWG - See [Starter System][# Starter System - Cummins R2.8 {#starter-system-cummins-r28}]

### PMU24 Subsections

- **[1.4.1 - Overview][# 1.4.1 PMU Overview {#141-pmu-overview}]** - Product specifications, capacity analysis, features, mounting
- **[1.4.2 - Outputs][# 1.4.2 PMU Outputs {#142-pmu-outputs}]** - 24-output configuration, load analysis, combined outputs
- **[1.4.3 - Inputs][# 1.4.3 PMU Inputs {#143-pmu-inputs}]** - Digital/analog inputs, CAN bus integration, ignition distribution
- **[1.4.4 - Programming][# 1.4.4 PMU Programming {#144-pmu-programming}]** - Logic examples, sequential startup, configuration, outstanding items

## Related Documentation

**Engine Bay Subsystems:**
- [HVAC System][# HVAC System {#hvac-system}] - Blower motor and A/C compressor clutch (PMU Out 1, Out 17)
- [Wiper System][# Windshield Wiper Control System {#windshield-wiper-control-system}] - Ron Francis WS-51C controller (PMU Out 11)
- [Radiator Fan][# Radiator Fan System {#radiator-fan-system}] - GM 84100128 Camaro radiator fan (PMU Out 2+3+4 combined, 30-60A)
- [Starter System][# Starter System - Cummins R2.8 {#starter-system-cummins-r28}] - Two-stage starter system (PMU Out 23)
- [Horn][# Horn {#horn}] - PIAA horn specifications (PMU Out 18)
- [Brake Booster][# Brake Booster System - Bosch iBooster Gen 2 {#brake-booster-system-bosch-ibooster-gen-2}] - Bosch iBooster Gen 2 (PMU Out 5+6, Out 19)

**Control Interfaces:**
- [Command Touch CT4][# Command Touch CT4 {#command-touch-ct4}] - Steering column controller (PMU Out 13)
- [Gauge Cluster][# Dakota Digital Gauge Cluster {#dakota-digital-gauge-cluster}] - Dakota Digital J1939 integration

**Power Distribution:**
- [Front Battery Distribution][# 1.2 Front Battery Distribution (Engine Bay) {#zone-1-front-battery-tray--primary-distribution-engine-bay}] - SWITCHED/CONSTANT bus bars
- [Firewall Ingress][# Firewall Penetrations & Ingress Points {#firewall-penetrations-ingress-points}] - Firewall penetrations and wire routing
