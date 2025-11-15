# Wire Routing & Physical Layout {#wire-routing-physical-layout}
### Major Wire Runs

#### Battery to Engine Bay Distribution

- **Path:** TBD
- **Cables:**
  - 2/0 AWG red (alternator to battery+)
  - 2/0 AWG black (battery- to chassis)
  - 2/0 AWG (engine block to chassis)
  - Large gauge to CONSTANT bus breaker
  - Large gauge to SWITCHED bus breaker

#### Firewall Penetrations

- **Grommet 1:** TBD - Engine RTMR to cabin circuits
- **Grommet 2:** TBD - Body RTMR to engine bay circuits
- **Grommet 3:** Outside temperature probe wire (from BIM-17-2 module on firewall HDPE panel to grille area)
- **Grommet 4 (NEW):** Rugged Radio G1 GMRS and STX Intercom battery power cables
  - **G1 GMRS Power:** Battery positive  15A inline fuse  through firewall  G1 radio (behind dash)
  - **G1 GMRS Ground:** G1 radio  through firewall  battery negative
  - **STX Intercom Power:** Battery positive  3A-5A inline fuse  through firewall  STX intercom (behind dash)
  - **STX Intercom Ground:** STX intercom  through firewall  battery negative
  - **Wire Gauge:** TBD (14 AWG or 12 AWG for power, 14 AWG for ground recommended)
  - **Grommet Size:** TBD - must accommodate 4 wires (2 power + 2 ground)
  - **Note:** These devices require direct battery connection (not through Body RTMR) to prevent ground loop noise
- **Cummins Harness Punch-through:** Dedicated penetration for Cummins R2.8 wiring harness (provided by Cummins)
  - J1939 CAN High/Low wires tap into this harness location
  - No additional firewall modification needed for J1939
- **Wire Bundles:** TBD - list of all wires passing through each grommet

**Dakota Digital Module Panel:**
- **Location:** HDPE sheet mounted to firewall behind dashboard (cabin side)
- **Components Mounted:**
  - 01-2-J1939 (J1939 interface module)
  - GPS-50-2 (GPS speed module)
  - BIM-22-3 (TPMS module)
  - BIM-17-2 (Compass/outside temp module)
- **Main Harness:** Single BIM/IO cable from Dakota Digital 1996-03 main cluster  HDPE panel  all 4 BIM modules
- **External Connections:**
  - **J1939 CAN Bus:** Tap into Cummins harness punch-through (CAN High/Low)  route to 01-2-J1939 module on HDPE panel
  - **GPS Antenna:** GPS-50-2 module to dash/windshield mounted antenna
  - **Outside Temp Probe:** BIM-17-2 module through Grommet 3 to grille area

#### Dash to Console

- **Path:** TBD - under dash, along firewall?
- **Circuits:** Switch panel wiring, USB power, radio wiring

#### Cab to Cargo Area

- **Path:** TBD - under seats? Through floor channels?
- **Circuits:**
  - Rear roll bar lights
  - Rear switches
  - Compressor power and control
  - Rear locker control

#### Roof/Roll Bar Wiring

- **Path:** TBD - through A-pillar? Along roll bar?
- **Circuits:**
  - Roof light bars (center section, outer spots)
  - Dome lights on front roll bar
  - Rear roll bar lights

### Ground Points

#### Engine Bay

- **Primary:** Battery negative to chassis (2/0 AWG) - location TBD
- **Engine Block:** Engine block to chassis (2/0 AWG) - location TBD
- **Accessories:** Dedicated ground stud on firewall or fender - TBD
- **SwitchPros:** Direct to battery negative (per manufacturer spec)

#### Cabin

- **Firewall:** Ground stud for body electronics - TBD
- **Floor Pan:** Ground point for seat electronics - TBD
- **Dash:** Radio and instrument cluster grounds - TBD

#### Cargo Area

- **Frame Rails:** Ground points for rear lighting - TBD
- **Tub Mounting Bolts:** Potential ground points - verify paint removal

**Outstanding Items:**

- [ ] Determine exact routing path for battery to engine bay distribution cables
- [ ] Determine all firewall penetration locations (Grommet 1, Grommet 2 for general circuits, Grommet 4 for G1/STX battery cables)
- [ ] Create complete wire bundle list for each firewall penetration
- [ ] Determine wire gauge for Grommet 4 (G1/STX battery cables): 14 AWG or 12 AWG recommended
- [ ] Determine grommet size for Grommet 4 (must accommodate 4 wires: 2 power + 2 ground)
- [ ] Determine exact routing path from dash to console for switch panel wiring
- [ ] Determine exact routing path from cab to cargo area (under seats or through floor channels)
- [ ] Determine exact routing path for roof/roll bar wiring (through A-pillar or along roll bar)
- [ ] Identify all specific ground point locations in engine bay
- [ ] Identify all specific ground point locations in cabin
- [ ] Identify all specific ground point locations in cargo area
- [ ] Verify paint removal at all ground points for clean metal-to-metal contact
- [ ] **Dakota Digital HDPE Panel:** Determine exact HDPE panel dimensions and mounting points on firewall
- [ ] **Dakota Digital HDPE Panel:** Plan exact cable routing for BIM/IO harness from dash cluster to firewall HDPE panel
- [ ] **Dakota Digital GPS:** Determine exact GPS antenna mounting location (dash top vs windshield mount) and cable routing
- [ ] **Dakota Digital Temp Probe:** Determine exact grille area mounting location and wire routing through firewall (Grommet 3)
- [ ] **Dakota Digital J1939:** Confirm J1939 CAN High/Low tap location at Cummins harness punch-through and routing to 01-2-J1939 module on HDPE panel
