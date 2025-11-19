---
hide:
  - toc
---

# Horn {#horn}
**Type:** PIAA horns (dual horn setup)
**Location:** Engine bay
**Control:** Steering wheel button → PMU In 1 → PMU Out 18
**Power Source:** PMU Out 18 (7A capacity, CONSTANT - always powered for safety)

## Specifications

**Horns:** PIAA high-output dual horns
- Current draw: 2.7A per horn × 2 = 5.4A total
- Mounting: Engine bay
- Ground: Chassis ground (engine bay)

**Control Button:**
- Type: Momentary push button (normally open)
- Location: Steering wheel PTT bracket
- Wiring: Button → PMU In 1

**PMU Configuration:**
- Input: In 1 (horn button signal)
- Output: Out 18 (7A capacity, powers horns directly)
- Logic: When In 1 closes, Out 18 activates (no external relay needed)
- Power: CONSTANT (works with ignition off for safety)

## Wiring Configuration

```
Starter Battery CONSTANT → PMU → Out 18 → PIAA Horns (5.4A) → Chassis Ground
                          ↑
                      Horn Button → In 1 (trigger)
```

**Power Flow:**
1. Starter Battery+ → CONSTANT bus → PMU
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

- [PMU Power Distribution][pmu-power-distribution] - PMU Out 18 circuit and programming
- [Starter Battery Distribution][starter-battery-distribution] - CONSTANT bus bar
- [Firewall Ingress][firewall-penetrations-ingress-points] - Horn button trigger wire routing
