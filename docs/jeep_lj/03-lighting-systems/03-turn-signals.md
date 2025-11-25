---
hide:
  - toc
tags:
  - product-details
  - lighting
  - turn-signals
---

# Turn Signals {#turn-signals}

**Controller:** [Command Touch CT4][command-touch-ct4] (SW1 = right turn, SW2 = left turn)

**Power Source:** START battery CONSTANT (via CT4 40A fuse)

**Features:** GPS auto-cancel, lane change mode, hazard function

## Front Turn Signals

![LED Side Marker](../images/led-side-marker.jpg){ loading=lazy width=200 }

**Type:** Amber LED turn signals
**Quantity:** 2 (left and right fenders)
**Function:** Turn signal only (CT4 controlled)

### Wiring

| Function   | Source  | Wire          | Destination       |
| :--------- | :------ | :------------ | :---------------- |
| Right Turn | CT4 SW1 | BROWN, 14 AWG | Right turn signal |
| Left Turn  | CT4 SW2 | RED, 14 AWG   | Left turn signal  |

## Rear Turn Signals

Rear turn signals are integrated into Maxbilt Round Trail Tail lights (YELLOW wire).
See [Tail/Brake/Reverse Lights][tail-brake-reverse-lights] for complete wiring.

## Outstanding Items

- [ ] Plan wire routing from CT4 to fender turn signal locations
- [ ] Verify turn signal flash rate meets DOT requirements

## Related Documentation

- [Command Touch CT4][command-touch-ct4] - Controller programming and wiring
- [Tail/Brake/Reverse Lights][tail-brake-reverse-lights] - Rear turn signal integration

[command-touch-ct4]: ../05-control-interfaces/03-command-touch-ct4.md
[tail-brake-reverse-lights]: 04-tail-brake-reverse.md
