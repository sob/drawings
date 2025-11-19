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

| Connection | Wire Gauge | Destination | Distance | Notes |
|:-----------|:-----------|:------------|:---------|:------|
| Positive Output | 2/0 AWG | START battery+ (driver wheel well) | 8 ft | **Required for 270A @ 60°C** - see calculations below |
| Ground | Via mounting | Engine block | N/A | Bonded via alternator mounting bolts |

**Wire Sizing Calculation (Engine Bay @ 60°C):**
- Distance: 8 ft one-way, 16 ft circuit
- Current: 270A continuous
- Temperature: 60°C (140°F) engine bay ambient
- **2/0 AWG @ 270A, 16 ft, 60°C: 2.81% voltage drop** (0.404V) ✅ Acceptable
- Voltage at battery: 14.4V - 0.404V = **13.996V** (adequate for AGM charging)
- **1/0 AWG @ 270A would yield 4.47% drop** (0.644V) ❌ Exceeds 3% threshold for critical charging circuits

Temperature derating factor: 1.2× resistance increase at 60°C vs 20°C (copper wire)

**Ground Path:** Alternator case → Engine block → Frame rail (2/0 AWG) → START battery-

See [Grounding Architecture][grounding] for complete system grounding.

## Load Analysis

**START battery System Peak Loads:**
- PMU24: 220A max
- Starter: 400-600A (brief cranking only)
- BCDC charging: 25A
- ECM + Grid Heater: TBD
- **Total:** ~265A continuous (excluding starter)

**Alternator Capacity:** 270A continuous

**Note:** Peak loads exceeding alternator capacity are brief and supplemented by START battery (850 CCA). Starter draws 400-600A only during brief cranking periods (not simultaneous with other high loads).

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
