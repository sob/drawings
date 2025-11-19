---
hide:
  - toc
tags:
  - product-details
  - engine-systems
  - hvac
  - climate-control
---

# HVAC System {#hvac-system}

/// html | div.product-info

**System:** Factory TJ (2005 LJ) HVAC System

**Power Source:** PMU Out 1 (A/C clutch) and Out 3 (blower motor)

**Control:** Factory TJ HVAC control panel

///

## System Overview

Factory 2005 TJ HVAC system with heater and A/C. Uses vacuum-operated mode doors, cable-operated temperature blend door, and factory dash control panel. Requires only 2 PMU outputs (blower + A/C clutch). R2.8 intake manifold provides vacuum for mode door actuation.

## Factory TJ HVAC Components

### HVAC Box Assembly

- **Type:** Factory 2005 TJ HVAC box (under dash, complete assembly)
- **Location:** Under dashboard, passenger side (factory location)
- **Components:**
  - Integrated heater core
  - Integrated A/C evaporator
  - Blower motor with resistor pack
  - Vacuum-operated mode door actuators (defrost/floor/vent)
  - Cable-operated temperature blend door
- **Mounting:** Factory TJ mounting points on firewall

### Blower Motor

- **Type:** Factory TJ blower motor (integrated in HVAC box)
- **Speed Control:** 4-speed resistor pack (Off, Low, Med, High)
- **Power:** PMU Out 3 (15A capacity, ~20A at max speed)
- **Control:** Factory dash rotary switch → resistor pack
- **Load:** 3-5A (low), 10-15A (med), ~20A (high)
- **Ground:** Chassis ground at HVAC box mounting point

**Speed Control:** Dash rotary switch selects resistor (Low/Med) or bypasses (High). PMU Out 3 provides power when ignition ON.

### A/C Compressor Clutch

- **Type:** R2.8 Cummins A/C compressor clutch
- **Power:** PMU Out 1 (15A capacity)
- **Trigger Source:** Factory TJ A/C button on dash panel
- **Load:** 3-5A typical for clutch coil
- **Protection:** PMU Out 1 integrated overcurrent protection

**PMU Integration:**
- Factory A/C switch signal → PMU In 9
- PMU Out 1 activates A/C clutch when:
  - A/C button pressed (In 9 active)
  - Battery voltage adequate (optional logic)
  - Optional: A/C pressure switch OK

### Temperature Control (Mechanical Cable)

- **Type:** Cable-operated blend door
- **Control:** Factory dash temperature knob
- **Function:** Cable mechanically moves blend door to mix hot/cold air
- **No PMU outputs needed** - 100% mechanical

### Mode Control (Vacuum-Operated)

**Mode Doors:** Vacuum-operated actuators control airflow direction
- **Defrost:** Directs air to windshield
- **Floor:** Directs air to floor vents
- **Dash Vents:** Directs air to dash vents
- **Bi-Level:** Combination of floor and dash vents

**Vacuum Source:** R2.8 intake manifold → check valve → reservoir → dash switch → mode actuators

**Control:** Factory dash rotary mode selector (pneumatic, no PMU outputs needed)

### Factory HVAC Control Panel

**Type:** Factory 2005 TJ dash-mounted HVAC control panel
**Location:** Center dash stack (factory location)

**Controls:**
- **Temperature Knob:** Rotary control, cold ← → hot (cable-operated)
- **Mode Selector:** Rotary control, defrost/floor/vent positions (vacuum-operated)
- **Blower Speed Knob:** Rotary selector, off/low/med/high (resistor pack)
- **A/C Button:** Toggle, on/off (electrical signal to PMU)
- **Recirculation Switch:** Toggle, fresh air/recirculate (vacuum-operated)

**Power:** 12V for A/C button backlighting only (minimal current)
**Wiring:** A/C button signal wire connects to PMU In 9

## PMU Wiring Integration

### Power Distribution

**PMU Outputs:**

| Output | Circuit | Connection | Load | Notes |
|:-------|:--------|:-----------|:-----|:------|
| **Out 1** | A/C Clutch | A/C compressor clutch coil | 3-5A | Triggered by PMU In 9 (A/C button on factory panel) |
| **Out 3** | Blower Motor Power | Factory blower motor power feed | ~20A | Constant power when ignition on, resistor pack controls speed |

**PMU Inputs:**

| Input | Function | Source | Notes |
|:------|:---------|:-------|:------|
| **In 9** | A/C Request | Factory TJ A/C button signal | 12V signal when A/C button pressed |

### Wiring Diagram

```
Factory TJ HVAC Control Panel
        |
        ├─ Temperature Knob ──────→ Blend Door Cable (mechanical)
        ├─ Mode Selector ─────────→ Vacuum Lines → Mode Door Actuators (vacuum)
        ├─ Blower Speed Knob ─────→ Resistor Pack → Blower Motor (electrical)
        ├─ A/C Button ────────────→ PMU In 9 (electrical signal)
        └─ Recirc Switch ─────────→ Vacuum Lines → Recirc Door Actuator (vacuum)

PMU
        |
        ├─ Out 1 (A/C Clutch) ─────→ A/C Compressor Clutch Coil
        └─ Out 3 (Blower Power) ───→ Factory Blower Motor → Resistor Pack → Blower Motor

R2.8 Engine
        |
        └─ Intake Manifold Vacuum Port → Vacuum Reservoir → Factory HVAC Vacuum System
```

## Vacuum System Installation

### Components Required

| Component | Qty | Cost | Notes |
|:----------|:----|:-----|:------|
| Vacuum line (1/4" ID) | 10-15 ft | $10-20 | Connect engine to HVAC box |
| Vacuum reservoir | 1 | $15-25 | Stores vacuum for consistent actuation |
| Check valve | 1 | $8-12 | Prevents vacuum loss |
| Vacuum tee fittings | 2-3 | $5-10 | Split vacuum to multiple circuits |
| **Total** | - | **$38-67** | - |

### Vacuum System Routing

1. R2.8 intake manifold vacuum port
2. Check valve (inline, prevents backflow)
3. Vacuum reservoir (engine bay)
4. Through firewall grommet
5. Factory HVAC mode selector switch
6. Mode door actuators in HVAC box

Use heat/oil resistant vacuum line, secure all connections, route away from exhaust.

## Power Flow

### Blower Motor Circuit

```
CONSTANT Power (START battery)
        ↓
PMU Out 3 (15A capacity, solid-state switching)
        ↓
Factory Blower Motor Power Input
        ↓
Factory Dash Blower Speed Knob (selects resistor)
        ↓
Factory Resistor Pack (limits current for Low/Med speeds)
        ↓
Factory Blower Motor (~20A at max speed)
        ↓
Chassis Ground (HVAC box mounting point)
```

### A/C Clutch Circuit

```
Factory TJ A/C Button (on dash panel)
        ↓
PMU In 9 (A/C request signal, 12V when button pressed)
        ↓
PMU Logic (check battery voltage, optional)
        ↓
PMU Out 1 (15A capacity, solid-state switching)
        ↓
A/C Compressor Clutch Coil (3-5A)
        ↓
Chassis Ground
```

### Temperature Control (No PMU Involvement)

```
Factory Dash Temperature Knob (rotary)
        ↓
Mechanical Cable
        ↓
Blend Door Actuator (moves door to mix hot/cold air)
        ↓
No PMU outputs consumed - entirely mechanical
```

### Mode Control (No PMU Involvement)

```
R2.8 Intake Manifold Vacuum Port
        ↓
Check Valve (prevents vacuum loss)
        ↓
Vacuum Reservoir (stores vacuum)
        ↓
Factory Dash Mode Selector Switch (rotary)
        ↓
Vacuum Lines (routes vacuum to selected actuator)
        ↓
Mode Door Actuators (move doors to direct airflow)
        ↓
No PMU outputs consumed - entirely vacuum-operated
```

## Outstanding Items

- [ ] Verify factory TJ HVAC system is complete and functional
- [ ] Install vacuum system: R2.8 manifold → check valve → reservoir → firewall → dash
- [ ] Test vacuum system for leaks
- [ ] Connect PMU Out 1 to A/C compressor clutch
- [ ] Connect PMU Out 3 to blower motor power
- [ ] Route A/C button signal to PMU In 9
- [ ] Program PMU: In 9 active → Out 1 (with voltage check)
- [ ] Test all functions: temperature, mode, blower speeds, A/C, heater
- [ ] Monitor PMU current draw on Out 1 and Out 3

## Related Documentation

- [Engine Systems][pmu-power-distribution] - PMU specifications and output allocation
