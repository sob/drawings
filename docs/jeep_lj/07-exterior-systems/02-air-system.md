---
hide:
  - toc
tags:
  - product-details
  - exterior-systems
  - air-compressor
  - air-lockers
  - arb
---

# Air System - ARB Compressor & Lockers {#air-system-arb-compressor-lockers}
## System Overview

The air system consists of an ARB Twin Compressor (brushless), 1-gallon air tank, and automatic pressure switch that powers both ARB air lockers and provides air for tire inflation, air tools, and other pneumatic accessories. The system features automatic pressure maintenance (135-150 PSI) via SwitchPros TRIGGER-3 integration, with manual override control via Button 11.

## ARB Twin Compressor (Brushless)

### Specifications

/// html | div.product-info

**Model:** ARB CKBLTA12 Brushless Twin Motor Onboard 12V Air Compressor

**Installation Guide:** [ARB CKBLTA12 Installation PDF](https://store.arbusa.com/content/CKBLTA12%20INST.pdf)

**Maximum Amperage Draw:** 90A total (45A per motor × 2 motors)

**Fuse Configuration:** Dual 60A MIDI fuses via SafetyHub 150 (one per motor)

- **Motor 1:** SafetyHub MIDI-1 (60A) → 10 AWG power wire → compressor motor 1
- **Motor 2:** SafetyHub MIDI-2 (60A) → 10 AWG power wire → compressor motor 2
- SafetyHub mounted in engine compartment (close to CONSTANT bus bar)

///

### Features

- Smart Start feature with staggered power-on to reduce startup spike
- 100% duty cycle
- Maximum pressure: 150 PSI
- Air flow at 0 PSI: 9.18 CFM
- IP67 water resistant

### Control System

- **Control:** SwitchPros OUTPUT-11 (15A output, Button 11)
  - OUTPUT-11 provides switched 12V control signal to compressor
  - Compressor has internal relay/control that handles high-current motor switching
  - 14 AWG wire from OUTPUT-11 to compressor control terminal
- **Ground:** 8 AWG black wire from compressor to chassis ground or battery negative
- **Location:** Under passenger seat (cabin, AUX battery area)

### Wiring Summary

1. **Motor 1 Power (+):** CONSTANT bus → SafetyHub (Blue Sea 100A breaker) → SafetyHub MIDI-1 (60A) → 10 AWG red wire → compressor motor 1 positive
2. **Motor 2 Power (+):** CONSTANT bus → SafetyHub (Blue Sea 100A breaker) → SafetyHub MIDI-2 (60A) → 10 AWG red wire → compressor motor 2 positive
3. **Ground (-):** Compressor negative terminal → 8 AWG black wire → chassis ground or battery negative
4. **Control (Automatic):** Pressure switch (ARB 180901) → SwitchPros TRIGGER-3 (Pin 17) → OUTPUT-11 → compressor control (auto 135-150 PSI)
5. **Control (Manual Override):** SwitchPros Button 11 → OUTPUT-11 → compressor control (manual on/off for tire inflation)

### Outstanding Items

- [ ] Route dual 10 AWG power wires from SafetyHub (engine bay) to compressor (under passenger seat)
- [ ] Route 8 AWG ground wire from compressor to nearest chassis ground point
- [ ] Route 14 AWG control wire from SwitchPros OUTPUT-11 to compressor control terminal
- [ ] Route pressure switch trigger wire from air tank to SwitchPros TRIGGER-3 (Pin 17, PINK)
- [ ] Verify ARB CKBLTA12 wiring harness connector pinout for motor 1, motor 2, and control terminals
- [ ] Confirm under-seat mounting bracket/location for compressor and 1-gallon tank

## Air Tank & Pressure Management

### ARB 1-Gallon Air Tank

**Model:** ARB 171601
**Product Page:** [ARB 1-Gallon Air Tank](https://www.amazon.com/ARB-171601-Steel-Tank/dp/B00IAAU66K)
**Capacity:** 1 gallon (4 liters)
**Working Pressure:** 150 PSI maximum
**Material:** Forged aluminum
**Mounting:** Under passenger seat (with compressor)
**Ports:** 2 ports (input from compressor, output to manifold)

**Purpose:**
- Instant locker engagement (no waiting for compressor to build pressure)
- Reduces compressor cycling frequency
- Multiple locker uses per tank fill
- Quick tire pressure adjustments
- Air reserve for emergency use

### ARB Pressure Switch

**Model:** ARB 180901
**Product Page:** [ARB Pressure Switch](https://store.arbusa.com/compressor-pressure-switch-180901/)
**Cut-In Pressure:** 135 PSI (compressor starts)
**Cut-Out Pressure:** 150 PSI (compressor stops)
**Mounting:** On air tank or manifold
**Electrical:** Low-current switch (<1A)

**Function:**
- Monitors tank pressure continuously
- Automatically activates compressor when pressure drops below 135 PSI
- Automatically deactivates compressor when pressure reaches 150 PSI
- Integrated with SwitchPros TRIGGER-3 for automatic control

### Air Manifold

**Configuration:** 4-6 port brass manifold or ARB-specific manifold
**Location:** Under passenger seat (with compressor and tank)

**Port Assignments:**
1. **Input:** Compressor output → manifold input
2. **Output 1:** Manifold → Front locker solenoid (1/4" air line)
3. **Output 2:** Manifold → Rear locker solenoid (1/4" air line)
4. **Output 3:** Manifold → Air chuck/quick-connect (cabin-accessible for tire inflation)
5. **Output 4:** Manifold → Pressure gauge (0-200 PSI, panel-mounted for visibility)
6. **Output 5:** Manifold → Pressure switch (ARB 180901)

### Automatic Pressure Control (SwitchPros Integration)

**Control Architecture:**

```
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

| Mode | Control Method | Use Case |
|------|---------------|----------|
| **Automatic** | Pressure switch via TRIGGER-3 | Normal operation - system maintains pressure automatically |
| **Manual Override** | Button 11 (latching mode) | Tire inflation - keep compressor running continuously |
| **Off** | Button 11 off + tank > 135 PSI | Compressor idle, tank maintains pressure for locker use |

### Wiring Details

| Circuit | Source | Destination | Wire Gauge | Protection | Function |
|---------|--------|-------------|------------|------------|----------|
| Pressure Switch Trigger | Pressure switch signal terminal | SwitchPros TRIGGER-3 (Pin 17) | 18 AWG | None (low current) | Auto compressor control |
| Pressure Switch Power | Tank pressure (mechanical) | Switch contacts | N/A | N/A | Pressure sensing |
| Compressor Control | SwitchPros OUTPUT-11 | Compressor control terminal | 14 AWG | OUTPUT-11 (15A) | Manual/auto compressor on/off |

### Outstanding Items

- [ ] Order ARB 1-gallon air tank (171601)
- [ ] Order ARB pressure switch (180901)
- [ ] Source 4-6 port air manifold with 1/4" NPT fittings
- [ ] Order 0-200 PSI pressure gauge (panel-mount or in-line)
- [ ] Determine air chuck mounting location (under seat access or cabin mount)
- [ ] Route pressure switch trigger wire from manifold to SwitchPros TRIGGER-3
- [ ] Configure SwitchPros: TRIGGER-3 OR Button 11 → OUTPUT-11 (compressor)
- [ ] Install pressure gauge for tank monitoring (accessible from cabin)
- [ ] Plan under-seat mounting bracket for compressor + tank + manifold assembly

## ARB Air Lockers

### Specifications

- **Model (Front and Rear):** ARB RD116 Air Locker
  - Dana 44, 30 spline, 3.92 & up air operated locking differential
  - Solenoid amperage draw: ~2A per locker
- **Front Locker Control:** SwitchPros OUTPUT-17 (low-side driver, 2A)
- **Rear Locker Control:** SwitchPros OUTPUT-10 (15A output, 2A draw)
- **Compressor:** Shared with ARB CKBLTA12 Twin Compressor above

### Axle Configuration

- **Front Axle:** Dana 44, 30 spline, 5.38 gear ratio → Compatible with RD116
- **Rear Axle:** Dana 44, 30 spline, 5.38 gear ratio → Compatible with RD116

### Wiring

- Each locker has a solenoid valve that controls air flow to engage/disengage the differential lock
- Solenoid controlled by SwitchPros outputs (2A draw each)
- Air lines run from compressor to each locker
- Requires 8A minimum ignition/ACC power circuit for switch wiring

### Air Line Routing

!!! info "Air Line Installation"
    Air lines from compressor must be routed to both front and rear axles with proper protection from heat, abrasion, and road debris.

- **Front Locker Air Line:** Compressor → along frame rail → through front axle housing to RD116 solenoid
- **Rear Locker Air Line:** Compressor → along frame rail → through rear axle housing to RD116 solenoid
- **Line Type:** ARB air line kit (typically 1/4" OD nylon tubing)
- **Fittings:** Push-to-connect fittings at compressor and locker ends
- **Protection:** Route inside frame rails where possible, use protective sleeving in exposed areas

### Control Integration

| Component | SwitchPros Output | Current Draw | Function |
|-----------|------------------|--------------|----------|
| ARB Compressor | OUTPUT-11 | Control signal only (~100mA) | Powers compressor on/off |
| Front Locker | OUTPUT-17 | 2A | Engages/disengages front diff lock |
| Rear Locker | OUTPUT-10 | 2A | Engages/disengages rear diff lock |

### Outstanding Items

- [ ] Route ARB locker solenoid control wiring from SwitchPros to front/rear axles
- [ ] Route air lines from manifold (under passenger seat) to front/rear axles
- [ ] Plan air line protection (sleeving, frame rail routing, heat protection)
- [ ] Verify ARB RD116 compatibility with Dana 44 30-spline 5.38 gear ratio
- [ ] Order ARB air line installation kit with 1/4" fittings for front/rear lockers

## System Integration

### Power Flow Diagram

```
CONSTANT Bus (AUX battery)
    │
    ├─→ SafetyHub 150 (Blue Sea 100A breaker)
    │       ├─→ MIDI-1 (60A) → 10 AWG → Compressor Motor 1
    │       └─→ MIDI-2 (60A) → 10 AWG → Compressor Motor 2
    │
ARB Twin Compressor → 1-Gallon Air Tank (150 PSI max) → Air Manifold
    │                                          │
    │                                          ├─→ Front Locker Solenoid
    │                                          ├─→ Rear Locker Solenoid
    │                                          ├─→ Air Chuck (tire inflation)
    │                                          ├─→ Pressure Gauge
    │                                          └─→ Pressure Switch (ARB 180901)
    │                                                  │
    │                                                  ↓ (trigger signal 135-150 PSI)
SwitchPros SP-1200
    ├─→ TRIGGER-3 (Pin 17) ← Pressure Switch (auto control)
    ├─→ Button 11 (manual override)
    │       ↓
    ├─→ OUTPUT-11 → 14 AWG → Compressor Control (auto OR manual)
    ├─→ OUTPUT-17 → Low-side driver → Front Locker Solenoid (2A)
    └─→ OUTPUT-10 → 15A output → Rear Locker Solenoid (2A)
```

### Operational Sequence

**System Startup (Automatic):**
1. Vehicle ignition ON
2. Pressure switch monitors tank pressure
3. If tank pressure < 135 PSI:
   - Pressure switch closes → TRIGGER-3 activates → OUTPUT-11 energizes
   - Compressor starts (Smart Start: Motor 1, then Motor 2)
   - Tank fills to 150 PSI
   - Pressure switch opens → TRIGGER-3 deactivates → OUTPUT-11 off → compressor stops
4. Tank maintains 135-150 PSI automatically without user intervention

**Trail Use (Locker Engagement):**
1. **Front Locker:**
   - Press Button 9 (OUTPUT-17)
   - Solenoid opens, pressurized air from tank → front locker
   - Front differential locks **instantly** (no waiting for compressor)
   - Release Button 9 to disengage

2. **Rear Locker:**
   - Press Button 10 (OUTPUT-10)
   - Solenoid opens, pressurized air from tank → rear locker
   - Rear differential locks **instantly**
   - Release Button 10 to disengage

3. **Automatic Refill:**
   - After multiple locker uses, tank pressure drops below 135 PSI
   - Pressure switch automatically activates compressor to refill tank
   - No user action required

**Manual Compressor Override (Tire Inflation):**
1. Press and hold Button 11 (latching mode)
2. Compressor runs continuously regardless of tank pressure
3. Use air chuck for tire inflation/deflation
4. Press Button 11 again to return to automatic pressure control mode

**Emergency/Backup Mode:**
- If pressure switch fails: Manual Button 11 control still available
- If tank pressure low: Lockers still work but may engage slower (direct compressor fill)

### Safety Considerations

!!! warning "Locker Operation"
    - Only engage lockers at low speeds (typically <5 mph)
    - Disengage lockers before returning to normal speeds
    - Never engage lockers on dry pavement
    - Ensure adequate air pressure before engaging lockers

!!! warning "Compressor Operation"
    - Monitor compressor duty cycle during extended use
    - Allow cooling periods if running continuously for tire inflation
    - Check air line connections regularly for leaks
    - Drain moisture from tank/system periodically

## Future Expansion Options

- **Larger Air Tank:** Upgrade from 1-gallon to 2.5-gallon tank for extended use and air tool capability
- **ARB E-Z Deflator Kit:** Quick tire deflation for off-road use
- **Air Tool Integration:** Impact wrench, air-powered tools (requires larger tank for sustained use)
- **Cabin Air Chuck Mount:** Quick-disconnect air chuck mounted in cabin for convenient access
- **Dual Pressure Gauges:** Separate gauges for tank pressure and line pressure monitoring
