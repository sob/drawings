---
hide:
  - toc
tags:
  - product-details
  - power-generation
  - alternator
---

# 1.1.2 Alternator {#alternator}

/// html | div.product-info
![Premier Power Welder HO-C28 Alternator](../../images/premier-power-welder-ho-c28-alternator.jpg){ loading=lazy }

**Type:** High-Output Welding Alternator

**Model:** Premier Power Welder HO-C28

**Manufacturer:** Premier Power Welder

**Product Page:** [Cummins R2.8 270A Alternator][premier-alternator]

**Rating:** 270 amps

**Application:** Cummins R2.8 Turbo Diesel

**Price:** $899.95

///

## Specifications

- **Output:** 270A continuous
- **Voltage:** 12V (standard automotive)
- **Application:** Cummins R2.8 engines
- **Type:** High-output welding alternator
- **SKU:** HO-C28

## System Configuration

**Primary Function:** Charges START battery and powers vehicle electrical systems

**Output Capacity:** 270A continuous (exceeds system maximum draw of ~326A with margin)

**Mounting:** Direct bolt-on replacement for Cummins R2.8

## Wiring

| Connection | Destination | Notes |
|:-----------|:------------|:------|
| Positive Output | START battery+ (driver wheel well) | See [START Battery Distribution][starter-battery] for wire specs |
| Ground | Engine block | Bonded via alternator mounting bolts |

**Ground Path:** Alternator case → Engine block → Frame rail → START battery-

See [START Battery Distribution][starter-battery] for complete wire specifications (gauge, distance, voltage drop calculations).

[starter-battery]: ../02-starter-battery-distribution/index.md

## Load Analysis

### Dual Battery Architecture

**Critical Understanding:** This vehicle uses a dual battery system with isolated charging:

- **START Battery (Engine Bay):** Charged directly by alternator, powers PMU and engine systems
- **AUX Battery (Wheel Well):** Charged by BCDC at 50A max, powers SwitchPros and accessories

The alternator only needs to supply START battery loads plus BCDC charging current. AUX battery loads (SwitchPros 127A, ARB compressor 90A, winch 400A) do NOT draw directly from the alternator.

### START Battery Loads (Alternator Must Supply)

| Circuit | Typical | Maximum | Notes |
|:--------|:--------|:--------|:------|
| PMU circuits (excl. radiator fan) | 106A | 160A | See [PMU Outputs][pmu-outputs] |
| Radiator fan (PWM) | 20A | 53A | Variable speed, 53A only when overheating |
| BCDC charging | 30A | 50A | Replenishes AUX battery |
| **TOTAL** | **156A** | **263A** | Well within 270A capacity |

### AUX Battery Loads (NOT Alternator Loads)

These loads draw from AUX battery, replenished by BCDC at 50A max:

| Circuit | Load | Source |
|:--------|:-----|:-------|
| SwitchPros (all offroad lighting) | 127A max | AUX battery via CONSTANT bus |
| ARB compressor | 90A | AUX battery via SafetyHub |
| BODY PDU | 10A | AUX battery via CONSTANT bus |
| Winch | 400A peak | AUX battery direct |

### Scenario Analysis

**Daily Driving:**
```
PMU circuits:          90A   (typical loads active)
Radiator fan @ 30%:    16A   (highway airflow keeps temps low)
BCDC charging:         30A   (maintaining AUX battery)
───────────────────────────
TOTAL:                136A
Alternator margin:   +134A ✅ EXCELLENT
```

**Hot Day Idling (A/C on, no airflow):**
```
PMU circuits:         100A   (HVAC blower high, A/C clutch)
Radiator fan @ 80%:    42A   (working hard, no airflow)
BCDC charging:         40A   (higher rate)
───────────────────────────
TOTAL:                182A
Alternator margin:    +88A ✅ EXCELLENT
```

**Offroad (Slow speed, hot engine, radio use):**
```
PMU circuits:         115A   (GMRS TX, aux fans, all systems)
Radiator fan @ 100%:   53A   (max cooling needed)
BCDC charging:         50A   (full rate to support accessories)
───────────────────────────
TOTAL:                218A
Alternator margin:    +52A ✅ GOOD
```

**Airing Up Tires (ARB compressor running):**
```
PMU circuits:          90A   (normal operation)
Radiator fan @ 50%:    27A   (stationary but not stressed)
BCDC charging:         50A   (full rate - AUX battery supplying ARB 90A)
───────────────────────────
TOTAL:                167A
Alternator margin:   +103A ✅ EXCELLENT

Note: ARB compressor (90A) draws from AUX battery, NOT alternator.
BCDC replenishes AUX battery at 50A - net deficit only 40A.
5-minute air-up uses ~3.3Ah from AUX battery (vs 7.5Ah with 25A BCDC).
```

### Capacity Verification

**Alternator Capacity:** 270A continuous ✅

**Worst Realistic Continuous Load:** 218A (offroad scenario)

**Margin:** 52A (19% headroom) ✅

**Note:** Theoretical PMU peak (253A) plus BCDC (50A) = 303A would exceed alternator by 33A, but this requires impossible simultaneous conditions (hard braking + both radios transmitting + horn + wipers + overheating). Brief peaks are supplemented by START battery (850 CCA, 68Ah).

## Outstanding Items

- [ ] Determine alternator positive output terminal size (for 1/0 AWG lug selection)
- [ ] Verify alternator voltage regulator set point (14.2-14.4V for AGM batteries)

## Related Documentation

- [Batteries][batteries] - START battery specifications (850 CCA)
- [START battery Distribution][starter-battery] - Alternator charging destination
- [Grounding Architecture][grounding] - Alternator ground path
- [Wire Distance Reference][wire-distance] - Alternator to battery routing distance

[premier-alternator]: https://premierpowerwelder.com/shop/high-output-welding-alternators/cummins-alternators/cummins-r2-8-270-amps-high-output-welding-alternator/
[batteries]: 01-batteries.md
[starter-battery]: ../02-starter-battery-distribution/index.md
[grounding]: ../05-grounding/index.md
[wire-distance]: 05-wire-distance-reference.md
[grid-heater]: ../../02-engine-systems/08-grid-heater.md
[pmu-outputs]: ../04-pmu/03-pmu-outputs.md
