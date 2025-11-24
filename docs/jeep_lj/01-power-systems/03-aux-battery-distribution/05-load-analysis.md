---
hide:
  - toc
---

# 1.3.5 AUX Battery Load Analysis {#aux-battery-load-analysis}

Scenario-based load analysis for AUX battery circuits (BCDC-charged at 50A max).

## AUX Battery Circuit Summary

All circuits powered by AUX battery (charged by BCDC at 50A max):

| Source | Circuit | Typical | Peak | Duty Cycle | Notes |
|:-------|:--------|--------:|-----:|:-----------|:------|
| **SwitchPros Outputs** | | | | | |
| OUTPUT-1 | Roof Center (6x BD XL) | 0A | 31A | Night offroad | Combo pattern |
| OUTPUT-2 | Ditch Lights (2x LP6) | 0A | 12A | Night offroad | Driving pattern |
| OUTPUT-3 | Fog Lights (3x Squadron) | 0A | 9A | Night/weather | Amber SAE |
| OUTPUT-4 | Dome Lights (4x Cyclone) | 0A | 4A | Doors open | Manual + trigger |
| OUTPUT-5 | Roof Outer Spots (2x XL) | 0A | 12A | Night offroad | Spot pattern |
| OUTPUT-6 | Rock Lights (6x Cyclone) | 0A | 3A | Night offroad | Under vehicle |
| OUTPUT-7 | Rear Chase (OnX6 Arc) | 0A | 6A | Night offroad | Amber wide |
| OUTPUT-8 | Available | 0A | 0A | — | Footwell lights on MLC-RW |
| OUTPUT-10 | Rear Locker | 0A | 2A | Technical terrain | Solenoid |
| OUTPUT-11 | Compressor Control | 0A | 15A | Control signal | To ARB |
| OUTPUT-12 | Rear Lights (2x S1 Pro) | 0A | 5A | Night driving | License plate |
| OUTPUT-13 | Cargo Light | 0A | 5A | Loading/unloading | Trigger-2 |
| OUTPUT-17 | Front Locker | 0A | 2A | Technical terrain | Low-side |
| **SafetyHub 150** | | | | | |
| MIDI-1 | ARB Compressor Motor 1 | 0A | 45A | Airing up | Half of twin |
| MIDI-2 | ARB Compressor Motor 2 | 0A | 45A | Airing up | Half of twin |
| ATC-1 | Winch Trigger | 0A | 10A | Recovery only | Contactor coil |
| **BODY PDU** | | | | | |
| CB30 | Fusion Radio (memory) | 1A | 1A | Continuous | Clock/presets |
| CB44 | Fusion Radio (amp) | 0A | 15A | Audio playing | Ignition-triggered |
| CB48 | USB Charging (2x 75W) | 2A | 13A | Devices charging | Always on |
| CB39 | WolfBox Camera | 2A | 10A | Continuous | Dash + backup |
| CB45 | Driver Heated Seat | 0A | 5A | Winter | Relay K21 |
| CB42 | Passenger Heated Seat | 0A | 5A | Winter | Relay K22 |
| CB43 | Winch Control (dash) | 0A | 2A | Recovery only | Rocker signal |
| **Direct** | | | | | |
| - | Winch Motor | 0A | 400A | 10-30 sec bursts | Recovery only |

## Charging Source

**BCDC Alpha 50:** Charges AUX battery at up to 50A from START battery/alternator

- **Solar input:** Up to 6.7A additional (80W panel)
- **Combined max:** ~57A charging rate (sunny day, engine running)
- **Typical charging:** 30-50A depending on AUX battery SOC

**AUX Battery Capacity:** 68Ah (Odyssey PC1500)

- **Safe discharge depth:** 50% for AGM = 34Ah usable
- **Recovery rate:** At 50A charging, recovers 34Ah in ~41 minutes

## Scenario Analysis

### Scenario 1: Daily Driving (Minimal Draw)

**Conditions:** Daytime driving, no offroad lights, radio off, no accessories

| Circuit | Load | Reason |
|:--------|-----:|:-------|
| **Fusion Radio memory (CB30)** | **1A** | Clock/presets |
| **USB Charging (CB48)** | **2A** | Phone charging |
| **WolfBox Camera (CB39)** | **2A** | Always recording |
| **TOTAL** | **5A** | |

**BCDC Charging:** 30-50A typical

**Net Battery Effect:** +25 to +45A (battery charging) ✅

**Battery SOC Trend:** Rising - battery maintains full charge quickly

---

### Scenario 2: Night Highway Driving

**Conditions:** Night driving, fog lights on, music playing, heated seats (winter)

| Circuit | Load | Reason |
|:--------|-----:|:-------|
| **Fog Lights (OUTPUT-3)** | **9A** | Visibility |
| **Rear Lights (OUTPUT-12)** | **5A** | License plate area |
| **Fusion Radio memory (CB30)** | **1A** | Always on |
| **Fusion Radio amp (CB44)** | **10A** | Music moderate |
| **USB Charging (CB48)** | **5A** | Devices |
| **WolfBox Camera (CB39)** | **2A** | Always recording |
| **Driver Heated Seat (CB45)** | **3A** | Cycling |
| **Passenger Heated Seat (CB42)** | **3A** | Cycling |
| **TOTAL** | **38A** | |

**BCDC Charging:** 50A (full rate)

**Net Battery Effect:** +12A (battery charging!) ✅

**Battery SOC Trend:** Rising - battery maintains full charge even with high accessory use

**Assessment:** Excellent - 50A BCDC fully covers all night highway loads with margin to spare

---

### Scenario 3: Night Offroad (Full Lighting)

**Conditions:** Technical trail at night, all forward lighting, rock lights, lockers engaged

| Circuit | Load | Reason |
|:--------|-----:|:-------|
| **Roof Center (OUTPUT-1)** | **31A** | Primary forward |
| **Ditch Lights (OUTPUT-2)** | **12A** | Peripheral |
| **Fog Lights (OUTPUT-3)** | **9A** | Close range |
| **Rock Lights (OUTPUT-6)** | **3A** | Obstacle spotting |
| **Rear Chase (OUTPUT-7)** | **6A** | Following vehicles |
| **Front Locker (OUTPUT-17)** | **2A** | Engaged |
| **Rear Locker (OUTPUT-10)** | **2A** | Engaged |
| **Fusion Radio memory (CB30)** | **1A** | Always on |
| **USB Charging (CB48)** | **2A** | Phone |
| **WolfBox Camera (CB39)** | **2A** | Recording |
| **TOTAL** | **70A** | |

**BCDC Charging:** 50A (full rate)

**Net Battery Effect:** -20A (slow discharge)

**Time to 50% SOC:** 34Ah / 20A = **102 minutes** to reach 50% SOC

**Assessment:** ✅ Excellent - 50A BCDC cuts discharge rate by more than half vs 25A. Extended night wheeling now practical without significant battery concerns.

---

### Scenario 4: Airing Up Tires (ARB Compressor)

**Conditions:** Parked after trail, engine idling, airing up 4 tires (5-10 minutes)

| Circuit | Load | Reason |
|:--------|-----:|:-------|
| **ARB Compressor Motor 1 (MIDI-1)** | **45A** | Running |
| **ARB Compressor Motor 2 (MIDI-2)** | **45A** | Running |
| **Compressor Control (OUTPUT-11)** | **15A** | Control signal |
| **Fusion Radio memory (CB30)** | **1A** | Always on |
| **USB Charging (CB48)** | **2A** | Phone |
| **WolfBox Camera (CB39)** | **2A** | Recording |
| **TOTAL** | **110A** | |

**BCDC Charging:** 50A (full rate)

**Net Battery Effect:** -60A (moderate discharge)

**5-minute air-up:** 60A × (5/60)h = **5Ah used** (7% of battery)

**10-minute air-up:** 60A × (10/60)h = **10Ah used** (15% of battery)

**Assessment:** ✅ Excellent - 50A BCDC reduces battery impact by 30%. Battery recovers in 10-20 minutes of driving.

---

### Scenario 5: Extended Airing Up (30+ minutes)

**Conditions:** Airing up 5 tires + air tank refill, extended compressor operation

| Circuit | Load | Reason |
|:--------|-----:|:-------|
| **ARB Compressor Motor 1 (MIDI-1)** | **45A** | Running |
| **ARB Compressor Motor 2 (MIDI-2)** | **45A** | Running |
| **Compressor Control (OUTPUT-11)** | **15A** | Control signal |
| **Fusion Radio memory (CB30)** | **1A** | Always on |
| **USB Charging (CB48)** | **2A** | Phone |
| **WolfBox Camera (CB39)** | **2A** | Recording |
| **TOTAL** | **110A** | |

**BCDC Charging:** 50A (full rate)

**Net Battery Effect:** -60A (moderate discharge)

**30-minute operation:** 60A × 0.5h = **30Ah used** (44% of battery)

**Assessment:** ✅ Now practical with 50A BCDC. For extended air-up:

- Battery stays above 50% SOC for 30+ minutes of continuous compressor operation
- Increase engine RPM to 1500+ for optimal charging
- Monitor AUX battery voltage (Dakota Digital gauge)
- Still wise to take breaks for very extended sessions (>45 min)

---

### Scenario 6: Winch Recovery (Brief High-Current)

**Conditions:** Vehicle recovery, 30-second winch pull at moderate load

| Circuit | Load | Reason |
|:--------|-----:|:-------|
| **Winch Motor** | **250A** | Moderate pull |
| **Winch Trigger (ATC-1)** | **10A** | Contactor coil |
| **Winch Control (CB43)** | **2A** | Dash rocker |
| **Fusion Radio memory (CB30)** | **1A** | Always on |
| **WolfBox Camera (CB39)** | **2A** | Recording |
| **TOTAL** | **265A** | |

**BCDC Charging:** 50A (full rate)

**Net Battery Effect:** -215A (heavy discharge)

**30-second pull:** 215A × (30/3600)h = **1.8Ah used** (3% of battery)

**Assessment:** ✅ Brief winch operations have minimal battery impact. 50A BCDC provides faster recovery between pulls.

---

### Scenario 7: Camp Mode (Engine Off)

**Conditions:** Parked at camp, engine off, minimal lighting, music

| Circuit | Load | Reason |
|:--------|-----:|:-------|
| **Dome Lights (OUTPUT-4)** | **4A** | Camp lighting |
| **Rock Lights (OUTPUT-6)** | **3A** | Ground lighting |
| **Footwell Lights (MLC-RW)** | **1A** | Ambiance |
| **Fusion Radio memory (CB30)** | **1A** | Always on |
| **Fusion Radio amp (CB44)** | **8A** | Music |
| **USB Charging (CB48)** | **10A** | Multiple devices |
| **TOTAL** | **27A** | |

**BCDC Charging:** 0A (engine off)

**Solar (daytime):** ~5-6A (80W panel)

**Net Battery Effect (day):** -21A

**Net Battery Effect (night):** -27A

**Time to 50% SOC (no solar):** 34Ah / 27A = **76 minutes**

**Assessment:** ⚠️ Limited camp time on battery alone. For extended camping:

- Minimize lighting to essentials
- Idle engine periodically to recharge
- Use solar during daytime
- Consider portable generator for multi-day camping

---

## Summary

| Scenario | Total Draw | BCDC | Net Effect | Duration Limit | Status |
|:---------|:-----------|:-----|:-----------|:---------------|:-------|
| Daily Driving | 5A | 50A | +45A | Unlimited | ✅ Fast charging |
| Night Highway | 38A | 50A | +12A | Unlimited | ✅ Charging! |
| Night Offroad | 70A | 50A | -20A | 102 minutes | ✅ Excellent |
| Air Up (5-10 min) | 110A | 50A | -60A | 10 minutes | ✅ Excellent |
| Air Up Extended | 110A | 50A | -60A | 34 minutes | ✅ Practical |
| Winch Recovery | 265A | 50A | -215A | 30-sec pulls | ✅ Brief OK |
| Camp Mode | 32A | 0A | -32A | 64 minutes | ⚠️ Limited |

**Key Insight:** The 50A BCDC upgrade transforms AUX battery capability. Night highway driving now charges the battery. Night offroad runtime more than doubles (45→102 min). Extended air-up is now practical without battery concerns. Only engine-off camp mode remains limited by battery capacity.

## AGM vs Lithium Comparison

For future reference if upgrading to LiFePO4:

| Factor | AGM (Current) | LiFePO4 |
|:-------|:--------------|:--------|
| Capacity | 68Ah | 100Ah typical |
| Safe DOD | 50% (34Ah usable) | 80% (80Ah usable) |
| Night Offroad Time | 45 min to 50% | 107 min to 20% |
| Extended Air-Up | 24 min to 50% | 56 min to 20% |
| Camp Time | 64 min to 50% | 150 min to 20% |
| Low SOC Damage | Sulfation risk | Minimal |
| Charge Acceptance | Tapers at high SOC | Near-full rate |

**Lithium Benefit:** 2-3× more usable capacity, no sulfation concern from occasional deep discharge.

## Related Documentation

- [BCDC Alpha 50][bcdc] - DC-DC charger specifications
- [SafetyHub 150][safetyhub] - ARB compressor fusing
- [SwitchPros SP-1200][switchpros] - Lighting control outputs
- [BODY PDU][body-pdu] - Cabin circuit details
- [START Battery Load Analysis][start-load-analysis] - Companion analysis for START battery
- [PMU ARB Load Shedding][arb-load-shedding] - Load management during ARB operation

[bcdc]: ../01-power-generation/03-bcdc.md
[safetyhub]: 04-safetyhub.md
[switchpros]: ../../05-control-interfaces/02-switchpros-sp1200.md
[body-pdu]: 03-body-pdu.md
[start-load-analysis]: ../02-starter-battery-distribution/02-load-analysis.md
[arb-load-shedding]: ../04-pmu/05-pmu-arb-load-shedding.md
