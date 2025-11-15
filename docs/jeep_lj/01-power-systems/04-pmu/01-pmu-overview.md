# 1.4.1 PMU Overview {#141-pmu-overview}
<!-- markdownlint-disable MD033 -->
<div class="image-gallery-float">
  <div class="image-gallery-container">
    <div class="image-gallery-grid">
      <figure class="image-gallery-figure">
        <img src="../../../images/ecumaster-pmu24.png" alt="ECUMaster PMU24 DL" loading="lazy" class="image-gallery-img" />
        <figcaption class="image-gallery-caption">ECUMaster PMU24 DL</figcaption>
      </figure>
      <figure class="image-gallery-figure">
        <img src="../../../images/ecumaster-pmu24-whats-in-box.jpg" alt="PMU24 Package Contents" loading="lazy" class="image-gallery-img" />
        <figcaption class="image-gallery-caption">What's in the box</figcaption>
      </figure>
    </div>
  </div>
</div>
<!-- markdownlint-enable MD033 -->

**Type:** Programmable Power Management Unit with Data Logging

**Model:** ECUMaster PMU24 DL

**Manufacturer:** ECUMaster

**Product Page:** [ECUMaster PMU24 DL](https://www.ecumaster.com/products/pmu24/)

**Installation Manual:** [PMU User Manual v101.1.5 (PDF)](https://www.ecumaster.com/files/PMU/PMU_Manual.pdf)

**Pinout Diagram:** [PMU-24 Pinout v1.1 (PDF)](https://www.ecumaster.com/files/PMU/PMU-24_Pinout_v1.1.pdf)

**Wiring Diagram:** See Installation Manual (pinout diagrams for PMU24)

## PMU24 Specifications

**Output Capacity:**

- Outputs 1-10: 25A each (250A total) - High-side, PWM capable
- Outputs 11-16: 15A each (90A total) - High-side
- Outputs 17-24: 7A each (56A total) - High-side, dual-purpose (analog input OR power output, software configurable)
- **Total continuous capacity: 170A** (not 396A - power supply limited)
- **Total outputs: 24** programmable high-side outputs
- **Key constraint:** Only outputs with same rating can be combined (e.g., 25A + 25A)

**Outputs 17-24 Dual-Purpose Specifications:**

- **As outputs:** 7A continuous high-side power outputs
- **As inputs:** 0-20V analog inputs (12-bit resolution, 500 Hz sampling, max 30V)
- **Pull resistors:** Configurable per pin (1MΩ pull-down, 10kΩ pull-down, or 10kΩ pull-up)
- **Configuration:** Selectable in PMU software

**Physical Specifications:**

- Dimensions: 131 x 112 x 33mm
- Weight: 385g
- Operating voltage: 6-22V (immunity to transients per ISO 7637)
- Temperature range: -40°C to +125°C (AECQ-100 GRADE 1)

**Features:**

- 24 programmable high-side outputs with overcurrent protection
- Dedicated 12V switched input (Pin 7)
- Up to 16 analog inputs (8 dedicated + outputs 17-24 can be configured as analog inputs)
- Digital inputs for triggers and switches
- 256MB data logger memory (up to 500 Hz logging)
- Real-time clock
- 3D accelerometer/gyroscope
- Built-in inertia switch
- 2x CAN 2.0 A/B interfaces (J1939 compatible)
- 24x tricolor LED output state indicators
- PC configuration via USB (requires [USB to CAN adapter](https://www.ecumaster.com/products/usb-to-can/))

**Configuration:**

- Software: [PMU Configuration Software v101.2.1 (Windows)](https://www.ecumaster.com/files/PMU/PMUSetup_101_2_1.exe)
- Interface: [ECUMaster USB to CAN Adapter](https://www.ecumaster.com/products/usb-to-can/) (required for PC configuration)

**Replaces:** Traditional relay/fuse panel, DRL relay, horn relay, fan controllers, TIPM functions

## Capacity Analysis

### Output Allocation

| Output Tier | Total Outputs | Used | Available | Primary Loads |
|:------------|:-------------:|:----:|:---------:|:--------------|
| 25A (OUT1-10) | 10 | 8 | 2 | Radiator fan (3), iBooster main (2), HVAC (1), aux fans (2) |
| 15A (OUT11-16) | 6 | 4 | 2 | Wipers, cluster, CT4, DRL |
| 7A (OUT17-24) | 8 | 6 | 2 | iBooster ignition, A/C, horn, lights, starter |
| **Total** | **24** | **18** | **6** | **75% capacity used** |

### Load Analysis

| Scenario | Current Draw | Duration | Notes |
|:---------|:-------------|:---------|:------|
| **Peak theoretical** | ~220A | Brief | All outputs at max simultaneously |
| **Realistic continuous** | ~120-150A | Normal operation | iBooster idle (0.25A), radiator fan avg (30-40A), HVAC/accessories (80-110A) |
| **Peak with braking** | ~190A | 1-3 seconds | iBooster peak (40A), radiator fan avg (40A), other loads (~110A) |
| **PMU24 capacity** | **170A continuous** | Continuous | Brief peaks above 170A acceptable (braking events short duration) |

**Assessment:** PMU24 capacity adequate with proper load management. Realistic continuous load well within 170A limit.

## Installation Notes

### Mounting
- **Location:** Engine bay - firewall or inner fender
- Must be accessible for LED diagnostics and USB configuration
- Protect from direct water spray
- Ensure adequate heat dissipation

### Power Connections

| Connection | Pin(s) | Source | Wire Gauge | Protection | Notes |
|:-----------|:-------|:-------|:-----------|:-----------|:------|
| **Main Power** | Power In | Front Battery CONSTANT bus | 2 AWG | 200A breaker (recommended) | All outputs powered from CONSTANT. Minimize voltage drop with short run. |
| **Ignition Sense** | Pin 7 | Ignition switch RUN | 18 AWG | N/A | Dedicated 12V switched input. <500mA total (shared with CT4, SwitchPros, Radio, BCDC). |
| **Ground** | Pin 25 | Front Battery- or NEGATIVE bus | 10 AWG | N/A | Low resistance path essential for proper operation and diagnostics. |
| **CAN Bus** | Pin 23/36 or 24/37 | Cummins ECM J1939 | 18-20 AWG twisted pair | N/A | Stub connection, no termination. See [PMU Inputs][143-pmu-inputs] for topology. |

## Related Documentation

- [PMU Outputs][142-pmu-outputs] - 24-output configuration and load details
- [PMU Inputs][143-pmu-inputs] - Input configuration and CAN bus integration
- [PMU Programming][144-pmu-programming] - Logic examples and configuration
- [Front Battery Distribution][zone-1-front-battery-tray--primary-distribution-engine-bay] - CONSTANT bus specifications

<br/><br/>
