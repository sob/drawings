# Control Interfaces - Overview {#control-interfaces-overview}
This section documents all control interfaces in the Jeep LJ build - the switches, controllers, and input devices that allow the driver to control various vehicle systems.

## System Controllers

- **[SwitchPros SP-1200][switchpros-sp-1200-rcr-force-12]** - Main lighting and accessory controller
  - 12-button control panel with Bluetooth app
  - 17 total outputs (12 main + 5 low-side drivers)
  - 150A total capacity on CONSTANT bus
  - Controls all auxiliary lighting and accessories

- **[Command Touch CT4][command-touch-ct4]** - Steering column turn signal and headlight controller
  - 4 programmable outputs for turn signals and headlights
  - GPS module for intelligent turn signal auto-cancel
  - Replaces factory multifunction stalk
  - Controls turn signals, headlights, and high beams

## Physical Switches

- **[Dashboard Controls][dashboard-physical-controls]** - Physical dash-mounted switches
  - Winch control switch
  - Other dash-mounted controls

## System Integration

All control interfaces integrate with the dual-battery electrical system:

- **SwitchPros SP-1200:** Powered by CONSTANT bus (rear battery)
- **Command Touch CT4:** Powered by front battery CONSTANT, integrates with PMU
- **Dashboard switches:** Various power sources depending on function

## Related Documentation

- **[Vehicle Lighting][vehicle-lighting-overview]** - Complete vehicle lighting circuits controlled by these interfaces
- **[Offroad Lighting][offroad-auxiliary-lighting]** - Auxiliary and offroad lighting controlled by SwitchPros
- **[Engine Systems][pmu-power-distribution]** - PMU power distribution and engine bay subsystems
- **[Horn][horn]** - PIAA horn system (engine bay component)
- **[Wipers][windshield-wiper-control-system]** - Ron Francis WS-51C wiper controller (engine bay component)
