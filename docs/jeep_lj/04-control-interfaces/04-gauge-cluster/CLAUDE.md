# Dakota Digital HDX Gauge System - Navigation Guide

## What's Here

Complete Dakota Digital HDX instrumentation system with HDX control module, dashboard cluster, and 4 BIM expansion modules.

## Files

### `index.md` - System Overview

**Contains:** System architecture, power distribution, component list

**Use when:** Understanding overall Dakota Digital system or finding power/wiring summary

### `01-hdx-control.md` - HDX Control Module

**Contains:** Main control box specifications, BIM connectivity, Bluetooth configuration

**Use when:** Finding control box details, BIM daisy-chain architecture, or configuration procedures

### `02-dashboard-cluster.md` - Dashboard Cluster

**Contains:** HDX-96J-TJ gauge display specs, analog gauges, digital message centers

**Use when:** Finding gauge ranges, display features, or dashboard installation details

### `03-bim-j1939.md` - J1939 CAN Interface

**Contains:** BIM-01-2-J1939 specifications, Cummins R2.8 ECM integration, J1939 parameters

**Use when:** Understanding J1939 CAN bus integration or ECM data availability

### `04-bim-gps.md` - GPS Speed/Compass Module

**Contains:** GPS-50-2 specifications, GPS speedometer benefits, antenna mounting

**Use when:** Understanding GPS-based speedometer or antenna placement requirements

### `05-bim-tpms.md` - Tire Pressure Monitoring

**Contains:** BIM-22-3 specifications, wireless sensor installation, TPMS display

**Use when:** Finding TPMS sensor details or tire pressure monitoring features

### `06-bim-compass.md` - Compass/Temperature Module

**Contains:** BIM-17-2 specifications, outside temperature sensor, compass functionality

**Use when:** Finding compass/temp details or temperature probe mounting

## Cross-Section References

**To Power Systems (1):**

- Critical Cabin PDU Slot 2: Power source (10A fuse)
- Firewall ground stud: Ground connection

**To Engine Systems (2):**

- Cummins R2.8 ECM: J1939 CAN bus data source (via BIM-01-2)
- Firewall Grommet 6: Temperature probe routing

**To Control Interfaces (4):**

- Part of overall control interface system

## Navigation Scenarios

**"What powers the Dakota Digital system?"** → `index.md` power distribution table

**"How do I configure the HDX system?"** → `01-hdx-control.md` Bluetooth app section

**"What gauges are in the dashboard?"** → `02-dashboard-cluster.md` analog gauges table

**"What J1939 data is available from the Cummins ECM?"** → `03-bim-j1939.md` J1939 data section

**"Where do I mount the GPS antenna?"** → `04-bim-gps.md` GPS antenna section

**"How do I install TPMS sensors?"** → `05-bim-tpms.md` sensor installation section

**"Where do I mount the outside temperature probe?"** → `06-bim-compass.md` temperature sensor section

## When Updating

**Adding BIM module:**

1. Create new product page (07-bim-xxx.md)
2. Update `index.md` system architecture and power table
3. Update `01-hdx-control.md` BIM daisy-chain diagram
4. Update mkdocs.yml navigation

**Changing power source:**

1. Update `index.md` power distribution table
2. Update Critical Cabin PDU circuit assignment
3. Update CONSTANT bus load table (if applicable)

**Updating current draw:**

1. Measure actual current draw during installation
2. Update `index.md` power distribution table
3. Update Critical Cabin PDU total load
4. Verify 10A fuse capacity

## Current Draw Status

**Confirmed from HDX Manual:**

- **Fuse Requirement:** 5-20A max (per manufacturer specification)
- **Installed Fuse:** 10A (middle of recommended range)
- **Expected Draw:** <10A for entire system (HDX control + cluster + 4 BIM modules)

**Status:** ✅ Fuse rating confirmed - 10A is within manufacturer's 5-20A spec

## Outstanding Work

See individual product pages for detailed outstanding items. Key items:

- Measure or obtain actual current draw specifications
- Finalize HDPE panel layout and mounting for all modules
- Determine GPS antenna mounting location
- Plan J1939 CAN tap location at Cummins punch-through
- Mount outside temperature probe in grille area
- Install TPMS sensors (requires tire dismount)
