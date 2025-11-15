# SwitchPros SP-1200 (RCR-Force 12) {#switchpros-sp-1200-rcr-force-12}
**Model:** RCR-Force 12
**Manual:** https://www.switchpros.com/wp-content/uploads/RCR-force-12-installation-guide-REV-1.9.pdf
**Power Source:** 150A breaker from CONSTANT bus (rear battery)
**Power Module Location:** Engine bay (rated to 125°C, IP67)
**Control Panel Location:** TBD - dash mount (4" L x 3" W x 0.375" H)
**Ground:** 4 AWG to front frame rail or front battery negative (per manufacturer spec - direct battery ground)
**IP Rating:** IP67 (both power module and control panel)

## Overview

The SwitchPros SP-1200 is the main lighting and accessory controller for the Jeep LJ build. It provides 17 total outputs controlled via a 12-button control panel with Bluetooth app integration.

**Specifications:**

- 150A total capacity on CONSTANT bus
- 17 outputs total:
  - 4 outputs @ 35A (high in-rush circuits)
  - 1 output @ 30A (high in-rush)
  - 11 outputs @ 15A (can be combined for larger loads)
  - 1 low-side driver @ 2A

## Control Panel Layout

| Button |       Circuit       | Draw |                      Details                      |    Output Pin(s)     |
| :----: | :-----------------: | :--: | :-----------------------------------------------: | :------------------: |
|   1    | Roof Center Section | 31A  |         6x BD XL Linkable (Combo Pattern)         |       OUTPUT-1       |
|   2    |    Ditch Lights     | 12A  |          2x BD LP6 Pro (Driving Pattern)          |       OUTPUT-2       |
|   3    |     Fog Lights      |  9A  |            3x BD Squadron SAE (Amber)             |       OUTPUT-3       |
|   4    |     Dome Lights     |  4A  | 4x KC Cyclone (manual + door-triggered)           |       OUTPUT-4       |
|   5    |  Roof Outer Spots   | 12A  |         2x BD XL Linkable (Spot Pattern)          |       OUTPUT-5       |
|   6    |     Rock Lights     |  3A  |               6x KC Cyclone Lights                |       OUTPUT-6       |
|   7    |  Rear Amber Chase   |  6A  |        BD OnX6 Arc (Amber, Wide Cornering)        |       OUTPUT-7       |
|   8    |    Party Lights     |  6A  |      1x BD RGB Whip + 4x Footwell LED Strips      |       OUTPUT-8       |
|   9    |    Front Locker     |  2A  |   ARB Locker (see [Air System][# Air System - ARB Compressor & Lockers {#air-system-arb-compressor-lockers}])   | OUTPUT-17 (low-side) |
|   10   |     Rear Locker     |  2A  |   ARB Locker (see [Air System][# Air System - ARB Compressor & Lockers {#air-system-arb-compressor-lockers}])   |      OUTPUT-10       |
|   11   |     Compressor      | 15A  |   ARB Twin Compressor (see [Air System][# Air System - ARB Compressor & Lockers {#air-system-arb-compressor-lockers}])   |      OUTPUT-11       |
|   12   |     Rear Lights     |  5A  |        2x BD S1 Pro (Above License Plate)         |      OUTPUT-12       |

**Notes:**

- **Button 2:** Ditch lights (2x BD LP6 Pro) for trail/night driving visibility
- **Button 4:** Dome lights have dual control - manual button OR door-triggered via TRIGGER-1
  - Driver door switch + Passenger door switch (wired in parallel) → TRIGGER-1 → OUTPUT-4
  - Either door opening or Button 4 press activates dome lights
- **Button 11:** OUTPUT-11 provides control signal to ARB compressor (main power is separate: CONSTANT bus → dual 60A fuses → compressor)
- **Cargo Light:** Not assigned to button - controlled by rear rocker switch via TRIGGER-2 → OUTPUT-13
- Total draw if all outputs on simultaneously: ~127A (within 150A capacity)

## Wiring Pinout

### 20-Pin Harness Connector

| Pin |   Label   |    Color    | Gauge  |  Max Load   | Assigned Circuit           | Load |              Notes               |
| :-: | :-------: | :---------: | :----: | :---------: | -------------------------- | :--: | :------------------------------: |
|  1  | OUTPUT-5  |    GREEN    | 14 AWG |     15A     | Roof Outer Spots           | 12A  |                                  |
|  2  | OUTPUT-6  |    BLUE     | 14 AWG |     15A     | Rock Lights                |  3A  |                                  |
|  3  | IGNITION  |   LT BLUE   |   -    |      -      | Connect to ignition signal |  -   |      For auto-off features       |
|  4  |  LIGHTS   |    WHITE    |   -    |      -      | Connect to parking lights  |  -   |       For DRL integration        |
|  5  | OUTPUT-7  |   PURPLE    | 14 AWG |     15A     | Rear Amber Chase           |  6A  |                                  |
|  6  | OUTPUT-8  |    GREY     | 14 AWG |     15A     | Party Lights               |  6A  |                                  |
|  7  | TRIGGER-1 |    PINK     |   -    |      -      | Door switches (driver + passenger) | - | Triggers OUTPUT-4 (dome lights) when doors open |
|  8  | TRIGGER-2 |    PINK     |   -    |      -      | Rear cargo rocker switch   |  -   | Triggers OUTPUT-13 (cargo light) |
|  9  | OUTPUT-9  |    WHITE    | 14 AWG | 30A (2x15A) | SPARE (can combine 9+10)   |  -   |                                  |
| 10  | OUTPUT-9B |    WHITE    | 14 AWG |      -      | SPARE (fused with 9)       |  -   |                                  |
| 11  | OUTPUT-10 |     TAN     | 14 AWG |     15A     | Rear Locker                |  2A  |                                  |
| 12  | OUTPUT-11 |    BROWN    | 14 AWG |     15A     | Compressor control         | 15A  | Control signal to compressor     |
| 13  | OUTPUT-12 |     RED     | 14 AWG |     15A     | Rear Lights                |  5A  |                                  |
| 14  |  GROUND   |    BLACK    |   -    |      -      | Direct to battery negative |  -   |   Critical - direct connection   |
| 15  | OUTPUT-13 |   ORANGE    | 14 AWG |     15A     | Cargo Light                |  5A  | Triggered by rear rocker switch (TRIGGER-2) |
| 16  | OUTPUT-14 |   YELLOW    | 14 AWG |     15A     | SPARE                      |  -   |                                  |
| 17  | TRIGGER-3 |    PINK     |   -    |      -      | Reverse signal (from trans) | -   | Triggers outputs when in reverse |
| 18  | OUTPUT-17 |  LT GREEN   |   -    |     2A      | Front Locker (low-side)    |  2A  |       Low-side switch only       |
| 19  | OUTPUT-15 | GREEN/BLACK | 14 AWG |     15A     | SPARE                      |  -   |                                  |
| 20  | OUTPUT-16 | BLUE/BLACK  | 14 AWG |     15A     | SPARE                      |  -   |                                  |

### 4-Pin Harness (High Current Outputs)

| Pin |  Label   | Color  | Gauge | Max Load | Assigned Circuit    | Load |        Notes         |
| :-: | :------: | :----: | :---: | :------: | ------------------- | :--: | :------------------: |
|  1  | OUTPUT-1 | BROWN  | 10AWG |   35A    | Roof Center Section | 31A  |                      |
|  2  | OUTPUT-2 |  RED   | 10AWG |   35A    | Ditch Lights        | 12A  |                      |
|  3  | OUTPUT-3 | ORANGE | 10AWG |   35A    | Fog Lights          |  9A  |                      |
|  4  | OUTPUT-4 | YELLOW | 10AWG |   35A    | Dome Lights         |  4A  |                      |

## Power and Ground Connections

- **Power:** 4 AWG wire from CONSTANT bus (rear battery) → 150A breaker → SwitchPros power module
- **Ground:** 4 AWG wire from SwitchPros power module → Front frame rail or front battery negative (direct battery ground per manufacturer spec)

## Trigger Input Assignments

### TRIGGER-1: Door Switches → Dome Lights

Driver and passenger door switches wired in parallel to activate dome lights when either door opens.

**Wiring:**
```
Driver Door Switch (NO) ──┬──→ TRIGGER-1 (Pin 7, PINK)
Passenger Door Switch (NO)─┘
```

**Configuration:**
- Program Button 4 to control OUTPUT-4 OR TRIGGER-1 → OUTPUT-4
- Manual control: Press Button 4
- Automatic control: Open driver or passenger door
- Both switches are normally open, close to ground when door opens

**Note:** Rear tailgate replaced factory rear door - no rear door switch needed

### TRIGGER-2: Rear Rocker Switch → Cargo Light

Physical rocker switch mounted in rear cargo area for convenient access when loading/unloading.

**Wiring:**
```
Rear Cargo Rocker Switch (SPST) → TRIGGER-2 (Pin 8, PINK)
```

**Configuration:**
- Program TRIGGER-2 → OUTPUT-13 (cargo light)
- No button assignment needed
- Physical switch location: Rear cargo area (easily accessible from tailgate)
- Switch type: SPST rocker or toggle switch

**Benefits:**
- Physical access from cargo area (don't need dashboard button or app)
- Independent from other lighting circuits
- Convenient when loading/unloading gear at night

### TRIGGER-3: Air Pressure Switch → Auto Compressor Control

ARB air tank pressure switch automatically activates compressor to maintain tank pressure between 135-150 PSI.

**Wiring:**
```
ARB Pressure Switch (180901) → TRIGGER-3 (Pin 17, PINK)
```

**Configuration:**

Program TRIGGER-3 to activate compressor when tank pressure drops below 135 PSI:

**SwitchPros Logic:**
- **TRIGGER-3 OR Button 11 → OUTPUT-11 (compressor)**
- When tank pressure < 135 PSI: TRIGGER-3 closes → OUTPUT-11 activates → compressor runs
- When tank pressure = 150 PSI: TRIGGER-3 opens → OUTPUT-11 deactivates → compressor stops
- Manual override: Button 11 can force compressor on regardless of tank pressure

**Signal Source:**
- ARB Pressure Switch model 180901 (cut-in: 135 PSI, cut-out: 150 PSI)
- Mounted on air manifold under passenger seat
- Low current signal wire (18 AWG from manifold to SwitchPros TRIGGER-3)

**Benefits:**
- Automatic pressure maintenance (no user intervention required)
- Instant locker engagement (tank always pressurized)
- Manual override available for tire inflation (Button 11)
- Prevents compressor over-cycling
- Tank ready for use whenever needed

**Related Documentation:**
- See [Air System][# Air System - ARB Compressor & Lockers {#air-system-arb-compressor-lockers}] for complete ARB compressor, tank, and pressure switch specifications

## Outstanding Items

- [ ] Determine exact SwitchPros power module mounting location in engine bay
  - IP67 rated, 125°C temperature rating suitable for engine bay
  - Locate near CONSTANT bus or front battery for short power/ground runs
- [ ] Determine SwitchPros control panel mounting location on dash
- [ ] Route 4 AWG ground wire from SwitchPros power module to front frame rail or front battery negative
  - Short run in engine bay, per manufacturer spec for direct battery ground
- [ ] Connect ignition signal from ignition switch RUN terminal to SwitchPros Pin 3 (IGNITION - LT BLUE)
  - 18 AWG wire, splits from main ignition signal distribution (see [PMU24][# 1.4.3 PMU Inputs {#143-pmu-inputs}])
- [ ] Determine parking lights signal source for SwitchPros Pin 4 (LIGHTS - WHITE) for DRL integration
- [ ] Plan control panel cable routing from engine bay power module to dash-mounted control panel
  - Cable length required for engine bay to dash mount
- [ ] Wire driver door switch + passenger door switch in parallel to TRIGGER-1 (Pin 7, PINK)
- [ ] Configure Button 4 programming: OUTPUT-4 OR TRIGGER-1 activates dome lights
- [ ] Install rear cargo rocker switch and wire to TRIGGER-2 (Pin 8, PINK)
- [ ] Determine rear cargo rocker switch mounting location (accessible from tailgate)
- [ ] Configure TRIGGER-2 programming: TRIGGER-2 → OUTPUT-13 (cargo light)
- [ ] Route cargo light wiring from SwitchPros OUTPUT-13 to cargo area
- [ ] Route ditch light wiring from SwitchPros OUTPUT-2 to A-pillar/hood mounts
- [ ] Wire ARB pressure switch signal to TRIGGER-3 (Pin 17, PINK)
  - 18 AWG wire from air manifold (under passenger seat) to SwitchPros TRIGGER-3
  - Route through cabin or under vehicle to engine bay SwitchPros power module
- [ ] Configure SwitchPros: TRIGGER-3 OR Button 11 → OUTPUT-11 (compressor auto/manual control)
- [ ] Test automatic pressure control: verify compressor activates at 135 PSI and stops at 150 PSI
- [ ] Assign spare outputs: OUTPUT-9 (30A), OUTPUT-14, OUTPUT-15, OUTPUT-16 (all 15A)

## Related Documentation

- [Control Interfaces Overview][# Control Interfaces - Overview {#control-interfaces-overview}] - Main control interfaces overview
- [Offroad Lighting][# Offroad & Auxiliary Lighting {#offroad-auxiliary-lighting}] - Complete wiring details for all lighting circuits controlled by SwitchPros
- [Air System][# Air System - ARB Compressor & Lockers {#air-system-arb-compressor-lockers}] - ARB locker and compressor wiring details
