# 1.1 Power Generation & Storage {#11-power-generation-storage}
### Battery System

- **Configuration:** Dual battery (front/rear split)
- **Primary Battery (Front - Engine Bay):**
  - Model: Odyssey ODX-34/78-AGM
  - Type: AGM (Absorbed Glass Mat)
  - CCA: 850A @ 0°F (-18°C)
  - CA: 1050A @ 32°F (0°C)
  - Amp-Hour Capacity: 68 Ah @ 20-hour rate
  - Reserve Capacity: 135 minutes @ 25A
  - Weight: 51 lbs
  - Dimensions: 10.86" L × 6.84" W × 7.78" H
  - Cycle Life: 400 cycles @ 80% DOD
  - Loads Powered: Starter, PMU (all critical/SWITCHED circuits), Front-mounted winch
- **Auxiliary Battery (Rear - Passenger Wheel Well):**
  - Model: Odyssey ODX-34/78-AGM (same as front)
  - Mounting: Enclosed compartment with access panel behind passenger seat
  - Loads Powered: SwitchPros, SafetyHub, Body RTMR (all convenience/CONSTANT circuits)
  - Charged by: RedArc BCDC Alpha 50
- **Total System Capacity:** 136 Ah combined (68 Ah × 2), 1700 CCA combined
- **Battery Isolator/Manager:** RedArc BCDC Alpha 50 (BCDC1250A)
  - 50A DC-DC charging output
  - Mounted near rear battery in wheel well compartment
  - Primary Input: 9-32V DC (from front battery/alternator)
  - Solar Input: Cascadia 4x4 80W hood solar panel
  - Multi-stage smart charging (AGM compatible)
  - Automatic battery isolation
  - Built-in jump start assist mode for emergency starting
  - Green Power Priority (solar prioritized when available)
  - Dimensions: 220mm L × 155mm W × 65mm H
  - Ignition signal required: Body RTMR F12 provides BCDC trigger signal

**System Design:**

- Front battery: Critical loads (starter, ECM, fuel pump, engine systems)
- Rear battery: Convenience loads (lights, radios, compressor, heated seats)
- BCDC Alpha 50 jump start assist: Parallels batteries if front battery fails
- Redundancy: Vehicle operates on front battery alone if rear system fails

### Solar Charging System

- **Solar Panel:** Cascadia 4x4 80W Hood Solar Panel
  - **Model:** Cascadia 4x4 80W Flexible Solar Panel
  - **Mounting:** Permanently adhered to hood surface
  - **Output:** 80W maximum (nominal)
  - **Type:** Monocrystalline flexible solar panel
  - **Connection:** Wired to BCDC Alpha 50 solar input
  - **Benefits:**
    - Maintains rear battery charge during stationary periods
    - Green Power Priority: BCDC prioritizes solar charging when available
    - Reduces alternator load during daylight operation
    - Enables extended off-grid camping without engine running
  - **Wiring:**
    - Solar panel positive (+) → BCDC Alpha 50 solar input (+)
    - Solar panel negative (-) → Chassis ground (vehicle ground)
    - Wire gauge: Per Cascadia 4x4 specifications (typically 10-12 AWG for 80W)
    - Route through hood to firewall, then to BCDC location in wheel well
    - Solar negative shares common ground with vehicle chassis

**Solar Charging:** 80W max input to BCDC (6.7A @ 12V), maintains rear battery when parked, supplements alternator when driving

### Alternator

- **Rating:** 200A (TBD - specific part number)
- **Output to Battery Positive:** 2/0 AWG cable (red)
- **Alternator Case Ground:** Factory grounded via mounting bolts to engine block

### Grounding Architecture

**High-Current Grounds (2/0 AWG to Frame Rails):**

All primary grounds use 2/0 AWG cable to frame rails for maximum current capacity and minimal voltage drop:

- **Front Battery Negative → Front Frame Rail:** 2/0 AWG cable (black)
  - Engine bay frame rail (driver or passenger side)
  - Provides ground return path for starter motor and high-current engine loads
- **Rear Battery Negative → Rear Frame Rail:** 2/0 AWG cable (black)
  - Rear frame rail near passenger wheel well (rear battery location)
  - Provides ground return path for all CONSTANT bus loads
- **Front to Rear Ground Reference:** 2/0 AWG cable
  - Front battery negative → Rear battery negative
  - Prevents voltage differential between batteries
  - Critical for BCDC operation and system stability
- **Engine Block → Front Frame Rail:** 2/0 AWG cable (black)
  - Engine block ground point to front frame rail or firewall frame mount point
  - Ensures solid ground return path for engine/starter and alternator charging current
  - Handles combined current from starter motor and 200A alternator return path
- **Alternator Case → Engine Block:** Factory ground connection
  - Alternator case bolts directly to engine block (already grounded via mounting)
  - Engine block provides ground return path via 2/0 AWG cable to frame rail
  - No separate alternator ground cable required
- **SwitchPros → Front Battery Negative:** 4 AWG cable (black)
  - SwitchPros power module mounted in engine bay
  - Direct connection to front battery negative terminal
  - 4 AWG sufficient for 150A total capacity at short distance
  - Per SwitchPros manufacturer specification (direct battery ground required)

**Low-Current Grounds (Firewall Ground Stud):**

All low-current body electronics and dash components ground to firewall ground stud:

- Body RTMR (all circuits)
- Dakota Digital instrument cluster and BIM modules
- Audio components (radio head unit, amplifier - see notes)
- WolfBox camera/mirror
- Other dash-mounted electronics

**PMU-Specific Grounds:**

- **PMU:** Front battery negative bus (2/0 AWG connection)
  - PMU mounted on firewall (engine bay side)
  - Direct connection to front battery negative bus for solid ground return
  - Handles all SWITCHED bus circuits (engine systems, critical loads)

**Special Ground Notes:**

- **BCDC Alpha 50:** Direct to rear battery negative (per manufacturer spec)
- **Fusion Apollo Amplifier:** Can use either:
  - Chassis ground near mounting location (if <18" wire run), or
  - Direct to rear battery negative (preferred for best audio performance)
- **Rugged Radio G1/STX:** Direct to front battery negative (per manufacturer spec, minimizes RF noise)

### System Load Summary

- Continuous load: TBD
- Peak load: TBD (SwitchPros 150A + engine systems 40-60A)
- Verify 200A alternator capacity sufficient

**Outstanding:**

- [ ] Determine alternator part number (200A)
- [ ] Calculate system loads (continuous, peak, worst-case) and verify 200A alternator sufficient
- [ ] Determine BCDC Alpha 50 mounting location in rear wheel well (near battery, water-protected, accessible)
- [ ] Determine SwitchPros power module mounting location in engine bay

**Installation Checklist:**

When installing the power generation system, verify the following:

- **Alternator:**
  - [ ] Route 2/0 AWG positive cable from alternator to front battery (shortest path)
  - [ ] Protect and secure alternator positive cable with appropriate clamps
  - [ ] Verify alternator mounting surfaces are clean (no paint/powder coat between alternator and engine block)
  - [ ] Confirm alternator case ground connection via mounting bolts

- **Front Battery Grounding:**
  - [ ] Identify front frame rail ground point in engine bay (driver or passenger side)
  - [ ] Clean frame rail mounting point to bare metal (remove paint/powder coat)
  - [ ] Install 2/0 AWG cable from front battery negative to front frame rail
  - [ ] Verify tight, corrosion-free connection with proper ring terminals

- **Rear Battery Grounding:**
  - [ ] Identify rear frame rail ground point inside wheel well
  - [ ] Clean frame rail mounting point to bare metal (remove paint/powder coat)
  - [ ] Install 2/0 AWG cable from rear battery negative to rear frame rail
  - [ ] Verify tight, corrosion-free connection with proper ring terminals

- **Battery Ground Reference:**
  - [ ] Route 2/0 AWG ground reference cable from front battery negative to rear battery negative
  - [ ] Identify routing path through frame or body channels
  - [ ] Measure and order appropriate cable length
  - [ ] Install and secure cable with proper protection

- **Engine Block Grounding:**
  - [ ] Locate factory engine ground point on R2.8 engine block
  - [ ] Route 2/0 AWG cable from engine block to front frame rail (shortest path)
  - [ ] Clean both connection points to bare metal
  - [ ] Install and torque ring terminals per specifications
  - [ ] Note: This cable handles combined starter and alternator return current (200A+)

- **Firewall Ground Stud:**
  - [ ] Locate existing factory ground stud or install new ground stud on firewall
  - [ ] Clean mounting area to bare metal (remove paint)
  - [ ] Verify all low-current body electronics ground to this stud

- **SwitchPros Grounding:**
  - [ ] Route 4 AWG ground wire from SwitchPros power module to front battery negative
  - [ ] Verify direct connection to battery negative terminal per manufacturer spec
  - [ ] Ensure wire run is <10 feet

- **Solar Panel Integration:**
  - [ ] Verify Cascadia 4x4 80W solar panel is properly adhered to hood surface
  - [ ] Route solar panel wiring from hood through firewall to BCDC location
  - [ ] Connect solar positive (+) to BCDC Alpha 50 solar input positive terminal
  - [ ] Connect solar negative (-) to chassis ground (vehicle ground, not to BCDC)
  - [ ] Verify solar panel polarity is correct (reverse polarity can damage BCDC)
  - [ ] Secure solar wiring with appropriate protection from heat and chafing
  - [ ] Ensure solar negative ground connection is clean metal-to-metal
  - [ ] Verify BCDC Green Power Priority is enabled (solar prioritized when available)
  - [ ] Test solar charging by monitoring BCDC status LED in daylight
