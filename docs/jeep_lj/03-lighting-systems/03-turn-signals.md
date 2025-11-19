---
hide:
  - toc
---

# Turn Signals {#turn-signals}
**Controller:** [Command Touch CT4][command-touch-ct4] (SW1 = right turn, SW2 = left turn)
**Power Source:** START battery CONSTANT (via CT4 40A fuse)
**Features:** GPS auto-cancel, lane change mode, hazard function

## Front Turn Signals

**Type:** Amber LED turn signal lights (dedicated turn signal only)
**Quantity:** 2 (left and right)
**Mounting Location:** Front fenders or bumper (TBD)
**Wire Gauge:** 14 AWG from CT4 to junction, 16 AWG to each light

**Wiring:**
- CT4 SW1 (brown wire) → Front right turn signal
- CT4 SW2 (red wire) → Front left turn signal

**Note:** Dedicated turn signals, NOT dual-function with parking lights

## Rear Turn Signals

Rear turn signals are integrated into Maxbilt Trail Tail lights (YELLOW wire).
See [Tail/Brake/Reverse Lights][tail-brake-reverse-lights] for complete wiring.

## Front Side Markers (Parking - NOT Turn Signals)

**Type:** 2" LED side markers (amber)
**Quantity:** 2 (left and right)
**Function:** Parking/marker lights only
**Control:** Automatic with ignition (DRL/parking circuit)
**Power:** PMU Out 9 (shared with LP6 DRL, license plate, tail markers)

See [DRL/Parking Lights][drl-parking-lights] for complete circuit details.

## Outstanding Items

- [ ] Determine exact mounting location for front turn signals (fenders vs bumper)
- [ ] Plan wire routing from CT4 to front turn signal locations
- [ ] Verify turn signal flash rate meets DOT requirements

## Related Documentation

- [Command Touch CT4][command-touch-ct4] - Controller programming and wiring
- [Tail/Brake/Reverse Lights][tail-brake-reverse-lights] - Rear turn signal integration
- [DRL/Parking Lights][drl-parking-lights] - Front marker parking lights
