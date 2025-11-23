---
hide:
  - toc
tags:
  - wire-routing
  - firewall
---

# 1.7.2 Firewall Ingress {#firewall-ingress}

All firewall penetration points for wire routing between engine bay and cabin.

## Summary

| Penetration | Size | Direction | Circuits |
|:------------|:-----|:----------|:---------|
| Cummins Bulkhead | 2" dia | Engine ↔ Cabin | ECM harness, J1939 CAN, accelerator pedal |
| Grommet 1 | 1" ID | Engine → Cabin | PMU outputs (lights, radio power) |
| Grommet 2 | 3/8" ID | Cabin → Engine | PMU inputs (switches, ignition sense) |
| Grommet 3 | 1/4" ID | Cabin → Grille | Dakota Digital outside temp probe |

---

## Cummins Bulkhead Connector

**Size:** 2" diameter hole with factory bulkhead connector (self-sealing)

**Contents:** Factory Cummins interior harness - ECM signals, accelerator pedal, warning lamps, J1939 CAN tap to Dakota Digital

---

## Grommet 1: PMU Outputs to Cabin

**Size:** 1" ID grommet (20% spare capacity)

| Circuit | PMU | Gauge |
|:--------|:----|:------|
| Brake lights | OUT21 | 16 AWG |
| Reverse lights | OUT22 | 16 AWG |
| GMRS Radio power | OUT6 | 10 AWG |
| Ham Radio power | OUT12 | 10 AWG |
| STX Intercom power | OUT20 | 14 AWG |
| Horn trigger return | - | 18 AWG |

---

## Grommet 2: Cabin Inputs to PMU

**Size:** 3/8" ID grommet

| Circuit | PMU | Gauge |
|:--------|:----|:------|
| Ignition sense | Pin 7 | 18 AWG |
| Brake switch | In 2 | 18 AWG |
| A/C request | In 9 | 18 AWG |
| Clutch switch output | - | 18 AWG |

---

## Grommet 3: Temp Probe

**Size:** 1/4" ID grommet

**Contents:** Dakota Digital BIM-17-2 outside temperature sensor (2-wire)

---

## Outstanding Items

None - design complete. See [installation checklist][install-checklist] for build tasks.

## Related Documentation

- [Wire Routing Overview][wire-routing] - Complete routing by location
- [PMU Outputs][pmu-outputs] - PMU output assignments
- [PMU Inputs][pmu-inputs] - PMU input assignments

[install-checklist]: ../../02-engine-systems/installation-checklist.md
[wire-routing]: index.md
[pmu-outputs]: ../04-pmu/03-pmu-outputs.md
[pmu-inputs]: ../04-pmu/02-pmu-inputs.md
