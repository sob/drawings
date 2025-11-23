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

---

## Phase 1: Starter System

- [ ] Confirm starter motor (DB Electrical 410-52442) mounted to engine block
- [ ] Confirm 2/0 AWG cable from START battery+ to starter battery post
- [ ] Confirm Cole Hersee 24213 solenoid mounted on firewall (engine bay side)
- [ ] Confirm 10 AWG from starter battery post to Cole Hersee input
- [ ] Confirm 10 AWG from Cole Hersee output to starter switch post
- [ ] Confirm 16 AWG ignition START wire routed through firewall to clutch switch
- [ ] Confirm clutch safety switch wired to Cole Hersee coil+
- [ ] Confirm Cole Hersee coil- grounded to engine bay ground bus

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

## Phase 8: Testing

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

- [ ] Verify clutch pedal switch prevents starting when clutch released
- [ ] Verify starter engages when clutch depressed and key in START
- [ ] Verify starter disengages cleanly when key released

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

---

## Reference Documentation

- **Starter:** [Starter System][starter]
- **iBooster:** [Brake Booster System][ibooster]
- **Grid Heater:** [Grid Heater System][grid-heater]
- **HVAC:** [HVAC System][hvac]
- **Wipers:** [Wiper System][wipers]
- **Horn:** [Horn System][horn]
- **Radiator Fan:** [Radiator Fan System][radiator-fan]

[tulays-harness]: https://tulayswirewerks.com/product/bosch-ibooster-gen-2-universal-wire-harness/
[starter]: 01-starter.md
[ibooster]: 02-brake-booster.md
[grid-heater]: 07-grid-heater.md
[hvac]: 03-hvac.md
[wipers]: 04-wipers.md
[horn]: 05-horn.md
[radiator-fan]: 06-radiator-fan.md
