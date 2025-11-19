---
hide:
  - toc
---

# 1.7 Wire Routing & Physical Layout {#wire-routing}

## 🔧 Driver Wheel Well (START Battery)

**High-current power distribution from START battery:**

| Circuit | Wire Gauge | Distance | Destination | Current | Notes |
|:--------|:-----------|:---------|:------------|:--------|:------|
| **Alternator charging input** | 2/0 AWG | 8 ft | FROM Alternator (engine) | 270A | Charges START battery - see [Alternator][alternator] |
| **Starter motor power** | 2/0 AWG | 6 ft | TO Starter motor | 400-600A | Brief cranking load - see [Starter][starter] |
| **CONSTANT bus feed** | 2×1/0 AWG | 5 ft | TO CONSTANT bus (firewall) | 356A max | Parallel conductors - see [CONSTANT Bus][constant-bus] |
| **Primary ground** | 2/0 AWG | 8 ft | TO Engine bay ground bus | 600A+ peak | Primary return path |
| **Battery cross-ground** | 1/0 AWG | 5-6 ft | TO AUX battery- (passenger) | BCDC reference | Critical for BCDC operation |

**Routing:** Frame rail along driver side, through wheel well to engine bay and firewall

---

## 🔋 Passenger Wheel Well (AUX Battery)

**Power distribution from AUX battery:**

| Circuit | Wire Gauge | Distance | Destination | Current | Notes |
|:--------|:-----------|:---------|:------------|:--------|:------|
| **Warn Zeon 10-S Winch power** | 1/0 AWG | 13 ft | TO Front bumper winch | 250A typ, 400A peak | Direct connection (no CB) - see [Recovery Systems][recovery-systems] |
| **Warn Zeon 10-S Winch ground** | 1/0 AWG | 13 ft | TO Winch motor ground | 250A typ, 400A peak | Return path via frame rail |
| **SwitchPros outputs** | Various | TBD | TO Engine bay/front | ~100A | Offroad lighting power - routing TBD |
| **Primary ground** | 2/0 AWG | 3 ft | TO Rear frame rail | 569A peak | Winch + accessories return |
| **Cross-ground reference** | 1/0 AWG | 5-6 ft | FROM START battery- (driver) | BCDC reference | Critical for BCDC operation |

**Routing:** Frame rail from passenger wheel well to front bumper (winch), rear to cargo, TBD to engine bay

---

## ⚙️ Engine Bay & CONSTANT Bus

**Engine compartment wiring:**

| Circuit | Wire Gauge | Distance | Source | Destination | Current | Notes |
|:--------|:-----------|:---------|:-------|:------------|:--------|:------|
| **Alternator to battery** | 2/0 AWG | 8 ft | Alternator | START battery+ | 270A | See Driver Wheel Well section |
| **Starter motor** | 2/0 AWG | 6 ft | START battery+ | Starter motor | 400-600A | See Driver Wheel Well section |
| **Engine block ground** | 2/0 AWG | 8 ft | Engine block | Engine bay ground bus | 600A+ peak | Starter/alternator return |
| **Frame ground** | 2/0 AWG | 3 ft | Engine bay ground bus | Front frame rail | 600A+ peak | Chassis ground point |

**CONSTANT Bus Location:** Engine bay firewall (near PMU) - feeds PMU, SafetyHub, BCDC

---

## 🚪 Firewall Penetrations

**Wire bundles passing through firewall:**

| Grommet | Location | Direction | Circuits | Wire Count | Notes |
|:--------|:---------|:----------|:---------|:-----------|:------|
| **Cummins Harness** | TBD | Engine ↔ Cabin | Engine harness, J1939 CAN | Factory | Dedicated punch-through with bulkhead connector |
| **Grommet 1 (Engine RTMR)** | TBD (near PMU) | Engine → Cabin | PMU outputs to cabin loads | TBD | See [Firewall Ingress][firewall-ingress] |
| **Grommet 2 (Body RTMR)** | TBD (near pedals) | Cabin → Engine | Body RTMR to engine circuits | TBD | See [Firewall Ingress][firewall-ingress] |
| **Grommet 5 (Temp Probe)** | TBD | Cabin → Grille | Outside temp sensor (BIM-17-2) | 1 pair | Dakota Digital module |
| **Grommet 6 (RF Power)** | TBD (near battery) | Engine → Cabin | G1 GMRS, STX, Ham Radio | 6× 14 AWG | Direct battery power/ground |

!!! info "J1939 CAN Bus"
    J1939 CAN High/Low wires tap into Cummins harness at firewall punch-through, then route to Dakota Digital 01-2-J1939 module on firewall HDPE panel (cabin side).

**Complete Grommet Details:** See [Firewall Ingress][firewall-ingress] for specifications and circuit lists

---

## 🏠 Cabin & Dashboard

**Interior wiring and controls:**

| Routing Path | Circuits | Method | Notes |
|:-------------|:---------|:-------|:------|
| **Dash → Console** | Switch panels, USB, radio | TBD | Under dash routing |
| **Firewall → Dash** | Dakota Digital cluster, CT4, controls | Behind dash | Main instrument panel area |

**Dakota Digital Firewall Panel (Cabin Side):**

| Component | Function | External Connections |
|:----------|:---------|:--------------------|
| 01-2-J1939 | J1939 CAN interface | CAN High/Low from Cummins harness (engine side) |
| GPS-50-2 | GPS speed sensor | Antenna (dash/windshield mount) |
| BIM-22-3 | TPMS module | Wireless (no external wiring) |
| BIM-17-2 | Compass/outside temp | Temp probe (through firewall to grille) |
| Main harness | BIM/IO cable | Dakota Digital cluster in dash |

**Panel Location:** TBD - firewall behind dashboard
**Mounting:** TBD - HDPE sheet dimensions and fasteners

---

## 📦 Cargo & Rear

**Rear area wiring:**

| Routing Path | Circuits | Method | Notes |
|:-------------|:---------|:-------|:------|
| **Cab → Cargo** | Rear lights, compressor, lockers | TBD | Under seats or floor channels |
| **Passenger wheel well → Cargo** | SwitchPros rear outputs | Via frame rail | Rear auxiliary power |

---

## 🌐 Roof & Exterior

**External and overhead wiring:**

| Routing Path | Circuits | Method | Notes |
|:-------------|:---------|:-------|:------|
| **Roof/Roll bar** | Light bars, dome lights | TBD | A-pillar or along roll bar |
| **Front exterior** | Turn signals, offroad lights | Engine bay to front | SwitchPros outputs |
| **Rear exterior** | Tail/brake/reverse, license plate | Cargo to rear | PMU and SwitchPros outputs |

---

## Ground Points Summary

**Primary grounding locations - see [Section 1.5 - Grounding Architecture][grounding] for complete details:**

| Location | Ground Bus | Wire Gauge | Connections | Notes |
|:---------|:-----------|:-----------|:------------|:------|
| 🔧 **Driver wheel well** | Engine bay ground bus | 2/0 AWG | START battery-, engine block, frame rail, AUX battery | Primary ground hub |
| 🔋 **Passenger wheel well** | Rear frame rail | 2/0 AWG | AUX battery- | AUX battery ground point |
| 🏠 **Firewall (cabin side)** | Firewall stud bus | 4 AWG max | Body electronics, sensors | Cabin electronics ground |
| ⚙️ **Firewall (engine side)** | Engine bay ground bus | Various | PMU, controllers, accessories | Engine bay ground hub |
| 🌐 **SwitchPros controller** | SwitchPros ground bus | 1 AWG | Lighting/aux loads | Dedicated lighting ground |

---

## Related Documentation

- [Grounding Architecture][grounding] - Complete grounding system design
- [START battery Distribution][starter-battery] - Driver wheel well power
- [AUX battery Distribution][aux-battery] - Passenger wheel well power
- [CONSTANT Bus][constant-bus] - Engine bay distribution
- [Alternator][alternator] - Charging system routing
- [Starter][starter] - Starter motor routing
- [Firewall Ingress][firewall-ingress] - Detailed firewall penetrations and grommet specifications
- [Recovery Systems][recovery-systems] - Winch installation and wiring

[grounding]: ../05-grounding/index.md
[starter-battery]: ../02-starter-battery-distribution/index.md
[aux-battery]: ../03-aux-battery-distribution/index.md
[constant-bus]: ../02-starter-battery-distribution/02-constant-bus.md
[alternator]: ../01-power-generation/02-alternator.md
[starter]: ../../02-engine-systems/01-starter.md
[firewall-ingress]: ../../02-engine-systems/07-firewall-ingress.md
[recovery-systems]: ../../07-exterior-systems/01-recovery-systems.md
