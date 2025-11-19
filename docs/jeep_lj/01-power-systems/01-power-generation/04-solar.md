---
hide:
  - toc
tags:
  - product-details
  - power-generation
  - solar-panel
---

# 1.1.4 Solar Charging {#solar-charging}

/// html | div.product-info
![Cascadia 4x4 Solar Panel](../../images/cascadia-solar-80w.jpg){ loading=lazy }

**Type:** Flexible Monocrystalline Solar Panel

**Model:** Cascadia 4x4 80W Hood Solar Panel (VSS System for TJ/LJ)

**Manufacturer:** Cascadia 4x4

**Product Page:** [Cascadia 4x4 VSS System][cascadia-solar]

**Retailer:** [ExtremeTerrain - CHF132CV][extremeterrain-solar]

///

## Specifications

- **Output:** 80W maximum (6.7A @ 12V nominal)
- **Type:** Monocrystalline flexible panel
- **Mounting:** Permanently adhered to hood surface
- **Connection:** Wired to BCDC Alpha 25 solar input

## Wiring

**Solar Panel Connections:**

- **Positive (+):** To BCDC Alpha 25 solar input positive terminal
- **Negative (-):** To chassis ground (NOT to BCDC negative)
- **Wire Gauge:** Per Cascadia 4x4 spec (typically 10-12 AWG for 80W)
- **Routing:** Hood → Firewall → BCDC location in wheel well

**Important:** Solar negative connects to chassis ground per REDARC specifications. The BCDC requires a common ground system where all batteries and components share the same ground reference (vehicle chassis).

## Function

80W panel maintains AUX battery during extended stops via BCDC solar input. Full sun output: ~80W (6.7A), variable in partial sun.

BCDC Green Power Priority uses solar first when available, combines with alternator when both sources present. See [BCDC Alpha 25][bcdc] for charging details.

**Installation:** See [Section 1 Installation Checklist][installation-checklist]

**Critical:** Verify polarity before connection - reverse polarity damages BCDC.

[cascadia-solar]: https://www.cascadia4x4.com/
[extremeterrain-solar]: https://www.extremeterrain.com/cascadia-4x4-jeep-wrangler-vss-complete-hood-mounted-solar-system-80-watt-chf132cv.html
[bcdc]: 03-bcdc.md
[installation-checklist]: ../installation-checklist.md#phase-4-integration-wiring
