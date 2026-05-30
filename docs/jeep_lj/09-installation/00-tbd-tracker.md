---
hide:
  - toc
---

# 8.1 TBD Tracker - Outstanding Items {#tbd-tracker}

**Purpose:** Central tracking for all To-Be-Determined items across the Jeep LJ electrical system documentation.

**Last Updated:** 2026-05-30

**Total Open Items:** 63 (+10 from the 2026-05-30 critical-spec verification audit)

---

## 🔴 CRITICAL (Installation Blockers)

Items that prevent build completion or system operation.

| Item                                   | Description | File | Priority |
| :------------------------------------- | :---------- | :--- | :------- |
| iBooster Backing Plate DXF Redesign    | Re-cut `lj-ibooster-backing-plate.dxf` from 72×72mm square to confirmed 60×80mm rectangular hole pattern (±30mm H / ±40mm V, 80mm vertical) before ordering SendCutSend steel. Vendor revised pattern 2026-05-30. | [iBooster][ibooster] | 🔴 Critical |
| MC Bore Recalculation (on hold)        | Wilwood **260-15542 is 1.00" bore**, not the 1-1/8" documented (1-1/8" = **260-15541**). Per owner decision (2026-05-30), **recalculate required MC bore** from brake hydraulics (caliper piston area, rotor radius, pedal ratio, effort/travel, iBooster assist) → select 260-15541 vs 260-15542. MC order HELD until resolved; re-confirm adapter fitment if it lands on 260-15541. | [iBooster][ibooster] | 🔴 Critical |

---

## HIGH PRIORITY (Needed for Final Design)

Items needed before installation begins but not system-critical.

| Item                              | Description                                                     | File                           | Priority |
| :-------------------------------- | :-------------------------------------------------------------- | :----------------------------- | :------- |
| Dakota Digital Panel Mounting     | HDPE sheet dimensions and location                              | [Wire Routing][wire-routing]   | High     |
| Turbolamik Aux: Reverse           | Confirm aux output channel + pinout configured for Reverse signal → PMU In 3 | [Transmission][transmission]   | High     |
| Turbolamik Aux: P/N               | Confirm aux output channel + pinout configured for P/N (start interlock) | [Transmission][transmission]   | High     |
| PBS-I Order                       | Order Digital Guard Dawg PBS-I kit (ICM, 2 iTag fobs, Start Button, Programming Button, Bypass Card, harnesses) | [Keyless Ignition][keyless]   | High     |
| WAIT-Gate Relay                   | Select SPST 30A automotive relay (NC contacts in start path; coil driven by ECM WAIT signal) | [Keyless Ignition][keyless]   | High     |
| PBS-I Mounting Location           | Cabin under-dash position; module is ~5.5"×3"×1.25"; away from heat/water; do NOT engine-bay mount | [Keyless Ignition][keyless]   | High     |
| Start Button Mounting Location    | Dash position within easy reach (button + 36" harness included in PBS-I kit)                  | [Keyless Ignition][keyless]   | High     |
| Programming Button Storage        | Hidden but accessible location (under dash or in trunk) for fob-learn and emergency bypass PIN entry | [Keyless Ignition][keyless] | Medium   |
| PBS-I Quiescent Current           | Measure or vendor-confirm standby draw to add to START battery parasitic budget               | [Keyless Ignition][keyless]   | Medium   |
| R2.8 Turbo Inlet OD               | Measure turbo inlet tube outside diameter to confirm AMOT 4261M-02 (2.8" body) fitment and select intake-side adapter | [Runaway Protection][runaway-protection] | High     |
| AMOT-to-Intake Adapters           | Source NPT-to-hose fittings sized to match measured turbo inlet OD                                | [Runaway Protection][runaway-protection] | High     |
| AMOT T-Handle Mounting Location   | Select dash mounting position for Midwest Control 30-144-TTL-BH-3 (reachable belted, away from accidental contact) | [Runaway Protection][runaway-protection] | High     |
| AMOT Cable Firewall Grommet       | Assign dedicated firewall grommet for AMOT push-pull cable pass-through (must not share with other cables) | [Runaway Protection][runaway-protection] | High     |
| Catch Can Mounting Bracket Point  | Select engine bracketry attachment point for Mishimoto MMOCC-UB universal bracket                  | [Runaway Protection][runaway-protection] | High     |
| iBooster Donor Sourcing           | Source 2018-2023 Honda Accord Hybrid iBooster + MC pull (eBay/LKQ/Car-Part.com)                   | [iBooster][ibooster] | High |
| iBooster Wiring Harness Selection | Choose between Tulay's Wire Werks Gen 2 universal vs EVcreate Gen 2 connector kit                  | [iBooster][ibooster] | High |
| LJ Firewall Mount Strategy        | Primary: direct mount via booster's integral 4-stud flange + SendCutSend cabin-side backing plate (drill new firewall holes 60×80mm M8, 80mm vertical + 62mm center). Fallback: SendCutSend custom one-off, then Back Bay commission (only if LJ trial-fit available) | [iBooster][ibooster] | High |
| Reservoir Standoff Design         | Design firewall standoff to mount 250-16393 dual bracket 4-6" above MC flange                      | [iBooster][ibooster] | High |
| Auto Brake Pedal Sourcing         | Source 03-06 TJ/LJ automatic brake pedal assembly + stop-lamp switch (Mopar 56045043AB if needed) | [iBooster][ibooster] | High |
| Clutch MC Firewall Hole Plug      | Block-off plate or weld closure for ~1.25" CMC pass-through (manual-to-auto pedal swap)            | [iBooster][ibooster] | High |

---

## 📋 MEDIUM PRIORITY (Design Optimization)

Items that improve the design but don't block installation.

| Item                                   | Description                                                                      | File                                 | Priority |
| :------------------------------------- | :------------------------------------------------------------------------------- | :----------------------------------- | :------- |
| Firewall Grommet Circuits              | Complete wire bundle lists                                                       | [Wire Routing][wire-routing]         | Medium   |
| Passenger Wheel Well Routing           | SwitchPros outputs path                                                          | [Wire Routing][wire-routing]         | Medium   |
| Dash to Console Routing                | Switch panels, USB, radio                                                        | [Wire Routing][wire-routing]         | Medium   |
| Cab to Cargo Routing                   | Rear lights, compressor, lockers                                                 | [Wire Routing][wire-routing]         | Medium   |
| Roof/Roll Bar Routing                  | Light bars, dome lights                                                          | [Wire Routing][wire-routing]         | Medium   |
| Speaker Mounting Locations             | Dash end caps or kick panels                                                     | [Audio Systems][audio-systems]       | Medium   |
| RF Power Grommet Location              | Grommet 6 location near battery for radio power                                  | [Wire Routing][wire-routing]         | Medium   |
| Solar Panel Wire Gauge                 | Wire sizing for Cascadia 4x4 80W panel connection                                | [BCDC][bcdc]                         | Medium   |
| Alternator Output Terminal Size        | Terminal size for 1/0 AWG lug selection                                          | [Alternator][alternator]             | Medium   |
| Alternator Voltage Regulator Set Point | Verify 14.2-14.4V for AGM batteries                                              | [Alternator][alternator]             | Medium   |
| BODY PDU Metri-Pack Pinout             | J301-J306 connector pinout (military TM or reverse engineering)                  | [BODY PDU][body-rtmr]                | Medium   |
| BODY PDU 12V Relay Part Numbers        | Replacement part numbers for K40, K42, K53 (currently 24V coils)                 | [BODY PDU][body-rtmr]                | Medium   |
| Winch Control Wire Routing             | Routing path from dash to bumper (~15-20 ft through multiple zones)              | [Dashboard Controls][dash-controls]  | Medium   |
| Winch Rocker Switch Sourcing           | Center-off momentary rocker switch (SPDT or DPDT, 10A rated)                     | [Dashboard Controls][dash-controls]  | Medium   |
| Rear Seat Switch Mounting Location     | Physical mounting location for Blue Sea 4160 push button (rear roll bar lights)  | [Dashboard Controls][dash-controls]  | Medium   |
| Fusion Apollo Amp Distance & Drop      | Wire distance and resulting voltage drop for MS-AP61800 (CONSTANT bus stud 5)    | [Constant Bus][constant-bus]         | Medium   |
| iBooster Reservoir Flexline Length     | Confirm Wilwood 220-12xxx length after firewall mockup (8"/10"/12" available)    | [iBooster][ibooster]                 | Medium   |

---

## 📝 LOW PRIORITY (Optional/Aesthetic)

Items that can be determined during build.

| Item                              | Description                                                                     | File                                 | Priority |
| :-------------------------------- | :------------------------------------------------------------------------------ | :----------------------------------- | :------- |
| BIM Module Current Draw           | Current draw for BIM-17-2, BIM-11-2, BIM-12-2, BIM-13-2 (powered via BIM cable) | [Gauge Cluster][gauge-cluster]       | Low      |
| LED4Life Wire Colors              | Confirm pod wire colors match MLC-RW pinout before install                      | [Footwell Lights][footwell-lights]   | Low      |

---

## 🔍 VERIFICATION NEEDED

Items that are estimated and need actual product specs to confirm.

| Item                | Description                                                                                     | File                       | Action Needed      |
| :------------------ | :---------------------------------------------------------------------------------------------- | :------------------------- | :----------------- |
| Grid Heater Current | Design value 80A - verify via element resistance measurement during installation (~0.15Ω @ 12V); Cummins publishes no current figure for 5467024 | [Grid Heater][grid-heater] | Measure resistance |

---

## 🔬 CRITICAL-SPEC VERIFICATION AUDIT (2026-05-30)

Findings from a source-validation pass over critical fab/order/wiring specs (per CLAUDE.md Imperative #7). Each is footnoted at its source page. **Confirmed** specs need no action; **mismatch/unverified** items below need a decision or measurement before fabrication/order.

| Item | Finding | File | Action Needed | Issue |
| :--- | :------ | :--- | :------------ | :---- |
| Fusion amp external fuse | ✅ **Resolved (2026-05-30):** external protection set to **40A** per Fusion install guide (owner decision); 100A was oversized. 78A is theoretical sine-max, not sustained; musical draw ~8-15A. 4 AWG retained; 125A internal fuse covers amp-side faults. | [Amplifier][amplifier] | ✅ Done — 40A | [PR #15][pr15] |
| Winch model + peak draw | ✅ **Resolved (2026-05-30):** model confirmed **WARN ZEON 10-S** (owner); VR EVO naming removed. Peak draw corrected to **409A** (WARN spec) throughout; 1/0 AWG retains margin. | [Winch][winch] | ✅ Done — Zeon 10-S / 409A | [PR #15][pr15] |
| MC bore recalc | ⛔ **On hold:** part/bore conflict (260-15542 = 1.00", not the documented 1.125" = 260-15541). Bore to be recalculated from brake hydraulics before ordering. | [iBooster][ibooster] | Recalc → select part | [#16][i16] |
| iBooster firewall torque | ✅ **Resolved (2026-05-30):** corrected **16.5 → 13 Nm (115 in-lb)** — Honda's M8 power-brake-booster mounting-nut spec (consistent across Accord generations); M8 confirmed by EVcreate. Conservative direction into the firewall/backing plate. | [iBooster][ibooster] | ✅ Done — 13 Nm | [#18][i18] |
| iBooster body-neck Ø | ⚠️ **Corroborated (2026-05-30):** ~62mm now backed by **two** independent sources (Back Bay vendor + iBooster retrofit community measurements of the Gen 2 Accord unit). Not a Honda-published spec. Final on-arrival measurement still warranted — only ~2mm clearance vs the 64mm backing-plate bore. | [iBooster][ibooster] | Confirm on donor (tight) | [#19][i19] |
| Ground bus stud torque | ✅ **Resolved (2026-05-30):** corrected **100-120 → 140 in-lb** — Blue Sea's published spec for the 2107's 3/8"-16 studs (the 120 in-lb was the 5/16"-18 value, undertorquing these). Cited to bluesea.com. | [Ground Bus][ground-bus] | ✅ Done — 140 in-lb | [#22][i22] |
| MC port threads | ⚠️ **Outlet resolved (2026-05-30):** confirmed **1/2-20 IF** per Wilwood datasheet (corrects the old 11/16-20, which was the flexline-adapter thread). **Reservoir/inlet port thread still TBD** — Wilwood lists inlet size but no clean thread spec, and it rides on the final bore (260-15541 vs 260-15542) selected by the #16 recalc. | [iBooster][ibooster] | Inlet thread → with bore | [#21][i21] |
| Radiator fan current/CFM | **53A / 4188 CFM** unverifiable — GM/ACDelco publish no figures for 84100128. | [Radiator Fan][radiator-fan] | Clamp-meter measure | [#23][i23] |
| SwitchPros power/ground gauge | ✅ **Resolved (2026-05-30):** confirmed adequate. 1/0 AWG power is a deliberate upsize over the supplied 30" cable (150A module, ~2 ft run); 4 AWG ground carries reference/logic current only — load return flows via each output's ground to the 1/0 AWG SwitchPros ground bus, per Switch-Pros design. | [SwitchPros][switchpros] | ✅ Done — adequate | [#24][i24] |
| iBooster donor year + part # | ✅ **Resolved (2026-05-30):** part #s **confirmed on the secured donor** (eBay listing #397546491129, offer accepted): OE/OEM `46680-T3Z-A00` + `01469-TWA-A58`, MC mfr # `46100-TWA-A550-M1`. Speculative model-year claim dropped — physical part is the fitment reference (Gen 2 Honda Accord). Final casting-# check on arrival. | [iBooster][ibooster] | ✅ Done — donor secured | [#20][i20] |

> **GitHub tracking:** the open audit items above are sub-issues of [#17 — Critical-spec verification audit][i17]. The MC bore ([#16][i16]) is tracked as a standalone blocker.

[pr15]: https://github.com/sob/drawings/pull/15
[i16]: https://github.com/sob/drawings/issues/16
[i17]: https://github.com/sob/drawings/issues/17
[i18]: https://github.com/sob/drawings/issues/18
[i19]: https://github.com/sob/drawings/issues/19
[i20]: https://github.com/sob/drawings/issues/20
[i21]: https://github.com/sob/drawings/issues/21
[i22]: https://github.com/sob/drawings/issues/22
[i23]: https://github.com/sob/drawings/issues/23
[i24]: https://github.com/sob/drawings/issues/24

**Confirmed-correct (footnoted, no action):** Cole Hersee 24213 = 200A (was wrongly 85A — corrected); MC stroke 1.10"; reservoir 260-16392 4oz/-3AN; ARB CKBLTA12 90A total; SwitchPros RCR-Force 12 output ratings (4×35A/1×30A/11×15A/150A); CT4 10A/output (40A); Odyssey PC1500 68Ah/850CCA; Dakota Lithium 135Ah; Mechanical Products 174-S2 breakers (250/150/100/80A); Blue Sea 2107 (600A) / 2105 (250A); Deutsch HDP24 contacts (size-12 25A / size-16 13A); DB Electrical 410-52442 starter (2.7kW/10-tooth); WARN line pull 10,000 lb; iBooster firewall pattern 60×80mm M8.

---

## 🚙 DRIVETRAIN (Section 10)

Mechanical drivetrain specifications, tracked separately from the electrical build. Most items need component selection before parts ordering.

| Item                              | Description                                                                                  | File                              | Priority |
| :-------------------------------- | :------------------------------------------------------------------------------------------- | :-------------------------------- | :------- |
| Transmission Shifter Type         | Electronic shifter input - depends on shifter selection                                      | [Transmission][transmission]      | Medium   |
| Transmission Pilot Bearing        | If required by flywheel/crank combination                                                    | [Transmission][transmission]      | Medium   |
| Transfer Case Specs               | Output type, fluid type and capacity                                                         | [Transfer Case][transfer-case]    | Medium   |
| Front Driveshaft Specs            | Type, length, U-joint selection                                                              | [Driveshafts][driveshafts]        | Medium   |
| Rear Driveshaft Specs             | Type, length, U-joint selection                                                              | [Driveshafts][driveshafts]        | Medium   |
| Front Axle Gearing & Manufacturer | Ratio and axle housing manufacturer                                                          | [Front Axle][front-axle]          | Medium   |
| Rear Axle Gearing & Locker        | Ratio, manufacturer, and locker type                                                         | [Rear Axle][rear-axle]            | Medium   |
| Front Suspension Components       | Coil rate, bypass valving, control arms, track bar, sway bar                                 | [Suspension][suspension]          | Medium   |
| Rear Suspension Components        | Coil rate, bypass valving, control arms, track bar, sway bar                                 | [Suspension][suspension]          | Medium   |
| Hydroboost Pump Specs             | Model, flow rate, pressure, drive type                                                       | [Steering][steering]              | Medium   |
| Hydroboost Ram Specs              | Model, bore, stroke, mount type                                                              | [Steering][steering]              | Medium   |
| Suspension Geometry               | Departure and breakover angles (calculated from chosen suspension)                           | [Suspension][suspension]          | Low      |
| Hydroboost Reservoir & Fluid      | Reservoir type/capacity/location and fluid type/capacity                                     | [Steering][steering]              | Low      |

---

## RECENTLY RESOLVED

Items completed since last update.

| Item                          | Resolution                                                                                                                    | Date       |
| :---------------------------- | :---------------------------------------------------------------------------------------------------------------------------- | :--------- |
| Back Bay MC Adapter Compatibility | Vendor (Back Bay Customs / Adam) confirmed: adapter fits Wilwood 260-15542 (1-1/8" Tandem Compact), is Honda-Accord-iBooster-only (not Tesla), and the 2× remote Wilwood reservoirs are fine. Blocker cleared — Wilwood + adapter cleared to order. Note: vendor also revised the firewall pattern to 60×80mm (80mm vertical), see new backing-plate DXF redesign item. | 2026-05-30 |
| Boomerang Bullet 230          | Removed from build — product was fabricated (does not exist). Replaced by Digital Guard Dawg PBS-I self-contained system     | 2026-05-30 |
| Boomerang Mounting Location   | Obsolete — Boomerang not used; PBS-I includes its own RFID receiver in the ICM                                                | 2026-05-30 |
| ECM Ignition Relay            | Obsolete — PBS-I PINK IGN (60A onboard relay) replaces the external ECM ignition relay                                        | 2026-05-30 |
| P/N Interlock Relay           | Obsolete — interlock provided by 8HP70 + Turbolamik (transmission won't shift out of Park without brake); no external relay  | 2026-05-30 |
| Engine-Running Lockout Relay  | Obsolete — relying on starter Bendix overrunning clutch + brake-required-to-crank UX; no external relay                       | 2026-05-30 |
| Engine-Running Voltage Filter | Obsolete — no engine-running lockout relay; no filter needed                                                                  | 2026-05-30 |
| Hidden Bypass Toggle          | Obsolete — PBS-I Emergency Bypass Card (4-digit PIN entered via Programming Button) replaces hardwired bypass                 | 2026-05-30 |
| Dash Push-Button (Keyless)    | Resolved — Start Button included in PBS-I kit (pre-wired 36" harness to ICM)                                                  | 2026-05-30 |
| PMU Output Strategy (Keyless) | Obsolete — PMU is no longer in the keyless logic path; OUT24 returned to Available                                            | 2026-05-30 |
| PMU24 Keyless State Machine   | Obsolete — PBS-I is self-contained; no PMU state machine required                                                             | 2026-05-30 |
| Keyless Firewall Pin Assignments | Resolved — Pin 12 reassigned to ignition signal outbound (cabin→EB), Pin 15 reassigned to WAIT-gated PURPLE START         | 2026-05-30 |
| Horn Relay Specs              | None required - PMU OUT 18 switches PIAA horns directly, no external relay                                                    | 2026-05-25 |
| Horn Load                     | 5.4A (PIAA 2.7A × 2)                                                                                                          | 2026-05-25 |
| Horn Circuit Protection       | None required - PMU OUT 18 has integrated electronic overcurrent/thermal protection                                           | 2026-05-25 |
| Horn Button Type              | Momentary (steering wheel button → PMU In 1)                                                                                  | 2026-05-25 |
| WolfBox License Plate         | Resolved - rear camera mounts above license plate; integration with plate lights not required                                 | 2026-05-25 |
| 3-Position Selector Switch    | Obsolete entry - no such switch in current design (SwitchPros outputs used directly)                                          | 2026-05-25 |
| Winch 3-Position Switch       | Obsolete entry - winch uses BODY PDU-fed center-off momentary rocker, not SwitchPros                                          | 2026-05-25 |
| Cummins Harness Wire Count    | Use factory bulkhead connector as-is; no per-wire enumeration needed                                                          | 2026-05-25 |
| R2.8 ECM A/C Pin (source sync)| Source file `02-engine-systems/03-hvac.md` updated to remove stale TBD; matches 2025-11-28 tracker resolution                 | 2026-05-25 |
| ADU7 Supplemental Display     | Removed from build - PMU OUT14 freed, An 5-8 returned to Available, boost/EGT/AUX-voltage sensors no longer required          | 2026-05-25 |
| Ham Radio                     | Removed from build - PMU OUT12 freed, firewall pin 2 freed, radio ground run eliminated                                       | 2026-05-25 |
| R2.8 ECM A/C Request Input    | CM2220 has no A/C request input - not applicable                                                                             | 2025-11-28 |
| Fusion Amp Mounting           | Back firewall in cab                                                                                                          | 2025-11-28 |
| STX Intercom Mounting         | Dash/behind dash                                                                                                              | 2025-11-28 |
| WolfBox Rear Camera Mount     | Above license plate                                                                                                           | 2025-11-28 |
| WolfBox Cable Length          | ~11 ft (windshield → A-pillar → rear center)                                                                                  | 2025-11-28 |
| GMRS Antenna Location         | Driver A-pillar (~6 ft from dash)                                                                                             | 2025-11-28 |
| Ham Antenna Location          | Passenger A-pillar (~4 ft to dash)                                                                                            | 2025-11-28 |
| Turn Signal Mounting          | Front fenders                                                                                                                 | 2025-11-28 |
| Radiator Fan Wire Length      | 6 ft (PMU to fan)                                                                                                             | 2025-11-28 |
| Speaker IPX Rating            | IP67                                                                                                                          | 2025-11-28 |
| Hi-Lift Jack Mount            | Not needed                                                                                                                    | 2025-11-28 |
| Recovery Board Storage        | Not needed                                                                                                                    | 2025-11-28 |
| SwitchPros Control Cable      | 10.5 ft standard cable (wheel well to dash)                                                                                   | 2025-11-28 |
| CT4 Power Source              | PMU Out 13 (15A CONSTANT) - ~9A actual load, allows hazards when ignition off                                                | 2025-11-26 |
| SwitchPros Power Module Location | Passenger rear wheel well (with AUX battery), 1/0 AWG power wire ~2 ft                                                     | 2025-11-26 |
| Rear Seat Switch              | Blue Sea 4160 (10A latching), 16 AWG, parallel with SwitchPros OUTPUT-4                                                      | 2025-11-26 |
| Door Switch Routing           | Factory plunger switches retained, 18 AWG to SwitchPros TRIGGER-1                                                            | 2025-11-26 |
| Turn Signal Distribution      | CT4 splice to front turn, Maxbilt rear, RTL-S amber (~0.9A per side)                                                         | 2025-11-26 |
| Brake Light Distribution      | PMU Out 21 splice to Maxbilt, RTL-S brake (~4.5A total)                                                                      | 2025-11-26 |
| Running Light Distribution    | PMU Out 23 splice to LP6 DRL, Maxbilt marker, RTL-S running (~2.6A total)                                                    | 2025-11-26 |
| RTL-S Wiring Configuration    | 4-wire: black ground, red running (PMU Out 23), yellow brake (OEM), blue work (PMU Out 23); 2-wire: yellow/blue turn (SwitchPros OUTPUT-7) | 2025-11-25 |
| Cargo Light Power Source      | BODY PDU CB20 (10A) with SPST switch on wheel well top; lights flush mounted in wheel well                                                   | 2025-11-26 |
| Rear Work Lights Position     | Above license plate, verified clear of WolfBox rear camera                                                                                   | 2025-11-26 |
| Reverse Lights Mount          | Rear armor brackets                                                                                                                          | 2025-11-26 |
| Cargo Light Switch            | Blue Sea 4160 (10A latching, 3/4" mount) on wheel well top                                                                                   | 2025-11-26 |
| Roof Lights OUTPUT-1 Overload | Corrected XL Sport specs (2.2A/pod, not 6A); 8 pods = 18A on single OUTPUT-1 (51% utilization)                               | 2025-11-25 |
| Fusion Amp Current Draw       | 6-ch MS-AP61800: 1.32A idle, 78A max, 125A electronic fuse                                                                    | 2025-11-24 |
| Fusion Amp CB Selection       | Blue Sea 187-series 40A breaker (per Fusion install guide; superseded earlier 100A), 4 AWG power/ground wiring, mount at CONSTANT bus       | 2026-05-30 |
| WolfBox Model                 | G900 TriPro selected                                                                                                          | 2025-11-24 |
| WolfBox Power Source          | BODY PDU F5 (10A, CONSTANT)                                                                                                   | 2025-11-24 |
| WolfBox Mounting              | Windshield mount (replaces factory rearview mirror)                                                                           | 2025-11-24 |
| WolfBox Ground                | Dash ground point                                                                                                             | 2025-11-24 |
| S8 10" Amber Part Number      | 701014 - Baja Designs S8 10" Wide Cornering Amber                                                                             | 2025-11-23 |
| Cargo Area Lighting Type      | BD Squadron Sport Flood (2 pods, 3,000 lumens total)                                                                          | 2025-11-23 |
| Cargo Area Light Quantity     | 2 BD Squadron Sport pods                                                                                                      | 2025-11-23 |
| RGB Controller                | BD RGB Whip has integrated controller                                                                                         | 2025-11-23 |
| iBooster Mounting Bolt Torque | 16.5 Nm (12 ft-lb) - 2x nyloc nuts, 13mm per Tesla Model Y service manual                                                     | 2025-11-23 |
| Grommet Locations             | Determined during installation (general areas documented)                                                                     | 2025-11-22 |
| Firewall Ground Stud Location | Determined during installation                                                                                                | 2025-11-22 |
| Wiper Controller Mounting     | Dash-mounted (WS-51C is integrated switch/controller)                                                                         | 2025-11-22 |
| Radiator Fan Mounting         | Radiator shroud (documented in fan motor specs)                                                                               | 2025-11-22 |
| Heated Seat Load              | Verified with vendor: 5A peak, 2A sustained per seat (not 15A)                                                                | 2025-11-22 |
| SafetyHub Location            | Consolidated to single SafetyHub 150 on AUX battery (ARB compressor, winch trigger); communications moved to PMU              | 2025-11-21 |
| AUX Battery CONSTANT Bus CB   | Resolved by connecting SafetyHub to CONSTANT bus - each load (SwitchPros, SafetyHub, BODY PDU) has individual CB protection   | 2025-11-22 |
| Wire Routing Protection       | Added comprehensive wire protection standards section covering split loom, heat sleeve, p-clamps, grommets by location        | 2025-11-22 |
| BCDC Temperature Sensor       | Documented installation location (side of AUX battery case), sensor specs, and installation procedure                         | 2025-11-22 |
| BCDC Wire Lengths             | Updated to 4 AWG @ 5-6 ft for 50A BCDC (0.94% voltage drop)                                                                   | 2025-11-22 |
| PMU PWM Frequency             | PMU24 supports 4-400 Hz on 25A outputs; GM brushless fan requires 100 Hz - compatible. Note: GM fans use inverted duty cycle. | 2025-11-22 |
| Radiator Fan Distance         | 6 ft estimated (firewall to radiator), 4 AWG wire sizing confirmed (3.2% drop @ 53A full speed)                               | 2025-11-21 |
| Radiator Fan Load             | GM Camaro fan 53A @ 100% PWM (variable speed: 16A @ 30%, 32A @ 60%, 53A @ 100%)                                               | 2025-11-21 |
| Radiator Fan Protection       | PMU OUT2+3+4 has integrated overcurrent/thermal protection, no external CB needed                                             | 2025-11-21 |
| PMU iBooster Thermal          | Resolved via non-adjacent combining: OUT1+10 (46A @ 40°C) vs OUT5+6 adjacent (32A @ 40°C)                                     | 2025-11-21 |
| Grid Heater Current           | Design value 80A (moved to Verification for field measurement)                                                                | 2025-11-21 |
| BCDC Temperature Sensor       | Included with BCDC unit (2-pin reversible, moved to High Priority for install documentation)                                  | 2025-11-21 |
| BODY PDU Model                | Bussmann LR-2 (301-1C-C-R1)                                                                                                   | 2025-11-18 |
| BODY PDU Ground               | Firewall Stud Bus Terminal 3 (14 AWG) - relay coil/logic reference only (~3A); high-side switching means loads ground separately | 2025-11-28 |
| Alternator Part Number        | Premier Power Welder HO-C28                                                                                                   | 2025-11-18 |

---

## Summary by Priority

| Priority         | Count  |
| :--------------- | :----- |
| 🔴 Critical      | 1      |
| High             | 20     |
| 📋 Medium        | 19     |
| 📝 Low           | 2      |
| 🔍 Verify        | 1      |
| 🚙 Drivetrain    | 13     |
| **TOTAL**        | **56** |

## Related Documentation

- [Section 1 Installation Checklist][section-1-install] - Power systems installation guide
- [Section 1.7 Wire Routing][wire-routing] - Wire routing organized by location

[bcdc]: ../01-power-systems/01-power-generation/03-bcdc.md
[gauge-cluster]: ../02-engine-systems/09-gauge-cluster/index.md
[radiator-fan]: ../02-engine-systems/06-radiator-fan.md
[wire-routing]: ../01-power-systems/07-wire-routing/index.md
[switchpros]: ../05-control-interfaces/02-switchpros-sp1200.md
[dash-controls]: ../05-control-interfaces/05-dashboard-controls.md
[audio-systems]: ../06-audio-systems/index.md
[communication]: ../07-communication-systems/index.md
[turn-signals]: ../03-lighting-systems/03-turn-signals.md
[offroad-lighting]: ../04-offroad-lighting/index.md
[cargo-lights]: ../04-offroad-lighting/07-cargo-lights.md
[chase-light]: ../04-offroad-lighting/04-chase-lights.md
[recovery-systems]: ../08-exterior-systems/01-winch.md
[body-rtmr]: ../01-power-systems/03-aux-battery-distribution/03-body-pdu.md
[section-1-install]: 01-power-systems-checklist.md
[grid-heater]: ../02-engine-systems/07-grid-heater.md
[alternator]: ../01-power-systems/01-power-generation/02-alternator.md
[hvac]: ../02-engine-systems/03-hvac.md
[ct4]: ../05-control-interfaces/03-command-touch-ct4.md
[roof-lights]: ../04-offroad-lighting/03-roof-lights.md
[rear-lights]: ../04-offroad-lighting/08-rear-lights.md
[footwell-lights]: ../04-offroad-lighting/09-footwell-lights.md
[transmission]: ../10-drivetrain/01-transmission.md
[transfer-case]: ../10-drivetrain/02-transfer-case.md
[driveshafts]: ../10-drivetrain/03-driveshafts.md
[front-axle]: ../10-drivetrain/04-front-axle.md
[rear-axle]: ../10-drivetrain/05-rear-axle.md
[suspension]: ../10-drivetrain/06-suspension.md
[steering]: ../10-drivetrain/07-steering.md
[constant-bus]: ../01-power-systems/03-aux-battery-distribution/02-constant-bus.md
[starter-doc]: ../02-engine-systems/01-starter.md
[keyless]: ../05-control-interfaces/06-keyless-ignition.md
[pmu-programming]: ../01-power-systems/04-pmu/04-pmu-programming.md
[firewall-ingress]: ../01-power-systems/07-wire-routing/02-firewall-ingress.md
[runaway-protection]: ../02-engine-systems/11-runaway-protection.md
[ibooster]: ../02-engine-systems/02-brake-booster.md
[amplifier]: ../06-audio-systems/02-amplifier.md
[winch]: ../08-exterior-systems/01-winch.md
[ground-bus]: ../01-power-systems/05-grounding/01-engine-bay-ground-bus.md
