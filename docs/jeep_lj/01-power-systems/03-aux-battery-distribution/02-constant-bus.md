---
hide:
  - toc
tags:
  - product-details
  - power-distribution
  - bus-bar
---

# 1.3.2 AUX battery CONSTANT Bus Bar {#rear-constant-bus}

/// html | div.product-info
![Blue Sea 2104 PowerBar](../../images/blue-sea-2104-powerbar.jpg){ loading=lazy }

**Type:** Bus Bar

**Model:** Blue Sea 2104 PowerBar

**Manufacturer:** Blue Sea Systems

**Product Page:** [PowerBar 225A BusBar][product-link]

///

## Overview

Provides organized distribution for accessory circuits in the rear wheel well compartment.

**Location:** Rear wheel well compartment (near battery)

**Power Source:** AUX battery via 1/0 AWG (~3 ft) - see [AUX battery Distribution][rear-battery]

## Specifications

- **Rating:** 225A continuous
- **Terminals:** 4× 3/8"-16 studs
- **Wire Range:** Up to 4/0 AWG
- **Features:** Tin-plated copper, corrosion resistant
- **Full Specs:** [Blue Sea 2104][product-link]

## Load Distribution

| Stud | Connection | Wire Gauge | Distance | Voltage @ Load | Protection | Load | Notes |
|:-----|:-----------|:-----------|:---------|:---------------|:-----------|:-----|:------|
| 1 | **AUX battery+ (INPUT)** | **1/0 AWG ✓** | **~3 ft** | **13.67V (0.9%)** | **None** | **~254A max** | **Power feed from battery - see [AUX battery][rear-battery]** |
| 2 | SwitchPros RCR-Force 12 | 4 AWG ✓ | ~2 ft | 13.51V (0.8%) | 150A CB | ~100A max | Auxiliary lighting control - see [SwitchPros][switchpros] |
| 3 | SafetyHub 150 | 4 AWG ✓ | ~2 ft | 13.51V (0.8%) | 150A CB | ~100A max | ARB compressor, winch trigger - see [SafetyHub][safetyhub] |
| 4 | BODY PDU | 6 AWG ✓ | ~12 ft | 13.40V (4.0% @ 20°C) | 100A CB | ~54A max | Cabin convenience circuits - see [BODY PDU][body-rtmr] |

**Stud Utilization:** 4 of 4 used (0 available for future expansion)

**Total Load:** ~254A max (SwitchPros 100A + BODY PDU 54A + SafetyHub 100A)

**Wire Sizing:** 1/0 AWG feed rated 325A continuous - 0.9% voltage drop @ 254A max load (13.67V at bus)

!!! info "Circuit Protection"
    No circuit breaker between battery and CONSTANT bus. Each load has individual CB protection: SwitchPros (150A), SafetyHub (150A), BODY PDU (100A). See [Circuit Breakers][circuit-breakers].

## Related Documentation

**Power Systems:**

- [AUX battery Distribution][rear-battery] - Complete overview
- [Circuit Breakers][circuit-breakers] - CB specifications

**Connected Systems:**

- [SwitchPros RCR-Force 12][switchpros] - Auxiliary lighting controller
- [SafetyHub 150][safetyhub] - ARB compressor and winch trigger
- [BODY PDU][body-rtmr] - Cabin convenience circuits
- [Installation Checklist][installation] - Bus bar mounting procedure

[product-link]: https://www.bluesea.com/products/2104/PowerBar_225A_BusBar_with_Four_1_4inch-20_Studs
[rear-battery]: index.md
[circuit-breakers]: 01-circuit-breakers.md
[switchpros]: ../../04-control-interfaces/02-switchpros-sp1200.md
[safetyhub]: 04-safetyhub.md
[body-rtmr]: 03-body-pdu.md
[installation]: ../installation-checklist.md#phase-2-power-distribution
