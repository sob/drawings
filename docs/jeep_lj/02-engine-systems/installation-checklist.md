# Section 2: Engine Systems - Installation Checklist

Organized by installation order for efficient build workflow.

---

## Procurement

### iBooster

- [ ] Source Bosch iBooster Gen 2 unit (Tesla Model 3 donor)
- [ ] Source Gen 2 master cylinder (Tesla Model 3)
- [ ] Order wiring harness from [Tulay's Wire Werks][tulays-harness]

---

## Phase 1: Brake System

### iBooster Installation

- [ ] Remove factory vacuum brake booster
- [ ] Install iBooster Gen 2 in factory brake booster location
- [ ] Install Gen 2 master cylinder
- [ ] Route brake lines from master cylinder to front/rear brakes
- [ ] Connect iBooster wiring harness
- [ ] Connect iBooster ground to firewall ground stud

---

## Phase 2: Grid Heater

- [ ] Wire ECM pins 46/21 directly to grid heater relay coil (Cummins 5467024)
- [ ] Install fusible link from START battery+ to grid heater relay main power terminal
- [ ] Connect grid heater relay ground to START battery- or NEGATIVE bus
- [ ] Mount grid heater relay (engine bay, near intake manifold)
- [ ] Measure grid heater element resistance to confirm 80A design value (~0.15Ω @ 12V)
- [ ] Test grid heater operation in cold conditions (below 50°F ambient)

---

## Phase 3: Testing

### iBooster Testing

- [ ] Verify 12V CONSTANT at iBooster main power (ignition OFF and ON)
- [ ] Verify 12V at iBooster ignition signal (ignition RUN only)
- [ ] Verify chassis ground continuity (<0.1 ohms)
- [ ] Test brake pedal feel with iBooster powered (ignition ON)
- [ ] Test fail-safe standalone mode (disconnect ignition signal, verify basic assist)
- [ ] Verify standby current draw (~12mA when ignition OFF)
- [ ] Road test brake assist (light braking, hard braking, engine off coasting)

---

## Reference Documentation

- **iBooster:** [Brake Booster System][ibooster]
- **Grid Heater:** [Grid Heater System][grid-heater]

[tulays-harness]: https://tulayswirewerks.com/product/bosch-ibooster-gen-2-universal-wire-harness/
[ibooster]: 02-brake-booster.md
[grid-heater]: 08-grid-heater.md
