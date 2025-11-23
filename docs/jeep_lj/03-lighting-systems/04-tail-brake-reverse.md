---
hide:
  - toc
tags:
  - product-details
  - lighting
  - tail-lights
  - led
---

# Tail, Brake & Reverse Lights {#tail-brake-reverse-lights}

/// html | div.product-info
![Maxbilt Trail Tail](../images/maxbilt-trail-tail.png){ loading=lazy }

**Type:** LED Tail Light (4-function: Brake, Turn, Marker, Reverse)

**Model:** Trail Tail

**Manufacturer:** On The Rox Fabrication (Maxbilt)

**Product Page:** [Maxbilt Trail Tail LED Tail Lights][product-link]

**Installation Guide:** [Maxbilt Tail Wiring][install-link]

**Quantity:** 2

**Mounting:** Rear quarter panels or tailgate

**Power Source:** CT4 (turn), PMU Out 17 (brake), PMU Out 18 (reverse), PMU Out 9 (marker)

///

## Wire Functions

| Color | Function | Connection | Wire Gauge | Notes |
|:------|:---------|:-----------|:-----------|:------|
| BLACK | Ground | Chassis ground | 14-16 AWG | Clean metal-to-metal |
| WHITE | Reverse | PMU Out 18 | 14 AWG | Parallel with factory backup lights |
| YELLOW | Brake/Turn | CT4 + PMU Out 17 (via diodes) | 14 AWG | Combined function - see diode section |
| RED | Marker/Parking | PMU Out 9 | 14 AWG | DRL/parking circuit |

## Reverse Lights

**Power:** PMU Out 18 (3A load, 14 AWG)
**Trigger:** Transmission reverse switch → PMU In 3
**Circuits:** Maxbilt WHITE + factory backup lights + WolfBox camera trigger (parallel)

**Wiring:**

1. Transmission reverse signal → PMU In 3
2. PMU Out 18 → backup lights + Maxbilt WHITE + WolfBox trigger (parallel)
3. Chassis ground

## Brake Lights

**Power:** PMU Out 17 (3A load, SWITCHED)
**Trigger:** Brake pedal switch → PMU In 2
**Circuits:** Maxbilt YELLOW + factory third brake light (if retained)

**Wiring:**

1. Brake pedal switch → PMU In 2
2. PMU Out 17 → diode → Maxbilt YELLOW (both tail lights)
3. PMU Out 17 → factory third brake light (if retained)

Brake circuit integrates with turn signals via diode isolation (see below).

## Brake/Turn Signal Diode Isolation

**Purpose:** Prevent backfeed between turn signal and brake circuits

**Diode Configuration:**

```text
     CT4 Left Turn (SW2) ──[Diode]──┬──→ Left Maxbilt YELLOW
                                     │
PMU Out 17 Brake Circuit ──[Diode]──┴──→ Left Maxbilt YELLOW

    CT4 Right Turn (SW1) ──[Diode]──┬──→ Right Maxbilt YELLOW
                                     │
PMU Out 17 Brake Circuit ──[Diode]──┴──→ Right Maxbilt YELLOW
```

**Diode Specifications:**

- 1N4001 or equivalent (1A, 50V minimum)
- Prevents backfeed between circuits

**Operation:**

- Right turn active → right tail light flashes
- Brake pressed → both tail lights solid
- Right turn + brake → right flashes, left stays solid

## Marker/Parking Lights

**Power:** PMU Out 9 (DRL/parking circuit)
**Maxbilt Connection:** RED wire
**Control:** Automatic with ignition
**Shared Circuit:** License plate lights, LP6 DRL, front markers

See [DRL/Parking Lights][drl-parking-lights] for circuit details.

## Outstanding Items

- [ ] Determine mounting location (quarter panels vs tailgate)
- [ ] Confirm reverse switch location and wiring to PMU In 3
- [ ] Verify parallel connection to WolfBox camera trigger
- [ ] Determine if factory backup lights need LED upgrade
- [ ] Confirm brake switch location and wiring to PMU In 2
- [ ] Determine if factory third brake light (CHMSL) is retained
- [ ] Verify brake light brightness meets DOT requirements
- [ ] Plan wire routing from CT4 to rear tail lights
- [ ] Plan wire routing from PMU Out 17 to rear tail lights via diodes
- [ ] Source diodes (1N4001 or equivalent)
- [ ] Test turn signal priority over brake lights
- [ ] Verify Maxbilt beam pattern meets DOT requirements

## Related Documentation

- [PMU Power Distribution][pmu-power-distribution] - PMU Out 17, Out 18 circuits
- [Command Touch CT4][command-touch-ct4] - Turn signal control
- [DRL/Parking Lights][drl-parking-lights] - Marker/parking circuit (RED wire)
- [Communication & Camera][communication-systems] - WolfBox camera reverse trigger

[product-link]: https://ontheroxfab.com/product/maxbilt-trail-tail-led-tail-lights/
[install-link]: https://ontheroxfab.com/wp-content/uploads/2019/10/MaxBilt-Taillight-Installation-12-3-2020.pdf
[pmu-power-distribution]: ../01-power-systems/04-pmu/index.md
[command-touch-ct4]: ../04-control-interfaces/03-command-touch-ct4.md
[drl-parking-lights]: 05-drl-parking.md
[communication-systems]: ../06-communication-systems/index.md
