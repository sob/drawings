---
hide:
  - toc
tags:
  - wire-routing
  - firewall
---

# 1.7.2 Firewall Ingress {#firewall-ingress}

All firewall penetration points for wire routing between engine bay and cabin.

## Cummins Bulkhead Connector

**Size:** 2" diameter hole with factory bulkhead connector (self-sealing)

**Contents:** Factory Cummins interior harness - ECM signals, accelerator pedal, warning lamps, J1939 CAN tap to Dakota Digital

---

## Deutsch HDP20 Bulkhead Connector

Single weatherproof bulkhead connector for all custom wiring through firewall.

### Connector Specification

| Component | Part Number | Description |
|:----------|:------------|:------------|
| **Receptacle** | HDP24-24-21PE-L015 | 21-pin bulkhead receptacle, flange mount (engine side) |
| **Plug** | HDP26-24-21SE | 21-pin plug (cabin side) |

**Insert Arrangement 24-21:** 4× size 12 + 17× size 16 contacts

- Size 12 contacts: 12-14 AWG, 25A (4 available, 0 used - reserved for future)
- Size 16 contacts: 14-20 AWG, 13A (17 available, 17 used)

**Mounting:** Single 1.5" diameter hole in firewall

**Sealing:** IP67/IP68, bayonet quick-connect coupling

### Why Single Connector

RF interference analysis determined that with ferrite chokes on radio power leads at the radio end, all circuits can share one connector safely. The temp probe routes separately to grille (not through main connector).

---

## Pin Assignment

### Engine Bay → Cabin (6 wires)

| Pin | Circuit | Gauge | Source | Destination | Contact |
|:---:|:--------|:-----:|:-------|:------------|:-------:|
| 1 | GMRS Radio power (+) | 14 AWG | PMU OUT6 | Midland G1 | #16 |
| 2 | Ham Radio power (+) | 14 AWG | PMU OUT12 | iCom IC-2730A | #16 |
| 3 | STX Intercom power | 14 AWG | PMU OUT20 | STX intercom | #16 |
| 4 | Brake lights | 16 AWG | PMU OUT21 | Rear tail lights | #16 |
| 5 | Reverse lights | 16 AWG | PMU OUT22 | Rear tail lights | #16 |
| 6 | DRL/Parking | 16 AWG | PMU OUT23 | Rear tail lights | #16 |

### Cabin → Engine Bay (11 wires)

| Pin | Circuit | Gauge | Source | Destination | Contact |
|:---:|:--------|:-----:|:-------|:------------|:-------:|
| 7 | Right turn signal | 14 AWG | CT4 SW1 | Right fender + rear | #16 |
| 8 | Left turn signal | 14 AWG | CT4 SW2 | Left fender + rear | #16 |
| 9 | Low beam headlights | 14 AWG | CT4 SW3 | LP6 Pin 1 (both) | #16 |
| 10 | High beam headlights | 14 AWG | CT4 SW4 | LP6 Pin 4 (both) | #16 |
| 11 | Horn button trigger | 18 AWG | Steering wheel button | PMU In 1 | #16 |
| 12 | Ignition sense | 18 AWG | Ignition switch RUN | PMU Pin 7 | #16 |
| 13 | Brake switch | 18 AWG | Brake pedal switch | PMU In 2 | #16 |
| 14 | A/C request | 18 AWG | HVAC controls | PMU In 9 | #16 |
| 15 | Clutch switch | 18 AWG | Clutch pedal switch | Starter circuit | #16 |
| 16 | Winch control IN | 18 AWG | Dash rocker switch | Winch contactor | #16 |
| 17 | Winch control OUT | 18 AWG | Dash rocker switch | Winch contactor | #16 |

### Reserved (4 pins)

| Pin | Contact | Notes |
|:---:|:-------:|:------|
| A-D | #12 | Size 12 cavities reserved for future 10-12 AWG circuits |

---

## Separate Routing (Not Through Main Connector)

### Cabin → Grille (Small Grommet)

| Circuit | Gauge | Source | Destination | Notes |
|:--------|:-----:|:-------|:------------|:------|
| Outside temp probe (+) | 22 AWG | BIM-17-2 | SEN-15-1 (grille) | Twisted pair |
| Outside temp probe (-) | 22 AWG | BIM-17-2 | SEN-15-1 (grille) | Twisted pair |

**Routing:** Separate small grommet near grille area - keeps analog sensor isolated from power circuits.

### Radio Grounds (Floor/Frame Routing)

Radio grounds do NOT go through firewall - they route through cab floor to START battery:

| Circuit | Gauge | Source | Destination |
|:--------|:-----:|:-------|:------------|
| GMRS Radio ground (-) | 14 AWG | Midland G1 | START battery negative |
| Ham Radio ground (-) | 14 AWG | iCom IC-2730A | START battery negative |
| STX Intercom ground (-) | 14 AWG | STX | START battery negative |

**Routing:** Radios (cabin) → under seat/floor → frame rail → START battery negative (driver wheel well)

---

## Wire Count Summary

| Gauge | Count | Circuits |
|:------|:-----:|:---------|
| 14 AWG | 7 | Radio power (3), CT4 outputs (4) |
| 16 AWG | 3 | PMU lighting outputs |
| 18 AWG | 7 | Switch signals (5), winch control (2) |
| **Main Connector** | **17** | HDP24-24-21 |
| 22 AWG | 2 | Temp probe (separate grommet) |

---

## Connector Bill of Materials

| Part Number | Description | Qty | ~Price |
|:------------|:------------|:---:|:------:|
| HDP24-24-21PE-L015 | 21-pin receptacle, flange mount | 1 | $35 |
| HDP26-24-21SE | 21-pin plug | 1 | $25 |
| 0460-202-16141 | Size 16 pin, solid, nickel | 17 | $0.50 ea |
| 0462-201-16141 | Size 16 socket, solid, nickel | 17 | $0.55 ea |
| 114017 | Sealing plug, size 12 cavity | 4 | $0.25 ea |
| 114018 | Sealing plug, size 16 cavity | 4 | $0.25 ea |

**Estimated Total:** ~$80

**Crimping Tool:** HDT-48-00 (size 12-20 solid contacts)

---

## DRL Auto-Off Signal

**Note:** The DRL cutoff signal does NOT require a separate wire through the firewall. The CT4 SW3 (low beam) wire is tapped on the engine bay side after it passes through the connector:

```text
CT4 SW3 (cabin) → Pin 9 → [ENGINE BAY TAP to PMU In 7] → LP6 headlights
```

PMU In 7 receives the headlight status signal from this tap, enabling DRL auto-off logic.

---

## Related Documentation

- [Wire Routing Overview][wire-routing] - Complete routing by location
- [PMU Outputs][pmu-outputs] - PMU output assignments
- [PMU Inputs][pmu-inputs] - PMU input assignments
- [Command Touch CT4][ct4] - CT4 controller and outputs
- [Dashboard Controls][dash-controls] - Winch rocker switch wiring
- [GMRS Radio][gmrs] - Radio power and ground routing
- [Intercom][intercom] - STX power routing

[wire-routing]: index.md
[pmu-outputs]: ../04-pmu/03-pmu-outputs.md
[pmu-inputs]: ../04-pmu/02-pmu-inputs.md
[ct4]: ../../05-control-interfaces/03-command-touch-ct4.md
[dash-controls]: ../../05-control-interfaces/05-dashboard-controls.md
[gmrs]: ../../07-communication-systems/01-gmrs-radio.md
[intercom]: ../../07-communication-systems/02-intercom.md
