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
- **[START battery Distribution](01-power-systems/02-starter-battery-distribution/index.md)** - Engine bay primary power distribution
- **[AUX battery Distribution](01-power-systems/03-aux-battery-distribution/index.md)** - Wheel well accessory power distribution
- **[Power Management Unit](01-power-systems/04-pmu/index.md)** - PMU24 programmable power management
- **[BODY PDU](01-power-systems/03-aux-battery-distribution/03-body-pdu.md)** - Body relay/fuse panel
- **[SafetyHub](01-power-systems/03-aux-battery-distribution/04-safetyhub.md)** - Safety control system

### Critical Systems

- **[Starter System](02-engine-systems/01-starter.md)** - Engine starting system
- **[Brake Booster](02-engine-systems/02-brake-booster.md)** - Vacuum brake booster
- **[HVAC System](02-engine-systems/03-hvac.md)** - Heating, ventilation, and air conditioning
- **[Wiper System](02-engine-systems/04-wipers.md)** - Windshield wipers
- **[Horn System](02-engine-systems/05-horn.md)** - Vehicle horn
- **[Radiator Fan](02-engine-systems/06-radiator-fan.md)** - Engine cooling fan
- **[Grid Heater](02-engine-systems/07-grid-heater.md)** - Diesel grid heater

### Lighting Systems

- **[Lighting Overview](03-lighting-systems/01-lighting-overview.md)** - Complete lighting system overview
- **[Headlights](03-lighting-systems/02-headlights.md)** - Main headlights
- **[Turn Signals](03-lighting-systems/03-turn-signals.md)** - Turn signal system
- **[Tail, Brake & Reverse](03-lighting-systems/04-tail-brake-reverse.md)** - Rear lighting
- **[DRL & Parking Lights](03-lighting-systems/05-drl-parking.md)** - Daytime running and parking lights
- **[Offroad & Aux Lighting](04-offroad-lighting/index.md)** - Auxiliary and offroad lighting

### Control Interfaces

- **[Overview](05-control-interfaces/01-overview.md)** - Control systems overview
- **[SwitchPros SP-1200](05-control-interfaces/02-switchpros-sp1200.md)** - SwitchPros lighting controller
- **[Command Touch CT4](05-control-interfaces/03-command-touch-ct4.md)** - Command Touch control panel
- **[Digital Gauge Cluster](02-engine-systems/09-gauge-cluster/index.md)** - Dakota Digital gauge cluster
- **[Dashboard Switches](05-control-interfaces/05-dashboard-controls.md)** - Physical dashboard controls

### Stereo Systems

- **[Audio Systems](06-audio-systems/index.md)** - Fusion head unit, Apollo amplifier, JL Audio speakers and subwoofer

### Communications

- **[Communication Systems](07-communication-systems/index.md)** - GMRS radio, intercom, dash camera

### Auxiliary Systems

- **[Winch](08-exterior-systems/01-winch.md)** - Warn Zeon 10-S winch (10,000 lb)
- **[Air Compressor](08-exterior-systems/02-air-compressor.md)** - ARB Twin Compressor and tank
- **[Air Lockers](08-exterior-systems/03-air-lockers.md)** - ARB RD116 front/rear lockers
- **[Rear Air Chuck](08-exterior-systems/04-rear-air-chuck.md)** - External air access

### Install Notes

- **[Wire Routing & Layout][wire-routing]** - Physical wire routing, grommets, grounds

[wire-routing]: 01-power-systems/07-wire-routing/index.md

</div>

## Key Features

### Dual Battery System

- **START battery:** Engine bay - powers critical engine systems via PMU and SafetyHub
- **AUX battery:** Wheel well - powers accessories via CONSTANT bus
- **Battery Isolation:** RedArc BCDC Alpha 50 DC-DC charger with automatic jump-start assist

See [Power Generation](01-power-systems/01-power-generation/index.md) for complete battery and charging system details.

### TIPM Replacement

Complete replacement of factory TIPM with modular power distribution:

- **[PMU24](01-power-systems/04-pmu/index.md):** Programmable 24-channel power management unit
- **[BODY PDU](01-power-systems/03-aux-battery-distribution/03-body-pdu.md):** Body relay/fuse panel for cabin accessories
- **[SafetyHub](01-power-systems/03-aux-battery-distribution/04-safetyhub.md):** 12-channel advanced safety controller
- **[Ron Francis WS-51C](02-engine-systems/04-wipers.md):** Wiper control system

### Major Systems

- **[Lighting Control](05-control-interfaces/02-switchpros-sp1200.md):** SwitchPros SP-1200 for offroad and auxiliary lighting
- **[Command Touch CT4](05-control-interfaces/03-command-touch-ct4.md):** Street-legal lighting and turn signal control
- **[Audio System](06-audio-systems/index.md):** Fusion Apollo 6-channel amp, JL Audio marine speakers with RGB LED
- **[Communication](07-communication-systems/index.md):** Rugged Radio G1 GMRS, STX 4-place intercom, WolfBox dash camera
- **[Recovery & Air](08-exterior-systems/index.md):** Warn 10,000 lb winch, ARB air lockers, ARB Twin Air Compressor

## Documentation Notes

!!! info "Outstanding Items"
Throughout this documentation, you'll find "Outstanding Items" checklists. These track design decisions, measurements, and tasks that need to be completed during installation.

    **[View Global TBD Tracker](09-installation/01-tbd-tracker.md)** - Centralized tracking of all To-Be-Determined items with priorities

!!! warning "Work in Progress"
This is a living document that evolves as the build progresses. Some specifications may be marked as TBD (To Be Determined) and will be updated during the build process.
