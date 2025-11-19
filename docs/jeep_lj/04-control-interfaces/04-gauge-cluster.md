---
hide:
  - toc
tags:
  - product-details
  - control-interface
  - gauge-cluster
  - digital-dash
---

# Dakota Digital Gauge Cluster {#dakota-digital-gauge-cluster}

/// html | div.product-info

**Model:** Dakota Digital 1996-03 TJ Style Gauge Cluster

**Power Source:** PMU Out 14 (15A, auto-on with ignition RUN)

**Ground:** Firewall ground stud

///

## System Overview

The Dakota Digital custom dash replaces the factory gauge cluster with a modern digital display system. It integrates with the Cummins R2.8 ECM via J1939 CAN bus to display engine data, and uses GPS for speedometer functionality.

## System Components

### Main Cluster

- **Model:** Dakota Digital 1996-03 (TJ style gauge cluster)
- **Power:** PMU Out 14 (15A, auto-on with ignition RUN)
- **Ground:** Firewall ground stud
- **Display:** Digital/analog hybrid display with customizable gauges
- **Functions:** Speedometer, tachometer, fuel level, coolant temp, oil pressure, voltmeter, odometer, trip meter
- **Critical System:** Speedometer required for legal vehicle operation

### J1939 Interface Module (01-2-J1939)

- **Function:** Connects to Cummins R2.8 ECM via J1939 CAN bus
- **Provides:** Tachometer, oil pressure, coolant temperature, fuel level, check engine light (CEL/MIL)
- **Wiring:** CAN High, CAN Low from ECM
- **Power:** Via BIM/IO cable from main cluster
- **Mounting:** HDPE panel on firewall behind dashboard

### GPS Speed Module (GPS-50-2)

- **Function:** Provides speedometer data via GPS
- **GPS Antenna:** Mounted for clear sky view (dash top or near windshield)
- **Benefits:**
  - Eliminates need for transmission speed sensor
  - Accurate speed regardless of gear ratios or tire size
  - Works with any transmission/transfer case combination
- **Power:** Via BIM/IO cable from main cluster
- **Mounting:** HDPE panel on firewall behind dashboard

### TPMS Module (BIM-22-3)

- **Function:** Tire Pressure Monitoring System
- **Sensors:** 4x wireless sensors (one per wheel)
- **Communication:** Wireless - no wiring to sensors required
- **Power:** Via BIM/IO cable from main cluster
- **Mounting:** HDPE panel on firewall behind dashboard

### Compass/Outside Temp Module (BIM-17-2)

- **Function:** Digital compass with outside temperature sensor
- **Temperature Probe:** Mounted in grille area
- **Power:** Via BIM/IO cable from main cluster
- **Mounting:** HDPE panel on firewall behind dashboard

## Physical Installation

### Module Panel (HDPE Sheet)

All 4 BIM modules are mounted to a single HDPE sheet on the firewall behind the dashboard:

- 01-2-J1939 (J1939 interface)
- GPS-50-2 (GPS speed module)
- BIM-22-3 (TPMS module)
- BIM-17-2 (Compass/outside temp module)

**Benefits:**
- Single consolidated mounting location for easy service access
- Clean cable management from modules to main cluster
- All modules receive power via BIM/IO cable harness (no separate power wiring needed)

### Sensor/Antenna Mounting

- **GPS Antenna:** Dash top or windshield mount (clear sky view)
  - Cable from GPS-50-2 module (on firewall HDPE panel) to antenna
- **Outside Temperature Probe:** Grille area
  - Cable from BIM-17-2 module (on firewall HDPE panel) to grille probe
- **TPMS Sensors:** 4x wireless sensors (one per wheel)
  - No wiring required - communicate wirelessly with BIM-22-3 module

## Power Distribution

- **Main Power:** PMU Out 14 (15A, auto-on with ignition RUN) → Dakota Digital main cluster
  - Auto-energized when ignition in RUN position (via PMU Pin 7/In 6)
  - Critical system: speedometer required for legal vehicle operation
  - Overcurrent protection via PMU
- **Module Power:** All BIM modules (J1939, GPS, TPMS, Compass/Temp) powered via BIM/IO cables from main cluster
  - No separate power wiring needed for individual modules
  - Modules receive power through interconnecting BIM/IO cable harness
- **Ground:** Firewall ground stud

## Data Flow

- Cummins R2.8 ECM → J1939 CAN bus (CAN High/CAN Low) → 01-2-J1939 module → Main Cluster
- GPS-50-2 module → Main Cluster (speedometer data)
- BIM-22-3 TPMS module → Main Cluster (tire pressure data)
- BIM-17-2 Compass/Temp → Main Cluster (compass heading and outside temperature)

## Wiring Summary

1. **Main Power:** PMU Out 14 → Dakota Digital 1996-03 main cluster (15A, auto-on with ignition RUN)
   - All BIM modules powered via BIM/IO cables from main cluster
   - Wire gauge: 14 AWG from PMU Out 14 to cluster power input
2. **Ground:** Cluster ground → firewall ground stud (14 AWG)
3. **Module Interconnect:** Single BIM/IO cable harness from main cluster → firewall HDPE panel → all 4 BIM modules
4. **J1939 CAN Bus:** Pickup from Cummins harness punch-through (engine bay) → J1939 CAN High/Low wires → 01-2-J1939 module (on HDPE panel)
   - Cummins wiring harness has its own firewall penetration
   - Tap into J1939 CAN High/Low at punch-through location
5. **GPS Antenna Cable:** GPS-50-2 module (on HDPE panel) → GPS antenna (dash/windshield)
6. **Temperature Probe Cable:** BIM-17-2 module (on HDPE panel) → through firewall (Grommet 3) → outside temp probe (grille area)
   - See [Firewall Ingress][firewall-penetrations-ingress-points] for penetration details

## J1939 CAN Bus Integration

The Cummins R2.8 ECM provides engine data via J1939 CAN bus:

- **Protocol:** J1939 (common for medium/heavy duty diesel engines)
- **Signals Provided:**
  - RPM (tachometer)
  - Oil pressure
  - Coolant temperature
  - Fuel level
  - Check Engine Light (CEL/MIL) status
  - Other engine parameters
- **Wiring:** CAN High and CAN Low from ECM
- **Tap Location:** Cummins harness firewall punch-through
- **Firewall Penetration:** See [Firewall Ingress][firewall-penetrations-ingress-points] for J1939 tap details

## Outstanding Items

- [ ] Verify 15A PMU output capacity is sufficient for entire Dakota Digital cluster system (main cluster + 4 BIM modules: 01-2-J1939, GPS-50-2, BIM-22-3, BIM-17-2)
- [ ] Route 14 AWG power wire from PMU Out 14 (engine bay) through firewall to Dakota Digital cluster (behind dash)
- [ ] Determine if transfer case position sensors (2WD/4WD/4LO indicators) are available via J1939 or need discrete wiring to Dakota Digital
- [ ] Determine exact GPS antenna mounting location (dash top vs windshield mount)
- [ ] Determine exact outside temperature probe mounting location in grille area
- [ ] Confirm TPMS sensor compatibility with wheel/tire setup (4x wireless sensors)
- [ ] Determine exact HDPE panel dimensions and mounting points on firewall
- [ ] Plan exact cable routing for BIM/IO harness from dash cluster to firewall HDPE panel
- [ ] Determine cable routing for GPS antenna cable from HDPE panel to dash/windshield
- [ ] Confirm J1939 CAN High/Low tap location at Cummins harness punch-through
- [ ] Determine wire gauge and routing for J1939 wires from Cummins punch-through to 01-2-J1939 module on HDPE panel

**Firewall Penetrations:**

See [Firewall Ingress][firewall-penetrations-ingress-points] for complete firewall penetration planning including:
- Grommet 3: Outside temperature probe routing from HDPE panel to grille area
- Cummins punch-through: J1939 CAN High/Low tap location and routing

## Related Documentation

- [PMU Power Distribution][pmu-power-distribution] - PMU Out 14 power specifications and ignition control
- [Engine Systems][pmu-power-distribution] - ECM J1939 CAN bus specifications
- [Body RTMR][body-rtmr] - Body RTMR cabin convenience circuits
- [Control Interfaces Overview][control-interfaces-overview] - All control interfaces
