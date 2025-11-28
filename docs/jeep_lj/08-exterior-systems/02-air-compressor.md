---
hide:
  - toc
tags:
  - product-details
  - exterior-systems
  - air-compressor
  - arb
---

# 8.2 Air Compressor {#air-compressor}

ARB Twin Compressor system with air tank and automatic pressure management for locker operation and tire inflation.

/// html | div.product-info

**Model:** ARB CKBLTA12 Brushless Twin Motor Onboard 12V Air Compressor

**Installation Guide:** [ARB CKBLTA12 Installation PDF](https://store.arbusa.com/content/CKBLTA12%20INST.pdf)

**Maximum Amperage Draw:** 90A total (45A per motor × 2 motors)

**Fuse Configuration:** Dual 60A MIDI fuses via SafetyHub 150 (one per motor)

**Location:** Under passenger seat

///

## Specifications

- Smart Start feature with staggered power-on to reduce startup spike
- 100% duty cycle
- Maximum pressure: 150 PSI
- Air flow at 0 PSI: 9.18 CFM
- IP67 water resistant

## Control System

- **Control:** SwitchPros OUTPUT-11 (15A output, Button 11)
  - OUTPUT-11 provides switched 12V control signal to compressor
  - Compressor has internal relay/control that handles high-current motor switching
  - 14 AWG wire from OUTPUT-11 to compressor control terminal
- **Ground:** 6 AWG black wire from compressor to AUX battery negative (direct connection for 90A return current)

## Wiring

| Circuit       | Source                       | Destination                 | Wire  | Protection | Notes                         |
| ------------- | ---------------------------- | --------------------------- | ----- | ---------- | ----------------------------- |
| Motor 1 Power | SafetyHub MIDI-1 (60A)       | Compressor motor 1 positive | 6 AWG | 60A MIDI   | Via SafetyHub 150A CB         |
| Motor 2 Power | SafetyHub MIDI-2 (60A)       | Compressor motor 2 positive | 6 AWG | 60A MIDI   | Via SafetyHub 150A CB         |
| Ground        | Compressor negative terminal | AUX battery negative        | 6 AWG | None       | Direct for 90A return current |
| Control       | SwitchPros OUTPUT-11         | Compressor control terminal | 14 AWG | 15A        | Auto or manual activation     |

**Wiring Summary:**

1. **Motor 1 Power (+):** CONSTANT bus → SafetyHub (150A breaker) → SafetyHub MIDI-1 (60A) → 6 AWG → compressor motor 1
2. **Motor 2 Power (+):** CONSTANT bus → SafetyHub (150A breaker) → SafetyHub MIDI-2 (60A) → 6 AWG → compressor motor 2
3. **Ground (-):** Compressor negative terminal → 6 AWG → AUX battery negative
4. **Control (Automatic):** Pressure switch (ARB 180901) → SwitchPros TRIGGER-3 (Pin 17) → OUTPUT-11 → compressor control
5. **Control (Manual Override):** SwitchPros Button 11 → OUTPUT-11 → compressor control

---

## Air Tank

### ARB 1-Gallon Air Tank

**Model:** ARB 171601

**Product Page:** [ARB 1-Gallon Air Tank](https://www.amazon.com/ARB-171601-Steel-Tank/dp/B00IAAU66K)

| Spec             | Value                                |
| ---------------- | ------------------------------------ |
| Capacity         | 1 gallon (4 liters)                  |
| Working Pressure | 150 PSI maximum                      |
| Material         | Forged aluminum                      |
| Mounting         | Under passenger seat (with compressor) |
| Ports            | 2 ports (input from compressor, output to manifold) |

**Purpose:**

- Instant locker engagement (no waiting for compressor to build pressure)
- Reduces compressor cycling frequency
- Multiple locker uses per tank fill
- Quick tire pressure adjustments
- Air reserve for emergency use

---

## Pressure Switch

### ARB Pressure Switch

**Model:** ARB 180901

**Product Page:** [ARB Pressure Switch](https://store.arbusa.com/compressor-pressure-switch-180901/)

| Spec             | Value                    |
| ---------------- | ------------------------ |
| Cut-In Pressure  | 135 PSI (compressor starts) |
| Cut-Out Pressure | 150 PSI (compressor stops)  |
| Mounting         | On air manifold          |
| Electrical       | Low-current switch (<1A) |

**Function:**

- Monitors tank pressure continuously
- Automatically activates compressor when pressure drops below 135 PSI
- Automatically deactivates compressor when pressure reaches 150 PSI
- Integrated with SwitchPros TRIGGER-3 for automatic control

---

## Air Manifold

**Configuration:** 4-6 port brass manifold

**Location:** Under passenger seat (with compressor and tank)

**Port Assignments:**

1. **Input:** Compressor output → manifold input
2. **Output 1:** Manifold → Front locker solenoid (1/4" air line)
3. **Output 2:** Manifold → Rear locker solenoid (1/4" air line)
4. **Output 3:** Manifold → [Rear Air Chuck Plate][rear-air-chuck] (1/4" air line)
5. **Output 4:** Manifold → Pressure gauge (0-200 PSI, panel-mounted)
6. **Output 5:** Manifold → Pressure switch (ARB 180901)

---

## Automatic Pressure Control

### SwitchPros Integration

**Control Architecture:**

```text
Air Tank Pressure Switch (ARB 180901)
    ↓ (trigger signal when pressure < 135 PSI)
SwitchPros TRIGGER-3 (Pin 17, PINK wire)
    ↓
SwitchPros Logic: TRIGGER-3 OR Button 11 → OUTPUT-11
    ↓
OUTPUT-11 activates compressor
    ↓
Compressor fills tank to 150 PSI → pressure switch opens → compressor stops
```

**SwitchPros Programming:**

- **TRIGGER-3 Input:** Pressure switch signal (tank < 135 PSI activates trigger)
- **OUTPUT-11 Logic:** Button 11 OR TRIGGER-3 → OUTPUT-11 (compressor)
- **Manual Override:** Press Button 11 anytime to force compressor on (e.g., for tire inflation)
- **Automatic Mode:** TRIGGER-3 maintains tank pressure 135-150 PSI without user intervention

**Operational Modes:**

| Mode                | Control Method                | Use Case                                                   |
| ------------------- | ----------------------------- | ---------------------------------------------------------- |
| **Automatic**       | Pressure switch via TRIGGER-3 | Normal operation - system maintains pressure automatically |
| **Manual Override** | Button 11 (latching mode)     | Tire inflation - keep compressor running continuously      |
| **Off**             | Button 11 off + tank > 135 PSI | Compressor idle, tank maintains pressure for locker use   |

### Pressure Switch Wiring

| Circuit                 | Source                          | Destination                   | Wire   | Protection         |
| ----------------------- | ------------------------------- | ----------------------------- | ------ | ------------------ |
| Pressure Switch Trigger | Pressure switch signal terminal | SwitchPros TRIGGER-3 (Pin 17) | 18 AWG | None (low current) |

---

## Safety Considerations

!!! warning "Compressor Operation"
    - Monitor compressor duty cycle during extended use
    - Allow cooling periods if running continuously for tire inflation
    - Check air line connections regularly for leaks
    - Drain moisture from tank/system periodically

## Outstanding Items

- [ ] Verify ARB CKBLTA12 wiring harness connector pinout for motor 1, motor 2, and control terminals
- [ ] Confirm under-seat mounting bracket/location for compressor and 1-gallon tank
- [ ] Source 4-6 port air manifold with 1/4" NPT fittings
- [ ] Order 0-200 PSI pressure gauge (panel-mount or in-line)

## Related Documentation

- [Air Lockers][air-lockers] - ARB RD116 front/rear lockers
- [Rear Air Chuck][rear-air-chuck] - External air access plate
- [SafetyHub][safetyhub] - Compressor power distribution
- [SwitchPros][switchpros] - Compressor control (OUTPUT-11, TRIGGER-3)

[air-lockers]: 03-air-lockers.md
[rear-air-chuck]: 04-rear-air-chuck.md
[safetyhub]: ../01-power-systems/03-aux-battery-distribution/04-safetyhub.md
[switchpros]: ../05-control-interfaces/02-switchpros-sp1200.md
