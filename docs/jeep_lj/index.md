# Jeep LJ Cummins R2.8 Build - Electrical Documentation {#jeep-lj-cummins-r28-build-electrical-documentation}
## Project Overview

This documentation covers the complete electrical system design for a 2006 Jeep LJ (Wrangler Unlimited) with a Cummins R2.8 Turbo Diesel engine swap. The build features a comprehensive electrical redesign including dual battery architecture, TIPM replacement, and extensive custom electronics.

## System Architecture

The electrical system is organized into zones for logical distribution and maintenance:

### Power Systems

- **[Power Generation & Storage][11-power-generation-storage]** - Alternators, batteries, charging systems
- **[Front Battery Distribution][zone-1-front-battery-tray--primary-distribution-engine-bay]** - Engine bay primary power distribution
- **[Rear Battery Distribution][13-rear-battery-distribution-wheel-well]** - Wheel well accessory power distribution

### Engine Systems

- **[Critical Engine Systems][pmu-power-distribution]** - PMU, Body RTMR, HVAC, wipers, cooling fans
- **[Auxiliary Engine Systems][auxiliary-systems]** - Dakota Digital gauges, cameras, sensors

### Control Interfaces

- **[Control Interfaces][control-interfaces-overview]** - SwitchPros, Command Touch CT4, physical switches, gauge cluster

### Lighting Systems

- **[Lighting][vehicle-lighting-overview]** - All vehicle lighting (front, roof, interior, rear, specialty)

### Audio Systems

- **[Audio & Stereo][audio-systems]** - Fusion head unit, Apollo amplifier, JL Audio speakers and subwoofer

### Communication Systems

- **[Communication & Camera][communication-systems]** - GMRS radio, intercom, Command Touch CT4, WolfBox camera

### Exterior Systems

- **[Recovery Systems][recovery-systems]** - Warn Zeon 10-S winch and recovery equipment
- **[Air System][air-system-arb-compressor-lockers]** - ARB Twin Compressor and air lockers

### Installation

- **[Wire Routing & Layout][wire-routing-physical-layout]** - Physical wire routing, grommets, grounds

## Key Features

### Dual Battery System

- **Front Battery:** Engine bay - powers critical engine systems via SWITCHED bus
- **Rear Battery:** Wheel well - powers accessories via CONSTANT bus
- **Battery Isolation:** RedArch BCDC Alpha 50 DC-DC charger with automatic jump-start assist

### TIPM Replacement

Complete replacement of factory TIPM with modular RTMRs (Relay/Fuse Panels):

- **Engine RTMR:** Critical engine systems (SWITCHED power)
- **Body RTMR:** Cabin accessories (CONSTANT power)
- **Ron Francis WS-51C:** Wiper control system

### Major Systems

- **Lighting Control:** SwitchPros SP-9100 (8-channel intelligent control)
- **Safety Systems:** SafetyHub 12 (12-channel advanced safety controller)
- **Audio System:** Fusion Apollo 6-channel amp, JL Audio marine speakers with RGB LED
- **Communication:** Rugged Radio G1 GMRS, STX 4-place intercom, Fusion MS-RA670 head unit
- **Recovery:** Warn 10,000 lb winch, ARB air lockers, ARB Twin Air Compressor

## Documentation Notes

!!! info "Outstanding Items"
    Throughout this documentation, you'll find "Outstanding Items" checklists. These track design decisions, measurements, and tasks that need to be completed during installation.

!!! warning "Work in Progress"
    This is a living document that evolves as the build progresses. Some specifications may be marked as TBD (To Be Determined) and will be updated during the build process.

## Quick Reference

| System | Power Source | Controller | Fuse/Breaker |
|--------|-------------|-----------|--------------|
| Engine critical | SWITCHED bus | Engine RTMR | Various |
| Body accessories | CONSTANT bus | Body RTMR | Various |
| Lighting | CONSTANT bus | SwitchPros SP-9100 | 10A each |
| Safety systems | CONSTANT bus | SafetyHub 12 | 10A each |
| Stereo amplifier | CONSTANT bus | Direct battery | 40-50A breaker |
| Rugged Radio G1/STX | Front battery | Direct battery | 15A/3-5A inline |
| Compressor | CONSTANT bus | SafetyHub MIDI | 60A each motor |
| Winch | Front battery | Dedicated contactor | 175A breaker |

## Navigation

Use the navigation menu on the left to explore each system in detail. Each section includes:

- System overview and architecture
- Component specifications
- Wiring diagrams and power flow
- Outstanding items and checklists
- Installation notes and best practices
