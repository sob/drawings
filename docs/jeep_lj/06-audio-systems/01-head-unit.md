---
hide:
  - toc
tags:
  - product-details
  - audio-systems
  - fusion
---

# 6.1 Head Unit {#head-unit}

Marine-grade entertainment system with multi-zone audio, Bluetooth, and NMEA 2000 integration.

/// html | div.product-info
![Fusion MS-RA670](../images/fusion-ms-ra670.jpg){ loading=lazy }

**Type:** Marine Entertainment System

**Model:** MS-RA670

**Manufacturer:** Fusion (Garmin)

**Product Page:** [Fusion MS-RA670][product-link]

**Manual:** [Installation Manual][manual-link]

**Mounting:** Dashboard center console (factory radio location)

**Power Source:** BODY PDU CB30 (10A memory) + CB44 via K27 (15A ignition-switched)

///

## Specifications

| Spec           |                 Value |
| :------------- | --------------------: |
| Display        |   2.7" full-color TFT |
| Speaker Output | 4x 50W RMS (not used) |
| Max Current    |                   15A |
| Waterproof     |                  IPX7 |

## Features

- AM/FM radio with RDS
- Bluetooth audio streaming and hands-free calling
- Multi-zone audio (3 zones + subwoofer)
- DSP with presets
- NMEA 2000 integration
- PartyBus networking
- USB audio playback

## RCA Pre-Outs

| Output     | Destination            | Amplifier      |
| :--------- | :--------------------- | :------------- |
| Zone 1 L+R | Front dash speakers    | Ch 3+4         |
| Zone 2 L+R | Rear roll bar speakers | Ch 5+6         |
| Zone 3 L+R | Available              | —              |
| Subwoofer  | Subwoofer              | Ch 1+2 bridged |

## Wiring

| Connection        | Wire     | Source          | Notes                 |
| :---------------- | :------- | :-------------- | :-------------------- |
| Constant (Yellow) | 18 AWG   | BODY PDU CB30   | Memory/clock (10A)    |
| Switched (Red)    | 18 AWG   | BODY PDU CB44   | Ignition on/off (15A) |
| Ground (Black)    | 18 AWG   | Dash ground     | Same ground as MLC-RW |
| Antenna           | Motorola | Factory antenna | Fender or windshield  |
| Remote Out        | 18 AWG   | To amplifier    | Turn-on signal        |

## Power Configuration

Head unit uses two BODY PDU circuits:

- **CB30 (10A, CONSTANT):** Yellow wire - memory/clock retention (~1A)
- **CB44 via K27 (15A, ignition-switched):** Red wire - main power when ignition on (~15A)

K27 relay triggered by ignition signal from SWITCHED bus.

## Outstanding Items

None - all specifications determined.

## Related Documentation

- [Audio Systems Overview][audio-overview]
- [Amplifier][amplifier]
- [BODY PDU][body-pdu]

[audio-overview]: index.md
[amplifier]: 02-amplifier.md
[body-pdu]: ../01-power-systems/03-aux-battery-distribution/03-body-pdu.md
[product-link]: https://www.garmin.com/en-US/p/635318/
[manual-link]: https://static.garmin.com/pumac/MS-RA670_OM_EN.pdf
