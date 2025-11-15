# Section 1: Power Systems {#power-systems}
Complete documentation of the dual-battery electrical power generation, storage, and distribution system.

## Contents

- **[1.1 Power Generation & Storage][# 1.1 Power Generation & Storage {#11-power-generation-storage}]** - Dual Odyssey AGM batteries, RedArc BCDC Alpha 50 DC-DC charger, Powermaster alternator, grounding architecture
- **[1.2 Front Battery Distribution][# 1.2 Front Battery Distribution (Engine Bay) {#zone-1-front-battery-tray--primary-distribution-engine-bay}]** - Engine bay battery distribution via Blue Sea 2104/2107 bus bars, CONSTANT/SWITCHED power, high-current circuits
- **[1.3 Rear Battery Distribution][# 1.3 Rear Battery Distribution (Wheel Well) {#13-rear-battery-distribution-wheel-well}]** - Wheel well battery distribution, CONSTANT bus, SwitchPros power, inverter, and winch circuits
- **[1.4 PMU Power Distribution][# 1.4 - PMU Power Distribution {#pmu-power-distribution}]** - ECUMaster PMU24 programmable power management, 24 outputs, engine bay distribution
  - **[1.4.1 PMU Overview][# 1.4.1 PMU Overview {#141-pmu-overview}]** - Product specifications, capacity analysis, features
  - **[1.4.2 PMU Outputs][# 1.4.2 PMU Outputs {#142-pmu-outputs}]** - 24-output configuration, load analysis, combined outputs
  - **[1.4.3 PMU Inputs][# 1.4.3 PMU Inputs {#143-pmu-inputs}]** - Digital/analog inputs, CAN bus integration, ignition distribution
  - **[1.4.4 PMU Programming][# 1.4.4 PMU Programming {#144-pmu-programming}]** - Logic examples, sequential startup, configuration
- **[1.5 Body RTMR][# 1.5 - Body RTMR {#body-rtmr}]** - Cabin power distribution, radio, USB charging, heated seats, camera
- **[1.6 SafetyHub][# 1.6 - SafetyHub 150 {#safetyhub-150}]** - Blue Sea 7748 high-current fuse panel, ARB compressor, winch contactor

## System Overview

The Jeep LJ uses a dual-battery electrical system with intelligent power distribution:

**Power Generation & Storage:**
- **Front Battery (Engine Bay):** Primary power for engine starting, engine bay systems, and critical circuits
- **Rear Battery (Wheel Well):** Auxiliary power for accessories, SwitchPros, inverter, and winch
- **RedArc BCDC Alpha 50:** DC-DC charger/isolator managing charge distribution between batteries
- **Grounding Architecture:** Dual 2/0 AWG grounds from each battery, consolidated grounding points for system stability

**Power Distribution:**
- **PMU24 (1.4):** Engine bay programmable power management - replaces traditional RTMR, 24 intelligent outputs
- **Body RTMR (1.5):** Cabin convenience power distribution - radio, USB, heated seats
- **SafetyHub (1.6):** High-current fuse panel - ARB compressor, winch contactor

Total system capacity: ~136Ah (68Ah per battery)
