---
hide:
  - toc
tags:
  - product-details
  - communication-systems
  - camera
---

# 7.4 Dash Camera {#dash-camera}

Rearview mirror replacement with integrated front dash camera and rear backup camera display.

/// html | div.product-info
![WolfBox Mirror Camera](../images/wolfbox-mirror-camera.jpg){ loading=lazy }

**Type:** Mirror Dash Camera System

**Model:** G900 TriPro

**Manufacturer:** WolfBox

**Product Page:** [WolfBox G900 TriPro][product-link]

**Mounting:** Windshield (replaces factory rearview mirror)

**Power Source:** BODY PDU F5 (10A fuse, CONSTANT)

///

## Specifications

| Spec | Value |
|:-----|------:|
| Front Camera | Integrated in mirror unit |
| Rear Camera | License plate mount |
| Display | Touchscreen (9.66" or 12") |
| Current Draw | 2-5A typical |
| Storage | SD card (loop recording) |

## Features

- Front-facing dash cam (always recording when powered)
- Rear camera display on reverse
- Loop recording to SD card
- G-sensor collision detection
- Night vision (front and rear)
- Lane departure warnings (model dependent)
- Parking mode (with CONSTANT power)

## Components

**Main Unit (Mirror):**

- Replaces factory rearview mirror
- Integrated front camera
- Touchscreen for settings/playback
- CONSTANT power enables parking mode recording

**Rear Camera:**

- Mounts above license plate or on tailgate
- Powered via cable from main unit
- Auto-displays when reverse gear engaged

## Wiring

| Connection | Wire | Source | Notes |
|:-----------|:-----|:-------|:------|
| Power (+) | 18 AWG | BODY PDU F5 | 10A fuse, CONSTANT |
| Ground (−) | 18 AWG | Dash ground | Firewall stud or local |
| Reverse Trigger | 18 AWG | Reverse light circuit | Signal only |
| Rear Camera | Included cable | Main unit | Power + video combined |

## Cable Routing

**Main Unit to Rear Camera:**

Windshield → along headliner → down A-pillar → under door sills → up tailgate to camera

**Reverse Trigger:**

Tap into reverse light circuit (Engine RTMR F7) → route to WolfBox trigger input

## Outstanding Items

- [ ] Verify G900 TriPro display size and features
- [ ] Confirm power requirement within 10A fuse capacity
- [ ] Verify CONSTANT vs SWITCHED power preference for parking mode
- [ ] Determine rear camera mount location (above license plate vs spare tire carrier)
- [ ] Verify rear camera cable length sufficient for routing
- [ ] Determine reverse trigger tap location
- [ ] Plan cable routing path from mirror to rear camera
- [ ] Determine ground connection point
- [ ] Verify WolfBox compatible with windshield mount
- [ ] Verify rear camera does not interfere with BD S1 Pro lights

## Related Documentation

- [Communication Systems Overview][comm-overview]
- [BODY PDU][body-pdu]

[comm-overview]: index.md
[body-pdu]: ../01-power-systems/03-aux-battery-distribution/03-body-pdu.md
[product-link]: https://wolfbox.com/products/wolfbox-g900tripro-bumper-version-4k-sony-starvis-2-mirror-dash-cam
