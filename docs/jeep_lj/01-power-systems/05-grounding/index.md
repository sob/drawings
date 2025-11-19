---
hide:
  - toc
---

# 1.5 Grounding Architecture {#grounding-architecture}

Multi-point grounding strategy with high-current grounds to frame rails and low-current grounds to firewall/chassis points.

**Location:** Multiple points (engine bay, AUX battery, firewall, chassis)

## Grounding Infrastructure

| Ground Point | Type | Location | Capacity | Used | Notes |
|:-------------|:-----|:---------|:---------|:-----|:------|
| **START battery (-)** | Battery Terminal | Engine bay | 6 connections | 5 active + 1 future | See [START battery Ground][front-battery-ground] |
| **AUX battery (-)** | Battery Terminal | Rear wheel well | 5 connections | 5 active | See [AUX battery Ground][rear-battery-ground] |
| **Engine Bay Ground Bus** | Blue Sea 2107 PowerBar | Firewall (engine bay) | 8 studs (600A) | 8 (fully assigned) | See [Engine Bay Ground Bus][engine-bay-ground-bus] |
| **Firewall Stud Bus** | Blue Sea 2105 MaxiBus | Firewall (cabin side) | 14 terminals (250A) | 7 assigned | See [Firewall Stud Bus][firewall-stud-bus] |
| **SwitchPros Ground Bus** | Blue Sea 2105 MaxiBus | Near SwitchPros controller | 14 terminals (250A) | 6+ assigned | See [SwitchPros Ground Bus][switchpros-ground-bus] |

## System Components

**Battery Grounds:**

- **[1.6.1 - START battery Ground][front-battery-ground]** - Direct battery negative connections (ECM, radios, infrastructure)
- **[1.6.2 - AUX battery Ground][rear-battery-ground]** - Direct battery negative connections (BCDC, amp, SwitchPros RCR)

**Ground Distribution:**

- **[1.6.3 - Engine Bay Ground Bus][engine-bay-ground-bus]** - Primary infrastructure hub (frame, engine, winch, PMU)
- **[1.6.4 - Firewall Stud Bus][firewall-stud-bus]** - Cabin electronics (BODY PDU, cluster, audio, camera)
- **[1.6.5 - SwitchPros Ground Bus][switchpros-ground-bus]** - Lighting and accessories (headlights, aux lights)

## Testing Requirements

| Test Point | Max Voltage Drop | Test Conditions |
|:-----------|:-----------------|:----------------|
| Battery to frame rail (front) | <0.1V | Engine @ 2000 RPM, DC voltmeter |
| Battery to frame rail (rear) | <0.1V | Engine @ 2000 RPM, DC voltmeter |
| START battery to AUX battery | <0.05V | Engine @ 2000 RPM, DC voltmeter |

**Installation & Testing:** See [Section 1 Installation Checklist][installation]

[installation]: ../installation-checklist.md#phase-1-foundations

[front-battery-ground]: 01-starter-battery-ground.md
[rear-battery-ground]: 02-aux-battery-ground.md
[engine-bay-ground-bus]: 03-engine-bay-ground-bus.md
[firewall-stud-bus]: 04-firewall-stud-bus.md
[switchpros-ground-bus]: 05-switchpros-ground-bus.md
