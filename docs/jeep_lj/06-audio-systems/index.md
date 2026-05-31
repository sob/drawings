---
tags:
  - audio-systems
hide:
  - toc
---

# Section 6: Audio Systems {#audio-systems-index}

Marine-grade audio system with multi-zone control and RGB LED lighting integration.

## System Components

| Component                        | Model                          | Power | Control            |
| :------------------------------- | :----------------------------- | ----: | :----------------- |
| [Head Unit][head-unit]           | Fusion MS-RA670                |   15A | BODY PDU F2        |
| [Amplifier][amplifier]           | Fusion Apollo MS-AP61800       |   40A | AUX battery+ direct (100A inline CB) — mounted under rear seat |
| [Front Speakers][speakers]       | JL Audio M6-650X-S-GmTi-i      |     — | Amp Ch 3+4         |
| [Rear Speakers][speakers]        | JL Audio M6-650VEX-Mb-S-GmTi-i |     — | Amp Ch 5+6         |
| [Subwoofers][subwoofer]          | 2× JL Audio M6-8IB-S-GmTi-i-4 (series-wired) | — | Amp Ch 1+2 bridged @ 8Ω |
| [LED Controller][led-controller] | JL Audio MLC-RW                |    5A | SwitchPros OUT-5   |

**Total System Power:** ~60A peak (40A amp + 15A head unit + 5A LED)

## Signal Flow

```text
MS-RA670 Head Unit
    │
    ├─► Zone 1 RCA ──► Amp Ch 3+4 ──► Front Dash Speakers
    ├─► Zone 2 RCA ──► Amp Ch 5+6 ──► Rear Roll Bar Speakers
    ├─► Sub RCA ────► Amp Ch 1+2 (bridged @ 8Ω) ──► 2× M6-8IB subs (series)
    └─► Remote Turn-On ──► Amplifier

MLC-RW LED Controller
    │
    └─► RGB outputs ──► All speaker LEDs + Footwell lights
```

## Outstanding Items

None - see individual component pages for specific items.

## Related Documentation

- [AUX Battery Distribution][aux-distribution] - Firewall CONSTANT Bus power source (via 300A master CB at AUX battery)
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
