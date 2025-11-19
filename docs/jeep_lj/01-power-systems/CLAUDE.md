# Section 1: Power Systems - Navigation Guide

## Section Overview

Section 1 documents the complete power generation and distribution architecture for the Jeep LJ build.

**Key Principle:** Direct battery connections via circuit breakers - no intermediate bus bars between batteries and major loads.

## File Organization

### 1.1 Power Generation (`01-power-generation/`)

**What's here:** Batteries, alternator, BCDC charger, solar panel

**Files:**
- `01-batteries.md` - Odyssey PC1500 specs (both front and rear)
- `02-alternator.md` - 270A alternator
- `03-bcdc.md` - RedArc BCDC Alpha 25 DC-DC charger with solar input
- `04-solar.md` - Cascadia 4x4 80W hood panel
- `index.md` - Power generation overview

**When to use:** Battery specs, charging system details, solar integration

### 1.2 START battery Distribution (`02-starter-battery-distribution/`)

**What's here:** Engine bay power distribution from START battery

**Files:**
- `01-circuit-breakers.md` - All START battery CBs (PMU, SafetyHub, BCDC input)
- `04-safetyhub.md` - Blue Sea SafetyHub 150 fused distribution
- `index.md` - START battery overview with terminal connection tables
- `CLAUDE.md` - Navigation guide

**When to use:** PMU power source, SafetyHub circuits, BCDC input protection, direct battery loads (winch, starter)

### 1.3 AUX battery Distribution (`03-aux-battery-distribution/`)

**What's here:** Wheel well power distribution from AUX battery

**Files:**
- `01-circuit-breakers.md` - All AUX battery CBs (SwitchPros, BODY PDU)
- `04-body-pdu.md` - Body relay/fuse panel for cabin circuits
- `index.md` - AUX battery overview with terminal connection tables
- `CLAUDE.md` - Navigation guide

**When to use:** SwitchPros power source, BODY PDU circuits, AUX battery loads

### 1.4 PMU (`04-pmu/`)

**What's here:** ECUMaster PMU24 power management unit

**Files:**
- `01-pmu-overview.md` - Product specs, capacity, mounting
- `02-pmu-outputs.md` - All 24 output assignments, loads, combining
- `03-pmu-inputs.md` - Digital/analog inputs, CAN bus integration
- `04-pmu-programming.md` - Logic examples, configuration software
- `index.md` - PMU navigation hub
- `CLAUDE.md` - Navigation guide

**When to use:** Programmable output assignments, CAN bus integration, input logic, capacity planning

### 1.5 Grounding Architecture (`05-grounding/`)

**What's here:** Complete grounding system design

**Files:**
- `01-starter-battery-ground.md` - Direct START battery negative connections
- `02-aux-battery-ground.md` - Direct AUX battery negative connections
- `03-engine-bay-ground-bus.md` - Engine bay ground bus bar
- `04-firewall-stud-bus.md` - Cabin electronics ground bus
- `05-switchpros-ground-bus.md` - Lighting/accessories ground bus
- `index.md` - Grounding architecture overview
- `CLAUDE.md` - Navigation guide

**When to use:** Ground connection locations, ground bus assignments, testing voltage drop

### 1.6 Ignition Signal Distribution (`06-ignition-signal/`)

**What's here:** Ignition sense signal distribution

**Files:**
- `index.md` - Blue Sea MaxiBus 2105 ignition bus bar

**When to use:** Ignition signal routing to CT4, SwitchPros, Fusion Radio, BCDC

### Installation Checklist

`installation-checklist.md` - Complete Section 1 installation organized by workflow phases

**When to use:** Build planning, installation sequencing, testing procedures

## Cross-Section Integration

### To Section 2 (Engine Systems)

**Firewall Ingress:** Wire routing paths, grommet specifications

**Starter:** Direct control (keyswitch → clutch switch → relay) - NOT PMU controlled

**HVAC:** PMU blower control (OUT1)

**Radiator Fan:** PMU combined outputs (OUT2+3+4)

**Find in:** `docs/jeep_lj/02-engine-systems/`

### To Section 3 (Lighting)

**DRL/Parking:** PMU OUT14 with auto-off logic

**Brake Lights:** PMU OUT21

**Reverse Lights:** PMU OUT22

**Offroad Lighting:** SwitchPros distribution via custom Delphi harnesses

**Find in:** `docs/jeep_lj/03-lighting-systems/`

### To Section 4 (Control Interfaces)

**Command Touch CT4:** PMU OUT13 (CONSTANT power)

**SwitchPros SP-1200:** AUX battery power via 150A CB, custom harnesses

**Dakota Digital Cluster:** PMU OUT12

**Find in:** `docs/jeep_lj/04-control-interfaces/`

### To Section 5 (Audio)

**Fusion Radio:** BODY PDU F2 (memory), F3 (amp)

**Find in:** `docs/jeep_lj/05-audio-systems/`

### To Section 6 (Communication)

**GMRS Radio:** SafetyHub ATC-2, direct battery ground

**STX Intercom:** SafetyHub ATC-3, direct battery ground

**Find in:** `docs/jeep_lj/06-communication-systems/`

### To Section 7 (Exterior Systems)

**Winch:** Direct START battery connection (no CB), SafetyHub contactor trigger

**ARB Compressor:** SafetyHub MIDI-1/2 (twin motors)

**Find in:** `docs/jeep_lj/07-exterior-systems/`

## Common Navigation Scenarios

**"Where does [component] get power?"**
→ Check front or AUX battery distribution `index.md` terminal tables

**"What's connected to PMU OUT[X]?"**
→ See `04-pmu/02-pmu-outputs.md`

**"Where does [wire] route through firewall?"**
→ See Section 2: `02-engine-systems/07-firewall-ingress.md`

**"What circuit breaker protects [load]?"**
→ Check battery distribution `01-circuit-breakers.md` in front or rear

**"Where does [component] ground?"**
→ Check grounding section - battery grounds vs. bus bars

**"How do I install [system]?"**
→ See `installation-checklist.md` for workflow-based sequence

## When Changing Section 1 Content

### Adding a New Load

1. Determine power source (front or AUX battery)
2. Calculate circuit breaker sizing
3. Update battery distribution `index.md` terminal table
4. Update circuit breaker file if new CB needed
5. Add to installation checklist in appropriate phase
6. Update grounding file for ground connection

### Moving Content Between Files

1. Update all cross-references in both source and destination
2. Search for inline links to old location: `grep -r "old-filename.md"`
3. Update section `index.md` if navigation changed
4. Verify build: `mkdocs build`

### Updating Specifications

1. Find authoritative source (product file or table)
2. Update in ONE location only
3. Ensure other files link to that source (don't duplicate)
4. If TBD → resolved, remove from Outstanding Items

### Reorganizing Subsections

1. Read all CLAUDE.md files first to understand structure
2. Update folder numbering if needed (maintain consistency)
3. Update mkdocs.yml navigation paths
4. Use find/sed for bulk reference updates
5. Verify no broken links after changes

## Design Rules (Do Not Violate)

**Power Architecture:**
- Direct battery → circuit breaker → major load (no intermediate bus bars)
- START battery: Critical systems (PMU, SafetyHub, starter, winch)
- AUX battery: Accessories (SwitchPros, BODY PDU)

**Grounding Architecture:**
- Battery negative → Frame rail (2/0 AWG)
- Battery-to-battery ground reference cable (2/0 AWG)
- Direct battery grounds for: ECM, grid heater, RF devices (GMRS, Ham, Intercom)
- Bus bar grounds for: Most other loads

**Circuit Protection:**
- All major loads via dedicated circuit breakers
- CB sizing: 125-160% of max load
- No fuses between CB and load (fuses at distribution panels only)

**Wiring Standards:**
- SwitchPros: Custom 2-pin Delphi harnesses (no individual wire routing)
- Reference-style links in all documentation
- Images in central `/docs/jeep_lj/images/` location

## Quick Reference

**Total Batteries:** 2 (Odyssey PC1500, 850 CCA, 68 Ah each)

**Power Controllers:**
- PMU24: Programmable outputs (24 channels)
- SafetyHub 150: Fused distribution (3× MIDI, 4× ATC)
- BODY PDU: Relay/fuse panel (12 circuits)

**Charging System:**
- 270A alternator
- BCDC Alpha 25: 25A DC-DC + solar input
- 80W solar panel (hood-mounted)

**Major Loads:**
- START battery: PMU (~220A max), SafetyHub (~111A max), starter, winch
- AUX battery: SwitchPros (~100A max), BODY PDU (~69A max)

**Ground System:**
- 5 ground buses total (negative, engine bay, firewall, SwitchPros, AUX battery)
- 6 direct START battery grounds
- 5 direct AUX battery grounds
