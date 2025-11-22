---
hide:
  - toc
---

# 2.6.1 Fan Motor {#fan-motor}

/// html | div.product-info
![GM 84100128 Camaro Electric Fan](../../images/gm-84100128-camaro-fan.jpg){ loading=lazy }

**Type:** Electric radiator fan

**Model:** GM 84100128

**Manufacturer:** General Motors

**Mounting:** Radiator shroud

///

## Specifications

- **Motor Type:** Brushless electric fan (PWM-capable)
- **Voltage:** 12V DC (14.5V with engine running)
- **Current Draw:** 50-53A @ full speed (14.5V), 14A @ 50% duty (3400 CFM)
- **Airflow (Installed):** 4188 CFM @ full speed (with radiator)
- **Airflow (Free Air):** 5690 CFM @ full speed (14.5V)
- **Control:** PWM via PMU OUT2+3+4 (variable speed 0-100%)
- **Duty Cycle:** Intermittent (temperature-based)

## Wiring

| Connection | Wire Gauge | Source | Destination | Distance | Voltage @ Load | Notes |
|:-----------|:-----------|:-------|:------------|:---------|:---------------|:------|
| **Fan Power (+)** | 4 AWG ✓ | PMU OUT2+3+4 | Fan motor (+) | ~TBD ft | TBD | Variable speed PWM control |
| **Fan Ground (-)** | 4 AWG ✓ | Fan motor (-) | Engine bay ground bus | <3 ft | - | Short run to ground |

**Wire Sizing (Engine Bay @ 60°C):**

- **4 AWG @ 53A, 26 ft circuit, 60°C: 3.4% voltage drop** (0.41V) ✅ Full speed operation
- Design capacity: 70A (relay rating) provides 32% safety margin
- Temperature derating: 1.2× resistance increase at 60°C vs 20°C

**Note:** Fan is brushless PWM-capable and controlled by PMU with variable speed (30% low, 60% medium, 100% full speed).

## Mounting

**Location:** Front radiator

**Installation:**

- Secure wiring away from moving parts (belts, pulleys, fan blades)
- Use zip ties or loom to protect wiring from abrasion

## Outstanding Items

- [ ] Test voltage at fan terminals under load (target >13V with engine running)

## Related Documentation

- [Radiator Fan System][radiator-fan] - Complete system overview (PMU PWM control)
- [PMU Outputs][pmu-outputs] - Power source (OUT2+3+4)
- [Engine Bay Ground Bus][ground-bus] - Ground connection

[radiator-fan]: index.md
[pmu-outputs]: ../../01-power-systems/04-pmu/03-pmu-outputs.md
[ground-bus]: ../../01-power-systems/05-grounding/01-engine-bay-ground-bus.md
