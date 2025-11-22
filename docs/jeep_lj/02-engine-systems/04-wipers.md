---
hide:
  - toc
---

# Windshield Wiper Control System {#windshield-wiper-control-system}
**Controller:** Ron Francis WS-51C
**Installation Manual:** [Ron Francis WS-51C Instructions](https://s3.amazonaws.com/cdn.ronfrancis.com/downloads/INSTRUCTIONS/WS51C-INST.pdf)
**Power Source:** PMU Out 11 (15A capacity, SWITCHED power)
**Wiper Motor:** Factory Jeep TJ/LJ wiper motor

## Overview

Ron Francis WS-51C replaces TIPM wiper functions. Provides delay/intermittent control for factory front wiper motor. Includes integrated washer pump control with auto-wipe feature.

**Note:** Rear wiper system is not currently implemented in this build. PMU Out 12 is assigned to Ham Radio (iCom IC-2730A, 13A).

## Components

### Wiper Control Module (WS-51C)

- **Mounting:** Dash-mounted (integrated switch/controller)
- **Power Requirements:**
  - Input Voltage: 12V DC
  - PMU Output: PMU Out 11 (15A capacity, SWITCHED power)
  - Typical wiper motor draw: 3-5A low speed, 6-8A high speed
- **Features:**
  - Off / Mist / Delay / Low / High functions
  - Variable delay adjustment (typical: 1-20 seconds)
  - Park position control
  - Compatible with single-motor wiper systems
  - Replaces TIPM wiper control functions

### Wiper Motor

- **Type:** Factory Jeep TJ/LJ wiper motor
- **Location:** Cowl area below windshield (factory location)
- **Configuration:** Single motor, two-speed with park position
- **Power:** Through WS-51C control module
- **Ground:** Chassis ground at firewall or cowl area

### Wiper Switch

- **Type:** Ron Francis wiper switch (included with WS-51C or separate)
- **Configuration:** Multi-function rotary or lever switch
- **Mounting:** Dash panel or column-mounted location
- **Positions:** Off / Mist / Int (Delay) / Low / High
- **Wiring:** Low-voltage control signal to WS-51C module

### Washer Pump

- **Type:** Factory TJ washer pump (or aftermarket replacement)
- **Location:** Washer fluid reservoir
- **Power:** WS-51C washer output (3-5A capacity)
- **Control:** Dash-mounted momentary washer button
- **Auto-Wipe Feature:** WS-51C automatically runs wipers when washer is activated

## Rear Wiper System (NOT IMPLEMENTED)

**Status:** Rear wiper system is not implemented in this build.

**Reason:** PMU outputs OUT12, OUT13, and OUT16 are assigned to radiator fan (GM 84100128, 30-60A) requiring 3 combined outputs for adequate capacity.

**Future Implementation Notes (if needed):**
- Rear wiper could be controlled via PMU spare input with dedicated relay
- Would require separate power source (not PMU output)
- Factory TJ/LJ rear wiper motor: Part 55155322AB (97-02), 55156278AA (03-06)

---

### ~~Rear Wiper Motor~~ (Reference Only - Not Implemented)

**Type:** Factory TJ/LJ rear wiper motor (hardtop models)
**Part Number (Reference):** 55155322AB (97-02), 55156278AA (03-06)
**Motor Type:** Single-speed, on/off only (no intermittent or variable speed)
**Power Source:** ~~PMU Out 12 (15A capacity, SWITCHED power)~~ **OUT12 now assigned to radiator fan**
**Control Method:** ~~Automatic synchronization with front wipers via PMU programming~~ **Not implemented**
**Location:** Rear hardtop window (factory mounting location)

**Motor Specifications:**
- 12V DC single-speed motor
- Simple on/off operation (no delay or variable speed)
- 3-wire configuration: Ground, constant 12V, switched 12V
- Typical current draw: 3-5A
- Auto-park function (returns to rest position when powered off)

### Synchronized Operation

**PMU Programming Logic:**

```
IF (PMU Out 11 == ACTIVE)
  THEN PMU Out 12 = ON
ELSE PMU Out 12 = OFF
```

**How It Works:**
1. Turn on front wipers (any speed: delay/low/high) → PMU Out 11 energizes
2. PMU detects Out 11 active → automatically energizes Out 12
3. Rear wiper runs continuously while front wipers are on
4. Turn off front wipers → Out 11 de-energizes → Out 12 de-energizes → rear wiper parks

**Benefits:**
- ✅ Automatic synchronization - no separate rear wiper switch needed
- ✅ Both wipers operate together for comprehensive visibility
- ✅ Single control point (front wiper switch controls both)
- ✅ Simplified dash layout (no rear wiper switch required)
- ✅ Rear wiper always operates when front wipers are on

**Trade-offs:**
- ❌ Cannot run rear wiper independently (always follows front)
- ❌ Rear wiper runs continuously (no delay mode like front)
- ❌ Rear wiper operates even when not needed (e.g., light rain)

**Note:** If you prefer independent rear wiper control, use PMU In 8 with a dash-mounted switch instead of automatic synchronization. This allows manual rear wiper control separate from front wipers.

### Rear Washer Pump

**Factory TJ Configuration:**
- **Dual-pump washer reservoir** (1997-2002 TJ with hardtop)
- **Two separate electric pumps:** One for front, one for rear
- **Reservoir location:** Driver's side front fender/wheel well
- **Independent controls:** Separate switches for front and rear washer activation

**Integration Options for This Build:**

**Option 1: Synchronized Washer Pumps (RECOMMENDED)**

Wire both front and rear washer pumps in parallel so both activate with front washer button:

```
Front Washer Button → WS-51C washer input → WS-51C washer output
    ├─→ Front Washer Pump (12V)
    └─→ Rear Washer Pump (12V, parallel connection)
```

**Wiring:**
- WS-51C washer output wire → split/junction → front pump + rear pump
- Both pumps activate simultaneously when front washer button pressed
- Total current draw: ~6-10A (both pumps together)
- WS-51C washer output rated for this load

**Benefits:**
- Both front and rear windows get washer fluid simultaneously
- Single button control (front washer button sprays both)
- Synchronized with front/rear wiper operation
- Simple, clean integration

**Option 2: Independent Rear Washer (Alternative)**

If you prefer separate rear washer control:
- Front washer: WS-51C washer output → front pump only
- Rear washer: PMU Out 15 or 16 → rear pump (separate dash button via PMU input)

**Option 3: Single Pump with T-Fitting (Simplest)**

Use one washer pump to feed both front and rear via fluid line T-split:
- WS-51C washer output → single pump
- Pump output → T-fitting → front nozzles + rear nozzles
- Both spray when washer button pressed
- Requires proper fluid line routing and pressure balance

**Recommended Approach:** Option 1 (synchronized dual pumps) - matches the synchronized wiper operation for comprehensive visibility in all conditions.

## Power Flow

### Front Wiper System
1. **Module Power:** CONSTANT power (START battery) → PMU Out 11 (15A) → WS-51C power input → chassis ground
2. **Front Wiper Motor:** WS-51C high/low outputs → front wiper motor high/low speed terminals → motor ground
3. **Control Switch:** Dash wiper switch → control signal wires → WS-51C control inputs
4. **Park Position:** Wiper motor park switch → WS-51C park input (auto-shutoff at rest position)

### Rear Wiper System (Synchronized)
1. **Rear Wiper Power:** CONSTANT power (START battery) → PMU Out 12 (15A) → rear wiper motor → chassis ground
2. **Synchronization Logic:** PMU monitors Out 11 state → activates Out 12 when Out 11 is active
3. **Automatic Operation:** Front wipers on (any mode) → rear wiper on automatically

### Washer System (Both Front and Rear)
1. **Washer Control:** Dash washer button → WS-51C washer input → WS-51C washer output
2. **Dual Pumps (Parallel):** WS-51C output → front pump + rear pump (both activate simultaneously)
3. **Auto-Wipe:** WS-51C triggers front wipers when washer activated

## Wiring Summary

### Front Wiper Circuit

1. **Power (+):** CONSTANT power (START battery) → PMU Out 11 (15A capacity) → WS-51C red power wire (12V input)
2. **Ground (-):** WS-51C black ground wire → chassis ground or firewall ground point
3. **Front Wiper Motor Outputs:**
   - **Low Speed:** WS-51C low speed output → wiper motor low speed terminal
   - **High Speed:** WS-51C high speed output → wiper motor high speed terminal
   - **Motor Ground:** Wiper motor ground → chassis ground (factory ground location)
4. **Park Switch:** Wiper motor park terminal → WS-51C park input (detects wiper rest position)
5. **Control Switch Inputs:**
   - Dash wiper switch → control wires → WS-51C module
   - Switch functions: Off, Mist (momentary), Delay (variable), Low, High

### Rear Wiper Circuit

1. **Power (+):** CONSTANT power (START battery) → PMU Out 12 (15A capacity) → rear wiper motor power terminal (12V input)
2. **Ground (-):** Rear wiper motor ground terminal → chassis ground (rear hardtop ground location)
3. **Control Logic:** PMU internal programming (Out 11 state monitoring → Out 12 activation)
4. **No Manual Switch Required:** Automatic synchronization with front wipers via PMU

### Washer Pump Circuit

**Option 1: Synchronized Dual Pumps (Recommended)**
1. **Washer Button:** Dash washer button → WS-51C washer input
2. **Pump Power:** WS-51C washer output → junction/split
   - **Output 1:** Front washer pump motor (3-5A)
   - **Output 2:** Rear washer pump motor (3-5A, parallel)
3. **Total Load:** ~6-10A (both pumps together, within WS-51C washer output capacity)
4. **Pump Grounds:** Both pumps → chassis ground (at washer reservoir location)

**Alternative: Single Pump with T-Fitting**
1. **Washer Button:** Dash washer button → WS-51C washer input → WS-51C washer output → single pump
2. **Fluid Distribution:** Pump output → T-fitting → front nozzles + rear nozzles
3. **Total Load:** 3-5A (single pump only)

## TIPM Functions Replaced

The WS-51C wiper control system replaces the following TIPM functions:
- Wiper motor low/high speed control
- Intermittent/delay wiper timing
- Mist function (momentary wipe)
- Park position control (auto-shutoff)
- Washer pump activation with auto-wipe feature

## Outstanding Items

None - design complete. See [installation checklist][install-checklist] for build tasks.

**Resolved:**

- **WS-51C mounting:** Dash-mounted (integrated switch/controller)
- **Rear wiper:** Not implemented - PMU OUT12 assigned to Ham Radio
- **Washer pump:** Factory single pump for front washer only (no rear washer needed)

See [installation checklist][install-checklist] for build tasks.

[install-checklist]: installation-checklist.md

## Related Documentation

- [Control Interfaces Overview][control-interfaces-overview] - Main control interfaces overview
- [Engine Systems][pmu-power-distribution] - PMU fuse and relay specifications
