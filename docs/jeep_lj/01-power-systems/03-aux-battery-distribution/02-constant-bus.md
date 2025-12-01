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
![Blue Sea 2107 PowerBar](../../images/blue-sea-2107-powerbar.jpg){ loading=lazy }

**Type:** Bus Bar

**Model:** Blue Sea 2107 PowerBar

**Manufacturer:** Blue Sea Systems

**Product Page:** [PowerBar 600A BusBar][product-link]

///

## Overview

Provides organized distribution for accessory circuits in the rear wheel well compartment.

**Location:** Rear wheel well compartment (near battery)

## Specifications

- **Rating:** 600A continuous
- **Terminals:** 8× 3/8"-16 studs
- **Wire Range:** Up to 4/0 AWG
- **Features:** Tin-plated copper, corrosion resistant
- **Full Specs:** [Blue Sea 2107][product-link]

!!! info "Circuit Protection"
No circuit breaker between battery and CONSTANT bus. Each load has individual CB protection: SwitchPros (150A), SafetyHub (150A), BODY PDU (100A), Fusion Amp (100A). See [Circuit Breakers][circuit-breakers].

## Load Distribution

| Stud | Connection                 | Wire Gauge | Distance | Voltage Drop | Protection | Load      | Notes                           |
| :--- | :------------------------- | :--------- | :------- | :----------- | :--------- | :-------- | :------------------------------ |
| 1    | **AUX battery+ (INPUT)**   | 1/0 AWG    | ~3 ft    | 0.9% @ 20°C  | None       | ~332A max | See [AUX battery][rear-battery] |
| 2    | [SwitchPros][switchpros]   | 2 AWG      | ~2 ft    | 0.4% @ 20°C  | 150A CB    | ~100A max | Auxiliary lighting              |
| 3    | [SafetyHub 150][safetyhub] | 2 AWG      | ~2 ft    | 0.4% @ 20°C  | 150A CB    | ~100A max | ARB compressor, winch trigger   |
| 4    | [BODY PDU][body-rtmr]      | 2 AWG      | ~12 ft   | 1.2% @ 20°C  | 100A CB    | ~54A max  | Cabin circuits                  |
| 5    | [Fusion Apollo Amp][audio] | 4 AWG      | TBD      | TBD          | 100A CB    | 78A max   | 6-channel amplifier             |
| 6-8  | _(Available)_              | -          | -        | -            | -          | -         | Future expansion                |

**Stud Utilization:** 5 of 8 used (3 available)

## Related Documentation

**Power Systems:**

- [AUX battery Distribution][rear-battery] - Complete overview
- [Circuit Breakers][circuit-breakers] - CB specifications

**Connected Systems:**

- [SwitchPros RCR-Force 12][switchpros] - Auxiliary lighting controller
- [SafetyHub 150][safetyhub] - ARB compressor and winch trigger
- [BODY PDU][body-rtmr] - Cabin convenience circuits
- [Installation Checklist][installation] - Bus bar mounting procedure

[product-link]: https://www.bluesea.com/products/2107/PowerBar_600A_BusBar_-_Eight_3_8in-16_Studs__
[rear-battery]: index.md
[circuit-breakers]: 01-circuit-breakers.md
[switchpros]: ../../05-control-interfaces/02-switchpros-sp1200.md
[safetyhub]: 04-safetyhub.md
[body-rtmr]: 03-body-pdu.md
[audio]: ../../06-audio-systems/02-amplifier.md
[installation]: ../../09-installation/02-power-systems-checklist.md#phase-2-power-distribution
