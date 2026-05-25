---
hide:
  - toc
tags:
  - engine-systems
  - installation
---

# Section 2: Engine Systems - Installation Checklist

Organized by installation order for efficient build workflow.

---

## Procurement

### iBooster

- [ ] Source Bosch iBooster Gen 2 unit (Tesla Model 3 donor)
- [ ] Source Gen 2 master cylinder (Tesla Model 3)
- [ ] Order wiring harness from [Tulay's Wire Werks][tulays-harness]

### Wipers

- [ ] Order Ron Francis WS-51C wiper controller module

### Runaway Protection

- [ ] Order Mishimoto MMOCC-CBT catch can + MMOCC-UB bracket
- [ ] Order AMOT 4261M02A027-AA air shutoff valve (2.8", manual/pneumatic, NPT)
- [ ] Order Midwest Control 30-144-TTL-BH-3 push-pull cable + T-handle
- [ ] Measure R2.8 turbo inlet OD and order matching NPT-to-hose adapters
- [ ] Source 2 ft of 5/8" oil-resistant hose + worm clamps for catch can plumbing

---

## Phase 1: Starter System

- [ ] Confirm starter motor (DB Electrical 410-52442) mounted to engine block
- [ ] Confirm 2/0 AWG cable from START battery+ to starter battery post
- [ ] Confirm Cole Hersee 24213 solenoid mounted on firewall (engine bay side)
- [ ] Confirm 10 AWG from starter battery post to Cole Hersee input
- [ ] Confirm 10 AWG from Cole Hersee output to starter switch post
- [ ] Confirm PMU OUT24 (Ignition Authorize) routed through firewall to dash push-button supply
- [ ] Confirm push-button output (cabin) wired in series with brake pedal switch start tap
- [ ] Confirm gated start signal routed through firewall Pin 15 → P/N relay contact in engine bay
- [ ] Confirm P/N interlock relay coil driven by Turbolamik P/N aux output
- [ ] Confirm engine-running lockout relay coil sensed from alternator B+ via filter circuit
- [ ] Confirm engine-running lockout relay NC contacts in series with Cole Hersee coil+
- [ ] Confirm Cole Hersee coil- grounded to engine bay ground bus
- [ ] Confirm ECM ignition relay coil driven by PMU OUT24 (parallel to crank chain supply)
- [ ] Confirm Boomerang Bullet 230 mounted, powered (CONSTANT), and output to PMU In 4
- [ ] Confirm hidden bypass toggle installed (battery+ via 5A fuse → ECM relay coil)

---

## Phase 2: Brake System

### iBooster Installation

- [ ] Confirm factory vacuum brake booster removed
- [ ] Confirm iBooster Gen 2 mounted in factory brake booster location
- [ ] Confirm iBooster mounting bolts torqued to 16.5 Nm (12 ft-lb) - 2x nyloc nuts
- [ ] Confirm Gen 2 master cylinder installed
- [ ] Confirm brake lines routed from master cylinder to front/rear brakes
- [ ] Confirm iBooster wiring harness connected per Tulay's diagram
- [ ] Confirm iBooster main power connected (10 AWG red from PMU OUT1+10)
- [ ] Confirm iBooster ignition signal connected (20 AWG green from PMU OUT19)
- [ ] Confirm iBooster ground connected to firewall ground stud (10 AWG black)

---

## Phase 3: Grid Heater

- [ ] Confirm ECM pins 46/21 wired to grid heater relay coil (Cummins 5467024)
- [ ] Confirm fusible link installed from START battery+ to grid heater relay
- [ ] Confirm grid heater relay ground connected to START battery- or NEGATIVE bus
- [ ] Confirm grid heater relay mounted in engine bay near intake manifold
- [ ] Verify grid heater element resistance ~0.15Ω (confirms 80A @ 12V design)

---

## Phase 4: HVAC

- [ ] Confirm factory TJ HVAC system complete and functional
- [ ] Confirm vacuum system installed: R2.8 manifold → check valve → reservoir → firewall → dash
- [ ] Verify vacuum system holds vacuum (no leaks)

---

## Phase 5: Wipers

- [ ] Confirm WS-51C wiper controller mounted in dash
- [ ] Confirm PMU OUT11 connected to WS-51C power input (14 AWG)
- [ ] Confirm WS-51C ground connected to firewall ground (14 AWG)
- [ ] Confirm WS-51C low/high outputs connected to factory wiper motor
- [ ] Confirm wiper motor park switch connected to WS-51C park input
- [ ] Confirm WS-51C washer output connected to factory washer pump

---

## Phase 6: Radiator Fan

- [ ] Confirm GM 84100128 fan mounted to radiator shroud
- [ ] Confirm PMU OUT2+3+4 connected to fan motor (4 AWG)
- [ ] Confirm fan ground connected to engine bay ground bus (4 AWG)
- [ ] Confirm PMU programmed with temperature-based PWM control

---

## Phase 7: Horn

- [ ] Confirm PIAA 85115 horns mounted in engine bay
- [ ] Confirm PMU OUT18 connected to horns (14 AWG)
- [ ] Confirm horns grounded to engine bay ground bus (Stud 6)
- [ ] Confirm horn button trigger wire routed through firewall to PMU In 1
- [ ] Confirm PMU programmed: In 1 closes → OUT18 activates

---

## Phase 8: Runaway Protection

### Catch Can Installation

- [ ] Confirm Mishimoto MMOCC-UB bracket mounted to selected engine bay location (TBD - intake side, away from exhaust)
- [ ] Confirm MMOCC-CBT catch can installed vertically with petcock at bottom
- [ ] Confirm 5/8" hose from R2.8 valve cover breather to catch can INLET (worm clamps both ends)
- [ ] Confirm 5/8" hose from catch can OUTLET to turbo inlet (worm clamps both ends)
- [ ] Verify catch can petcock closed before first engine start
- [ ] Verify no hose chafing against engine, exhaust, or moving parts

### AMOT Air Shutoff Installation

- [ ] Confirm AMOT 4261M02A027-AA installed in pre-turbo intake tract (between air filter outlet and turbo inlet)
- [ ] Confirm NPT-to-hose adapters secure on both AMOT ports
- [ ] Confirm AMOT butterfly cocks fully open and latches; verify lever orientation matches cable pull direction
- [ ] Confirm intake clamps torqued on both sides of AMOT (no boost or vacuum leaks)
- [ ] Confirm AMOT body oriented so the trip lever clears engine bay obstructions through full motion

### Cable and T-Handle Installation

- [ ] Confirm Midwest 30-144-TTL-BH-3 T-handle mounted at selected dash location (TBD)
- [ ] Confirm cable conduit passes through dedicated firewall grommet (TBD - must not share with other cables)
- [ ] Confirm cable secured every 12" with adel clamps; no sharp bends (≥6" radius)
- [ ] Confirm cable end attaches to AMOT trip lever; pull stroke ≥0.5" past trip point
- [ ] Confirm T-handle sits flush against dash bezel when AMOT is cocked open
- [ ] Confirm T-handle is labeled `EMERGENCY ENGINE SHUTOFF — PULL TO STOP`

---

## Phase 9: Testing

### iBooster Testing

- [ ] Verify 12V CONSTANT at iBooster main power (ignition OFF)
- [ ] Verify 12V CONSTANT at iBooster main power (ignition ON)
- [ ] Verify 12V at iBooster ignition signal (ignition RUN only)
- [ ] Verify iBooster ground continuity <0.1Ω to battery negative
- [ ] Verify brake pedal feel with iBooster powered
- [ ] Verify fail-safe mode works (disconnect ignition signal, confirm basic assist)
- [ ] Verify standby current ~12mA (ignition OFF)
- [ ] Road test: light braking, hard braking, engine-off coasting

### HVAC Testing

- [ ] Verify temperature control (hot/cold blend)
- [ ] Verify mode control (defrost/vent/floor)
- [ ] Verify blower speeds (all settings)
- [ ] Verify A/C clutch engagement
- [ ] Verify heater output

### Wiper Testing

- [ ] Verify wiper speeds: Off / Mist / Delay / Low / High
- [ ] Verify wiper park position (returns to rest)
- [ ] Verify washer pump activates
- [ ] Verify auto-wipe triggers after washer spray

### Starter Testing

- [ ] Verify starter does NOT crank with shifter in R, D, or manual gates (P/N interlock relay open)
- [ ] Verify starter does NOT crank when brake pedal is released (brake interlock open)
- [ ] Verify starter does NOT crank when push-button is not pressed
- [ ] Verify starter does NOT crank without Boomerang fob present (PMU blocks OUT24 assertion)
- [ ] Verify starter cranks when fob + push-button + brake + P/N all asserted (engine off)
- [ ] Verify engine-running lockout opens once alternator output > 13V (no Bendix re-engagement)
- [ ] Verify push-button press while engine running kills the engine (OUT24 de-asserts, ECM off)
- [ ] Verify hidden bypass toggle powers ECM ignition relay independent of PMU
- [ ] Verify Boomerang fob lost while running does NOT kill the engine (PMU stay-on logic)

### Grid Heater Testing

- [ ] Verify grid heater activates in cold conditions (<50°F ambient)
- [ ] Verify "Wait to Start" lamp illuminates during preheat

### Horn Testing

- [ ] Verify horn sounds when button pressed (ignition OFF)
- [ ] Verify horn sounds when button pressed (ignition ON)

### Radiator Fan Testing

- [ ] Verify voltage at fan terminals >13V under load (engine running)
- [ ] Verify fan activates at temperature setpoints
- [ ] Verify inverted duty cycle behavior (high duty = low speed)
- [ ] Tune temperature setpoints for R2.8 under real-world conditions

### Runaway Protection Testing

- [ ] Static test: engine OFF, pull T-handle, verify AMOT butterfly snaps fully closed (visual through air filter housing)
- [ ] Reset test: re-cock AMOT manually, push T-handle to flush, verify butterfly returns fully open
- [ ] Cable freedom: pull T-handle through full 3" stroke, verify no binding in conduit
- [ ] Functional test (with engine running at idle, away from people/objects): pull T-handle, verify engine stalls within 2 seconds
- [ ] Catch can drain check: after first 100 miles, drain petcock and inspect for oil collection (confirms PCV flow)
- [ ] Visual inspection: verify catch can hoses, AMOT cable, and conduit show no chafing or heat damage

---

## Reference Documentation

- **Starter:** [Starter System][starter]
- **iBooster:** [Brake Booster System][ibooster]
- **Grid Heater:** [Grid Heater System][grid-heater]
- **HVAC:** [HVAC System][hvac]
- **Wipers:** [Wiper System][wipers]
- **Horn:** [Horn System][horn]
- **Radiator Fan:** [Radiator Fan System][radiator-fan]
- **Runaway Protection:** [Diesel Runaway Protection][runaway-protection]

[tulays-harness]: https://tulayswirewerks.com/product/bosch-ibooster-gen-2-universal-wire-harness/
[starter]: ../02-engine-systems/01-starter.md
[ibooster]: ../02-engine-systems/02-brake-booster.md
[grid-heater]: ../02-engine-systems/07-grid-heater.md
[hvac]: ../02-engine-systems/03-hvac.md
[wipers]: ../02-engine-systems/04-wipers.md
[horn]: ../02-engine-systems/05-horn.md
[radiator-fan]: ../02-engine-systems/06-radiator-fan.md
[runaway-protection]: ../02-engine-systems/11-runaway-protection.md
