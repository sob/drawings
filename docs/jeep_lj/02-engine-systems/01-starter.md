---
hide:
  - toc
tags:
  - product-details
  - engine-systems
  - starter
---

# 2.1 Starter System {#starter-system-cummins-r28}

/// html | div.product-info
![DB Electrical 410-52442 Starter](../images/db-electrical-410-52442-starter.jpg){ loading=lazy }

**Type:** High-Torque Diesel Starter

**Model:** DB Electrical 410-52442

**Manufacturer:** DB Electrical

**Product Page:** [DB Electrical 410-52442][db-starter]

**Voltage:** 12V

**Power:** 2.7 kW

**Rotation:** Clockwise (CW)

**Teeth:** 10-tooth pinion

**Mount Type:** PLGR (Planetary Gear Reduction)

**Weight:** 19 lbs

**Mounting:** Engine block (PLGR mount)

**Power Source:** START battery+ direct connection (2/0 AWG)

**OEM Cross-Reference:**

- Cummins: 4996706
- Denso: 428000-7090, 438000-3110
- Isuzu: 5-128000-980

///

## System Configuration

**Control Method:** Two-stage relay system

**Main Power Source:** START battery+ direct connection (see [START Battery Distribution][starter-battery] for wire specs)

**Control Solenoid:** Cole Hersee 24213 (85A continuous-duty)

**Safety Interlock:** PMU24 state machine (OUT24) supplies a hardware crank chain — push button + brake pedal switch + Turbolamik P/N relay + engine-running lockout (all four gates required). See [Keyless Ignition][keyless-ignition] for the full architecture.

**Battery Requirement:** 800 CCA minimum (Odyssey PC1500 provides 850 CCA)

## Wiring

| Circuit               | Source                   | Destination                       | Wire Gauge | Current  | Notes                                                            |
| :-------------------- | :----------------------- | :-------------------------------- | :--------- | :------- | :--------------------------------------------------------------- |
| Main Power            | START battery+           | Starter solenoid battery post     | 2/0 AWG    | 400-600A | See [START Battery Distribution][starter-battery] for wire specs |
| Solenoid Power Tap    | START battery post       | Cole Hersee 24213 input           | 10 AWG     | 30-75A   | ~2 ft                                                            |
| Crank Chain Supply    | PMU OUT24                | Dash push-button supply (cabin)   | 18 AWG     | ~1.6A    | Asserted by PMU state machine; routed through firewall to cabin  |
| Push Button Output    | Dash push-button         | Brake switch (start tap)          | 18 AWG     | ~1.6A    | Cabin                                                            |
| Brake-gated Start     | Brake switch (start tap) | Firewall Pin 15 → P/N relay contact | 18 AWG   | ~1.6A    | Via Deutsch HDP24-24-21 Pin 15                                   |
| P/N Relay Coil        | Turbolamik P/N aux output| P/N interlock relay coil          | 18 AWG     | ~0.1A    | Engine bay; energized when shifter in P or N                     |
| P/N Relay Output      | P/N interlock relay (NO) | Engine-running lockout relay      | 18 AWG     | ~1.6A    | Engine bay                                                       |
| Engine-Run Relay Coil | Alternator B+ (filtered) | Engine-running relay coil         | 18 AWG     | ~0.1A    | Diode + zener filter; >13V threshold = engine running            |
| Lockout-gated Drive   | Engine-running relay NC  | Cole Hersee 24213 coil+           | 16 AWG     | ~1.6A    | NC contacts: closed when engine off, opens once running          |
| Solenoid Coil Ground  | Cole Hersee 24213 coil-  | Engine bay ground bus             | 16 AWG     | ~1.6A    | ~3 ft                                                            |
| Solenoid Output       | Cole Hersee 24213 output | Starter solenoid switch post      | 10 AWG     | 30-75A   | ~2 ft                                                            |
| Ground Return         | Starter case             | Engine block → START battery-     | 2/0 AWG    | 400-600A | Via engine bay ground bus                                        |

## Control Flow

```text
PMU OUT24 (Ignition Authorize) → Push Button (cabin) → Brake Switch → Pin 15 (firewall) →
                                                          P/N Relay (coil = Turbolamik P/N) →
                                                          Engine-Running Lockout Relay (NC, coil = alternator) →
                                                              ↓
                                                          Cole Hersee 24213 Coil → Ground
                                                              ↓
                                                          Solenoid Closes (all four gates asserted)
                                                              ↓
                              START battery Post → Cole Hersee Output → Starter Switch Post
                                                              ↓
                                                          Main Solenoid Engages
                                                              ↓
                                                              Starter Cranks
                                                              ↓
                                                  Engine starts → alternator output rises →
                                                  Engine-Running Relay opens → Cole Hersee de-energized
```

## Starter Motor Terminals

**Battery Post (M8 x 1.25 thread, qty 2):**

- Main power from START battery (2/0 AWG)
- Power tap for control solenoid (10 AWG)

**Switch Post (6.3mm flat male push-on):**

- Trigger from Cole Hersee 24213 output (10 AWG, 30-75A)

**Ground:**

- Via starter mounting bolts to engine block

## Cole Hersee 24213 Solenoid

**Specifications:**

- Rating: 85A continuous duty
- Coil Voltage: 12V DC
- Coil Draw: ~1.6A
- Mounting: Firewall (engine bay side)

**Terminals:**

- Large Stud 1 (Input): From START battery post (M8 terminal, 10 AWG)
- Large Stud 2 (Output): To starter switch post (6.3mm female push-on, 10 AWG)
- Small Terminal 1 (Coil+): From engine-running lockout relay NC output (16-18 AWG)
- Small Terminal 2 (Coil-): To engine bay ground bus (16-18 AWG)

## Outstanding Items

Starter-circuit-specific items are tracked in the [Keyless Ignition][keyless-ignition] doc and the [TBD Tracker][tbd-tracker], since the new crank chain is part of the keyless ignition design.

See [installation checklist][install-checklist] for build tasks.

[install-checklist]: ../09-installation/02-engine-systems-checklist.md

## Related Documentation

- [START battery Distribution][starter-battery-distribution] - Main power source
- [Firewall Ingress][firewall-ingress] - Ignition START wire routing
- [Engine Bay Ground Bus][engine-bay-ground-bus] - Ground connections
- [Power Generation][power-generation] - Battery specifications
- [Wire Distance Reference][wire-distance] - Starter to battery routing distances
- [Keyless Ignition][keyless-ignition] - State machine driving OUT24 and the crank chain

[db-starter]: https://www.dbelectrical.com/products/starter-for-2-8-cummins-isf2-8-qsb3-9-30-qsb4-5-4996706-428000-7090.html
[starter-battery-distribution]: ../01-power-systems/02-starter-battery-distribution/index.md
[starter-battery]: ../01-power-systems/02-starter-battery-distribution/index.md
[firewall-ingress]: ../01-power-systems/07-wire-routing/02-firewall-ingress.md
[engine-bay-ground-bus]: ../01-power-systems/05-grounding/01-engine-bay-ground-bus.md
[power-generation]: ../01-power-systems/01-power-generation/index.md
[wire-distance]: ../01-power-systems/01-power-generation/05-wire-distance-reference.md
[keyless-ignition]: ../05-control-interfaces/06-keyless-ignition.md
[tbd-tracker]: ../09-installation/00-tbd-tracker.md
