---
hide:
  - toc
---

# Offroad & Auxiliary Lighting {#offroad-auxiliary-lighting}
Non-DOT-required lighting circuits controlled by the SwitchPros SP-1200 controller.

!!! info "Controller Documentation"
    See [SwitchPros SP-1200][switchpros-sp-1200-rcr-force-12] for complete specifications, wiring, and installation.

## System Overview

**Controller:** SwitchPros RCR-Force 12 (SP-1200)
- **Power:** CONSTANT bus (aux battery, 150A breaker)
- **Outputs:** 17 total (12 main + 5 low-side drivers)
- **Control:** 12-button panel + Bluetooth app

**Lighting Circuits:**
- Button 1: Roof Center Section (6x BD XL) - 31A
- Button 2: Ditch Lights (2x BD LP6 Pro) - 12A
- Button 3: Fog Lights (3x BD Squadron SAE) - 9A
- Button 4: Dome Lights (4x KC Cyclone) - 4A
- Button 5: Roof Outer Spots (2x BD XL) - 12A
- Button 6: Rock Lights (6x KC Cyclone) - 3A
- Button 7: Rear Amber Chase (BD OnX6 Arc) - 6A
- Button 8: Party Lights (RGB Whip + LED Strips) - 6A
- Button 12: Rear Lights (2x BD S1 Pro) - 5A

**Total load:** 88A

## Front Auxiliary Lighting

### Ditch Lights

**Type:** Baja Designs LP6 Pro LED Pods
**Quantity:** 2 (A-pillar or hood mounts)
**Draw:** 12A (6A per light)
**Control:** SwitchPros Button 2 (OUTPUT-2, RED, 10 AWG, 4-pin harness)

**Wiring:**
- **Power:** OUTPUT-2 (RED, 10 AWG) → 14 AWG → Y-splitter → both pods
- **Ground:** Chassis ground at A-pillar or fender
- **Routing:** Dashboard → firewall grommet → mount location

### Fog Lights

**Type:** Baja Designs Squadron SAE
**Quantity:** 3 lights (front bumper or lower valance)
**Draw:** 9A (3A per light)
**Control:** SwitchPros Button 3 (OUTPUT-3, ORANGE, 10 AWG, 4-pin harness)

**Wiring:**
- **Power:** OUTPUT-3 (ORANGE, 10 AWG) → 14 AWG → 3-way splitter → all lights
- **Ground:** Chassis ground at bumper or frame
- **Routing:** Dashboard → firewall grommet → front bumper

## Roof Lighting

### Roof Center Section (Light Bar)

**Type:** Baja Designs XL Linkable LED Pods
**Quantity:** 6 pods (roof rack center section)
**Draw:** 31A (5.2A per pod)
**Control:** SwitchPros Button 1 (OUTPUT-1, BROWN, 10 AWG, 4-pin harness)

**Wiring:**
- **Power:** OUTPUT-1 (BROWN, 10 AWG) → first pod → linked to remaining 5 pods (BD XL Linkable harness)
- **Ground:** Chassis ground at roof rack mount
- **Routing:** Dashboard → A-pillar → headliner → roof rack

### Roof Outer Spots

**Type:** Baja Designs XL Linkable LED Pods
**Quantity:** 2 pods (roof rack outer positions, left/right corners)
**Draw:** 12A (6A per pod)
**Control:** SwitchPros Button 5 (OUTPUT-5, GREEN, 14 AWG, 20-pin harness)

**Wiring:**
- **Power:** OUTPUT-5 (GREEN, 14 AWG) → Y-splitter → both pods
- **Ground:** Chassis ground at roof rack mount
- **Routing:** Dashboard → A-pillar → headliner → roof rack outer mounts

### Rear Amber Chase Light

**Type:** Baja Designs OnX6 Arc LED Light Bar (amber lens)
**Quantity:** 1 bar (rear roof rack or roll bar mount)
**Draw:** 6A
**Control:** SwitchPros Button 7 (OUTPUT-7, PURPLE, 14 AWG, 20-pin harness)

**Wiring:**
- **Power:** OUTPUT-7 (PURPLE, 14 AWG) → light bar
- **Ground:** Chassis ground at roof rack or roll bar mount
- **Routing:** Dashboard → A-pillar → headliner → rear roof mount

## Interior/Dome Lighting

### Dome Lights (Roll Bar Mounted)

**Type:** KC HiLiTES Cyclone LED Pods
**Quantity:** 4 pods (2 front roll bar, 2 rear roll bar)
**Draw:** 4A (1A per pod)
**Control:** SwitchPros Button 4 (OUTPUT-4, YELLOW, 10 AWG, 4-pin harness)
**Mounting:**
- 2x front roll bar (above driver/passenger seats)
- 2x rear roll bar (above rear cargo area)

**Wiring:**
- **Power:** OUTPUT-4 (YELLOW, 10 AWG) → 14 AWG → 4-way splitter → all pods
- **Rear Seat Switch:** TBD - parallel wiring for rear seat passenger control
- **Ground:** Chassis ground at roll bar mounts
- **Routing:** Dashboard → overhead headliner → roll bar mounts

## Rock & Underbody Lighting

### Rock Lights

**Type:** KC HiLiTES Cyclone LED Pods
**Quantity:** 6 pods (wheel wells, frame rails, or rocker panels)
**Draw:** 3A (0.5A per pod)
**Control:** SwitchPros Button 6 (OUTPUT-6, BLUE, 14 AWG, 20-pin harness)

**Wiring:**
- **Power:** OUTPUT-6 (BLUE, 14 AWG) → 6-way splitter → all pods
- **Ground:** Chassis ground at frame or body mounts
- **Routing:** Dashboard → firewall → frame rails → wheel wells/rockers
- **Protection:** Conduit or protective sleeving in exposed areas

## Rear Auxiliary Lighting

### Cargo Area Light

**Type:** TBD - LED light bar or pod lights
**Quantity:** TBD (depends on cargo area coverage needed)
**Draw:** ~5A
**Control:** Rear rocker switch → TRIGGER-2 (Pin 8, PINK) → OUTPUT-13 (ORANGE, 14 AWG, 20-pin harness)

**Wiring:**
- **Power:** OUTPUT-13 (ORANGE, 14 AWG) → cargo light(s)
- **Ground:** Chassis ground at cargo area mounting location
- **Trigger:** Rear rocker switch (SPST) → TRIGGER-2 (Pin 8, PINK)
- **Routing:**
  - Power: Dashboard → firewall → cargo area
  - Trigger: Rear rocker switch location → forward to SwitchPros power module (engine bay)

**Switch Mounting:**
- Physical rocker switch in rear cargo area
- Easily accessible from tailgate when loading/unloading
- Possible locations: side panel, rear tub, near tailgate hinge

**Benefits:**
- Physical switch access from cargo area (no need for dashboard button or app)
- Independent control when working in rear of vehicle
- Convenient for nighttime loading/unloading

### Rear Lights (License Plate Area)

**Type:** Baja Designs S1 Pro LED Pods
**Quantity:** 2 pods (above license plate or spare tire carrier)
**Draw:** 5A
**Control:** SwitchPros Button 12 (OUTPUT-12, RED, 14 AWG, 20-pin harness)

**Wiring:**
- **Power:** OUTPUT-12 (RED, 14 AWG) → Y-splitter → both pods
- **Ground:** Chassis ground at tailgate or tire carrier
- **Routing:** Dashboard → cargo area → tailgate/license plate mount

## Specialty Lighting

### Party Lights (RGB)

**Type:** RGB LED whip antenna + RGB footwell/interior strips
**Draw:** 6A
**Control:** SwitchPros Button 8 (OUTPUT-8, GREY, 14 AWG, 20-pin harness)
**Mounting:**
- **RGB Whip:** Rear bumper or tire carrier mount
- **Footwell Strips:** Under dashboard and rear cargo area

**Wiring:**
- **Power:** OUTPUT-8 (GREY, 14 AWG) → RGB controller → whip + strips
- **RGB Controller:** TBD - for color/pattern selection
- **Ground:** Chassis ground
- **Routing:**
  - Whip: Dashboard → firewall → rear bumper
  - Strips: Dashboard → under dash

## Power Distribution Summary

| Button | Circuit | SwitchPros Output | Wire Color | Wire Gauge | Total Draw | Notes |
| :----: | :------ | :---------------- | :--------- | :--------- | :--------- | :---- |
| 1 | Roof Center Section | OUTPUT-1 | BROWN | 10 AWG | 31A | 6x BD XL Linkable (4-pin harness) |
| 2 | Ditch Lights | OUTPUT-2 | RED | 10 AWG | 12A | 2x BD LP6 Pro (4-pin harness) |
| 3 | Fog Lights | OUTPUT-3 | ORANGE | 10 AWG | 9A | 3x BD Squadron SAE (4-pin harness) |
| 4 | Dome Lights | OUTPUT-4 | YELLOW | 10 AWG | 4A | 4x KC Cyclone (4-pin harness) |
| 5 | Roof Outer Spots | OUTPUT-5 | GREEN | 14 AWG | 12A | 2x BD XL Linkable (20-pin harness) |
| 6 | Rock Lights | OUTPUT-6 | BLUE | 14 AWG | 3A | 6x KC Cyclone (20-pin harness) |
| 7 | Rear Amber Chase | OUTPUT-7 | PURPLE | 14 AWG | 6A | BD OnX6 Arc (20-pin harness) |
| 8 | Party Lights | OUTPUT-8 | GREY | 14 AWG | 6A | RGB Whip + LED Strips (20-pin harness) |
| 12 | Rear Lights | OUTPUT-12 | RED | 14 AWG | 5A | 2x BD S1 Pro (20-pin harness) |
| TRIGGER-2 | Cargo Light | OUTPUT-13 | ORANGE | 14 AWG | 5A | Rear rocker switch activated (20-pin harness) |

**Total load:** 93A

## Spare Outputs

Available for future expansion:

- **OUTPUT-9 / OUTPUT-9B:** 30A combined (2x 15A) - WHITE (20-pin harness)
- **OUTPUT-14:** 15A - YELLOW (20-pin harness)
- **OUTPUT-15:** 15A - GREEN/BLACK (20-pin harness)
- **OUTPUT-16:** 15A - BLUE/BLACK (20-pin harness)

## Outstanding Items

### Ditch Lights
- [ ] Confirm mounting location (A-pillar vs hood)
- [ ] Confirm LP6 Pro beam pattern (spot, driving, combo)
- [ ] Determine wire routing path from dashboard to mounts
- [ ] Verify Y-splitter connector type

### Fog Lights
- [ ] Confirm mounting configuration (center + corners or 3x spread)
- [ ] Confirm Squadron SAE beam pattern compliance
- [ ] Determine wire routing path from dashboard to bumper
- [ ] Verify 3-way splitter connector type

### Roof Center Section
- [ ] Confirm XL Linkable harness length and connector type
- [ ] Determine roof rack mounting method for 6 pods
- [ ] Verify OUTPUT-1 capacity (31A) is within spec
- [ ] Determine wire routing path from dash to roof (A-pillar vs B-pillar)
- [ ] Plan weatherproofing at roof penetration

### Roof Outer Spots
- [ ] Determine if outer spots will be linked or independently wired
- [ ] Confirm spot beam pattern
- [ ] Verify Y-splitter connector type if wired independently
- [ ] Determine exact mounting positions on roof rack

### Rear Amber Chase Light
- [ ] Determine OnX6 Arc length (20", 30", 40", 50")
- [ ] Confirm amber lens option and strobing capability
- [ ] Verify mounting method on rear roof rack or roll bar

### Dome Lights
- [ ] Determine wiring for rear seat switch control
- [ ] Verify 4-way splitter connector type
- [ ] Plan wire routing from dash to front/rear roll bar mounts

### Rock Lights
- [ ] Determine exact mounting locations (6 positions)
- [ ] Confirm KC Cyclone mounting brackets for underbody use
- [ ] Verify 6-way splitter connector type
- [ ] Plan wire routing from dash to frame rails and wheel wells
- [ ] Determine protection method for exposed wiring (conduit, sleeving)

### Cargo Area Light
- [ ] Determine cargo light type (LED bar, pod lights, strip lights)
- [ ] Determine cargo area light mounting location (overhead, side mount, tailgate area)
- [ ] Determine rear rocker switch mounting location (accessible from tailgate)
- [ ] Source SPST rocker switch for cargo light control
- [ ] Route TRIGGER-2 wire from rear switch location to SwitchPros power module (engine bay)
- [ ] Configure SwitchPros: TRIGGER-2 → OUTPUT-13 (cargo light activation)
- [ ] Verify cargo light draw is within 15A OUTPUT-13 capacity

### Rear Lights
- [ ] Determine exact mounting location (license plate vs spare tire carrier)
- [ ] Confirm S1 Pro beam pattern (spot vs driving)
- [ ] Verify mounting does not interfere with WolfBox rear camera
- [ ] Verify Y-splitter connector type

### Party Lights (RGB)
- [ ] Determine RGB whip antenna model and mounting location
- [ ] Determine RGB LED strip model and lengths for footwell
- [ ] Confirm RGB controller model and integration with SwitchPros
- [ ] Verify total amperage draw for OUTPUT-8 capacity
- [ ] Determine color/pattern control method

## Related Documentation

- [SwitchPros SP-1200][switchpros-sp-1200-rcr-force-12] - Complete SwitchPros controller specifications, pinouts, and installation
- [Control Interfaces Overview][control-interfaces-overview] - All control interfaces
- [Vehicle Lighting][vehicle-lighting-overview] - Street-legal and DOT-required lighting circuits
- [Dashboard Controls][dashboard-physical-controls] - Rear seat switch for dome light control
