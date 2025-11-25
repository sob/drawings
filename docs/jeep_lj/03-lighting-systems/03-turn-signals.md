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
**Size:** 0.8" × 0.8" × 1.1"
**Draw:** ~0.2A each (~0.4A total, estimated)

### Wiring

| Function   | Source  | Wire          | Current | Ampacity @60°C | Utilization |
| :--------- | :------ | :------------ | :------ | :------------- | :---------- |
| Right Turn | CT4 SW1 | BROWN, 14 AWG | ~0.2A   | 20A            | 1%          |
| Left Turn  | CT4 SW2 | RED, 14 AWG   | ~0.2A   | 20A            | 1%          |

**Routing:** CT4 (steering column) → firewall grommet → engine bay → fenders

**Connections:** Soldered with marine heat shrink (waterproof)

## Rear Turn Signals

Rear turn signals are integrated into Maxbilt Round Trail Tail lights (YELLOW wire).
See [Tail/Brake/Reverse Lights][tail-brake-reverse-lights] for complete wiring.

## Outstanding Items

- [x] ~~Plan wire routing from CT4 to fender turn signal locations~~ → Via firewall grommet
- [ ] Verify turn signal flash rate meets DOT requirements
- [ ] Measure wire distance: CT4 → firewall → fenders (see [Wire Distance Reference][wire-distance])

[wire-distance]: ../01-power-systems/01-power-generation/05-wire-distance-reference.md

## Related Documentation

- [Command Touch CT4][command-touch-ct4] - Controller programming and wiring
- [Tail/Brake/Reverse Lights][tail-brake-reverse-lights] - Rear turn signal integration

[command-touch-ct4]: ../05-control-interfaces/03-command-touch-ct4.md
[tail-brake-reverse-lights]: 04-tail-brake-reverse.md
