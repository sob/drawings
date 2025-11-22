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

---

## Phase 1: Brake System

### iBooster Installation

- [ ] Confirm factory vacuum brake booster removed
- [ ] Confirm iBooster Gen 2 mounted in factory brake booster location
- [ ] Ensure iBooster mounting bolts torqued to spec (TBD ft-lb)
- [ ] Confirm Gen 2 master cylinder installed
- [ ] Confirm brake lines routed from master cylinder to front/rear brakes
- [ ] Confirm iBooster wiring harness connected per Tulay's diagram
- [ ] Confirm iBooster main power connected (10 AWG red from PMU OUT1+10)
- [ ] Confirm iBooster ignition signal connected (20 AWG green from PMU OUT19)
- [ ] Confirm iBooster ground connected to firewall ground stud (10 AWG black)

---

## Phase 2: Grid Heater

- [ ] Confirm ECM pins 46/21 wired to grid heater relay coil (Cummins 5467024)
- [ ] Confirm fusible link installed from START battery+ to grid heater relay
- [ ] Confirm grid heater relay ground connected to START battery- or NEGATIVE bus
- [ ] Confirm grid heater relay mounted in engine bay near intake manifold
- [ ] Verify grid heater element resistance ~0.15Ω (confirms 80A @ 12V design)

---

## Phase 3: HVAC

- [ ] Confirm factory TJ HVAC system complete and functional
- [ ] Confirm vacuum system installed: R2.8 manifold → check valve → reservoir → firewall → dash
- [ ] Verify vacuum system holds vacuum (no leaks)

---

## Phase 4: Wipers

- [ ] Confirm WS-51C wiper controller mounted in dash
- [ ] Confirm PMU Out 11 connected to WS-51C power input
- [ ] Confirm WS-51C outputs connected to front wiper motor
- [ ] Confirm front washer pump wired to WS-51C washer output
- [ ] Confirm washer fluid lines routed to front nozzles

---

## Phase 5: Radiator Fan

- [ ] Verify PMU to fan motor wire length matches design (6 ft estimated)
- [ ] Verify voltage at fan terminals >13V under load (engine running)
- [ ] Verify voltage drop acceptable at all PWM speeds
- [ ] Tune temperature setpoints for R2.8 under real-world conditions
- [ ] Tune PWM curve based on observed cooling performance
- [ ] Verify inverted duty cycle behavior (0% = full speed, 100% = off)

---

## Phase 6: Testing

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

### Grid Heater Testing

- [ ] Verify grid heater activates in cold conditions (<50°F ambient)
- [ ] Verify "Wait to Start" lamp illuminates during preheat

---

## Reference Documentation

- **iBooster:** [Brake Booster System][ibooster]
- **Grid Heater:** [Grid Heater System][grid-heater]
- **HVAC:** [HVAC System][hvac]
- **Wipers:** [Wiper System][wipers]
- **Radiator Fan:** [Radiator Fan System][radiator-fan]

[tulays-harness]: https://tulayswirewerks.com/product/bosch-ibooster-gen-2-universal-wire-harness/
[ibooster]: 02-brake-booster.md
[grid-heater]: 08-grid-heater.md
[hvac]: 03-hvac.md
[wipers]: 04-wipers.md
[radiator-fan]: 06-radiator-fan/index.md
