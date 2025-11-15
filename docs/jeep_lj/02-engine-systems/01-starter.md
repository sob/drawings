# Starter System - Cummins R2.8 {#starter-system-cummins-r28}
**Type:** Two-stage starter system with control relay
**Main Power Source:** Front Battery+ (direct connection)
**Control Signal:** PMU Out 11 (PMU-controlled) OR Ignition switch "START" position via clutch safety switch (direct control)

## System Overview

Two-stage design: low-current ignition switch (~1A) controls starter control relay, which provides high current (30-75A) to main starter solenoid.

**Why Two Stages:**
- Ignition switch limited to ~10-20A
- Main solenoid requires 30-75A
- Voltage drop over long wire runs
- Control relay provides high current close to starter

## System Components

### 1. Main Starter Motor & Solenoid

**Location:** Engine bay, mounted on engine block
**Type:** High-torque diesel starter with integrated solenoid

**Terminals:**
- **Battery Post (large terminal):**
  - Direct connection from Front Battery+ via large cable (2 AWG or larger)
  - Provides main cranking power (400-600A during cranking)
  - Also provides power tap for starter control relay
- **Switch Post (small terminal):**
  - Triggered by starter control relay output (30-75A)
  - Engages main solenoid to connect battery power to starter motor
- **Ground:** Via starter motor mounting to engine block

### 2. Starter Control Relay

**Location:** Engine bay, near front battery
**Type:** High-current automotive relay (30-75A continuous rating)
**Mounting:** TBD - determine mounting location near battery

**Note:** Similar architecture to SWITCHED bus relay in [Front Battery Distribution][zone-1-front-battery-tray--primary-distribution-engine-bay].

**Terminals:**
- **Power (85/86 or 30):** Tapped from main starter solenoid battery post
- **Trigger (85/86):** PMU Out 11 (~1A signal) OR Ignition switch "START" → clutch safety switch (~1A signal)
- **Output (87):** High current (30-75A) to main starter solenoid switch post
- **Ground (85/86):** Chassis ground

**Design Options:**
- **Standard Automotive Relay:** 30-40A continuous
- **Heavy-Duty Relay:** 50-75A continuous
- **Blue Sea ML-Series:** 30-75A model if available

### 3. Clutch Safety Switch

**Type:** Factory TJ clutch safety switch (normally open)
**Location:** Clutch pedal bracket
**Function:** Prevents starter engagement unless clutch is fully depressed

**Wiring:**
- Input: Ignition switch "START" output (through firewall Grommet 2)
- Output: Starter control relay trigger circuit
- Must be wired in series - starter will not engage unless both ignition switch AND clutch switch are closed

**Firewall Penetration:** See [Firewall Ingress][firewall-penetrations-ingress-points]

## Control Methods

### Method 1: PMU24 Control (Recommended)

**Configuration:**
- PMU Out 11 powers starter control relay coil
- PMU In 4: Clutch safety switch signal
- PMU In 5: Ignition switch START signal
- PMU logic: Only activate Out 11 when BOTH In 4 AND In 5 are active

**Programming Logic:**
```
IF (In5_IgnitionSTART == ON) AND (In4_ClutchSwitch == CLOSED)
  THEN Out11_StarterRelay = ON
ELSE
  Out11_StarterRelay = OFF
END
```

See [Engine Systems - Starter Safety Logic][144-pmu-programming] for complete PMU programming details.

### Method 2: Direct Ignition Switch Control (Traditional)

**Configuration:**
- Ignition switch START output → Clutch safety switch → Starter control relay coil
- Clutch safety switch wired in series (relay only activates when clutch depressed)
- Direct wiring from cabin to engine bay (through Grommet 2)

**Note:** PMU method provides superior safety, diagnostics, and data logging.

## Wiring Configuration

### Power Flow Diagram (PMU Method)

```
Front Battery+ (12V)
    ├─→ Main Starter Solenoid Battery Post (2 AWG or larger)
    │       ├─→ Starter Motor (via solenoid contacts when engaged)
    │       └─→ Starter Control Relay Power (tap from battery post)
    │
    ├─→ Ignition Switch "START" Position → PMU In 5 (START signal)
    │
    └─→ Clutch Safety Switch → PMU In 4 (clutch depressed signal)
            ↓
        PMU Logic (In 5 AND In 4 must both be active)
            ↓
        PMU Out 11 Activates (~1A)
            ↓
        Starter Control Relay Coil Energized
            ↓
        Relay Closes
            ↓
        Relay Output (30-75A) → Main Starter Solenoid Switch Post
            ↓
        Main Solenoid Engages
            ↓
        Battery Power → Starter Motor
            ↓
        Engine Cranks
```

### Detailed Wiring Path (PMU Method)

1. **Main Power:**
   - Front Battery+ → Main starter solenoid battery post (2 AWG or larger)
   - Main solenoid battery post → Starter control relay power terminal

2. **Control Signals (to PMU):**
   - Ignition switch "START" output → Through firewall (Grommet 2) → PMU In 5
   - Clutch safety switch → PMU In 4
   - PMU monitors both inputs and applies programmed logic

3. **PMU Output to Relay:**
   - PMU Out 11 → Starter control relay coil (~1A)
   - Relay coil → Chassis ground
   - PMU only activates Out 11 when BOTH In 4 AND In 5 are active

4. **Relay Output:**
   - Starter control relay output (87) → Main starter solenoid switch post
   - When relay closes: 30-75A flows to solenoid switch post
   - Main solenoid engages, connecting battery power to starter motor

5. **Ground Path:**
   - Starter motor case → Engine block → Front battery negative (2/0 AWG)

## Wire Specifications

| Connection | Wire Gauge | Current | Notes |
|:-----------|:-----------|:--------|:------|
| Battery+ to Main Solenoid Battery Post | 2 AWG or larger | 400-600A cranking | Per Cummins specifications |
| Main Solenoid Battery Post to Relay Power | 10 AWG | 30-75A | Tap from battery post |
| Ignition Switch START to PMU In 5 | 16-18 AWG | ~1A | Through Grommet 2 (PMU method) |
| Clutch Switch to PMU In 4 | 16-18 AWG | ~1A | Low current signal (PMU method) |
| PMU Out 11 to Relay Coil | 16-18 AWG | ~1A | Low current trigger (PMU method) |
| Relay Output to Main Solenoid Switch Post | 10 AWG | 30-75A | High current relay output |
| Starter Ground via Engine Block | Per mounting | 400-600A | Bonded via starter mounting bolts |

## Installation Checklist (PMU Method)

- [ ] Mount starter control relay in engine bay near front battery
- [ ] Run main power cable from Front Battery+ to main starter solenoid battery post (2 AWG or larger)
- [ ] Tap power for starter control relay from main solenoid battery post (10 AWG)
- [ ] Run ignition switch "START" wire through firewall (Grommet 2) to PMU In 5
- [ ] Wire clutch safety switch to PMU In 4
- [ ] Run PMU Out 11 wire to starter control relay coil (16-18 AWG)
- [ ] Run relay output wire to main starter solenoid switch post (10 AWG)
- [ ] Connect relay coil ground to chassis ground
- [ ] Verify engine block to front battery negative ground connection (2/0 AWG)
- [ ] Program PMU Out 11 with starter safety logic (In 4 AND In 5 must both be active)
- [ ] Test PMU logic prevents starter engagement when clutch is released
- [ ] Test PMU logic prevents starter engagement when ignition not in START position
- [ ] Test starter engages properly when clutch is depressed AND ignition in START position
- [ ] Verify no voltage drop during cranking (starter should crank strongly)
- [ ] Verify PMU24 logs starter activation events correctly

## Outstanding Items

- [ ] Confirm starter control relay part number and specifications (30-75A continuous rating)
- [ ] Determine exact relay mounting location (engine bay, near front battery)
- [ ] Verify main power cable gauge from Cummins specifications (2 AWG minimum, may require larger)
- [ ] Confirm wire gauge for relay power tap from main solenoid battery post
- [ ] Confirm wire gauge for relay output to main solenoid switch post
- [ ] Determine exact routing for ignition "START" wire through firewall (Grommet 2)

## Troubleshooting

### Starter Does Not Engage

**Checks:**
1. Verify 12V at clutch safety switch when ignition in START position
2. Verify 12V at starter control relay coil when clutch depressed and ignition in START
3. Verify relay clicks/closes when triggered
4. Measure voltage at main solenoid switch post when relay engaged (~11-12V)
5. Check continuity of ground from starter case to battery negative

### Starter Cranks Slowly

**Checks:**
1. Measure battery voltage under load (should not drop below 9.5V during cranking)
2. Measure voltage drop across main power cable during cranking (<0.5V)
3. Measure voltage drop across ground path during cranking (<0.5V)
4. Load test battery to verify capacity

## Related Documentation

- [Engine Systems][pmu-power-distribution] - PMU Out 11 configuration and starter safety logic programming
- [Front Battery Distribution][zone-1-front-battery-tray--primary-distribution-engine-bay] - Main power source and distribution
- [Firewall Ingress][firewall-penetrations-ingress-points] - Ignition switch "START" wire routing (Grommet 2)
