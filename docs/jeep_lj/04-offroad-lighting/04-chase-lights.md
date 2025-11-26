---
hide:
  - toc
tags:
  - product-details
  - lighting
  - offroad
  - switchpros-controlled
  - baja-designs
---

# 4.4 Chase Light {#chase-light}

Multi-function rear safety light for convoy visibility, plus integrated brake, turn, and work lighting.

/// html | div.product-info
![Baja Designs RTL-S 30"](../images/baja-designs-rtl-s-30.jpg){ loading=lazy }

**Type:** LED Chase Light Bar

**Model:** RTL-S 30"

**Part Number:** 103004

**Manufacturer:** Baja Designs

**Product Page:** [RTL-S 30"][product-link]

**Quantity:** 1

**Mounting:** Baja Designs tube mounts on rear roll cage

**Power Source:** Multiple (see Functions table)

**Harness:** RTL-S wiring harness (Part #: 640134)

///

## Wiring

### 4-Wire Connector (Main Functions)

| Wire   | Function     | Draw   | Source                                       |
| :----- | :----------- | :----- | :------------------------------------------- |
| Black  | Ground       | -      | Chassis ground                               |
| Red    | Running      | 0.8A   | PMU Out 23 (ignition-switched)               |
| Yellow | Brake        | 1.45A  | OEM brake circuit via [Tail Lights][tail-brake-reverse] |
| Blue   | Work (White) | 1.3A   | PMU Out 23 (shared with running)             |

### 2-Wire Connector (Amber Sections)

| Wire   | Function    | Draw   | Source                                      |
| :----- | :---------- | :----- | :------------------------------------------ |
| Yellow | Right Amber | 0.36A  | CT4 right turn OR SwitchPros OUTPUT-7 (via diode) |
| Blue   | Left Amber  | 0.36A  | CT4 left turn OR SwitchPros OUTPUT-7 (via diode)  |

**Max Draw:** ~4A

**Light Bar Layout:** Solid Red | Flashing Amber | White Center | Flashing Amber | Solid Red

## Control

- **Turn Signals:** CT4 left/right outputs - synced with front turn signals for on-road use
- **Chase Mode:** SwitchPros Button 7 (OUTPUT-7) - both amber sections flash together
- **Isolation:** Diodes prevent backfeed between CT4 and SwitchPros circuits
- **Brake (Red):** OEM brake circuit - taps into existing brake light feed
- **Running + Work (Red/White):** PMU Out 23 - running on with ignition, work light same circuit

```
CT4 Right Turn ──|>|──┬── Yellow (Right Amber)
                      │
SwitchPros OUT7 ─|>|──┘

CT4 Left Turn ───|>|──┬── Blue (Left Amber)
                      │
SwitchPros OUT7 ─|>|──┘
```

## Related Documentation

- [Offroad Lighting Overview][offroad-overview]
- [SwitchPros SP-1200][switchpros-sp-1200]
- [Tail/Brake/Reverse Lights][tail-brake-reverse]

[offroad-overview]: index.md
[switchpros-sp-1200]: ../05-control-interfaces/02-switchpros-sp1200.md
[tail-brake-reverse]: ../03-lighting-systems/04-tail-brake-reverse.md
[product-link]: https://www.bajadesigns.com/products/rtl-led-rear-light-bar/?sku=103004
