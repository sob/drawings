---
hide:
  - toc
tags:
  - product-details
  - audio-systems
  - jl-audio
---

# 6.4 Subwoofers {#subwoofer}

Pair of 8" infinite baffle marine subwoofers with RGB LED lighting, mounted symmetrically in the rear quarter panels.

/// html | div.product-info
![JL Audio M6-8IB-S-GmTi-i-4](../images/jl-audio-m6-8ib-s-gmti-i-4.jpg){ loading=lazy }

**Type:** 8" Infinite Baffle Marine Subwoofer

**Model:** M6-8IB-S-GmTi-i-4

**Manufacturer:** JL Audio

**Product Page:** [M6-8IB-S-GmTi-i-4][product-link]

**Quantity:** 2 (pair)

**Mounting:** Rear quarter panels (one per side, above wheel wells, firing inward)

**Power Source:** Amplifier Channels 1+2 (bridged), wired **in series** across both subs

///

## Specifications (per sub)

| Spec               |                Value |
| :----------------- | -------------------: |
| Power Handling     |        200W RMS @ 4Ω |
| Impedance          |              4Ω SVC |
| Sensitivity        |        ~85 dB @ 1W/1m |
| Voice Coil         |                  2" |
| Overall Diameter   |              ~9.5" |
| Mounting Depth     |              ~4.25" |
| Weight             |             ~7 lbs |
| Warranty           |              3 years |

## Wiring Configuration {#wiring}

Both subs wired **in series** to the Fusion amp bridged Ch1+2 output. This is the only safe configuration with this amp/sub combination:

| Wiring | Total Z | Fusion AP61800 Output | Per Sub | Safe? |
| :----- | :-----: | :------------------: | :-----: | :----: |
| Parallel | 2Ω | n/a — below 4Ω bridged minimum | n/a | ❌ Damages amp |
| **Series** | **8Ω** | ~290W | ~145W | ✅ 72% of RMS rating |

**Series wiring path:**

```
Amp Ch1+2 (+) → Sub A (+)
              Sub A (−) → Sub B (+)
                          Sub B (−) → Amp Ch1+2 (−)
```

Total amp output ~290W into the pair (~145W per sub) — well-controlled, headroom for transients, no risk of over-excursion at sane gain settings.

## Infinite Baffle Requirements

- **Minimum air volume:** 0.75 cu ft per sub (1.5 cu ft pair)
- **Installation type:** No dedicated enclosure required
- **Ideal location:** Rear quarter panels above wheel wells, firing inward into cabin
- **IB chamber:** Rear cargo area / behind quarter trim (effectively unlimited volume in an LJ)

## Features

- Transflective RGB LED lighting (via MLC-RW)
- Gunmetal trim ring with titanium sport grille
- Marine-grade construction
- Mica-filled polypropylene cone
- Synthetic rubber surround

## Wiring

| Connection  | Wire   | Notes                   |
| :---------- | :----- | :---------------------- |
| Speaker (+) | 14 AWG | From amp Ch 1+2 bridged to Sub A (+) |
| Sub A (−) → Sub B (+) | 14 AWG | Series jumper between subs |
| Speaker (−) | 14 AWG | From Sub B (−) back to amp Ch 1+2 bridged (−) |
| LED         | 20 AWG | RGB from MLC-RW (one tap per sub) |

Standard speaker wire (no XM-WHTMFC needed for subwoofer audio).

## Why Two 8" vs Single 12"

The single 12" M7-12IB option (600W RMS, 14" overall diameter, 7.94" mounting depth, requires 3+ cu ft IB chamber) was ruled out for LJ-specific install reasons:

- **Mounting depth:** 7.94" of basket depth makes most LJ panels impractical — cage tubes, wheel wells, and tailgate clearance all conflict.
- **Single-sub asymmetry:** harder to integrate cosmetically vs symmetric L/R 8" pair.
- **No matching 12" M6:** JL doesn't make a 12" M6-IB (M6 IB line tops at 10"), so the pair option doesn't exist at 12".

**Tradeoff accepted:** total sub output drops from 580W (single M7-12IB @ 4Ω bridged) to ~290W (2× M6-8IB @ 8Ω bridged), about half. Acceptable for a soft-top Jeep where wind noise dominates at highway speed anyway, and the symmetric placement + easier install win out.

## Outstanding Items

- [ ] Confirm exact mounting locations in rear quarter panels (clear of cage tubes and rear seatbelts)
- [ ] Verify quarter panel material can support sub weight + mounting torque (may need backing plate)

## Related Documentation

- [Audio Systems Overview][audio-overview]
- [Amplifier][amplifier]
- [LED Controller][led-controller]

[audio-overview]: index.md
[amplifier]: 02-amplifier.md
[led-controller]: 05-led-controller.md
[product-link]: https://www.garmin.com/en-US/p/1851253/
