---
tags:
  - audio-systems
hide:
  - toc
---

# Section 6: Audio Systems {#audio-systems-index}

Marine-grade audio system with multi-zone control and RGB LED lighting integration.

## System Components

| Component | Model | Power | Control |
|:----------|:------|------:|:--------|
| [Head Unit][head-unit] | Fusion MS-RA670 | 15A | BODY PDU F2 |
| [Amplifier][amplifier] | Fusion Apollo MS-AP61800 | 40A | CONSTANT bus CB |
| [Front Speakers][speakers] | JL Audio M6-650X-S-GmTi-i | — | Amp Ch 3+4 |
| [Rear Speakers][speakers] | JL Audio M6-650VEX-Mb-S-GmTi-i | — | Amp Ch 5+6 |
| [Subwoofer][subwoofer] | JL Audio M7-12IB-S-GmTi-i-4 | — | Amp Ch 1+2 bridged |
| [LED Controller][led-controller] | JL Audio MLC-RW | 10A | BODY PDU (30A) |

**Total System Power:** ~65A peak (40A amp + 15A head unit + 10A LED)

## Signal Flow

```
MS-RA670 Head Unit
    │
    ├─► Zone 1 RCA ──► Amp Ch 3+4 ──► Front Dash Speakers
    ├─► Zone 2 RCA ──► Amp Ch 5+6 ──► Rear Roll Bar Speakers
    ├─► Sub RCA ────► Amp Ch 1+2 (bridged) ──► Subwoofer
    └─► Remote Turn-On ──► Amplifier

MLC-RW LED Controller
    │
    └─► RGB outputs ──► All speaker LEDs + Footwell lights
```

## Outstanding Items

None - see individual component pages for specific items.

## Related Documentation

- [AUX Battery Distribution][aux-distribution] - CONSTANT bus power source
- [BODY PDU][body-pdu] - Head unit and LED controller power
- [Footwell Lights][footwell-lights] - RGB lights controlled by MLC-RW

[head-unit]: 01-head-unit.md
[amplifier]: 02-amplifier.md
[speakers]: 03-speakers.md
[subwoofer]: 04-subwoofer.md
[led-controller]: 05-led-controller.md
[aux-distribution]: ../01-power-systems/03-aux-battery-distribution/index.md
[body-pdu]: ../01-power-systems/03-aux-battery-distribution/03-body-pdu.md
[footwell-lights]: ../04-offroad-lighting/09-footwell-lights.md
