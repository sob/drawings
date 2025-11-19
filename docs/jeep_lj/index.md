---
hide:
  - toc
---

# Jeep LJ Cummins R2.8 Build - Electrical Documentation {#jeep-lj-cummins-r28-build-electrical-documentation}

## Project Overview

This documentation covers the complete electrical system design for a 2006 Jeep LJ (Wrangler Unlimited) with a Cummins R2.8 Turbo Diesel engine swap. The build features a comprehensive electrical redesign including dual battery architecture, TIPM replacement, and extensive custom electronics.

<div class="mobile-nav-only" markdown="1">

## System Architecture

The electrical system is organized into zones for logical distribution and maintenance:

### Power Systems

- **[Power Generation](01-power-systems/01-power-generation/index.md)** - Batteries, alternator, BCDC, solar, grounding
- **[Starter Battery Distribution](01-power-systems/02-starter-battery-distribution/index.md)** - Engine bay primary power distribution
- **[Aux Battery Distribution](01-power-systems/03-aux-battery-distribution/index.md)** - Wheel well accessory power distribution
- **[Power Management Unit](01-power-systems/04-pmu/index.md)** - PMU24 programmable power management
- **[Body RTMR](01-power-systems/03-aux-battery-distribution/04-body-rtmr.md)** - Body relay/fuse panel
- **[SafetyHub](01-power-systems/02-starter-battery-distribution/04-safetyhub.md)** - Safety control system

### Critical Systems

- **[Starter System](02-engine-systems/01-starter.md)** - Engine starting system
- **[Brake Booster](02-engine-systems/02-brake-booster.md)** - Vacuum brake booster
- **[HVAC System](02-engine-systems/03-hvac.md)** - Heating, ventilation, and air conditioning
- **[Wiper System](02-engine-systems/04-wipers.md)** - Windshield wipers
- **[Horn System](02-engine-systems/05-horn.md)** - Vehicle horn
- **[Radiator Fan](02-engine-systems/06-radiator-fan.md)** - Engine cooling fan
- **[Firewall Ingress](02-engine-systems/07-firewall-ingress.md)** - Firewall wire pass-through
- **[Grid Heater](02-engine-systems/08-grid-heater.md)** - Diesel grid heater

### Lighting Systems

- **[Lighting Overview](03-lighting-systems/01-lighting-overview.md)** - Complete lighting system overview
- **[Headlights](03-lighting-systems/02-headlights.md)** - Main headlights
- **[Turn Signals](03-lighting-systems/03-turn-signals.md)** - Turn signal system
- **[Tail, Brake & Reverse](03-lighting-systems/04-tail-brake-reverse.md)** - Rear lighting
- **[DRL & Parking Lights](03-lighting-systems/05-drl-parking.md)** - Daytime running and parking lights
- **[Offroad & Aux Lighting](03-lighting-systems/06-offroad-lighting.md)** - Auxiliary and offroad lighting

### Control Interfaces

- **[Overview](04-control-interfaces/01-overview.md)** - Control systems overview
- **[SwitchPros SP-1200](04-control-interfaces/02-switchpros-sp1200.md)** - SwitchPros lighting controller
- **[Command Touch CT4](04-control-interfaces/03-command-touch-ct4.md)** - Command Touch control panel
- **[Digital Gauge Cluster](04-control-interfaces/04-gauge-cluster.md)** - Dakota Digital gauge cluster
- **[Dashboard Switches](04-control-interfaces/05-dashboard-controls.md)** - Physical dashboard controls

### Stereo Systems

- **[Audio Systems](05-audio-systems/01-audio.md)** - Fusion head unit, Apollo amplifier, JL Audio speakers and subwoofer

### Communications

- **[Communication Systems](06-communication-systems/01-communication.md)** - GMRS radio, intercom, Command Touch CT4, WolfBox camera

### Auxiliary Systems

- **[Recovery Systems](07-exterior-systems/01-recovery-systems.md)** - Warn Zeon 10-S winch and recovery equipment
- **[Air System](07-exterior-systems/02-air-system.md)** - ARB Twin Compressor and air lockers

### Install Notes

- **[Wire Routing & Layout][wire-routing]** - Physical wire routing, grommets, grounds

[wire-routing]: 01-power-systems/07-wire-routing/index.md

</div>

## Key Features

### Dual Battery System

- **Starter Battery:** Engine bay - powers critical engine systems via PMU and SafetyHub
- **Aux Battery:** Wheel well - powers accessories via CONSTANT bus
- **Battery Isolation:** RedArc BCDC Alpha 25 DC-DC charger with automatic jump-start assist

See [Power Generation](01-power-systems/01-power-generation/index.md) for complete battery and charging system details.

### TIPM Replacement

Complete replacement of factory TIPM with modular power distribution:

- **[PMU24](01-power-systems/04-pmu/index.md):** Programmable 24-channel power management unit
- **[Body RTMR](01-power-systems/03-aux-battery-distribution/04-body-rtmr.md):** Body relay/fuse panel for cabin accessories
- **[SafetyHub](01-power-systems/02-starter-battery-distribution/04-safetyhub.md):** 12-channel advanced safety controller
- **[Ron Francis WS-51C](02-engine-systems/04-wipers.md):** Wiper control system

### Major Systems

- **[Lighting Control](04-control-interfaces/02-switchpros-sp1200.md):** SwitchPros SP-1200 for offroad and auxiliary lighting
- **[Command Touch CT4](04-control-interfaces/03-command-touch-ct4.md):** Street-legal lighting and turn signal control
- **[Audio System](05-audio-systems/01-audio.md):** Fusion Apollo 6-channel amp, JL Audio marine speakers with RGB LED
- **[Communication](06-communication-systems/01-communication.md):** Rugged Radio G1 GMRS, STX 4-place intercom, Fusion MS-RA670 head unit
- **[Recovery & Air](07-exterior-systems/01-recovery-systems.md):** Warn 10,000 lb winch, ARB air lockers, ARB Twin Air Compressor

## Documentation Notes

!!! info "Outstanding Items"
    Throughout this documentation, you'll find "Outstanding Items" checklists. These track design decisions, measurements, and tasks that need to be completed during installation.

    **[View Global TBD Tracker](08-installation/01-tbd-tracker.md)** - Centralized tracking of all To-Be-Determined items with priorities

!!! warning "Work in Progress"
    This is a living document that evolves as the build progresses. Some specifications may be marked as TBD (To Be Determined) and will be updated during the build process.
