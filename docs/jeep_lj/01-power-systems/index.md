---
hide:
  - toc
---

# Section 1: Power Systems {#power-systems}

## System Overview

The Jeep LJ uses a dual-battery electrical system with intelligent power distribution and programmable power management.

### Power Generation & Storage

- **Starter Battery:** Odyssey PC1500 (850 CCA, 68 Ah) in engine bay - critical systems only
- **Aux Battery:** Odyssey PC1500 (850 CCA, 68 Ah) in wheel well - accessories, inverter, winch (jump start capable)
- **RedArc BCDC Alpha 25:** DC-DC charger/isolator - batteries operate independently when isolated
- **270A Alternator:** Charges starter battery, BCDC charges aux battery from front

See [Power Generation](01-power-generation/index.md) for complete details on batteries, alternator, BCDC, and solar charging.

### Power Distribution

Both batteries use CONSTANT bus bars for organized distribution with individual circuit breaker protection:

- **[Starter Battery Distribution](02-starter-battery-distribution/index.md):** CONSTANT bus (Blue Sea 2107, 600A) feeds PMU, SafetyHub, BCDC
- **[Aux Battery Distribution](03-aux-battery-distribution/index.md):** CONSTANT bus (Blue Sea 2104, 225A) feeds SwitchPros, Body RTMR

The system replaces the factory TIPM with modular programmable controllers:

- **[PMU24](04-pmu/index.md):** 24-channel programmable power management - engine bay critical circuits
- **[Body RTMR](03-aux-battery-distribution/04-body-rtmr.md):** Cabin convenience circuits - radio, USB, heated seats, camera
- **[SafetyHub](02-starter-battery-distribution/04-safetyhub.md):** High-current safety circuits - ARB compressor, winch contactor

Ground distribution architecture:

- **[Grounding Architecture](05-grounding/index.md):** Battery grounds, engine bay ground bus, firewall stud bus, distributed grounding system
