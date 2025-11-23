---
hide:
  - toc
tags:
  - product-details
  - audio-systems
  - head-unit
  - fusion
---

# Audio Systems {#audio-systems}

### Communication Systems {#audio-communication-systems}

#### Radio Head Unit

**System Overview:**
The dash-mounted radio head unit provides AM/FM radio, Bluetooth connectivity, and NMEA 2000 integration for marine-grade performance in off-road conditions.

**Components:**

/// html | div.product-info

**Radio Head Unit:** Fusion MS-RA670 Marine Entertainment System

**Manual:** [Fusion MS-RA670 Installation Manual](https://pdf.crutchfieldonline.com/ImageBank/v20190610170100/Manuals/917/917RA670.PDF)

**Location:** Dashboard center console (factory radio location)

**Power Requirements:**

- **Constant Power (Memory):** Yellow wire - 12V constant (battery direct)
- **Switched Power (Ignition):** Red wire - 12V switched (on with ignition)
- **Fuse Rating:** 15A (per manual specifications)
- **Combined Circuit:** BODY PDU F2 (20A fuse, SWITCHED power with constant power tap)

**Features:**

- AM/FM radio with RDS
- Bluetooth audio streaming and hands-free calling
- Multi-zone audio (3 zones + subwoofer)
- DSP (Digital Signal Processing) with presets
- NMEA 2000 integration (future expansion for GPS/depth/wind data)
- PartyBus networking (link multiple Fusion units)
- IPX7 waterproof rating (marine-grade for off-road dust/water resistance)
- USB audio playback

**RCA Pre-Outs (to Fusion Apollo amplifier):**

- Zone 1: Left + Right RCA outputs (to amplifier channels 3 & 4 for front dash speakers)
- Zone 2: Left + Right RCA outputs (to amplifier channels 5 & 6 for rear roll bar speakers)
- Zone 3: Left + Right RCA outputs (available for future expansion)
- Subwoofer: Mono RCA output (to amplifier channels 1+2 bridged for subwoofer)

**Speaker Outputs:** 4x 50W RMS (not used - amplifier powers all speakers)

**Antenna:** Factory Jeep AM/FM antenna (mounted on fender or windshield)

- Motorola connector (standard automotive antenna)

**Display:** 2.7" full-color TFT display with sunlight viewability

**Load:** 15A maximum (per manual specifications)

///

**Wiring:**

1. **Constant Power (Yellow wire):** CONSTANT bus  BODY PDU F2 (20A)  MS-RA670 constant power (memory)
   - Note: F2 will need to source from CONSTANT bus (not SWITCHED bus) to provide both constant and switched power
   - Alternative: Run separate constant power wire from CONSTANT bus to radio, keep F2 on SWITCHED bus
2. **Switched Power (Red wire):** SWITCHED bus  BODY PDU F2 (20A)  MS-RA670 switched power (ignition)
   - Radio powers on/off with ignition
3. **Ground (Black wire):** MS-RA670 ground  firewall ground stud or dash ground point
   - Clean ground critical for audio quality and noise reduction
4. **Speaker Wiring:** MS-RA670 speaker outputs  front/rear speakers via factory harness (where possible)
   - Front Left: White (+) / White-Black (-)
   - Front Right: Gray (+) / Gray-Black (-)
   - Rear Left: Green (+) / Green-Black (-)
   - Rear Right: Purple (+) / Purple-Black (-)
5. **Antenna:** MS-RA670 antenna input (blue Motorola connector)  factory antenna cable
6. **Bluetooth Microphone:** MS-RA670 microphone input  wired microphone mounted near driver (for hands-free calling)

**Power Source Clarification:**
Since the MS-RA670 requires both constant power (memory/clock) and switched power (on/off), BODY PDU F2 needs to be configured to provide both:

**Option 1 (Recommended):** Modify F2 to support dual power

- F2 constant power input from CONSTANT bus  MS-RA670 yellow wire (memory)
- F2 switched power input from SWITCHED bus  MS-RA670 red wire (ignition on/off)
- Single 20A fuse protects both circuits (15A radio draw is within capacity)

**Option 2:** Separate circuits

- F2 (SWITCHED bus, 20A)  MS-RA670 red wire only (ignition power)
- New spare BODY PDU circuit (CONSTANT bus, 15A)  MS-RA670 yellow wire only (memory)

**Outstanding Items:**

- [ ] Verify radio ignition trigger wire connection for on/off control
- [ ] Determine ground connection point for MS-RA670 (firewall stud or dash ground)
- [ ] Plan wiring for Bluetooth microphone mounting location (near driver for hands-free calling)
- [ ] Determine if NMEA 2000 integration will be used (future GPS/depth/wind data display on radio)
- [ ] Configure MS-RA670 DSP settings for subwoofer crossover (typically 80-120 Hz low-pass filter)
- [ ] Verify MS-RA670 Zone 1/2/3 RCA output configuration in settings (assign zones to front/rear/sub)

#### Fusion Apollo Amplifier

**System Overview:**
The Fusion Apollo amplifier provides high-power audio for speakers and subwoofer, delivering marine-grade performance with Class-D efficiency.

**Components:**

- **Amplifier:** Fusion Apollo Marine 6-Channel Amplifier
  - **Model:** MS-AP61800 / 010-02284-65
  - **Installation Manual:** [Fusion Apollo Multichannel Amplifiers Installation Instructions](https://static.garmin.com/pumac/Fusion_Apollo_Multichannel_Amplifiers_Install_EN-US.pdf)
  - **Mounting:** TBD - cargo area or under rear seat (recommended for central speaker wire routing)
  - **Power Source:** Direct from CONSTANT bus or AUX battery (high current)
  - **Class:** Class-D amplifier (high efficiency, low heat)
  - **Total Power Output:** 1800W total rated power
  - **Channel Configuration:**
    - **6-Channel Mode:** 6x 150W RMS per channel @ 4© @ 14.4V input, <1% THD
    - **Bridged Mode:** 3x 580W RMS @ 4© @ 14.4V input, <1% THD
      - Each pair of channels is independently bridgeable (1+2, 3+4, 5+6)
      - Can be configured as 6-channel, 5-channel, 4-channel, or 3-channel
    - **Recommended Configuration (4 speakers + 1 subwoofer):**
      - Channels 1+2 bridged: 580W RMS @ 4© for subwoofer
      - Channels 3+4: 2x 150W RMS @ 4© for front door speakers
      - Channels 5+6: 2x 150W RMS @ 4© for rear roll bar tower speakers
  - **Bridge Adapters (Included):**
    - Fusion includes bridge adapters with built-in magnets
    - Magnets automatically trigger amplifier "High Power Mode" when bridging
    - Adapters block unused speaker terminal wires for clean subwoofer bridging
    - Adapter blocks one RCA input to create mono subwoofer channel
  - **Fuse Rating:** 40A fast-acting fuse (per Fusion Apollo manual specifications)
  - **Current Draw:** TBD - verify actual amperage (estimated 35-45A continuous, 60-70A peak at full volume)
    - Class-D efficiency typically 70-85%, so ~40A continuous draw at full power (1800W ÷ 12V ÷ 0.75 efficiency H 40A)
  - **Protection Features:**
    - Reverse voltage protection
    - Input under/over voltage protection
    - Over temperature protection
    - Output short circuit protection
    - Ignition Safety Protected (SAE J1171)
  - **Operating Temperature:** 32°F to 122°F (0°C to 50°C)
  - **Dimensions:** 11.69" W × 7.06" H × 2.13" D (with mounting bracket)
  - **Weight:** 5.95 lbs (2.7 kg)
  - **Features:**
    - High-power mode adapters for bridging (included)
    - IPX2 waterproof rating (marine-grade for dust/water resistance)
    - Compatible with Fusion PartyBus for multi-zone audio
    - DSP-enabled integration with MS-RA670 head unit
    - Independent channel pair bridging for flexible configuration

**Speaker Configuration:**

- **Front Dash Speakers (Channels 3 & 4):** JL Audio M6-650X-S-GmTi-i (pair)
  - **Model:** M6-650X-S-GmTi-i (6.5" 2-way coaxial marine speakers)
  - **Product Page:** [JL Audio M6-650X-S-GmTi-i](https://www.jlaudio.com/products/m6-650x-s-gmti-i-marine-audio-coaxial-speakers-93715)
  - **Type:** 2-way coaxial (integrated 0.8" silk dome tweeter - no separate tweeter installation needed)
  - **Power Handling:** 75W RMS per speaker @ 4© (25-150W recommended amplifier power)
  - **Amplifier Output:** 150W RMS per channel (channels 3 & 4)
    - **Power Headroom:** 2:1 ratio (150W amp / 75W speaker) - excellent headroom for clean, undistorted power
  - **Impedance:** 4©
  - **Frequency Response:** 55-25,000 Hz (±3dB)
  - **Sensitivity:** 89.5 dB @ 1W/1m
  - **Features:**
    - Integrated 0.8" pure silk dome tweeter (marine-treated, mounted on woofer)
    - Multi-order 2-way passive crossover (built into speaker chassis)
    - Automatic solid-state tweeter protection circuit
    - Transflective RGB LED lighting (controlled separately from audio)
    - Injection-molded mica-filled polypropylene woofer with synthetic rubber surround
    - Gunmetal trim ring with titanium sport grille
  - **Mounting:** Dashboard (custom 6.5" cutouts)
    - TBD: Exact dash mounting locations (typical: dash end caps or kick panels)
    - May require custom speaker pods or dash modification for flush mount
- **Rear Roll Bar Tower Speakers (Channels 5 & 6):** JL Audio M6-650VEX-Mb-S-GmTi-i (pair)
  - **Model:** M6-650VEX-Mb-S-GmTi-i (6.5" 2-way enclosed marine tower speakers)
  - **Product Page:** [JL Audio M6-650VEX-Mb-S-GmTi-i](https://www.jlaudio.com/products/m6-650vex-mb-s-gmti-i-marine-audio-enclosed-speaker-systems-vex-93411)
  - **Power Handling:** 75W RMS per speaker @ 4©
  - **Amplifier Output:** 150W RMS per channel (channels 5 & 6)
    - **Power Headroom:** 2:1 ratio (150W amp / 75W speaker) - excellent headroom for clean, undistorted power
  - **Impedance:** 4©
  - **Frequency Response:** 100-25,000 Hz
  - **Sensitivity:** 89.5 dB
  - **Features:**
    - Built-in RGB LED lights (controlled separately from audio)
    - 3/4" silk dome tweeters
    - Injection-molded, mica-filled polypropylene woofers with synthetic rubber surrounds
    - Enclosed design with weather-resistant enclosures for dust/water exposure
  - **Dimensions:** 7-1/16" W × 7-5/16" H × 6-1/4" D
  - **Mounting:** Roll bar/cage mount (wakeboard tower style clamps)
- **Subwoofer (Channels 1+2 Bridged):** JL Audio M7-12IB-S-GmTi-i-4
  - **Model:** M7-12IB-S-GmTi-i-4 (12" marine infinite baffle subwoofer with RGB LED)
  - **Product Page:** [JL Audio M7-12IB-S-GmTi-i-4](https://www.garmin.com/p/1708661/pn/010-03288-00)
  - **Power Handling:** 600W RMS @ 4© (recommended amplifier power: 200-600W)
  - **Amplifier Output:** 580W RMS @ 4© (channels 1+2 bridged)
    - **Power Match:** 580W / 600W = 97% - excellent match within recommended range
  - **Impedance:** 4©
  - **Sensitivity:** 86.7 dB @ 1W/1m
  - **Frequency Response:**
    - Free Air Resonance (FS): 35.34 Hz
    - Sealed enclosure -3dB cutoff: 35.52 Hz
    - Ported enclosure -3dB cutoff: 20.96 Hz
  - **Type:** Infinite Baffle (IB) - designed to operate without dedicated enclosure
    - Requires large air volume behind subwoofer (minimum 3 cu. ft. / 84.95 liters)
    - Ideal for mounting in cargo area wall or under-seat location with access to large air space
  - **Voice Coil:** 4" diameter (102mm)
  - **Cone Material:** Injection-molded, mica-filled polypropylene with synthetic rubber surround
  - **Features:**
    - Transflective" RGB LED lighting (controlled separately from audio via MLC-RW)
    - Gunmetal trim ring with titanium sport grille
    - Marine-grade construction (IPX rating TBD from spec sheet)
  - **Dimensions:**
    - Overall diameter: 14" (356mm)
    - Overall depth: 9.39-9.42" (239-240mm)
    - Mounting depth clearance: 7.94" (202mm)
    - Mounting hole cutout: 12.0625" (306mm)
    - Bolt hole circle: 12.813" (325mm)
    - Frontal grille protrusion: 1.45-1.48"
  - **Weight:** 25.35 lbs (11.5 kg)
  - **Mounting:**
    - Infinite baffle installation in cargo area wall or rear seat/tub wall
    - Requires 12.0625" (306mm) circular cutout in mounting surface
    - Must have access to at least 3 cu. ft. air space behind mounting surface
    - Jeep LJ cargo area provides ideal infinite baffle environment (large enclosed volume)
  - **Warranty:** 3 years

**JL Audio LED Lighting System:**

- **LED Controller:** JL Audio MLC-RW Marine LED Lighting Controller
  - **Product Page:** [JL Audio MLC-RW](https://www.jlaudio.com/marine-audio-speakers-speaker-accessories-mlc-rw-99816)
  - **Power Output:** 30A (400W) continuous output for LED circuits
  - **Capacity:** Controls LEDs for up to 60 JL Audio marine speakers (with appropriate wiring)
  - **Control:** WiFi app (LiteWave ITI for iOS/Android) + included rotary encoder
  - **Technology:** PWM (Pulse Width Modulation) for efficient RGB LED control
  - **Protection:** Over-current, short-circuit, voltage/temperature monitoring
  - **Power Requirements:**
    - Input Voltage: 12V DC
    - Current Draw: Up to 30A (30A fuse or breaker required for full LED capacity)
    - For 5 JL Audio speakers (4x M6 + 1x M7): Estimated 5-10A total LED draw
  - **Mounting Configuration:**
    - **MLC-RW Controller Unit:** Mount next to Fusion Apollo amplifier (behind dash or cargo area)
      - Keeps LED controller and amplifier in same location for clean wiring
    - **Rotary Encoder:** Dash-mounted with extension cable from MLC-RW unit
      - Allows user-accessible LED control without accessing controller unit
      - Extension cable from controller to dash location (typically near radio or center console)
- **Integrated Speaker/LED Cable:** JL Audio XM-WHTMFC Multifunction Cable
  - **Model:** XM-WHTMFC-25 or XM-WHTMFC-250 (25 ft or 250 ft spools)
  - **Configuration:** Single cable with integrated speaker + LED wires
    - 2x 16 AWG OFC copper speaker leads (audio signal)
    - 4x 20 AWG OFC copper LED power leads (RGB + common for LED lighting)
  - **Construction:** Fine-strand OFC, stannum-plated for corrosion resistance, marine-grade white PVC jacket
  - **Use:** Single cable run from amplifier/MLC-RW to each speaker (audio + LED control)

**Wiring Summary:**

1. **Amplifier Power (+):** CONSTANT bus  40A Blue Sea breaker  6 AWG red wire  amplifier B+ terminal
   - Direct connection to CONSTANT bus (AUX battery) for high current
   - Run dedicated 6 AWG wire from AUX battery or CONSTANT bus bar to amplifier (1800W requires heavier gauge)
   - Replace amplifier's included 40A inline fuse with centrally-located Blue Sea breaker for easier access
2. **Amplifier Ground (-):** Amplifier ground terminal  6 AWG black wire  chassis ground or AUX battery negative
   - Clean, solid ground critical for amplifier performance and noise reduction
   - Keep ground wire <18 inches for best performance
3. **MLC-RW LED Controller Power (+):** CONSTANT bus  BODY PDU spare circuit (30A)  MLC-RW power input
   - MLC-RW rated for 30A output (400W), requires 30A fuse/breaker for full capacity
   - For 5 speakers: estimated 5-10A actual draw, but 30A circuit allows full controller capacity
   - Note: BODY PDU can accommodate additional fuse slots if needed
4. **MLC-RW LED Controller Ground (-):** MLC-RW ground  chassis ground or dash ground point
5. **Remote Turn-On:** MS-RA670 remote turn-on output  18 AWG wire  amplifier remote terminal
   - Radio sends 12V signal to turn on amplifier when radio is on
   - Amplifier shuts off automatically when radio turns off
6. **Audio Input (RCA):** MS-RA670 RCA outputs  shielded RCA cables  amplifier RCA inputs
   - Zone 1 (Front): MS-RA670 Zone 1 L+R RCA  amplifier channels 3 & 4 (front dash speakers)
   - Zone 2 (Rear): MS-RA670 Zone 2 L+R RCA  amplifier channels 5 & 6 (rear roll bar tower speakers)
   - Subwoofer: MS-RA670 mono subwoofer RCA  amplifier channels 1 & 2 (bridged for sub)
   - Zone 3: MS-RA670 Zone 3 L+R RCA available for future expansion
7. **Speaker + LED Outputs (using JL Audio XM-WHTMFC integrated cable):**
   - **Channel 3 (Front Left Dash):** XM-WHTMFC cable to speaker
     - 16 AWG speaker leads: Amplifier Ch3  speaker audio
     - 20 AWG LED leads: MLC-RW RGB outputs  speaker LED (R/G/B/common)
   - **Channel 4 (Front Right Dash):** XM-WHTMFC cable to speaker
     - 16 AWG speaker leads: Amplifier Ch4  speaker audio
     - 20 AWG LED leads: MLC-RW RGB outputs  speaker LED (R/G/B/common)
   - **Channel 5 (Rear Left Roll Bar):** XM-WHTMFC cable to speaker
     - 16 AWG speaker leads: Amplifier Ch5  speaker audio
     - 20 AWG LED leads: MLC-RW RGB outputs  speaker LED (R/G/B/common)
   - **Channel 6 (Rear Right Roll Bar):** XM-WHTMFC cable to speaker
     - 16 AWG speaker leads: Amplifier Ch6  speaker audio
     - 20 AWG LED leads: MLC-RW RGB outputs  speaker LED (R/G/B/common)
   - **Channels 1+2 (Bridged Subwoofer):** Standard 12-14 AWG speaker wire (no LED)

**Circuit Protection:**

- **Fuse:** 40A fast-acting fuse (per Fusion Apollo manual specifications)
  - Amplifier includes inline fuse holder with 40A fuse
  - **Recommendation:** Replace inline fuse with centrally-located Blue Sea circuit breaker
- **Recommended:** Blue Sea 40A breaker at CONSTANT bus or AUX battery location
  - Easier reset than inline fuse (no need to access amplifier)
  - Mount breaker at CONSTANT bus or AUX battery for easy access
  - Protects full power wire run from battery to amplifier
  - Blue Sea 7178 (40A) or 7184 (50A) thermal circuit breaker recommended

**Mounting Location Options:**

1. **Behind Dashboard:** Near radio head unit
   - Shortest RCA cable runs from MS-RA670 to amplifier
   - Central location for speaker wire routing to dash and roll bar
   - MLC-RW LED controller can mount next to amplifier in same location
   - Adequate ventilation behind dash for Class-D amplifier (low heat)
2. **Cargo Area:** Behind rear seat or on sidewall
   - Easy access to speakers and subwoofer
   - Requires longer power cables from AUX battery
   - Longer RCA cable runs from radio
3. **Under Rear Seat:** Hidden installation
   - Shorter power cables to AUX battery
   - Good heat dissipation with air circulation
   - Moderate RCA cable lengths

**Outstanding Items:**

- [ ] Determine Fusion Apollo 6-channel amplifier mounting location (behind dash preferred, cargo area or under rear seat optional)
- [ ] Verify amplifier current draw at operating power (music listening vs full test tone)
- [ ] Select Blue Sea circuit breaker: 40A (7178) for amplifier power protection
- [ ] Plan Blue Sea breaker mounting location at CONSTANT bus or AUX battery for easy access
- [ ] Remove amplifier's included 40A inline fuse and replace with centrally-located Blue Sea breaker
- [ ] Confirm 6 AWG wire gauge is sufficient for power run from CONSTANT bus to amplifier
- [ ] Determine amplifier ground connection point (chassis ground or direct to AUX battery negative)
- [ ] Verify ground wire length is <18 inches for best performance
- [ ] Plan RCA cable routing from MS-RA670 to amplifier (shortest run if behind dash)
- [ ] Determine speaker wire routing from amplifier to front dash and rear roll bar
- [ ] Calculate exact XM-WHTMFC cable lengths needed for each speaker location
- [ ] Determine subwoofer mounting orientation in cargo area wall (front-firing or downward-firing)
- [ ] Verify Jeep LJ cargo area provides minimum 3 cu. ft. air space behind infinite baffle mount
- [ ] Determine exact dash mounting locations for M6-650X-S-GmTi-i speakers (dash end caps or custom location)
- [ ] Add BODY PDU circuit for MLC-RW LED controller (30A CONSTANT power)
- [ ] Determine exact MLC-RW rotary encoder dash mounting location (near radio or center console)
- [ ] Plan LED power cable routing from MLC-RW to all 5 speakers (4x tower/dash + 1x subwoofer)
- [ ] Confirm XM-WHTMFC cable includes appropriate connectors for MLC-RW RGB output
- [ ] Plan rotary encoder extension cable routing from MLC-RW unit to dash location
