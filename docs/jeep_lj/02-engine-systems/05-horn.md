---
hide:
  - toc
tags:
  - product-details
  - engine-systems
  - horn
---

# 2.5 Horn System {#horn}

/// html | div.product-info

**Type:** Dual Tone Horns

**Model:** PIAA Dual-Tone Horns

**Manufacturer:** PIAA

**Mounting:** Engine bay

**Power Source:** PMU Out 18 (7A capacity, CONSTANT)

///

## Specifications

- **Current draw:** 2.7A per horn × 2 = 5.4A total
- **Ground:** Chassis ground (engine bay)

## Control

**Button:** Momentary push button (normally open) on steering wheel PTT bracket

**PMU Configuration:**

- Input: In 1 (horn button signal)
- Output: Out 18 (7A capacity, powers horns directly)
- Logic: When In 1 closes, Out 18 activates (no external relay needed)
- Power: CONSTANT (works with ignition off for safety)

## Wiring Configuration

```
START battery CONSTANT → PMU → Out 18 → PIAA Horns (5.4A) → Chassis Ground
                          ↑
                      Horn Button → In 1 (trigger)
```

**Power Flow:**
1. START battery+ → CONSTANT bus → PMU
2. Horn button (steering wheel) → PMU In 1 (trigger signal)
3. PMU Out 18 activated when In 1 closes
4. PMU Out 18 → PIAA horns (5.4A) → chassis ground (engine bay)

**Notes:**
- PMU Out 18 switches directly (no external relay needed)
- Works with ignition off (CONSTANT power for safety)

## Outstanding Items

- [ ] Mount PIAA horns in engine bay, ground to chassis
- [ ] Run PMU Out 18 to horns (14 AWG for 5.4A load)
- [ ] Run horn button trigger wire through firewall to PMU In 1
- [ ] Configure PMU: In 1 closes → Out 18 activates
- [ ] Test with ignition OFF (verify CONSTANT power)

## Related Documentation

- [PMU Outputs][pmu-outputs] - PMU Out 18 circuit and programming
- [START Battery Distribution][starter-battery-distribution] - CONSTANT bus bar
- [Firewall Ingress][firewall-ingress] - Horn button trigger wire routing

[pmu-outputs]: ../01-power-systems/04-pmu/03-pmu-outputs.md
[starter-battery-distribution]: ../01-power-systems/02-starter-battery-distribution/index.md
[firewall-ingress]: 07-firewall-ingress.md
