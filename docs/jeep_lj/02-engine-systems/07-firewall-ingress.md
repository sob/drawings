---
hide:
  - toc
---

# Firewall Penetrations & Ingress Points {#firewall-penetrations-ingress-points}
Centralized reference for all firewall penetration points, wire routing, and grommet specifications.

## Overview

All electrical penetrations through the firewall must be properly sized and sealed to prevent water ingress.

## Firewall Penetration Map

### Grommet 1: PMU to Cabin Circuits

**Location:** TBD - engine bay side near PMU
**Direction:** Engine bay → Cabin

**Wire Bundle:**

- Tail/brake light circuit (PMU Out 17) - 14-16 AWG
- Reverse light circuit (PMU Out 18) - 14-16 AWG
- Horn button signal wire (steering wheel → PMU In 1) - 18 AWG
- A/C request signal wire (factory TJ A/C button → PMU In 9) - 18 AWG
- Other TBD circuits from PMU to cabin

**Note:** Rear defrost is not implemented.

**Outstanding Items:**

- [ ] Determine exact Grommet 1 location on firewall
- [ ] Complete wire bundle list for Grommet 1 (verify all PMU cabin connections)
- [ ] Determine grommet size based on wire count and gauges

### Grommet 2: Cabin to Engine Bay Circuits

**Location:** TBD - cabin side near pedal area
**Direction:** Cabin → Engine bay

**Wire Bundle:**

- Clutch safety switch wire (clutch pedal → PMU digital input)
- Brake light switch wire (brake pedal → PMU digital input)
- Other TBD circuits from cabin to PMU

**Outstanding Items:**

- [ ] Determine exact Grommet 2 location on firewall (near pedal area preferred for clutch/brake switches)
- [ ] Complete wire bundle list for Grommet 2
- [ ] Determine grommet size based on wire count and gauges

**Related Documentation:**

- [Engine Systems][pmu-power-distribution] - Clutch and brake switch wiring

### Grommet 3: Reserved

**Status:** No longer required - BODY PDU receives CONSTANT power directly from AUX battery via circuit breaker in wheel well

**Note:** BODY PDU circuits (WolfBox camera, heated seats, USB, radio) are now on CONSTANT power with manual/trigger control. No firewall penetration needed for BODY PDU power feed.
- **Note:** Radio amplifier (15A, F3) on CONSTANT power (remote wire from deck triggers amp)

**Outstanding Items:**

- [ ] Grommet 3 no longer required (BODY PDU powered from AUX battery)

**Related Documentation:**

- [BODY PDU][body-rtmr] - BODY PDU specifications and circuit breakdown

### Grommet 4: Critical Cabin PDU Power Feed {#grommet-4-critical-cabin-pdu}

**Location:** TBD - near CONSTANT bus (engine bay side)
**Direction:** Engine bay (CONSTANT bus) → Cabin (Critical Cabin PDU)

**Wire Bundle:**

- Critical Cabin PDU power feed: CONSTANT bus → 40A CB → Critical Cabin PDU - 6 AWG

**Wire Specifications:**

- **Power Wire:** 6 AWG (<10A typical load, 40A CB protected)
- **Distance:** ~8 ft (engine bay to cabin firewall area)
- **Load:** Dakota Digital modules + PAC-2800BT controller (<10A combined)

**Configuration:**

- **Power Source:** CONSTANT bus via 40A circuit breaker
- **Destination:** Blue Sea 5025 Critical Cabin PDU (cabin side firewall)
- **Load:** Powers Dakota Digital instrumentation and critical cabin electronics

**Outstanding Items:**

- [ ] Determine exact Grommet 4 location on firewall
- [ ] Determine grommet size for 6 AWG wire
- [ ] Verify voltage drop calculation for Critical Cabin PDU feed

**Related Documentation:**

- [Critical Cabin PDU][cabin-pdu] - Blue Sea 5025 specifications and circuit assignments
- [CONSTANT Bus][constant-bus] - Power source

### Grommet 5: PAC-2800BT Radiator Fan Relay Trigger {#grommet-5-pac-2800bt-relay-trigger}

**Location:** TBD - near Dakota Digital HDPE panel (cabin side)
**Direction:** Cabin (PAC-2800BT controller) → Engine bay (external relay)

**Wire Bundle:**

- Relay trigger wire: PAC-2800BT output → External relay Terminal 85 (ground-trigger) - 18 AWG

**Wire Specifications:**

- **Trigger Wire:** 18 AWG (low current, ground-trigger signal)
- **Distance:** ~8 ft (cabin to engine bay relay location)
- **Signal:** Ground-trigger from PAC-2800BT when coolant temp exceeds setpoint

**Configuration:**

- **Controller:** PAC-2800BT (cabin-mounted on Dakota Digital HDPE panel)
- **External Relay:** Bosch-style relay (engine bay, near fan)
- **Operation:** Controller triggers ground to relay coil → relay closes → fan runs

**Outstanding Items:**

- [ ] Determine exact Grommet 5 location on firewall
- [ ] Determine grommet size for 18 AWG wire
- [ ] Determine relay mounting location in engine bay

**Related Documentation:**

- [Radiator Fan System][radiator-fan] - Complete fan controller documentation
- [Fan Controller][fan-controller] - Dakota Digital PAC-2800BT specifications

### Grommet 6: Dakota Digital Outside Temperature Probe {#grommet-6-dakota-digital-outside-temperature-probe}

**Location:** TBD - path from firewall cabin side to grille area
**Direction:** Cabin (HDPE panel) → Engine bay (grille area)

**Wire Bundle:**

- Outside temperature probe wire (BIM-17-2 module on HDPE panel → grille temp sensor)

**Outstanding Items:**

- [ ] Determine exact Grommet 6 location on firewall
- [ ] Determine exact grille area mounting location for temperature probe
- [ ] Determine wire gauge and length for temperature probe cable
- [ ] Determine grommet size

**Related Documentation:**

- [Gauge Cluster][dakota-digital-gauge-cluster] - Dakota Digital BIM-17-2 compass/temp module

### Grommet 7: Communication Devices (G1 GMRS, STX Intercom, Ham Radio) {#grommet-7-communication-devices}

**Location:** TBD - near START battery/SafetyHub location
**Direction:** Engine bay (SafetyHub/battery) → Cabin (radios behind dash)

**Wire Bundle:**

- G1 GMRS power: Battery+ → SafetyHub 15A fuse → G1 radio (14 AWG)
- G1 GMRS ground: G1 radio → Battery- direct (14 AWG)
- STX Intercom power: Battery+ → SafetyHub 5A fuse → STX intercom (14 AWG)
- STX Intercom ground: STX intercom → Battery- direct (14 AWG)
- Ham Radio power (future): Battery+ → SafetyHub 25A fuse → Ham radio (10 AWG)
- Ham Radio ground (future): Ham radio → Battery- direct (10 AWG)

**Wire Specifications:**

- G1/STX power: 14 AWG (adequate for 15A and 5A respectively)
- G1/STX ground: 14 AWG (direct to Battery-)
- Ham Radio power: 10 AWG (20-25A transmit current)
- Ham Radio ground: 10 AWG (heavier for transmit current)
- Grommet must accommodate up to 6 wires (3 power + 3 ground when ham installed)

**Power Distribution Architecture:**

- **Positive feeds:** SafetyHub fused outputs (centralized fusing)
- **Ground returns:** Direct to Battery- (prevents ground loop noise)
- **Why this works:** Ground loop prevention depends on ground path, not positive path
- SafetyHub provides cleaner organization than scattered inline fuses

**Outstanding Items:**

- [ ] Determine exact Grommet 7 location on firewall (near SafetyHub/battery preferred)
- [ ] Confirm wire gauge: 14 AWG for G1/STX, 10 AWG for Ham Radio
- [ ] Determine grommet size (must accommodate 6 wires: 3 power + 3 ground)
- [ ] Determine SafetyHub mounting location (near START battery)

**Related Documentation:**

- [Communication & Camera][communication-systems] - G1 GMRS radio and STX intercom specifications

### Cummins R2.8 Interior Harness Bulkhead Connector {#cummins-r28-harness-punch-through}

**Location:** Per Cummins installation instructions
**Direction:** Engine bay (ECM) → Cabin
**Penetration:** 2" diameter hole with bulkhead connector

**Wire Bundle:**

- Complete Cummins interior harness (factory-provided with bulkhead connector)
- J1939 CAN High/Low wires (tapped from this harness for Dakota Digital)
- Dashboard indicator wires (Wait to Start, MIL/CEL, warning lamps)
- Accelerator pedal position sensor wires (dual redundant sensors)
- Keyswitch power input (Pin 41 - requires 5A fused ignition RUN power)

**Key Harness Pins:**

- **Pin 35:** Wait to Start lamp (grid heater active indicator)
- **Pin 49:** Red Stop Lamp (critical warning)
- **Pin 36:** Amber Warning Lamp (caution)
- **Pin 22:** Malfunction Indicator Lamp (MIL/CEL)
- **Pin 09:** Tachometer signal (may be redundant with J1939)
- **Pin 40:** Tachograph (not used in this build)
- **Pins 57/44/56:** Accelerator Pedal Sensor 1 (supply/signal/return)
- **Pins 42/43/55:** Accelerator Pedal Sensor 2 (supply/signal/return)
- **Pin 41:** Keyswitch power input (5A fused ignition RUN power required)

**Installation Specifications:**

- **Hole Size:** 2" diameter
- **Hardware:** Bulkhead connector (provided with Cummins interior harness)
- **Sealing:** Factory bulkhead connector provides weatherproof seal
- **No additional grommet needed** - bulkhead connector is self-sealing

**Notes:**

- J1939 CAN bus wires for Dakota Digital tap from this harness at bulkhead location
- Pin 41 (Keyswitch) requires connection to ignition RUN power with 5A inline fuse
- Both accelerator pedal sensors (S1 and S2) must be connected for ECM to accept throttle input

**Outstanding Items:**

- [ ] Confirm 2" hole location on firewall per Cummins installation instructions
- [ ] Confirm J1939 CAN High/Low tap location at bulkhead connector (engine bay or cabin side)
- [ ] Determine wire gauge and routing for J1939 wires from bulkhead to 01-2-J1939 module on HDPE panel
- [ ] Wire Pin 41 (Keyswitch) to ignition RUN power with 5A inline fuse
- [ ] Determine if Wait to Start lamp (Pin 35) will connect to dashboard indicator

**Related Documentation:**

- [Engine Systems][pmu-power-distribution] - ECM and J1939 CAN bus specifications
- [Gauge Cluster][dakota-digital-gauge-cluster] - Dakota Digital J1939 interface module

## Firewall-Mounted Components

### Engine Bay Side (Exterior)

- **PMU:** Firewall-mounted programmable power distribution unit for engine circuits
  - Power source: START battery CONSTANT bus (SWITCHED logic via Pin 7 ignition sense)
  - Ground: START battery negative bus via pin 25 - 10 AWG
  - See [Engine Systems][pmu-power-distribution] for complete specifications

### Cabin Side (Interior)

- **Dakota Digital Module Panel (HDPE Sheet):**
  - Location: Firewall behind dashboard
  - Components mounted:
    - 01-2-J1939 (J1939 interface module)
    - GPS-50-2 (GPS speed module)
    - BIM-22-3 (TPMS module)
    - BIM-17-2 (Compass/outside temp module)
  - See [Gauge Cluster][dakota-digital-gauge-cluster] for complete specifications

- **Firewall Ground Stud:**
  - Purpose: Central ground point for cabin electronics and Dakota Digital cluster
  - Wire gauge: TBD - must accommodate all cabin ground connections
  - Location: TBD

## Installation Best Practices

### Planning Phase

- Document all wire runs before drilling
- Group wires by function and direction (engine→cabin vs cabin→engine)
- Size grommets with 20% spare capacity
- Minimize penetration points by bundling related circuits

### Installation Phase

- Use proper firewall grommets with rubber sealing
- Route wires with service loops on both sides for maintenance access
- Label all wires before passing through firewall
- Protect wires from abrasion at grommet entry points

### Testing Phase

- Water test all penetrations after installation
- Verify no wire chafing or stress at grommet entry points
- Test all circuits for proper connectivity
- Check ground connections for continuity and low resistance

## Outstanding Items Summary

### Grommet Locations

- [ ] Determine exact location for Grommet 1 (PMU to cabin)
- [ ] Determine exact location for Grommet 2 (Cabin to engine bay - near pedals)
- [ ] Determine exact location for Grommet 4 (Critical Cabin PDU power feed)
- [ ] Determine exact location for Grommet 5 (PAC-2800BT relay trigger)
- [ ] Determine exact location for Grommet 6 (Dakota Digital temp probe)
- [ ] Determine exact location for Grommet 7 (G1/STX/Ham battery cables - near battery)

### Wire Bundles

- [ ] Complete wire bundle list for Grommet 1 (PMU cabin circuits)
- [ ] Complete wire bundle list for Grommet 2 (clutch, brake, ignition signals)
- [ ] Verify wire gauge for Grommet 4 (Critical Cabin PDU: 6 AWG)
- [ ] Verify wire gauge for Grommet 5 (PAC-2800BT relay trigger: 18 AWG)
- [ ] Determine wire gauge for Grommet 6 (temp probe)
- [ ] Confirm wire gauge for Grommet 7: 14 AWG for G1/STX, 10 AWG for Ham Radio

### Grommet Sizing

- [ ] Determine grommet size for Grommet 1 (multiple signal wires + power circuits)
- [ ] Determine grommet size for Grommet 2 (clutch, brake, ignition signals)
- [ ] Determine grommet size for Grommet 4 (6 AWG power wire)
- [ ] Determine grommet size for Grommet 5 (18 AWG trigger wire)
- [ ] Determine grommet size for Grommet 6 (temp probe)
- [ ] Determine grommet size for Grommet 7 (must accommodate 6 wires: 3 power + 3 ground)

### J1939 CAN Bus

- [ ] Confirm J1939 CAN High/Low tap location at Cummins harness punch-through
- [ ] Determine wire gauge and routing for J1939 wires from Cummins punch-through to 01-2-J1939 module

### Ground Points

- [ ] Determine firewall ground stud location (cabin side)
- [ ] Determine firewall ground stud wire gauge capacity

## Related Documentation

- [Engine Systems][pmu-power-distribution] - PMU power distribution and clutch/brake switches
- [Gauge Cluster][dakota-digital-gauge-cluster] - Dakota Digital modules and HDPE panel
- [Communication & Camera][communication-systems] - G1 GMRS and STX intercom battery wiring
- [Wire Routing & Layout][wire-routing] - Overall wire routing strategy

[wire-routing]: ../01-power-systems/07-wire-routing/index.md
[radiator-fan]: 06-radiator-fan/index.md
[fan-controller]: 06-radiator-fan/02-fan-controller.md
[cabin-pdu]: ../01-power-systems/02-starter-battery-distribution/03-critical-cabin-pdu.md
[constant-bus]: ../01-power-systems/02-starter-battery-distribution/02-constant-bus.md
