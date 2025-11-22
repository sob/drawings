---
hide:
  - toc
tags:
  - product-details
  - communication-systems
  - radio
  - gmrs
  - rugged-radio
---

# Communication Systems {#communication-systems}
## System Overview

The communication systems provide essential radio communication capabilities including GMRS for vehicle-to-vehicle communication, professional intercom systems for in-vehicle coordination, and future Ham radio expansion for long-distance emergency communication.

---



**System Overview:**
The Rugged Radio G1 is a 50W GMRS (General Mobile Radio Service) two-way radio for vehicle-to-vehicle communication and group coordination. GMRS operates on UHF frequencies (462-467 MHz) and requires an FCC license (family license, no exam required).

**Components:**

/// html | div.product-info

**Radio Unit:** Rugged Radio G1 GMRS Radio

**Model:** G1-GMRS (50W output)

**User Manual:** [Rugged Radio G1 Manual](https://cdn.shopify.com/s/files/1/0240/3280/4960/files/G1_Manual.pdf)

**Mounting:**

- Location: Behind dash, next to STX intercom
- Universal mounting brackets included (vehicle-specific brackets sold separately)
- **IMPORTANT:** Do NOT mount near ignition box to avoid RF interference

**Power Requirements:**

- Input Voltage: 12V DC (not compatible with 24V systems)
- **Power Source:** PMU OUT6 (25A capacity, CONSTANT power) - see [PMU Outputs][pmu-outputs]
- **Ground:** Direct START battery negative (RF grounding requirement)
- Current Draw: 1-2A receive, up to 15A transmit at 50W (max)

**Features:**

- 50W output power (maximum allowed for GMRS)
- 16 GMRS channels + repeater inputs
- CTCSS/DCS privacy codes
- VOX (voice-activated transmission)
- Scan function
- IP67 waterproof rating with all-aluminum chassis
- RFI (Radio Frequency Interference) protection

**Antenna:** Roof-mounted GMRS antenna (1/4 wave or 1/2 wave)

- Frequency: 462-467 MHz
- Mounting: Roof rack, fender, or NMO mount on roof
- Cable: RG58 or better coax (50© impedance)

**Intercom Integration:** Connects to Rugged Radio Intercom (see below)

- Allows driver/passengers to communicate via headsets
- Push-to-talk (PTT) button integration

///

**Wiring Summary:**
1. **Power (+):** Battery positive  inline fuse (15A)  G1 radio power input (12V DC)
   - **CRITICAL:** Direct battery connection required (not through BODY PDU or other circuits)
   - Run dedicated power wire from battery positive terminal through firewall (Grommet 4) to G1 radio
   - Firewall penetration: See [Firewall Ingress][firewall-penetrations-ingress-points]
   - Install 15A inline fuse holder within 18" of battery connection
   - Do NOT connect to ignition or other switched power sources (causes ground loop noise)
2. **Ground (-):** G1 ground  battery negative terminal (preferred) or chassis ground
   - Direct battery negative connection recommended for best RF performance
   - Clean ground critical for radio performance and noise reduction
   - Run ground wire through firewall (Grommet 4) from G1 to battery negative
   - Firewall penetration: See [Firewall Ingress][firewall-penetrations-ingress-points]
3. **Antenna:** G1 antenna output  coax cable  roof-mounted GMRS antenna
   - Use quality coax (RG58 or better) to minimize signal loss
   - Keep cable length <25 ft for best performance
   - **IMPORTANT:** Route antenna cable away from power leads to avoid interference
4. **Intercom Connection:** G1 radio RADIO port  Rugged Radio STX intercom RADIO port
   - Rugged Radio integration cable (specific cable for G1 GMRS to STX connection)
   - Handles audio in/out, PTT, and mute functions automatically

**Outstanding Items:**
- [ ] Run power wire from PMU OUT6 to G1 radio mounting location (10 AWG, via firewall Grommet 1)
- [ ] Run dedicated ground wire from G1 to START battery negative terminal (10 AWG, along tub to driver wheel well)
- [ ] Verify G1 and STX mounting behind dash does NOT place units near ignition box (avoid RF interference)
- [ ] Determine roof-mounted GMRS antenna mounting location and type (1/4 wave vs 1/2 wave)
- [ ] Plan antenna coax cable routing away from power leads (avoid interference)
- [ ] Verify coax cable type and quality (RG58 minimum, RG8 or LMR-400 preferred for long runs)
- [ ] Order Rugged Radio integration cable for G1 GMRS to STX intercom RADIO port connection
- [ ] Plan PTT button mounting location for driver (steering wheel, dash, or hand mic)
- [ ] Consider vehicle-specific mounting brackets for G1 (universal brackets included, specific brackets sold separately)

#### Rugged Radio Intercom System

**System Overview:**
The Rugged Radio STX Intercom allows driver and passengers to communicate via headsets, and integrates with the GMRS radio and Fusion head unit for external communication and music sharing.

**Components:**
- **Intercom Unit:** Rugged Radio STX 4-Place Intercom
  - **Quick Start Guide:** [Rugged Radio STX Quick Start Guide](https://cdn.shopify.com/s/files/1/0240/3280/4960/files/STX_-_Quick_Start_Guide.pdf?v=1724339126)
  - **Mounting:**
    - Universal mounting brackets included (vehicle-specific brackets sold separately)
    - Mount location: TBD - under dash or center console
    - **IMPORTANT:** Do NOT mount near ignition box to avoid RF interference
  - **Power Requirements:**
    - Input Voltage: 9-16V DC (12V nominal)
    - Current Draw: <2A typical
    - **CRITICAL:** Power must connect directly to 12V battery (not through BODY PDU)
      - Route all power cables directly to battery
      - Do NOT connect inline with other components
      - Do NOT tie to ignition, lights, or other power sources (causes ground loop noise)
      - Do NOT remove factory fuses or modify power cables
  - **Features:**
    - 4 headset ports (driver + 3 passengers)
    - VOX (voice-activated) or PTT (push-to-talk) mode per headset
    - Individual volume controls per headset
    - **RADIO port:** Connects to optional radio (G1 GMRS radio via Rugged Radio cable)
    - **AUX port:** Connects to cell phones, audio recorders, and other devices (Fusion MS-RA670 audio output)
    - **EXT port:** Optional modules available to connect up to 8 headsets (4-place can expand to 8-place)
    - Music mute when radio transmits or intercom is active
    - Compact form factor: 5.5" W × 3.5" D × 1.5" H
- **Headsets:** Rugged Radio headsets with microphones
  - **Type:** Over-ear or in-ear (behind-the-helmet style for off-road)
  - **Quantity:** 4 headsets (driver + 3 passengers)
  - **Connectors:** Rugged Radio proprietary push-to-connect headset jacks
  - **Cable Length:**
    - Front headsets: 6 ft cables (included with headsets)
    - Rear headsets: Custom extended cables (user-provided, not addressed here per user request)
- **PTT Buttons:** Push-to-talk buttons for GMRS radio transmission
  - **Mounting:** Driver PTT on steering wheel or dash, passenger PTT on grab handle or dash
  - **Wiring:** PTT button  STX intercom PTT input  G1 radio PTT output (via Rugged Radio integration cable)
  - **Note:** STX has built-in PTT inputs on each headset port

**Wiring Summary:**
1. **Power (+):** Battery positive  inline fuse (3A-5A recommended)  STX red power wire (9-16V DC input)
   - **CRITICAL:** Direct battery connection required (not through BODY PDU or other circuits)
   - Run dedicated power wire from battery positive terminal through firewall (Grommet 4) to STX intercom
   - Firewall penetration: See [Firewall Ingress][firewall-penetrations-ingress-points]
   - Install inline fuse holder within 18" of battery connection
   - Do NOT connect to ignition or other switched power sources (causes ground loop noise)
2. **Ground (-):** STX black ground wire  battery negative terminal (preferred) or chassis ground
   - Direct battery negative connection recommended for best audio quality
   - Clean ground critical for preventing ground loop noise in audio system
   - Run ground wire through firewall (Grommet 4) from STX to battery negative
   - Firewall penetration: See [Firewall Ingress][firewall-penetrations-ingress-points]
3. **Headset Connections:** 4 headset ports on STX unit
   - Port 1 (Driver): Front left position, 6 ft cable
   - Port 2 (Front Passenger): Front right position, 6 ft cable
   - Port 3 (Rear Left Passenger): Custom extended cable to rear seat
   - Port 4 (Rear Right Passenger): Custom extended cable to rear seat
4. **Radio Integration:** STX  G1 GMRS radio (audio in/out, PTT, mute)
   - Rugged Radio integration cable (specific cable for G1 GMRS to STX connection)
   - PTT handled automatically through integration cable
   - Radio audio mixes into intercom when receiving
   - Radio mutes music/intercom when transmitting
5. **Aux Input:** Fusion MS-RA670 audio output  STX aux input (3.5mm or RCA cable)
   - Music from radio plays through all headsets
   - Auto-mutes when intercom is active or radio transmits
6. **PTT Buttons (Optional):** External PTT buttons can be wired to STX PTT inputs
   - Each headset port has dedicated PTT input terminal
   - Driver PTT: Steering wheel or dash-mounted button  STX Port 1 PTT input
   - Passenger PTT: Dash or grab handle-mounted buttons  STX Port 2/3/4 PTT inputs

**Headset Port Mounting:**
- **Front Headset Ports (Ports 1 & 2):** Mount STX unit under dash or center console
  - 6 ft headset cables reach driver and front passenger positions
- **Rear Headset Ports (Ports 3 & 4):** Custom extended cables from STX unit to rear seat
  - User will run custom wires to rear passengers (not addressed here per user request)
  - Suggest mounting remote headset jacks in rear grab handles or on roll bar

**Outstanding Items:**
- [ ] Determine STX mounting location (under dash or center console)
- [ ] **IMPORTANT:** Ensure STX intercom is NOT mounted near ignition box (avoid RF interference)
- [ ] Run dedicated power wire from PMU OUT20 to STX (10 AWG, via firewall Grommet 1)
- [ ] PMU output has integrated 5A protection - no inline fuse needed
- [ ] Run dedicated ground wire from STX to START battery negative terminal (10 AWG, along tub to driver wheel well)
- [ ] Plan headset port access (all 4 ports on STX unit, or extend rear ports to rear grab handles)
- [ ] Determine if external PTT buttons will be used (or rely on headset-mounted PTT buttons)
- [ ] Plan PTT button mounting locations (driver: steering wheel or dash, passengers: grab handles)
- [ ] Order Rugged Radio integration cable for G1 GMRS to STX RADIO port connection
- [ ] Determine aux input cable type for Fusion MS-RA670 to STX AUX port (3.5mm or RCA)
- [ ] Plan cable routing for aux input from Fusion radio to STX intercom
- [ ] Consider vehicle-specific mounting brackets for STX (universal brackets included, specific brackets sold separately)

#### Ham Radio (Future)

**System Overview:**
Reserved circuit for future amateur (ham) radio installation. Ham radio requires an FCC license (Technician, General, or Amateur Extra) and provides long-range communication on VHF/UHF and HF frequencies.

**Reserved Circuit:**
- **Power:** PMU OUT12 (15A capacity, CONSTANT power) - see [PMU Outputs][pmu-outputs]
  - 15A capacity supports up to ~180W output radios (most mobile ham radios are 50-100W)
  - CONSTANT power allows radio to receive when vehicle is off
- **Ground:** Direct START battery negative (RF grounding requirement)
- **Wire Gauge:** 10 AWG for power (via firewall Grommet 1), 10 AWG for ground (along tub to driver wheel well)

**Potential Future Radio Types:**
- **VHF/UHF Mobile Radio:** 2-meter (144 MHz) and 70-cm (440 MHz) dual-band radio
  - Typical power: 50W VHF, 35W UHF
  - Amperage: ~10A transmit, 1A receive
  - Antenna: Roof-mounted dual-band whip (NMO mount)
- **HF Mobile Radio:** Long-range HF radio (3-30 MHz)
  - Typical power: 100W
  - Amperage: ~15A transmit, 1-2A receive
  - Antenna: Bumper-mounted or roof-rack-mounted HF antenna (requires tuner)

**Outstanding Items:**
- [ ] Determine if/when ham radio will be installed
- [ ] Decide on VHF/UHF vs HF vs both (dual installation)
- [ ] Verify 15A fuse is sufficient for chosen radio model
- [ ] Determine antenna mounting location (roof, bumper, or rack)
- [ ] Plan coax cable routing from radio to antenna
- [ ] Determine if ham radio will integrate with Rugged Radio Intercom

### SwitchPros Command Touch CT4

**Model:** Command Touch CT4
**Manual:** https://www.switchpros.com/wp-content/uploads/CT4-Rev-1.0.pdf
**Mounting:** 1.5" steering column
**Power Source:** TBD - likely BODY PDU SWITCHED circuit or direct from SwitchPros
**Ground:** TBD - chassis ground or dash ground point

**Functions:**

- **Turn Signals:** Left and right turn signal activation
  - Integrated with factory turn signal system or standalone
  - GPS module enables auto-cancel after completing turn
- **Horn Button:** Center button activates horn
  - Requires horn relay integration (see below)
- **License Plate Light Control:** TBD - integration with existing license plate lights
- **GPS Module:** Auto-cancel turn signals after turn completion
  - GPS module included with CT4
  - Mounting: TBD - under dash or on firewall

**Horn Relay Integration:**
- **Horn Relay:** TBD - relay specifications (contact rating, coil voltage)
  - **Trigger:** CT4 horn button  relay coil (low current, ~100-200mA)
  - **Main Power:** Battery+ or SWITCHED bus  relay contacts  horn
  - **Horn Load:** TBD - factory Jeep horn amperage (typically 3-6A)
  - **Fuse/Protection:** TBD - inline fuse or breaker for horn circuit (10A typical)
- **Horn Location:** Factory Jeep horn location (engine bay)

**Turn Signal Integration:**
- **Option 1: Factory Integration**
  - CT4 triggers factory turn signal flasher and bulbs
  - Wiring taps into existing turn signal circuits
- **Option 2: Standalone System**
  - CT4 controls separate turn signal LED lights (aftermarket)
  - Independent from factory wiring

**Outstanding Items:**

- [ ] Determine Command Touch CT4 power source circuit (BODY PDU SWITCHED or SwitchPros output)
- [ ] Determine Command Touch CT4 ground connection (chassis or dash ground point)
- [ ] Decide on turn signal integration method (factory integration vs standalone)
- [ ] Determine horn relay specifications (contact rating, coil voltage)
- [ ] Determine horn circuit fuse/breaker size (typically 10A)
- [ ] Verify factory horn amperage draw (typically 3-6A)
- [ ] Determine if horn relay will be mounted in engine bay or cabin
- [ ] Confirm horn relay trigger wiring from CT4 to relay coil
- [ ] Determine license plate light control integration (if used)
- [ ] Determine GPS module mounting location for auto-cancel turn signals (under dash or firewall)
- [ ] Confirm Command Touch CT4 mounting on 1.5" steering column (verify Jeep LJ steering column diameter)

---

## Camera Systems

### WolfBox Rearview Mirror Camera

**System Overview:**
The WolfBox system replaces the factory rearview mirror with a smart mirror that includes a front-facing dash camera and displays the rear backup camera feed.

**Components:**
- **Main Unit:** WolfBox rearview mirror with integrated display and front camera
  - **Location:** Windshield mount (replaces factory rearview mirror)
  - **Functions:**
    - Front-facing dash camera (always recording when powered)
    - Rear camera display (triggered by reverse gear or manual activation)
    - Touchscreen display for settings and playback
  - **Power:** BODY PDU F5 (10A fuse, CONSTANT power) - See [2.10 - BODY PDU][body-rtmr]
    - Always-on power allows continuous dash cam recording (parking mode)
    - Alternative: Could be SWITCHED power if parking mode not desired
  - **Features:**
    - Loop recording to SD card
    - G-sensor for collision detection
    - Night vision (front and rear cameras)
    - Lane departure warnings (if equipped)
  - **Display:** TBD - screen size (typically 9.66" or 12" models)
- **Rear Camera:**
  - **Location:** Mounted above license plate or rear tailgate
  - **Trigger:** Engine RTMR F7 (reverse light circuit, 10A)
    - When vehicle is in reverse, mirror automatically displays rear camera
  - **Power:** Via cable from main WolfBox unit (powered camera, not separate power needed)
  - **Cable Length:** TBD - verify cable length for routing from mirror to rear (typically 20-30 ft)
  - **Mounting:** Above license plate or integrated into spare tire carrier

**Wiring Summary:**
1. **Main Unit Power (+):** CONSTANT bus → BODY PDU F5 (10A) → WolfBox mirror unit power input
2. **Main Unit Ground (-):** WolfBox mirror ground → firewall ground stud or dash ground point
3. **Reverse Trigger:** Engine RTMR F7 (reverse light circuit) → WolfBox reverse trigger input
   - Camera automatically displays rear view when reverse signal is active
4. **Rear Camera Power:** Main WolfBox unit → rear camera via included cable (powered by main unit)
5. **Rear Camera Video:** Rear camera → main WolfBox unit via included cable

**Cable Routing:**
- **Main Unit to Rear Camera:** Route cable from windshield → along headliner → down A-pillar → under door sills → up tailgate or through rear cargo area to camera location
- **Reverse Trigger Wire:** Tap into Engine RTMR F7 reverse light circuit → route to WolfBox mirror unit
  - Can tap at reverse light switch location or at reverse light fixture
  - 18-20 AWG wire, low current (signal only)

**Outstanding Items:**
- [ ] Determine specific WolfBox model number (9.66" vs 12" screen, features)
- [ ] Confirm WolfBox power requirement is within 10A fuse capacity (typically 2-5A)
- [ ] Verify if CONSTANT or SWITCHED power is preferred for parking mode dash cam functionality
- [ ] Determine exact rear camera mounting location (above license plate vs spare tire carrier)
- [ ] Verify rear camera cable length is sufficient for routing from mirror to rear
- [ ] Determine reverse trigger wire tap location (reverse light switch or reverse light fixture)
- [ ] Plan cable routing path from windshield to rear camera (along headliner, under door sills)
- [ ] Determine ground connection point for WolfBox mirror unit (firewall stud or dash ground)
- [ ] Verify WolfBox compatibility with existing windshield mount or if adapter needed
- [ ] Verify WolfBox rear camera mounting above license plate does not interfere with BD S1 Pro lights

### Additional Camera Considerations (Future)

**Potential Future Cameras:**
- **Side Cameras:** For blind spot monitoring or trail spotting
  - Would require additional camera inputs (WolfBox may support multi-camera with upgraded model)
  - Power: BODY PDU spare circuits (CONSTANT power)
- **Front Camera:** Separate from WolfBox integrated front camera
  - For trail spotting or front bumper view during obstacles
  - Would need separate display or integration with WolfBox system
