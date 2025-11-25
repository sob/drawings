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

## Firewall Grommet - All Custom Wiring

Complete list of wires passing through firewall grommet(s). Grommet size TBD based on final wire count.

### Engine Bay → Cabin

| Circuit             | Source     | Gauge  | Destination           |
| :------------------ | :--------- | :----- | :-------------------- |
| Brake lights        | PMU OUT21  | 16 AWG | Rear tail lights      |
| Reverse lights      | PMU OUT22  | 16 AWG | Rear tail lights      |
| DRL/Parking         | PMU OUT23  | 16 AWG | Rear tail lights      |
| GMRS Radio power    | PMU OUT6   | 10 AWG | Midland G1            |
| Ham Radio power     | PMU OUT12  | 10 AWG | iCom IC-2730A         |
| STX Intercom power  | PMU OUT20  | 14 AWG | STX intercom          |
| Horn trigger return | Horn       | 18 AWG | Steering wheel button |

### Cabin → Engine Bay

| Circuit              | Source              | Gauge  | Destination                    |
| :------------------- | :------------------ | :----- | :----------------------------- |
| Ignition sense       | Ignition switch RUN | 18 AWG | PMU Pin 7                      |
| Brake switch         | Brake pedal switch  | 18 AWG | PMU In 2                       |
| A/C request          | HVAC controls       | 18 AWG | PMU In 9                       |
| Clutch switch        | Clutch pedal switch | 18 AWG | Starter circuit                |
| Right turn signal    | CT4 SW1             | 14 AWG | Right fender + rear tail light |
| Left turn signal     | CT4 SW2             | 14 AWG | Left fender + rear tail light  |
| Low beam headlights  | CT4 SW3             | 14 AWG | LP6 Pin 1 (both lights)        |
| High beam headlights | CT4 SW4             | 14 AWG | LP6 Pin 4 (both lights)        |
| DRL cutoff signal    | CT4 SW3 tap         | 18 AWG | PMU In 7 (DRL auto-off logic)  |

### Cabin → Grille

| Circuit            | Source         | Gauge       | Destination              |
| :----------------- | :------------- | :---------- | :----------------------- |
| Outside temp probe | Dakota Digital | 2-wire, 22 AWG | BIM-17-2 sensor (grille) |

---

## Wire Count Summary

| Gauge  | Count | Notes                              |
| :----- | :---- | :--------------------------------- |
| 10 AWG | 2     | Radio power (GMRS, Ham)            |
| 14 AWG | 5     | CT4 outputs, STX power             |
| 16 AWG | 3     | PMU lighting outputs               |
| 18 AWG | 6     | Signal wires (switches, triggers)  |
| 22 AWG | 2     | Temp probe                         |
| **Total** | **18** |                                 |

---

## Outstanding Items

- [ ] Determine grommet size based on wire bundle diameter
- [ ] Determine if RF-sensitive wires (radio power) need separate grommet

## Related Documentation

- [Wire Routing Overview][wire-routing] - Complete routing by location
- [PMU Outputs][pmu-outputs] - PMU output assignments
- [PMU Inputs][pmu-inputs] - PMU input assignments
- [Command Touch CT4][ct4] - CT4 controller and outputs

[install-checklist]: ../../02-engine-systems/installation-checklist.md
[wire-routing]: index.md
[pmu-outputs]: ../04-pmu/03-pmu-outputs.md
[pmu-inputs]: ../04-pmu/02-pmu-inputs.md
[ct4]: ../../05-control-interfaces/03-command-touch-ct4.md
