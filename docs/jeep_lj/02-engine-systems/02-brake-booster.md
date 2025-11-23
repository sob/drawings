---
hide:
  - toc
tags:
  - product-details
  - engine-systems
  - brake-system
  - ibooster
---

# Brake Booster System - Bosch iBooster Gen 2 {#brake-booster-system-bosch-ibooster-gen-2}

**Type:** Bosch iBooster Gen 2 (electric vacuum-independent brake booster)
**Generation:** Gen 2 (eliminates secondary power circuit required by Gen 1)
**Power Source:** PMU Out 1+10 (main power, combined 25A outputs, non-adjacent), Out 19 (ignition signal)
**Installation:** Replaces traditional vacuum brake booster

## Overview

The Bosch iBooster is an electromechanical brake booster that eliminates the need for engine vacuum. Critical for diesel conversions (Cummins R2.8) which produce minimal vacuum. Provides consistent brake assist regardless of engine load or altitude.

**Why Gen 2:** Gen 2 eliminates the secondary 5A constant power circuit required by Gen 1, simplifying wiring and freeing PMU OUT20 for other uses.

/// html | div.product-info

**Type:** Bosch iBooster Gen 2

**Manufacturer:** Bosch Mobility

**Product Page:** [Bosch iBooster][bosch-ibooster]

**Mounting:** Factory brake booster location on firewall

**Power Source:** PMU Out 1+10 (main power), Out 19 (ignition signal)

**Wiring Harness:** [Tulay's Wire Werks Gen 2 Universal Harness][tulays-harness]

**Connector Kit:** [Tulay's Wire Werks Gen 2 Connector Kit][tulays-connector]

///

## Component Specifications

**Type:** Bosch iBooster Gen 2
**Configuration:** Round booster design (vs Gen 1 square design)
**Mounting:** Integrated mounting bolts in housing
**Mounting Bolt Torque:** TBD ft-lb

### Physical Dimensions

- Length: 9.6"
- Width: 7.5"
- Center to top: 3.9"
- Center to bottom: 6.3"
- Booster portion: ~9" diameter circle, 6.5" deep
- Weight: Significantly lighter than Gen 1

### Common Gen 2 Donor Vehicles

- Tesla Model 3
- Tesla Model Y
- 2018+ Honda Accord

**Master Cylinder Compatibility:** Gen 2 master cylinders are NOT interchangeable with Gen 1.

## Power Requirements (Gen 2)

### Main Power (PMU OUT1+10 Combined)

- **Voltage:** 12V CONSTANT (not switched - safety requirement)
- **Current:** 40A peak during active braking, 0.25A idle, 12mA standby
- **PMU Allocation:** 2x 25A outputs paralleled, non-adjacent (OUT1 + OUT10 = 46A capacity @ 40°C)
- **Fusing:** 40A fuse at PMU output (built-in overcurrent protection)
- **Wire gauge:** 2.50 mm² (10 AWG equivalent) red wire per PMU output specification
- **Circuit:** CONSTANT bus → PMU OUT1+10 → iBooster main power connector

### Ignition Signal (PMU OUT19)

- **Voltage:** 12V SWITCHED (ignition RUN)
- **Current:** ~5A
- **PMU Allocation:** OUT19 (7A output)
- **Fusing:** 5A fuse at PMU output
- **Wire gauge:** 0.50 mm² (20 AWG equivalent) green wire
- **Circuit:** Ignition signal → PMU OUT19 → iBooster ignition input
- **Purpose:** Tells iBooster when vehicle is on

### Ground

- **Wire gauge:** 2.50 mm² (10 AWG equivalent) black wire
- **Connection:** Chassis ground (firewall or frame)
- **Circuit:** iBooster ground → chassis ground point

### Secondary Power (Gen 2 Does NOT Require This)

**Gen 1 Difference:** Gen 1 required a third power circuit - 5A CONSTANT power (1.50 mm² red wire). Gen 2 eliminated this requirement.

**PMU Impact:** PMU OUT20 (7A output) is available for other uses since Gen 2 doesn't need secondary power.

## Wiring Summary (Gen 2)

### Power Connections (3 wires total)

1. **Red (2.50 mm² / 10 AWG):** CONSTANT bus → PMU OUT1+10 combined → iBooster main power (40A fused)
2. **Green (0.50 mm² / 20 AWG):** Ignition RUN → PMU OUT19 → iBooster ignition signal (5A fused)
3. **Black (2.50 mm² / 10 AWG):** iBooster ground → chassis ground

### Additional Connections

- **Pedal Travel Sensor Connector:** Internal wiring between pedal sensor and iBooster ECU (integrated in Gen 2, at least 7 wires total between sensor and ECU)
- **CAN Bus (Optional):** Some Gen 2 units support CAN communication for advanced features

## Gen 1 vs Gen 2 Comparison

| Feature                  | Gen 1                              | Gen 2                              |
|:-------------------------|:-----------------------------------|:-----------------------------------|
| **Shape**                | Square booster                     | Round booster                      |
| **Dimensions**           | 6.1" W × 4.9" H (top) × 3.5" H (bottom) | 9.6" L × 7.5" W × 9" circle × 6.5" deep |
| **Weight**               | Heavier                            | Significantly lighter              |
| **Mounting**             | Separate flange piece              | Integrated into housing            |
| **Main Power**           | 40A fused, 4.00 mm² red wire       | 40A fused, 2.50 mm² (10 AWG) red wire |
| **Ignition Signal**      | 5A fused, 0.50 mm² green wire      | 5A fused, 0.50 mm² green wire      |
| **Secondary Power**      | **Required:** 5A fused, 1.50 mm² red wire | **Not required** (eliminated)      |
| **Total Power Wires**    | 4 (including ground)               | 3 (including ground)               |
| **Pedal Travel Sensor**  | External sensor, separate wiring   | Integrated sensor, internal wiring |
| **Master Cylinder**      | Gen 1 specific                     | Gen 2 specific (not interchangeable) |
| **Common Donors**        | Tesla Model S/X, Chevy Malibu/Bolt, Honda CR-V | Tesla Model 3/Y, 2018+ Honda Accord |
| **PMU Outputs**        | OUT5+6 (main), OUT19 (ign), OUT20 (secondary) | OUT1+10 (main), OUT19 (ign), OUT20 available |

**Sources:**

- Physical specifications: LS1TECH forum (iBooster vs Hydroboost detail overview)
- Wiring specifications: Tulay's Wire Werks (Gen-1 and Gen-2 Universal Wire Harness product pages)
- Sensor integration: DIY Electric Car Forums
- Donor vehicles: EVcreate iBooster donor vehicles list

## PMU Configuration

### Output Programming

**OUT1 + OUT10 (Main Power - Combined, Non-Adjacent):**

- Type: 25A high-side outputs, paralleled, non-adjacent terminals
- Capacity: 46A @ 40°C (non-adjacent combining per ECUMaster spec)
- Control: CONSTANT (always on, not switched)
- Load: 40A peak, 0.25A idle
- Utilization: 87% @ 40°C (excellent thermal margin)
- Logic: No switching logic - permanently energized
- Protection: 40A fuse recommended

**OUT19 (Ignition Signal):**

- Type: 7A high-side output
- Control: Auto (ignition RUN)
- Load: ~5A
- Trigger: Ignition signal (Pin 7/In 6)
- Logic: Energizes when ignition in RUN position
- Protection: 5A fuse recommended

**OUT20 (Available for Other Uses):**

- Gen 1 required this output for secondary power
- Gen 2 does not use this output
- Available for future expansion (7A capacity)

## Installation Notes

### Why CONSTANT Power is Required

**Safety Requirement:** iBooster main power must be CONSTANT (not switched with ignition) for several reasons:

1. **Fail-safe operation:** Provides brake assist even if ignition fails
2. **Key-off braking:** Allows brake assist when moving vehicle with engine off
3. **Emergency situations:** Ensures braking capability in all scenarios

**Standby Draw:** 12mA standby current when vehicle is off (negligible battery drain)

### Fail-Safe Standalone Mode

iBooster can operate in "fail-safe standalone mode" with just:

- Main power (40A CONSTANT)
- Chassis ground

This minimal configuration provides basic brake assist without ignition signal or advanced features.

**Full Functionality Requires:**

- Main power (OUT1+10 combined)
- Ignition signal (OUT19)
- Chassis ground
- Pedal travel sensor connection

## Outstanding Items

None - design complete. See [installation checklist][install-checklist] for build tasks.

**Design Decisions (Resolved):**

- **Donor vehicle:** Tesla Model 3
- **Mounting location:** Factory brake booster location on firewall
- **Chassis ground:** Firewall ground stud (same location as factory booster ground)
- **PMU configuration:** See [PMU Outputs][pmu-outputs] - OUT1+10 CONSTANT, OUT19 ignition RUN
- **Wiring harness:** [Tulay's Wire Werks Gen 2 Universal Harness][tulays-harness]

## Installation Resources

- [Wiring the iBooster - EVcreate][evcreate-wiring]
- [Installing the iBooster - EVcreate][evcreate-install]
- [iBooster Donor Vehicles - EVcreate][evcreate-donors]

## Related Documentation

- [PMU Outputs][pmu-outputs] - PMU OUT1+10 and OUT19 specifications
- [START Battery Distribution][starter-battery-distribution] - CONSTANT bus bar configuration
- [Firewall Ingress][firewall-penetrations-ingress-points] - iBooster mounting and wiring routing through firewall

[install-checklist]: installation-checklist.md
[bosch-ibooster]: https://www.bosch-mobility.com/en/solutions/driving-safety/ibooster/
[tulays-harness]: https://tulayswirewerks.com/product/bosch-ibooster-gen-2-universal-wire-harness/
[tulays-connector]: https://tulayswirewerks.com/product/bosch-ibooster-gen-2-connector-kit/
[evcreate-wiring]: https://www.evcreate.com/wiring-the-ibooster/
[evcreate-install]: https://www.evcreate.com/installing-the-ibooster/
[evcreate-donors]: https://www.evcreate.com/ibooster-donor-vehicles/
[pmu-outputs]: ../01-power-systems/04-pmu/03-pmu-outputs.md
[starter-battery-distribution]: ../01-power-systems/02-starter-battery-distribution/index.md
[firewall-penetrations-ingress-points]: 07-firewall-ingress.md
