---
hide:
  - toc
---

# Section 5: Control Interfaces {#control-interfaces}

Driver control interfaces: switches, controllers, and input devices for vehicle system control.

## Contents

- **[5.1 Overview][control-interfaces-overview]** - Control interface system architecture and integration
- **[5.2 SwitchPros SP-1200][switchpros-sp-1200-rcr-force-12]** - Main auxiliary lighting controller, 12-button panel, 17 outputs, Bluetooth app
- **[5.3 Command Touch CT4][command-touch-ct4]** - Steering column turn signal and headlight controller with GPS auto-cancel
- **[Dakota Digital Gauge Cluster][dakota-digital-gauge-cluster]** - Digital gauge cluster with J1939 CAN integration, GPS speedometer, TPMS (see Section 2.9)
- **[5.4 Dashboard Controls][dashboard-physical-controls]** - Physical dash-mounted switches (winch control, rear seat switch)

## System Overview

**Primary Controllers:**

- **SwitchPros SP-1200:** Auxiliary lighting and accessories (AUX battery CONSTANT bus, 150A capacity)
- **Command Touch CT4:** Turn signals and headlights (START battery, PMU integration)
- **Dakota Digital:** Gauge cluster with J1939 engine data (PMU Out 14, 15A)

**Physical Controls:**

- **Dashboard switches:** Winch 3-position switch, other dash controls
- **Rear seat switch:** Dome light control for rear passengers

[control-interfaces-overview]: 01-overview.md
[switchpros-sp-1200-rcr-force-12]: 02-switchpros-sp1200.md
[command-touch-ct4]: 03-command-touch-ct4.md
[dakota-digital-gauge-cluster]: ../02-engine-systems/09-gauge-cluster/index.md
[dashboard-physical-controls]: 05-dashboard-controls.md
