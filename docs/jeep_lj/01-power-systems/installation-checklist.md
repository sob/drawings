# Section 1: Power Systems - Installation Checklist

Organized by installation order for efficient build workflow.

---

## Phase 1: Foundations

### Battery Compartments

- [ ] Install Odyssey PC1500 in factory engine bay location (front)
- [ ] Build enclosed compartment in passenger wheel well with access panel (rear)
- [ ] Install Odyssey PC1500 in rear wheel well

### Grounding System

**Frame Rail Grounds:**

- [ ] Identify front frame rail ground point location
- [ ] Identify rear frame rail ground point location
- [ ] Install 2/0 AWG: START battery- → Front Frame Rail
- [ ] Install 2/0 AWG: AUX battery- → Rear Frame Rail
- [ ] Install 2/0 AWG: Engine Block → Front Frame Rail

**Battery Ground Reference:**

- [ ] Route 2/0 AWG: START battery- → AUX battery- (8 ft measured routing distance - see [Wire Distance Reference][wire-distance])

**Firewall Ground Stud:**

- [ ] Install firewall ground stud (existing or new with backing plate)

**Ground Testing:**

- [ ] Verify <0.1V drop: START battery- to front frame rail (engine @ 2000 RPM)
- [ ] Verify <0.1V drop: AUX battery- to rear frame rail (engine @ 2000 RPM)
- [ ] Verify <0.05V drop: START battery- to AUX battery- (engine @ 2000 RPM)
- [ ] Verify <0.05V drop: START battery- to AUX battery- (BCDC charging @ 25A)
- [ ] Verify <0.2V drop: START battery- to AUX battery- (winch operation @ 400A)

---

## Phase 2: Power Distribution

### START battery Bus Bars & Circuit Breakers

**Bus Bars:**

- [ ] Mount CONSTANT bus bar (Blue Sea 2107 PowerBar, 600A) on firewall near PMU
- [ ] Mount NEGATIVE bus bar on firewall (engine bay side)

**Circuit Breakers:**

- [ ] Mount Mechanical Products 174-S2-300-2 300A (PMU main power)
- [ ] Mount Mechanical Products 174-S2-150-2 150A (SafetyHub 100)
- [ ] Mount Mechanical Products 174-S2-040-2 40A (BCDC input)

**CONSTANT Bus Wiring:**

- [ ] Run 2/0 AWG: START battery+ → CONSTANT bus (~5 ft)
- [ ] Run 1 AWG: CONSTANT bus → 300A CB → PMU main power (~7-10 ft, temp-derated for 60°C)
- [ ] Run 4 AWG: CONSTANT bus → 150A CB → SafetyHub 100
- [ ] Run 4 AWG: CONSTANT bus → 40A CB → BCDC input

**NEGATIVE Bus Wiring:**

- [ ] Run 2/0 AWG: START battery- → NEGATIVE bus bar
- [ ] Run 2/0 AWG: NEGATIVE bus → Engine block
- [ ] Run 2/0 AWG: NEGATIVE bus → Chassis ground
- [ ] Run 2/0 AWG: NEGATIVE bus → AUX battery (8 ft measured routing - see [Wire Distance Reference][wire-distance])
- [ ] Connect PMU ground reference (per harness) and relay grounds (14-16 AWG)

**Direct Battery Connections (No Circuit Breaker):**

- [ ] Connect ECM power/ground directly to START battery terminals (12 AWG, Cummins harness)
- [ ] Run 6-8 AWG: START battery+ → Grid heater relay (via integrated fusible link, 40-80A)
- [ ] Connect grid heater ground directly to START battery-
- [ ] Run 1/0 AWG: AUX battery+ → Winch positive (13 ft one-way, direct connection - no CB)
- [ ] Run 1/0 AWG: AUX battery- → Winch negative (13 ft one-way, matches positive path)

**Testing:**

- [ ] Verify PMU main power always on (via 300A CB)
- [ ] Measure voltage drop across main power cables under load
- [ ] Measure ground resistance: NEGATIVE bus to battery- (<0.1 ohms)

### AUX battery Bus Bars & Circuit Breakers

**Inter-Battery Wiring:**

- [ ] Route cables along frame rail with protection: Front → AUX battery area

**Bus Bars & Protection:**

- [ ] Mount CONSTANT bus bar (Blue Sea 2104 PowerBar, 225A) in rear wheel well
- [ ] Install 150A CB: AUX battery+ → CONSTANT bus → SwitchPros RCR-Force 12
- [ ] Install 100A CB: CONSTANT bus → BODY PDU

**CONSTANT Bus Wiring:**

- [ ] Run 2/0 AWG: AUX battery+ → CONSTANT bus (~3 ft)
- [ ] Run per spec: CONSTANT bus → 150A CB → SwitchPros RCR-Force 12
- [ ] Run 8 AWG: CONSTANT bus → 100A CB → BODY PDU

### BCDC Alpha 25 Installation

- [ ] Mount BCDC in wheel well (water-protected, LED visibility access)
- [ ] Run 4 AWG: START battery+ → 40A CB → BCDC input (8 ft measured routing - see [Wire Distance Reference][wire-distance])
- [ ] Run 4 AWG: BCDC output → AUX battery+
- [ ] Run 4 AWG: BCDC negative → AUX battery- (per BCDC spec)
- [ ] Route ignition trigger from PMU to BCDC (18 AWG)
- [ ] Install battery temperature sensor on AUX battery

**BCDC Configuration & Testing:**

- [ ] Configure Green Power Priority via RedArc app
- [ ] Test jump start assist function

### Alternator

- [ ] Install 270A alternator (Premier Power Welder HO-C28)
- [ ] Route 2/0 AWG positive: Alternator → START battery (shortest path)
- [ ] Connect positive to START battery terminal
- [ ] Connect negative to NEGATIVE bus bar

---

## Phase 3: Controllers - Physical Installation & Main Power

### PMU24 Physical Installation

- [ ] Mount PMU (firewall or inner fender - accessible for LED/USB diagnostics)
- [ ] Connect PMU ground reference to NEGATIVE bus via Pin 25 (per harness - logic/CAN reference only)

### BODY PDU Physical Installation

- [ ] Determine BODY PDU part number
- [ ] Mount under dash (passenger side)
- [ ] Route CONSTANT power from AUX battery via 8 AWG, 100A circuit breaker

### SafetyHub Physical Installation

- [ ] Mount SafetyHub 150 in engine bay
- [ ] Connect power from START battery via 150A CB
- [ ] Connect ground to NEGATIVE bus bar

### SwitchPros RCR-Force 12 Physical Installation

- [ ] Mount SwitchPros controller
- [ ] Connect power from AUX battery via 150A CB
- [ ] Connect ground to lighting ground bus

**SwitchPros Custom Harness Note:**

!!! info "Custom Delphi Harness Design"
    Create 12 custom 2-pin Delphi harnesses at SwitchPros:

    - Each SwitchPros output → 2-pin Delphi plug (power + ground combined)
    - Each light → matching 2-pin Delphi plug
    - Back of SwitchPros: ~12 Delphi connectors for plug-and-play lighting
    - Eliminates individual wire routing - each light is single plug connection

---

## Phase 4: Integration & Wiring

### Ignition Signal Distribution

- [ ] Route 18 AWG from ignition RUN through Grommet 2
- [ ] Split to: PMU Pin 7, PMU In 6, CT4, SwitchPros, Fusion Radio, BCDC
- [ ] Total current <500mA for all taps

### PMU Input Wiring

- [ ] Run 18 AWG: Ignition RUN → PMU Pin 7
- [ ] Run 18 AWG: Ignition RUN → PMU In 6
- [ ] Wire horn button → In 1
- [ ] Wire brake pedal switch → In 2
- [ ] Wire reverse switch → In 3
- [ ] Wire clutch pedal switch → In 4
- [ ] Wire ignition START → In 5
- [ ] Wire CT4 SW3 (headlight status) → In 7
- [ ] Wire A/C button → In 9

### PMU Output Wiring

**High-Current Outputs (Combined):**

- [ ] Wire radiator fan → OUT2+3+4 combined (75A total capacity)
- [ ] Wire iBooster main → OUT5+6 combined (50A total capacity)

**Individual Outputs:**

- [ ] Wire HVAC blower → OUT1 (20A)
- [ ] Wire iBooster ignition → OUT19 (7A)
- [ ] Wire oil cooler fan → OUT7 (15A)
- [ ] Wire PS cooler fan → OUT8 (15A)
- [ ] Wire wipers (WS-51C) → OUT11 (15A)
- [ ] Wire Dakota Digital cluster → OUT12 (15A)
- [ ] Wire CT4 → OUT13 (10A, CONSTANT)
- [ ] Wire DRL/parking → OUT14 (8A)
- [ ] Wire A/C clutch → OUT17 (5A)
- [ ] Wire horn → OUT18 (5.4A)
- [ ] Wire brake lights → OUT21 (3A)
- [ ] Wire reverse lights → OUT22 (3A)

### PMU CAN Bus Integration

- [ ] T-tap J1939 CAN High → PMU Pin 23/24 (18-20 AWG twisted pair, <12" stub)
- [ ] T-tap J1939 CAN Low → PMU Pin 36/37 (18-20 AWG twisted pair, <12" stub)
- [ ] Disable PMU internal CAN termination in software
- [ ] Verify 60Ω resistance across CAN High/Low at ECM connector (harness disconnected, ignition off)
- [ ] Configure PMU to read J1939 SPNs: 100, 110, 175, 190

### BODY PDU Circuit Wiring

- [ ] Wire Fusion Radio memory (F2, 5A, 18 AWG, CONSTANT)
- [ ] Wire Fusion Radio amp (F3, 15A, 14 AWG, CONSTANT)
- [ ] Wire USB ports (F4, 20A, 14 AWG, CONSTANT) - 2× Powerwerx PanelUSB-75W
- [ ] Wire WolfBox camera (F5, 10A, 16 AWG, CONSTANT)
- [ ] Wire heated seats (F6/F7, 15A each, 14 AWG, SWITCHED) via manual switches

**Verification:**

- [ ] Verify Fusion radio current draw matches fuse ratings
- [ ] Verify WolfBox model and 10A fuse adequate
- [ ] Verify heated seat draw is 15A/seat (PRP EnduroTrek spec)

### SafetyHub Circuit Wiring

- [ ] Wire ARB compressor motor 1 → MIDI-1 (60A, 10 AWG, CONSTANT)
- [ ] Wire ARB compressor motor 2 → MIDI-2 (60A, 10 AWG, CONSTANT)
- [ ] Wire winch contactor trigger → ATC-1 (10A, from 3-position selector)

### Solar Panel Installation

- [ ] Install Cascadia 4x4 80W panel per manufacturer instructions
- [ ] Route wiring: Hood → Firewall → BCDC (~10-12 ft)
- [ ] Connect solar positive to BCDC solar input
- [ ] Connect solar negative to chassis ground (NOT BCDC negative)
- [ ] **CRITICAL:** Verify polarity before connection
- [ ] Monitor BCDC LED in daylight to verify solar charging

---

## Phase 5: Testing & Programming

### PMU Programming

**Output Combining:**

- [ ] Configure radiator fan combining (OUT2+3+4)
- [ ] Configure iBooster combining (OUT5+6)

**Logic Programming:**

- [ ] Program DRL auto-off when headlights active (In 6 + In 7 logic)
- [ ] Program starter safety (In 4 clutch + In 5 START required)
- [ ] Program A/C clutch engagement logic
- [ ] Program oil cooler fan based on SPN 175 (220-230°F hysteresis)
- [ ] Program PS cooler fan based on SPN 110 (210-220°F hysteresis)
- [ ] Configure sequential load startup delays (0.5s, 1.0s, 1.5s)

**Backup:**

- [ ] Export/backup configuration (.pmu format) to git repository
- [ ] Print critical logic (DRL, fan control, starter safety) for emergency recovery

### PMU Testing

- [ ] Verify J1939 communication and data accuracy
- [ ] Test DRL auto-off logic
- [ ] Test starter safety (requires clutch + START)
- [ ] Test A/C clutch engagement
- [ ] Test CAN-based fan controls at threshold temps
- [ ] Test sequential load startup timing
- [ ] Verify LED diagnostics show correct states

### System Integration Testing

- [ ] Verify all PMU outputs operate correctly
- [ ] Test all BODY PDU circuits
- [ ] Test SafetyHub circuits (ARB, winch trigger)
- [ ] Verify SwitchPros Delphi connectors and outputs
- [ ] Final voltage drop measurements under load
- [ ] Final ground resistance verification

---

## Reference Documentation

- **PMU24:** [PMU User Manual v101.1.5][pmu-manual]
- **BCDC Alpha 25:** [Installation Manual][bcdc-install]
- **Odyssey PC1500:** [Product Page][odyssey-pc1500]
- **Blue Sea Systems:** Product-specific installation instructions per part number

[pmu-manual]: https://www.ecumaster.com/files/PMU/PMU_Manual.pdf
[bcdc-install]: https://cdn.intelligencebank.com/au/share/yE9N/zJpl/NNRlJ/original/Install+Guide+BCDC+Alpha+50R+EN
[odyssey-pc1500]: https://www.odysseybattery.com/products/odx-agm34-battery-34-pc1500t/
[wire-distance]: 01-power-generation/05-wire-distance-reference.md
