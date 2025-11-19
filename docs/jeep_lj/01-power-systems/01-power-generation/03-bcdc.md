---
hide:
  - toc
tags:
  - product-details
  - power-generation
  - battery-charger
  - dc-dc-charger
---

# 1.1.3 BCDC Alpha 25 {#bcdc-alpha-25}

/// html | div.product-info
![RedArc BCDC Alpha 25](../../images/redarc-bcdc-alpha-25.jpg){ loading=lazy }

**Type:** Battery Isolator and DC-DC Charger

**Model:** RedArc BCDC Alpha 25 (BCDC1225A)

**Manufacturer:** RedArc Electronics

**Product Page:** [BCDC Alpha 25][redarc-bcdc]

**Installation Guide:** [BCDC Alpha Installation Manual][bcdc-install]

**Instruction Manual:** [BCDC Alpha Instruction Manual][bcdc-manual]

///

## Specifications

- **Output:** 25A DC-DC charging, multi-stage AGM compatible (0.37C charge rate for 68Ah battery - ideal for AGM longevity)
- **Inputs:** 9-32V primary (alternator), 9-48V solar (up to 200W)
- **Features:** Auto isolation, jump start assist, Green Power Priority, ignition-triggered
- **Dimensions:** 198mm L × 121mm W × 60mm H
- **Full Specs:** [Installation Manual][bcdc-install] | [Instruction Manual][bcdc-manual]

## Wiring

| Connection | Terminal Label | Wire Gauge | Terminal Size | Source/Destination | Notes |
|:-----------|:---------------|:-----------|:--------------|:-------------------|:------|
| Start Battery (+) | Red | 6 AWG | TBD | Starter battery positive (driver wheel well) | INPUT from alternator-charged battery - via 40A CB <br/>see [STARTER BATTERY CIRCUIT BREAKERS][starter-cbs] |
| Auxiliary Battery (+) | Brown | 6 AWG | TBD | Aux battery positive (passenger wheel well) | OUTPUT to aux battery - 25A charging |
| Solar (+) | Yellow | Per solar panel | TBD | Cascadia 4x4 80W panel | See [Solar Charging][solar] |
| Ground (-) | Black | 6 AWG | TBD | Aux battery negative | Direct connection per BCDC spec |
| Ignition | Blue | 18 AWG | Spade | PMU ignition sense tap | Activates charging when engine running - see [PMU Inputs][pmu-inputs] |
| Battery Temp Sensor | +/- (reversible) | Per sensor | 2-pin plug | Aux battery (AGM sensor) | **REQUIRED** - critical for AGM temperature-compensated charging, polarity reversible |

**Inter-Battery Cable Routing:** Starter battery (driver wheel well) → under vehicle along frame rail → aux battery (passenger wheel well) - 5-6 ft measured routing (see [Wire Distance Reference][wire-distance]). Use proper cable protection for under-vehicle routing.

**Wire Gauge Analysis (25A @ 5-6 ft measured routing):**

- 6 AWG: 0.75% voltage drop (0.090V @ 12V) - **Optimized** ✅ Excellent performance
- 4 AWG: 0.37% voltage drop (0.044V @ 12V) - minimal benefit over 6 AWG ✅

**Recommendation:** 6 AWG provides excellent performance with <1% voltage drop for the measured 5-6 ft routing distance. Upgrading to 4 AWG offers minimal benefit (0.38% improvement) at increased cost and difficulty routing heavier cable.

**Ground Reference:** Starter-to-aux battery ground cable (1/0 AWG) is **REQUIRED** for BCDC operation - provides reference ground for charging logic and fault current path. See [Grounding Architecture][grounding].

**Critical:** Verify solar input polarity before connection - reverse polarity damages unit.

## Function

The BCDC manages charging and isolation between starter and aux batteries:

- **Normal Operation:** Charges aux battery from starter battery/alternator at 25A
- **Solar Priority:** Uses solar input first when available (Green Power Priority)
- **Jump Start Assist:** Parallels batteries if starter battery voltage drops critically
- **Isolation:** Prevents aux battery from draining starter battery when engine off

## Mounting

- **Location:** Passenger wheel well near aux battery (water-protected, accessible for LED visibility)
- **Installation:** See [Section 1 Installation Checklist][installation-checklist]

**Critical:** Verify solar input polarity before connection - reverse polarity damages unit.

[redarc-bcdc]: https://www.redarcelectronics.com/eu/bcdc-alpha25-r
[bcdc-install]: https://cdn.intelligencebank.com/au/share/yE9N/zJpl/NNRlJ/original/Install+Guide+BCDC+Alpha+50R+EN
[bcdc-manual]: https://cdn.intelligencebank.com/au/share/yE9N/zJpl/l7ZzG/original/Instruction+Manual+BCDC+Alpha+50R+EN
[starter-cbs]: ../02-starter-battery-distribution/01-circuit-breakers.md
[solar]: 04-solar.md
[pmu-inputs]: ../04-pmu/02-pmu-inputs.md
[grounding]: ../05-grounding/index.md
[installation-checklist]: ../installation-checklist.md#phase-2-power-distribution
[wire-distance]: 05-wire-distance-reference.md
