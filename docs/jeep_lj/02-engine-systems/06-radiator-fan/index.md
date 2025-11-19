---
hide:
  - toc
---

# 2.6 Radiator Fan System {#radiator-fan-system}

## System Overview

Electric radiator fan with automatic temperature control. Dakota Digital PAC-2800BT controller monitors coolant temperature via J1939 CAN bus and activates fan via 70A relay.

**Components:**

- GM 84100128 Camaro electric radiator fan (brushless, 53A @ full speed)
- Dakota Digital PAC-2800BT controller (Bluetooth programmable, cabin-mounted)
- BIM-01-2 adapter (J1939 CAN bus translation)
- External relay (Bosch-style, included with controller, engine bay-mounted)

**Operation:**

- ECM broadcasts coolant temp on J1939 CAN bus
- BIM-01-2 translates J1939 messages for PAC-2800BT (cabin)
- When temp exceeds setpoint: PAC-2800BT triggers ground to relay (engine bay)
- Relay closes → fan runs at full speed
- When temp drops: PAC-2800BT releases ground → relay opens → fan stops

**Power:**

- **Controller:** Critical Cabin PDU (5A) → PAC-2800BT (cabin)
- **Relay:** CONSTANT bus (80A CB) → Relay Terminal 30 → Terminal 87 → Fan motor

**Note:** Main radiator fan only. Oil cooler and PS cooler fans controlled separately via PMU.

## Programming

**Via Bluetooth App (iOS/Android):**

1. Download Dakota Digital app
2. Power controller and pair via Bluetooth
3. Set temperature setpoints:
   - **Activation:** TBD (typically 195-205°F)
   - **Deactivation:** TBD (typically 185-195°F)
4. Test and adjust during shakedown runs

**Recommended for R2.8:** 200°F activation, 190°F deactivation

## Installation

**Mounting:**

- PAC-2800BT controller: Dakota Digital HDPE panel (cabin, with other Dakota Digital modules)
- BIM-01-2 adapter: Same HDPE panel
- External relay: Engine bay (near fan, weatherproof location)
- 80A circuit breaker: Engine bay (near CONSTANT bus)

**Power Wiring:**

- **Controller:** Critical Cabin PDU Slot 1 (5A) → PAC-2800BT (16 AWG)
- **Relay high-current:** CONSTANT bus → 80A CB → Relay Terminal 30 (4 AWG)
- **Relay output:** Terminal 87 → Fan motor (+) (4 AWG)
- **Relay coil:** CONSTANT bus → 80A CB → Terminal 86 (18 AWG, shares power with Terminal 30)
- **Relay trigger:** PAC-2800BT → through firewall → Terminal 85 (18 AWG)
- **Fan ground:** Fan motor (-) → Engine bay ground bus (4 AWG)

**CAN Bus:**

- BIM-01-2 adapter taps J1939 at Dakota Digital gauge cluster
- BIM-01-2 3-wire cable provides power, ground, and data to PAC-2800BT

**Testing:**

- Program temperature setpoints via Bluetooth
- Verify fan activation at setpoint
- Check voltage at fan motor (>13V with engine running)
- Verify relay trigger signal from controller

## Wire Sizing

**Fan Motor Circuit:** 4 AWG @ 53A, 26 ft total (relay to fan), 60°C: 3.4% drop (0.41V) ✅

**Relay Power Input:** 4 AWG (CONSTANT bus via 80A CB, ~3 ft)

**Controller Power:** 16 AWG (Critical Cabin PDU, <1A, <2 ft)

**Relay Trigger:** 18 AWG (cabin to engine bay, ~8 ft, low current)

**Note:** Fan is brushless PWM-capable but runs full speed (53A) with on/off relay control.

## Components

- **[2.6.1 Fan Motor][fan-motor]** - Camaro electric fan, power wiring, wire sizing
- **[2.6.2 Fan Controller][fan-controller]** - Dakota Digital PAC-2800BT, CAN integration, relay control

## Outstanding Items

- [ ] Source 80A circuit breaker for relay power
- [ ] Determine optimal temperature setpoints for R2.8
- [ ] Test voltage drop under load at fan terminals
- [ ] Confirm CAN tap location at Dakota Digital gauge cluster
- [ ] Determine relay mounting location in engine bay
- [ ] Determine firewall grommet for relay trigger wire

## Related Documentation

- [Firewall Ingress][firewall-ingress] - Relay trigger wire through firewall
- [Critical Cabin PDU][cabin-pdu] - Controller power source
- [CONSTANT Bus][constant-bus] - Relay power source (Terminal 30 + Terminal 86)
- [PMU Outputs][pmu-outputs] - Oil cooler and PS cooler fans (PMU controlled)
- [Dakota Digital Gauge Cluster][gauge-cluster] - J1939 CAN bus tap location
- [Engine Bay Ground Bus][ground-bus] - Ground connection location

[fan-motor]: 01-fan-motor.md
[fan-controller]: 02-fan-controller.md
[firewall-ingress]: ../07-firewall-ingress.md
[cabin-pdu]: ../../01-power-systems/02-starter-battery-distribution/03-critical-cabin-pdu.md
[constant-bus]: ../../01-power-systems/02-starter-battery-distribution/02-constant-bus.md
[pmu-outputs]: ../../01-power-systems/04-pmu/03-pmu-outputs.md
[gauge-cluster]: ../../04-control-interfaces/04-gauge-cluster.md
[ground-bus]: ../../01-power-systems/05-grounding/03-engine-bay-ground-bus.md
