---
hide:
  - toc
tags:
  - product-details
  - power-generation
  - battery-charger
  - dc-dc-charger
---

# 1.1.3 BCDC Alpha 50 {#bcdc-alpha-50}

/// html | div.product-info
![RedArc BCDC Alpha 50](../../images/redarc-bcdc-alpha-50.jpg){ loading=lazy }

**Type:** Battery Isolator and DC-DC Charger

**Model:** RedArc BCDC Alpha 50 (BCDC1250R)

**Manufacturer:** RedArc Electronics

**Product Page:** [BCDC Alpha 50][redarc-bcdc]

**Installation Guide:** [BCDC Alpha Installation Manual][bcdc-install]

**Instruction Manual:** [BCDC Alpha Instruction Manual][bcdc-manual]

///

## Specifications

- **Output:** 50A DC-DC charging, multi-stage AGM compatible (0.74C charge rate for 68Ah battery)
- **Inputs:** 9-32V primary (alternator), 9-48V solar (up to 350W)
- **Features:** Auto isolation, jump start assist, Green Power Priority, ignition-triggered
- **Dimensions:** 260mm L × 160mm W × 70mm H
- **Full Specs:** [Installation Manual][bcdc-install] | [Instruction Manual][bcdc-manual]

## Wiring

| Connection | Terminal Label | Terminal Size | Source/Destination | Notes |
|:-----------|:---------------|:--------------|:-------------------|:------|
| Start Battery (+) | Red | M8 | START battery positive | See [START Battery Distribution][starter-battery] for wire specs |
| Auxiliary Battery (+) | Brown | M8 | AUX battery positive | See [AUX Battery Distribution][aux-battery] for wire specs |
| Solar (+) | Yellow | TBD | Cascadia 4x4 80W panel | See [Solar Charging][solar] |
| Ground (-) | Black | M8 | AUX battery negative | See [AUX Battery Distribution][aux-battery] for wire specs |
| Ignition | Blue | Spade | PMU ignition sense tap | 18 AWG - see [PMU Inputs][pmu-inputs] |
| Battery Temp Sensor | +/- (reversible) | 2-pin plug | AUX battery positive terminal | **REQUIRED** - AGM temperature-compensated charging |

See [START Battery Distribution][starter-battery] and [AUX Battery Distribution][aux-battery] for complete wire specifications (gauge, distance, routing, circuit breakers).

**Critical:** Verify solar input polarity before connection - reverse polarity damages unit.

[starter-battery]: ../02-starter-battery-distribution/index.md
[aux-battery]: ../03-aux-battery-distribution/index.md

## Function

The BCDC manages charging and isolation between starter and aux batteries:

- **Normal Operation:** Charges AUX battery from START battery/alternator at up to 50A
- **Solar Priority:** Uses solar input first when available (Green Power Priority)
- **Jump Start Assist:** Parallels batteries if START battery voltage drops critically
- **Isolation:** Prevents AUX battery from draining START battery when engine off

## AUX Battery Charging Impact

**Upgrade from 25A to 50A BCDC provides significant improvement for high-draw scenarios:**

| Scenario | AUX Draw | 25A BCDC | 50A BCDC | Improvement |
|:---------|:---------|:---------|:---------|:------------|
| Night Offroad (full lights) | 70A | -45A drain | **-20A drain** | 2.3× longer runtime |
| Airing Up Tires | 110A | -85A drain | **-60A drain** | 30% less battery impact |
| Recovery after air-up | - | 34 min to recover 10Ah | **17 min** | Half the recovery time |

See [AUX Battery Load Analysis][aux-load-analysis] for complete scenario details.

## Mounting

- **Location:** Passenger wheel well near AUX battery (water-protected, accessible for LED visibility)
- **Installation:** See [Section 1 Installation Checklist][installation-checklist]

**Critical:** Verify solar input polarity before connection - reverse polarity damages unit.

## Temperature Sensor Installation

The BCDC includes a battery temperature sensor (2-pin, polarity reversible) that is **REQUIRED** for proper AGM charging.

**Sensor Specifications:**

- **Type:** NTC thermistor with 2-pin connector
- **Cable Length:** ~6 ft (included with BCDC)
- **Polarity:** Reversible - either orientation works

**Installation Location:**

- **Mount Position:** AUX battery positive terminal
- **Attachment:** Ring terminal under battery terminal bolt
- **Why Positive Terminal:** Measures both voltage and temperature at the battery for accurate charge control

**Why Required:**

- AGM batteries are temperature-sensitive during charging
- Overcharging at high temps causes thermal runaway risk
- Undercharging at low temps leads to sulfation
- BCDC adjusts charge voltage based on sensor reading (temperature compensation)

**Installation Notes:**

1. Install ring terminal on AUX battery positive terminal bolt
2. Route sensor cable to BCDC (short run - both in passenger wheel well)
3. Plug into BCDC temperature sensor port (2-pin connector)

[redarc-bcdc]: https://www.redarcelectronics.com/products/the-manager30
[bcdc-install]: https://cdn.intelligencebank.com/au/share/yE9N/zJpl/NNRlJ/original/Install+Guide+BCDC+Alpha+50R+EN
[bcdc-manual]: https://cdn.intelligencebank.com/au/share/yE9N/zJpl/l7ZzG/original/Instruction+Manual+BCDC+Alpha+50R+EN
[starter-cbs]: ../02-starter-battery-distribution/01-circuit-breakers.md
[solar]: 04-solar.md
[pmu-inputs]: ../04-pmu/02-pmu-inputs.md
[grounding]: ../05-grounding/index.md
[installation-checklist]: ../installation-checklist.md#phase-2-power-distribution
[wire-distance]: 05-wire-distance-reference.md
[tbd-tracker]: ../../08-installation/01-tbd-tracker.md
[aux-load-analysis]: ../03-aux-battery-distribution/05-load-analysis.md
