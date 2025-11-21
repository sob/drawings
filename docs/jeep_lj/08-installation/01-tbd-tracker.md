---
hide:
  - toc
---

# 8.1 TBD Tracker - Outstanding Items {#tbd-tracker}

**Purpose:** Central tracking for all To-Be-Determined items across the Jeep LJ electrical system documentation.

**Last Updated:** 2025-11-21

**Total Open Items:** 41

---

## 🔴 CRITICAL (Installation Blockers)

Items that prevent build completion or system operation.

| Item | Description | File | Priority |
|:-----|:------------|:-----|:---------|
| **BCDC Temperature Sensor Install** | Document installation location and verify included sensor specs (comes with BCDC) | [BCDC][bcdc] | High |
| **Wire Routing Protection** | Specify split loom, heat sleeve, p-clamps, grommets for all major cables | [Wire Routing][wire-routing] | Critical |
| BCDC Wire Lengths | Actual routing distances for wire sizing | [BCDC][bcdc] | High |

---

## ⚠️ HIGH PRIORITY (Needed for Final Design)

Items needed before installation begins but not system-critical.

| Item | Description | File | Priority |
|:-----|:------------|:-----|:---------|
| **PMU PWM Frequency** | Verify ECUMaster PMU24 PWM frequency compatible with GM Camaro fan motor (100-1000 Hz optimal) | [PMU][pmu-outputs] | High |
| **AUX Battery CONSTANT Bus CB** | Consider adding 200A CB between battery and bus for cable fault protection | [AUX Battery][aux-battery] | High |
| Grommet 1 Location | Engine bay side near PMU | [Firewall Ingress][firewall-ingress] | High |
| Grommet 2 Location | Cabin side near pedal area | [Firewall Ingress][firewall-ingress] | High |
| Grommet 5 Location | Path from firewall to grille area | [Firewall Ingress][firewall-ingress] | High |
| Grommet 6 Location | Near START battery/SafetyHub | [Firewall Ingress][firewall-ingress] | High |
| Firewall Ground Stud Wire | Wire gauge for all cabin grounds | [Firewall Ingress][firewall-ingress] | High |
| Firewall Ground Stud Location | Physical location on firewall | [Firewall Ingress][firewall-ingress] | High |
| Dakota Digital Panel Mounting | HDPE sheet dimensions and location | [Wire Routing][wire-routing] | High |
| SwitchPros Control Panel Location | Dash mount location (4" x 3") | [SwitchPros][switchpros] | High |
| Fusion Amp Mounting | Cargo area or under rear seat | [Audio Systems][audio-systems] | High |
| Fusion Amp Current Draw | Verify 35-45A continuous, 60-70A peak | [Audio Systems][audio-systems] | High |

---

## 📋 MEDIUM PRIORITY (Design Optimization)

Items that improve the design but don't block installation.

| Item | Description | File | Priority |
|:-----|:------------|:-----|:---------|
| Radiator Fan Mounting | Physical location on radiator | [Radiator Fan][radiator-fan] | Medium |
| Firewall Grommet Circuits | Complete wire bundle lists | [Wire Routing][wire-routing] | Medium |
| Passenger Wheel Well Routing | SwitchPros outputs path | [Wire Routing][wire-routing] | Medium |
| Dash to Console Routing | Switch panels, USB, radio | [Wire Routing][wire-routing] | Medium |
| Cab to Cargo Routing | Rear lights, compressor, lockers | [Wire Routing][wire-routing] | Medium |
| Roof/Roll Bar Routing | Light bars, dome lights | [Wire Routing][wire-routing] | Medium |
| 3-Position Selector Switch Assignment | Which SwitchPros output controls | [Dashboard Controls][dash-controls] | Medium |
| Speaker Mounting Locations | Dash end caps or kick panels | [Audio Systems][audio-systems] | Medium |
| CB Radio Mount Location | Under dash or center console | [Communication][communication] | Medium |
| WolfBox Power Source | BODY PDU or SwitchPros | [Communication][communication] | Medium |
| WolfBox Ground | Chassis or dash ground point | [Communication][communication] | Medium |
| WolfBox Mounting | Under dash or on firewall | [Communication][communication] | Medium |
| Horn Relay Specs | Contact rating, coil voltage | [Communication][communication] | Medium |
| Horn Load | Factory Jeep horn amperage (3-6A) | [Communication][communication] | Medium |
| Horn Circuit Protection | Inline fuse/breaker (10A typical) | [Communication][communication] | Medium |
| WolfBox Cable Length | Mirror to rear routing (20-30 ft) | [Communication][communication] | Medium |
| Turn Signal Mounting | Front fenders or bumper | [Turn Signals][turn-signals] | Medium |
| Winch 3-Position Switch Assignment | Which SwitchPros output controls | [Recovery Systems][recovery-systems] | Medium |

---

## 📝 LOW PRIORITY (Optional/Aesthetic)

Items that can be determined during build.

| Item | Description | File | Priority |
|:-----|:------------|:-----|:---------|
| Wiper Controller Mounting | Under dash or near wiper motor | [Wiper System][wiper-system] | Low |
| Horn Button Type | Momentary or latching | [Dashboard Controls][dash-controls] | Low |
| Speaker IPX Rating | Verify from spec sheet | [Audio Systems][audio-systems] | Low |
| WolfBox Display Size | 9.66" or 12" model | [Communication][communication] | Low |
| WolfBox License Plate Integration | With existing license plate lights | [Communication][communication] | Low |
| Rear Seat Switch | Parallel wiring for passenger control | [Offroad Lighting][offroad-lighting] | Low |
| Cargo Area Lighting Type | LED bar or pod lights | [Offroad Lighting][offroad-lighting] | Low |
| Cargo Area Light Quantity | Based on coverage needed | [Offroad Lighting][offroad-lighting] | Low |
| RGB Controller | For rock light color/pattern selection | [Offroad Lighting][offroad-lighting] | Low |
| Recovery Board Storage | MaxTrax storage location | [Recovery Systems][recovery-systems] | Low |
| Hi-Lift Jack Mount | Hood, bumper, or rear swing-out | [Recovery Systems][recovery-systems] | Low |

---

## 🔍 VERIFICATION NEEDED

Items that are estimated and need actual product specs to confirm.

| Item | Description | File | Action Needed |
|:-----|:------------|:-----|:--------------|
| **Grid Heater Current** | Design value 80A - verify via element resistance measurement during installation (~0.15Ω @ 12V) | [Grid Heater][grid-heater] | Measure resistance |
| Heated Seat Load | Verify PRP EnduroTrek 15A/seat spec | [BODY PDU][body-rtmr] | Verify spec sheet |
| Fusion Amp Current | Verify 35-45A continuous rating | [Audio Systems][audio-systems] | Verify spec sheet |

---

## ✅ RECENTLY RESOLVED

Items completed since last update.

| Item | Resolution | Date |
|:-----|:-----------|:-----|
| SafetyHub Location | Consolidated to single SafetyHub 150 on AUX battery (ARB compressor, winch trigger); communications moved to PMU | 2025-11-21 |
| Radiator Fan Distance | 6 ft estimated (firewall to radiator), 4 AWG wire sizing confirmed (3.2% drop @ 53A full speed) | 2025-11-21 |
| Radiator Fan Load | GM Camaro fan 53A @ 100% PWM (variable speed: 16A @ 30%, 32A @ 60%, 53A @ 100%) | 2025-11-21 |
| Radiator Fan Protection | PMU OUT2+3+4 has integrated overcurrent/thermal protection, no external CB needed | 2025-11-21 |
| PMU iBooster Thermal | Resolved via non-adjacent combining: OUT1+10 (46A @ 40°C) vs OUT5+6 adjacent (32A @ 40°C) | 2025-11-21 |
| Grid Heater Current | Design value 80A (moved to Verification for field measurement) | 2025-11-21 |
| BCDC Temperature Sensor | Included with BCDC unit (2-pin reversible, moved to High Priority for install documentation) | 2025-11-21 |
| BODY PDU Model | Bussmann LR-2 (301-1C-C-R1) | 2025-11-18 |
| BODY PDU Ground | Firewall Stud Bus Terminal 3 (14 AWG) | 2025-11-18 |
| Alternator Part Number | Premier Power Welder HO-C28 | 2025-11-18 |

---

!!! info "Maintenance Instructions"
    For instructions on updating this tracker, priority definitions, and review schedules, see [Section 8 CLAUDE.md](CLAUDE.md).

---

## Summary by Priority

| Priority | Count |
|:---------|:------|
| 🔴 Critical | 1 |
| ⚠️ High | 12 |
| 📋 Medium | 18 |
| 📝 Low | 11 |
| 🔍 Verify | 3 |
| **TOTAL** | **41** |

## Related Documentation

- [Section 1 Installation Checklist][section-1-install] - Power systems installation guide
- [Section 1.7 Wire Routing][wire-routing] - Wire routing organized by location

[bcdc]: ../01-power-systems/01-power-generation/03-bcdc.md
[radiator-fan]: ../02-engine-systems/06-radiator-fan/index.md
[wiper-system]: ../02-engine-systems/04-wipers.md
[firewall-ingress]: ../02-engine-systems/07-firewall-ingress.md
[wire-routing]: ../01-power-systems/07-wire-routing/index.md
[switchpros]: ../04-control-interfaces/02-switchpros-sp1200.md
[dash-controls]: ../04-control-interfaces/05-dashboard-controls.md
[audio-systems]: ../05-audio-systems/01-audio.md
[communication]: ../06-communication-systems/01-communication.md
[turn-signals]: ../03-lighting-systems/03-turn-signals.md
[offroad-lighting]: ../03-lighting-systems/06-offroad-lighting.md
[recovery-systems]: ../07-exterior-systems/01-recovery-systems.md
[body-rtmr]: ../01-power-systems/03-aux-battery-distribution/04-body-pdu.md
[section-1-install]: ../01-power-systems/installation-checklist.md
[pmu-outputs]: ../01-power-systems/04-pmu/03-pmu-outputs.md
[grid-heater]: ../02-engine-systems/08-grid-heater.md
[aux-battery]: ../01-power-systems/03-aux-battery-distribution/index.md
