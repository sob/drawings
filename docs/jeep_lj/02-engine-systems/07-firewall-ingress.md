---
hide:
  - toc
---

# Firewall Penetrations & Ingress Points {#firewall-penetrations-ingress-points}

Centralized reference for all firewall penetration points and wire routing.

## Overview

**Total Penetrations:** 4 (1 Cummins bulkhead + 3 grommets)

| Penetration | Purpose | Direction | Key Circuits |
|:------------|:--------|:----------|:-------------|
| **Cummins Bulkhead** | Engine harness | Engine ↔ Cabin | ECM, J1939 CAN, accelerator pedal |
| **Grommet 1** | PMU outputs to cabin | Engine → Cabin | Lights, horn, radio power |
| **Grommet 2** | Cabin inputs to PMU | Cabin → Engine | Clutch/brake switches |
| **Grommet 3** | Dakota Digital temp probe | Cabin → Grille | Outside temp sensor |

---

## Cummins R2.8 Bulkhead Connector {#cummins-bulkhead}

**Location:** Per Cummins installation instructions (factory-specified)

**Penetration:** 2" diameter hole with factory bulkhead connector

**Direction:** Engine bay (ECM) ↔ Cabin

### Wire Bundle

Factory Cummins interior harness includes:

| Pin | Function | Notes |
|:----|:---------|:------|
| 35 | Wait to Start lamp | Grid heater active indicator |
| 49 | Red Stop Lamp | Critical warning |
| 36 | Amber Warning Lamp | Caution |
| 22 | MIL/CEL | Malfunction indicator |
| 09 | Tachometer signal | Redundant with J1939 |
| 57/44/56 | Accelerator Pedal Sensor 1 | Supply/signal/return |
| 42/43/55 | Accelerator Pedal Sensor 2 | Supply/signal/return |
| 41 | Keyswitch power input | 5A fused ignition RUN power |

**J1939 CAN Tap:** CAN High/Low wires tap from this harness to Dakota Digital 01-2-J1939 module

**Sealing:** Factory bulkhead connector is self-sealing (no additional grommet needed)

---

## Grommet 1: PMU Outputs to Cabin {#grommet-1}

**Location:** Engine bay side near PMU (exact location determined during installation)

**Direction:** Engine bay → Cabin

### Wire Bundle

| Circuit | PMU Output | Wire Gauge | Notes |
|:--------|:-----------|:-----------|:------|
| Brake lights | OUT21 | 16 AWG | To rear brake lights |
| Reverse lights | OUT22 | 16 AWG | To rear reverse lights |
| Horn trigger return | - | 18 AWG | Ground return from horn button |
| G1 GMRS Radio power | OUT6 | 10 AWG | 15A fused at PMU |
| STX Intercom power | OUT20 | 10 AWG | 5A fused at PMU |
| Ham Radio power | OUT12 | 10 AWG | 25A fused at PMU (future) |

**Estimated wire count:** 6-7 wires (10-18 AWG)

**Grommet size:** 1" ID (with 20% spare capacity)

---

## Grommet 2: Cabin Inputs to PMU {#grommet-2}

**Location:** Cabin side near pedal area (exact location determined during installation)

**Direction:** Cabin → Engine bay

### Wire Bundle

| Circuit | PMU Input | Wire Gauge | Notes |
|:--------|:----------|:-----------|:------|
| Ignition START | - | 16 AWG | To clutch switch (starter interlock input) |
| Clutch safety switch | Digital input | 18 AWG | Starter interlock output to Cole Hersee 24213 |
| Brake light switch | Digital input | 18 AWG | Brake light activation |
| A/C request | Digital input | 18 AWG | A/C clutch enable signal |

**Estimated wire count:** 4-5 wires (16-18 AWG signals)

**Grommet size:** 3/8" ID

---

## Grommet 3: Dakota Digital Temp Probe {#grommet-3}

**Location:** Path from cabin to grille area (exact location determined during installation)

**Direction:** Cabin (HDPE panel) → Engine bay (grille)

### Wire Bundle

| Circuit | Module | Wire Gauge | Notes |
|:--------|:-------|:-----------|:------|
| Outside temp probe | BIM-17-2 | Per sensor | 2-wire thermistor |

**Estimated wire count:** 2 wires (sensor cable)

**Grommet size:** 1/4" ID

---

## Firewall-Mounted Components

### Engine Bay Side

- **PMU24** - Firewall-mounted, powers engine/safety systems
  - Power: START battery via 250A CB
  - Ground: Engine bay ground bus

### Cabin Side

- **Dakota Digital HDPE Panel** - Behind dashboard
  - 01-2-J1939 (J1939 CAN interface)
  - GPS-50-2 (GPS speed module)
  - BIM-22-3 (TPMS module)
  - BIM-17-2 (Compass/outside temp)

- **Firewall Ground Stud** - Central ground for cabin electronics
  - Location: Determined during installation
  - Wire gauge: 10 AWG minimum (accommodates all cabin grounds)

---

## What Does NOT Go Through Firewall

These systems are powered directly from AUX battery in passenger wheel well:

| System | Power Source | Notes |
|:-------|:-------------|:------|
| SwitchPros (all lighting) | CONSTANT bus via 150A CB | Outputs route externally |
| SafetyHub (ARB, winch trigger) | CONSTANT bus via 150A CB | Passenger wheel well |
| BODY PDU (radio, USB, seats, camera) | CONSTANT bus via 100A CB | Under dash, powered from rear |
| BCDC | START battery input, AUX battery output | Both in wheel wells |
| Radio grounds | START battery negative | Cabin along tub side to driver wheel well |

---

## Outstanding Items

None - design complete.

**Resolved:**

- **J1939 CAN tap:** At Cummins bulkhead connector
- **Grommet locations:** Determined during installation (general areas documented above)
- **Firewall ground stud:** Determined during installation

## Related Documentation

- [PMU Outputs][pmu-outputs] - PMU output assignments
- [Gauge Cluster][gauge-cluster] - Dakota Digital modules
- [Wire Routing][wire-routing] - Overall wire routing strategy
- [Grounding Architecture][grounding] - Ground point locations

[pmu-outputs]: ../01-power-systems/04-pmu/03-pmu-outputs.md
[gauge-cluster]: ../04-control-interfaces/04-gauge-cluster/index.md
[wire-routing]: ../01-power-systems/07-wire-routing/index.md
[grounding]: ../01-power-systems/05-grounding/index.md
