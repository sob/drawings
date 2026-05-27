---
hide:
  - toc
tags:
  - product-details
  - control-interfaces
  - ignition
  - keyless
  - boomerang
---

# 5.6 Keyless Ignition System {#keyless-ignition}

Modern push-button ignition for the Cummins R2.8 + 8HP70 build. Replaces the factory keyswitch entirely. Single dash button starts and stops the engine. Boomerang Bullet 230 RFID provides theft deterrence. State machine runs on the PMU24.

## Architecture

/// html | div.product-info

**Type:** RFID-enabled push-button start/stop with diesel-specific interlocks

**Anti-theft:** Boomerang Bullet 230 (RFID fob required to enable)

**State Machine:** PMU24 firmware (logic in `04-pmu-programming.md`)

**Crank Interlocks:** Brake pedal + Turbolamik P/N + engine-running lockout

**Emergency Bypass:** Hidden hardwired toggle (get-home mode)

///

## Components

### Boomerang Bullet 230 (RFID Immobilizer)

| Specification     | Value                                            |
| :---------------- | :----------------------------------------------- |
| Type              | RFID transponder + fob                           |
| Detection Range   | 3-6 ft                                           |
| Output            | Single transistor output (12V when fob in range) |
| Power             | 12V CONSTANT (so fob can be detected key-off)    |
| Mounting          | Under dash, near driver position                 |
| Product Page      | [Boomerang Bullet 230][boomerang]                |

### Dash Push-Button

| Specification     | Value                                            |
| :---------------- | :----------------------------------------------- |
| Type              | Momentary, normally open, illuminated            |
| Diameter          | 19mm or 22mm panel mount                         |
| Illumination      | LED, driven by PMU (state feedback)              |
| Mounting          | Dash, within easy reach from driver seat         |
| Part              | TBD (Otto P9-113121 or equivalent)               |

### ECM Ignition Relay

| Specification     | Value                                            |
| :---------------- | :----------------------------------------------- |
| Type              | Automotive SPST, 30/40A                          |
| Coil              | 12V DC, ~150 mA draw                             |
| Contacts          | Switches Cummins ECM 12V supply                  |
| Mounting          | Engine bay, near ECM                             |
| Part              | TBD (Hella H41730011 or Bosch 0332019150)        |

### P/N Interlock Relay

| Specification     | Value                                            |
| :---------------- | :----------------------------------------------- |
| Type              | Automotive SPST, 30A                             |
| Coil              | 12V DC, driven by Turbolamik P/N aux output      |
| Contacts          | NO; in series with crank circuit                 |
| Mounting          | Engine bay, near Cole Hersee 24213               |
| Part              | TBD                                              |

### Engine-Running Lockout Relay

Prevents Cole Hersee from energizing while the engine is running, even if the start button is pressed with brake + P/N held. Protects the starter from Bendix engagement against a spinning flywheel.

| Specification     | Value                                            |
| :---------------- | :----------------------------------------------- |
| Type              | Automotive SPST, 30A                             |
| Coil              | 12V DC, driven by alternator output (~14V when running) |
| Coil Trigger      | Simple diode + zener filter on alternator B+ tap (>13V threshold) |
| Contacts          | NC; opens when engine running                    |
| Mounting          | Engine bay, near Cole Hersee 24213               |
| Part              | TBD                                              |

## State Machine

| Current State | Trigger                                              | Action                                       | New State |
| :------------ | :--------------------------------------------------- | :------------------------------------------- | :-------- |
| OFF           | Fob detected + button press                          | Assert OUT24 (ECM powered)                   | RUN       |
| OFF           | Fob detected + button + brake + P/N                  | Assert OUT24 → hardware crank chain closes   | CRANK     |
| CRANK         | J1939 RPM > 500 (engine running)                     | Engine-running relay opens, crank disengages | RUN       |
| RUN           | Button press (with or without brake)                 | De-assert OUT24, ECM loses power, engine off | OFF       |
| Any           | Hold button > 3 sec                                  | Force OFF (emergency)                        | OFF       |
| Any           | Fob lost while moving (RPM > 0)                      | Stay in current state, log alarm             | unchanged |
| OFF           | Button press, fob NOT detected                       | No action, optional alarm chirp              | OFF       |

**Fob-lost behavior:** If the fob leaves range while driving, the PMU does not kill the engine — only blocks re-start at the next OFF cycle. Modern-car convention; prevents stranding on dead fob battery.

## Wiring

### PMU24 I/O (new)

| PMU Channel | Function                                | Source                       | Destination               | Notes                          |
| :---------- | :-------------------------------------- | :--------------------------- | :------------------------ | :----------------------------- |
| **In 4**    | Boomerang fob present                   | Bullet 230 transistor output | PMU In 4                  | 12V active when fob in range   |
| **In 5**    | Push button                             | Dash button (NO contact)     | PMU In 5                  | Pulled up; goes high on press  |
| **In 6**    | Turbolamik P/N                          | Turbolamik P/N aux output    | PMU In 6                  | 12V active when in P or N      |
| **Out 24**  | Ignition Authorize                      | PMU OUT24                    | ECM ignition relay + start circuit supply | ~5A, switched by PMU logic |

J1939 RPM is read via the existing CAN bus connection ([PMU Inputs - CAN][pmu-inputs]). No new wire needed for the engine-running input to the state machine.

### Power & Control Wiring

| Connection                 | Wire Gauge | Source                       | Destination                          | Notes                                |
| :------------------------- | :--------- | :--------------------------- | :----------------------------------- | :----------------------------------- |
| Boomerang power            | 18 AWG     | Critical Cabin PDU (CONSTANT)| Bullet 230 +12V input                | ~50 mA standby; CONSTANT required    |
| Boomerang ground           | 18 AWG     | Cabin ground bus             | Bullet 230 ground                    |                                      |
| Boomerang → PMU In 4       | 18 AWG     | Bullet 230 transistor output | Firewall Pin (TBD) → PMU In 4        | Cabin → Engine Bay                   |
| Push button signal         | 18 AWG     | Dash button NO contact       | Firewall Pin 15 → PMU In 5           | Cabin → Engine Bay                   |
| Push button LED supply     | 22 AWG     | PMU OUT24 (or dedicated tap) | Button LED+                          | Illuminates when ignition authorized |
| Button LED ground          | 22 AWG     | Button LED-                  | Cabin ground bus                     |                                      |
| OUT24 → ECM relay coil     | 18 AWG     | PMU OUT24                    | ECM ignition relay coil+             | Engine bay                           |
| OUT24 → crank supply       | 18 AWG     | PMU OUT24                    | Push button supply (cabin)           | Engine Bay → Cabin (firewall)        |
| Start chain (cabin)        | 18 AWG     | Push button output (gated)   | Brake switch start tap               | Cabin                                |
| Start chain (firewall)     | 18 AWG     | Brake switch start tap       | Firewall Pin (TBD) → P/N relay       | Cabin → Engine Bay                   |
| P/N relay coil             | 18 AWG     | Turbolamik P/N aux output    | P/N interlock relay coil             | Engine bay                           |
| ER lockout coil            | 18 AWG     | Alternator B+ (via filter)   | Engine-running relay coil            | Engine bay; opens contacts when RPM up |
| Cole Hersee drive          | 16 AWG     | ER lockout relay NC output   | Cole Hersee 24213 coil+              | Engine bay                           |
| Hidden bypass toggle       | 18 AWG     | Battery+ (via fuse)          | ECM ignition relay coil+ (parallel)  | Get-home mode, hidden under dash     |

### Firewall Pin Assignments

Three pins are used by the keyless system. Pin 15 was reassigned from the prior P/N interlock placeholder (the P/N signal now stays in the engine bay since PMU and Turbolamik are co-located).

| Pin | Direction       | Signal                          | Source                | Destination          |
| :-- | :-------------- | :------------------------------ | :-------------------- | :------------------- |
| 15  | Cabin → EB      | Push button signal              | Dash button NO        | PMU In 5             |
| TBD | Cabin → EB      | Boomerang fob present           | Bullet 230 output     | PMU In 4             |
| TBD | EB → Cabin      | OUT24 ignition supply           | PMU OUT24             | Dash button supply   |
| TBD | Cabin → EB      | Gated start (post-brake)        | Brake switch output   | P/N relay contact    |

See [Firewall Ingress][firewall-ingress] for the full pin map.

## Emergency Bypass

A hidden hardwired toggle (under dash, location TBD) bypasses the PMU and directly powers the ECM ignition relay coil from CONSTANT 12V via a 5A inline fuse. This provides a get-home mode if:

- PMU24 firmware locks up or fails
- Boomerang Bullet 230 fails or fob battery dies and PMU programming has no fallback
- A CAN bus fault prevents the state machine from running

**Bypass does NOT enable cranking** — only ignition. Cranking still requires the full hardware interlock chain (brake + P/N + engine-running lockout). In bypass mode you can still start by holding the dash button if all hardware interlocks are intact.

## Diesel Runaway Note

The Cummins R2.8 is a modern electronic common-rail diesel. Normal engine shutdown is achieved by cutting power to the ECM, which stops commanding the injectors. However, ECM-only kill does not stop a true runaway — if the engine is being fed oil, fuel, or hydrocarbon vapor from an external source, cutting ECM power does nothing.

This build provides independent mechanical protection: a Mishimoto catch can in the crankcase ventilation path (prevention) plus an AMOT 4261M air shutoff valve with dash-mounted manual cable (termination). See [Diesel Runaway Protection][runaway-protection] for the full specification.

## Outstanding Items

- [ ] Select Boomerang Bullet 230 mounting location (under dash, near driver)
- [ ] Select dash push-button part (Otto, Apem, Carling, etc.) - 19mm/22mm, illuminated, momentary NO
- [ ] Select ECM ignition relay part (Hella/Bosch SPST 30-40A automotive)
- [ ] Select P/N interlock relay part (SPST 30A automotive)
- [ ] Select engine-running lockout relay part (SPST 30A, NC contacts)
- [ ] Design alternator B+ voltage filter for engine-running relay coil drive (diode + zener + resistor)
- [ ] Assign 3 new firewall HDP24 pin numbers (currently TBD): fob signal, OUT24 supply to cabin, gated start return
- [ ] Determine hidden bypass toggle location and part
- [ ] Confirm Turbolamik aux output channel can be configured for P/N (12V when in P or N)
- [ ] Decide PMU output strategy: OUT24-only with engine-running lockout (current plan) vs. freeing OUT15 winch trigger for dedicated crank output
- [ ] Write PMU24 state-machine logic in ECUMaster Light Client (see [PMU Programming][pmu-programming])

## Related Documentation

- [PMU Inputs][pmu-inputs] - In 4, In 5, In 6 assignments
- [PMU Outputs][pmu-outputs] - OUT24 assignment
- [PMU Programming][pmu-programming] - State machine logic
- [Starter System][starter] - Cole Hersee 24213 and crank chain
- [Transmission][transmission] - Turbolamik aux outputs (P/N source)
- [Ignition Signal Distribution][ignition-signal] - Why the keyswitch is gone
- [Firewall Ingress][firewall-ingress] - Pin assignments

[boomerang]: https://boomerangtag.com/products/bullet-230
[pmu-inputs]: ../01-power-systems/04-pmu/02-pmu-inputs.md
[pmu-outputs]: ../01-power-systems/04-pmu/03-pmu-outputs.md
[pmu-programming]: ../01-power-systems/04-pmu/04-pmu-programming.md
[starter]: ../02-engine-systems/01-starter.md
[transmission]: ../10-drivetrain/01-transmission.md
[ignition-signal]: ../01-power-systems/06-ignition-signal/index.md
[firewall-ingress]: ../01-power-systems/07-wire-routing/02-firewall-ingress.md
[standards-exceptions]: ../01-power-systems/STANDARDS-EXCEPTIONS.md
[runaway-protection]: ../02-engine-systems/11-runaway-protection.md
