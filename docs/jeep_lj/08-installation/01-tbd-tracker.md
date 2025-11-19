---
hide:
  - toc
---

# 8.1 TBD Tracker - Outstanding Items {#tbd-tracker}

**Purpose:** Central tracking for all To-Be-Determined items across the Jeep LJ electrical system documentation.

**Last Updated:** 2025-11-19

**Total Open Items:** 40

---

## 🔴 CRITICAL (Installation Blockers)

Items that prevent build completion or system operation.

| Item | Description | File | Priority |
|:-----|:------------|:-----|:---------|
| BCDC Wire Lengths | Actual routing distances for wire sizing | [BCDC][bcdc] | High |
| Radiator Fan Load | Actual amperage (20-40A range) | [Radiator Fan][radiator-fan] | High |
| Radiator Fan Protection | CB/fuse size based on fan specs | [Radiator Fan][radiator-fan] | High |

---

## ⚠️ HIGH PRIORITY (Needed for Final Design)

Items needed before installation begins but not system-critical.

| Item | Description | File | Priority |
|:-----|:------------|:-----|:---------|
| Grommet 1 Location | Engine bay side near PMU | [Firewall Ingress][firewall-ingress] | High |
| Grommet 2 Location | Cabin side near pedal area | [Firewall Ingress][firewall-ingress] | High |
| Grommet 5 Location | Path from firewall to grille area | [Firewall Ingress][firewall-ingress] | High |
| Grommet 6 Location | Near starter battery/SafetyHub | [Firewall Ingress][firewall-ingress] | High |
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
| WolfBox Power Source | Body RTMR or SwitchPros | [Communication][communication] | Medium |
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
| Heated Seat Load | Verify PRP EnduroTrek 15A/seat spec | [Body RTMR][body-rtmr] | Verify spec sheet |
| Fusion Amp Current | Verify 35-45A continuous rating | [Audio Systems][audio-systems] | Verify spec sheet |

---

## ✅ RECENTLY RESOLVED

Items completed since last update.

| Item | Resolution | Date |
|:-----|:-----------|:-----|
| Body RTMR Model | Bussmann LR-2 (301-1C-C-R1) | 2025-11-18 |
| Body RTMR Ground | Firewall Stud Bus Terminal 3 (14 AWG) | 2025-11-18 |
| Alternator Part Number | Premier Power Welder HO-C28 | 2025-11-18 |

---

!!! info "Maintenance Instructions"
    For instructions on updating this tracker, priority definitions, and review schedules, see [Section 8 CLAUDE.md](CLAUDE.md).

---

## Summary by Priority

| Priority | Count |
|:---------|:------|
| 🔴 Critical | 3 |
| ⚠️ High | 10 |
| 📋 Medium | 18 |
| 📝 Low | 11 |
| 🔍 Verify | 2 |
| **TOTAL** | **40** |

## Related Documentation

- [Section 1 Installation Checklist][section-1-install] - Power systems installation guide
- [Section 1.7 Wire Routing][wire-routing] - Wire routing organized by location

[bcdc]: ../01-power-systems/01-power-generation/03-bcdc.md
[radiator-fan]: ../02-engine-systems/06-radiator-fan.md
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
[body-rtmr]: ../01-power-systems/03-aux-battery-distribution/04-body-rtmr.md
[section-1-install]: ../01-power-systems/installation-checklist.md
