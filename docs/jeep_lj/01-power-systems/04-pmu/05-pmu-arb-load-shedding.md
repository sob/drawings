---
hide:
  - toc
---

# 1.4.5 PMU ARB Load Shedding Logic {#pmu-arb-load-shedding}

Automatic load management during ARB compressor operation to prevent exceeding alternator capacity.

## Purpose

Manage alternator capacity when ARB twin compressor runs (90A load). Automatically sheds non-critical loads to prevent exceeding 270A alternator capacity during tire inflation and air system use.

## Problem Statement

**Alternator Capacity Issue:**

ARB compressor (90A) + radiator fan (53A) + PMU typical loads (100A) + BCDC (18-25A) + cabin PDU (10A) = **271-278A total**, which exceeds 270A alternator capacity by 1-8A during extended tire inflation operations.

**Impact:**
- Battery supplements deficit during tire inflation
- Voltage drops below optimal charging range (14.2-14.4V → 13.5-13.8V)
- Repeated deep draws reduce battery lifespan
- System voltage may trigger low-voltage warnings

## Solution Overview

Detect ARB compressor activation and automatically disable non-critical loads to maintain system voltage above 13.0V and stay within alternator capacity.

**Load Shedding Strategy:**
- Shed cosmetic loads first (DRL)
- Shed comfort loads second (A/C)
- Conditionally shed cooling loads if temperatures allow (oil/PS cooler fans)
- Maintain critical systems (iBooster, HVAC blower, lights, CT4)

## Load Shedding Logic

```
// Monitor SwitchPros OUTPUT-11 state via shared CAN bus or hardwired trigger
IF (SwitchPros_OUT11_ARB == ON) OR (BatteryVoltage < 13.0V AND EngineRPM > 1000):

  // Shed non-critical loads (priority order: lowest to highest impact)
  Out14_DRL = OFF              // -8A: Daytime running lights (cosmetic)
  Out17_AC_Clutch = OFF        // -5A: Air conditioning (comfort)

  // Conditionally shed cooler fans if temperatures allow
  IF (J1939_SPN175_OilTemp < 220°F):
    Out7_OilFan = OFF          // -15A: Oil cooler fan (temp-dependent)

  IF (J1939_SPN110_CoolantTemp < 210°F):
    Out8_PSFan = OFF           // -15A: PS cooler fan (temp-dependent)

  // Total load reduction: 28-43A depending on temperatures

  // Optional: Trigger dashboard indicator
  Out_ARB_Active_Indicator = ON  // Visual feedback to driver

ELSE:
  // Restore normal operation when ARB stops
  Out14_DRL = (Per DRL auto-off logic)
  Out17_AC_Clutch = (Per A/C request logic)
  Out7_OilFan = (Per oil temp thresholds)
  Out8_PSFan = (Per coolant temp thresholds)
  Out_ARB_Active_Indicator = OFF
```

## Load Reduction Analysis

| Load Shed | Current Saved | Impact | When Disabled |
|:----------|:--------------|:-------|:--------------|
| DRL (OUT14) | 8A | Low - cosmetic only | Always when ARB runs |
| A/C Clutch (OUT17) | 5A | Medium - comfort loss | Always when ARB runs |
| Oil Cooler Fan (OUT7) | 15A | Low - if oil temp <220°F | Temperature-dependent |
| PS Cooler Fan (OUT8) | 15A | Low - if coolant temp <210°F | Temperature-dependent |
| **Total Saved** | **28-43A** | - | - |

## Before/After Comparison

### WITHOUT Load Shedding (Sunny Day)

```
PMU typical:        100A
ARB compressor:      90A
Radiator fan:        53A
BCDC (with solar):   18A  (solar contributes 6.7A, alternator 18.3A)
Cabin PDU:           10A
─────────────────────────
Total:              271A
Alternator:         270A
Deficit:             -1A  ❌
Battery Voltage:    ~13.5V (marginal)
```

### WITH Load Shedding (Minimum - 28A shed)

```
PMU reduced:         72A  (was 100A, shed DRL + A/C = 13A, plus fans idle = 15A)
ARB compressor:      90A
Radiator fan:        53A
BCDC (with solar):   18A
Cabin PDU:           10A
─────────────────────────
Total:              243A
Alternator:         270A
Margin:             +27A  ✅
Battery Voltage:    ~14.0V (good)
```

### WITH Load Shedding (Maximum - 43A shed)

**When oil and coolant temps allow both cooler fans to be disabled:**

```
PMU reduced:         57A  (was 100A, shed 43A total)
ARB compressor:      90A
Radiator fan:        53A
BCDC (with solar):   18A
Cabin PDU:           10A
─────────────────────────
Total:              228A
Alternator:         270A
Margin:             +42A  ✅ Excellent
Battery Voltage:    ~14.2V (excellent)
```

## Implementation Details

### Detection Methods (Priority Order)

**1. Hardwired Trigger (Preferred):**
- Wire from SwitchPros OUTPUT-11 to PMU digital input
- Direct, reliable detection
- Lowest latency

**2. CAN Bus Monitoring:**
- If SwitchPros broadcasts output states on CAN
- No additional wiring required
- Slight latency

**3. Voltage-Based Fallback:**
- `IF (BatteryVoltage < 13.0V) AND (EngineRPM > 1000)`
- Triggers on ANY high load (not just ARB)
- Universal protection regardless of cause

### Temperature Safety Checks

**Critical:** Always verify temperatures before disabling cooler fans.

```
// Oil Cooler Fan
IF (J1939_SPN175_OilTemp < 220°F):
  Safe to disable Out7_OilFan
ELSE:
  KEEP Out7_OilFan = ON (engine protection priority)

// PS Cooler Fan
IF (J1939_SPN110_CoolantTemp < 210°F):
  Safe to disable Out8_PSFan
ELSE:
  KEEP Out8_PSFan = ON (engine protection priority)
```

**Hysteresis:** Use 10°F hysteresis to prevent rapid cycling when temps hover near threshold.

### User Communication

**Dashboard Indicator Options:**

1. **Simple LED:** ARB button backlight changes color
2. **Message:** "ARB MODE - DRL/AC OFF"
3. **Dakota Digital Display:** Custom message via BIM module
4. **No indicator:** Silent operation (driver may not notice DRL/AC disabled)

**Recommended:** Backlight color change (green → amber when load shedding active)

## Operational Procedures (Supplemental)

**Best Practices for ARB Use:**

1. **Increase Engine RPM:** Run engine at 1500+ RPM during tire inflation
   - Alternator output increases with RPM
   - Better voltage regulation at higher speeds
   - Faster tire inflation

2. **Monitor Voltage:** Watch Dakota Digital voltage gauge during ARB use
   - Normal: 14.0-14.4V (load shedding working)
   - Marginal: 13.5-14.0V (acceptable, brief periods)
   - Low: <13.5V (increase RPM or reduce loads)

3. **Hot Weather:** Avoid prolonged ARB use at idle when ambient temp >95°F
   - Radiator fan + ARB + heat soak = high total load
   - Let engine cool between inflation cycles

4. **Avoid Simultaneous High Loads:**
   - ❌ ARB + winch (both 90A+ loads)
   - ❌ ARB + all accessories at idle
   - ✅ ARB + normal driving loads at 1500+ RPM

## Testing & Validation

### Initial Shakedown Testing

**Test 1: ARB Load Shedding Activation**

1. Start engine, let idle stabilize
2. Activate ARB (SwitchPros Button 11)
3. **Verify:**
   - DRL turns OFF
   - A/C compressor disengages (if running)
   - Dashboard indicator activates (if implemented)
   - Voltage stays >13.5V

**Test 2: Temperature-Based Fan Shedding**

1. Start engine cold (<180°F coolant)
2. Activate ARB
3. **Verify:**
   - Oil cooler fan OFF (temp below threshold)
   - PS cooler fan OFF (temp below threshold)
4. Run engine to operating temp (>220°F)
5. Activate ARB
6. **Verify:**
   - Cooler fans stay ON (engine protection priority)

**Test 3: Load Restoration**

1. Activate ARB
2. Verify loads shed
3. Deactivate ARB
4. **Verify:**
   - DRL returns to normal logic (on with ignition)
   - A/C returns if requested
   - Cooler fans return to temp-based control

### Data Logging

**Enable PMU Continuous Logging:**

```
LOG BatteryVoltage (1 Hz)
LOG TotalCurrent_PMU (1 Hz)
LOG EngineRPM (J1939_SPN190)
LOG Out14_DRL (state)
LOG Out17_AC_Clutch (state)
LOG Out7_OilFan (state)
LOG Out8_PSFan (state)
LOG SwitchPros_OUT11_ARB (state or trigger input)
```

**Analysis:**

1. Export logs after tire inflation sessions
2. Verify voltage stays >13.5V during ARB operation
3. Confirm load shedding activates/deactivates correctly
4. Identify any unexpected load combinations

### Long-Term Monitoring

**Track Over Time:**
- Battery voltage during ARB use (should be consistent)
- Frequency of load shedding activation
- Any low-voltage warnings or failures
- Battery state of charge recovery after ARB use

**Adjust if Needed:**
- Modify shed priority if testing shows different needs
- Add/remove loads from shed list
- Adjust temperature thresholds for cooler fans

## Related Documentation

**Power Systems:**
- [Alternator Specifications][alternator] - 270A capacity, load analysis
- [PMU Overview][pmu-overview] - PMU capacity and limitations
- [PMU Outputs][pmu-outputs] - Individual output assignments
- [PMU Programming][pmu-programming] - Other programming examples

**ARB Compressor:**
- [Air System][air-system] - ARB twin compressor specifications (90A total load)
- [SwitchPros][switchpros] - OUTPUT-11 control integration

**Analysis:**
- `/docs/ANALYSIS-2025-11-19-CURRENT.md` Section 1.1 - Detailed alternator capacity analysis

[alternator]: ../01-power-generation/02-alternator.md
[pmu-overview]: 01-pmu-overview.md
[pmu-outputs]: 03-pmu-outputs.md
[pmu-programming]: 04-pmu-programming.md
[air-system]: ../../07-exterior-systems/02-air-system.md
[switchpros]: ../../04-control-interfaces/02-switchpros-sp1200.md
