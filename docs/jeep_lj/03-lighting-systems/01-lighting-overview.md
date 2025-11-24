---
hide:
  - toc
---

# Vehicle Lighting Overview {#vehicle-lighting-overview}

This section covers all street-legal DOT-required lighting circuits controlled by the Command Touch CT4 and PMU.

## System Components

**Controller:** [Command Touch CT4][command-touch-ct4] - Steering column-mounted multifunction controller

- Turn signal control (left/right) with GPS auto-cancel
- Headlight control (low/high beam)
- Powered by START battery CONSTANT (40A fuse) + Ignition RUN signal

**Power Distribution:** [PMU][pmu-power-distribution] - Programmable power management

- DRL/Parking lights (Out 9)
- Brake lights (Out 17)
- Reverse lights (Out 18)

## Lighting Systems

### Headlights {#headlights-overview}

- **Type:** Baja Designs LP6 DOT LED (complete replacement)
- **Low Beam:** CT4 SW3 (3.6A total) - latching on/off
- **High Beam:** CT4 SW4 (5.6A total) - momentary or latching
- **DRL:** PMU Out 9 (0.8A total) - automatic with ignition, auto-off when headlights on
- **See:** [Headlights][headlights] for complete specifications

### Turn Signals {#turn-signals-overview}

- **Front:** Dedicated amber LED turn signals (CT4 SW1/SW2)
- **Rear:** Integrated into Maxbilt Trail Tail lights (YELLOW wire)
- **Features:** GPS auto-cancel, lane change mode, hazard function
- **See:** [Turn Signals][turn-signals] for complete specifications

### Tail, Brake & Reverse Lights {#tail-brake-reverse-overview}

- **Type:** Maxbilt Trail Tail LED (4-function)
- **Brake:** PMU Out 17 (3A) - trigger via brake pedal switch
- **Reverse:** PMU Out 18 (3A) - trigger via transmission switch, also activates WolfBox camera
- **Turn:** CT4 SW1/SW2 (combined with brake via diode isolation)
- **Marker/Parking:** PMU Out 9 (DRL/parking circuit)
- **See:** [Tail, Brake & Reverse][tail-brake-reverse-lights] for complete specifications

### DRL & Parking Lights {#drl-parking-overview}

- **Circuit:** PMU Out 9 (8A capacity)
- **Components:** LP6 DRL, license plate lights, front/rear markers
- **Control:** Automatic with ignition, PMU logic disables when headlights on
- **No external relay needed** - handled by PMU programming
- **See:** [DRL & Parking Lights][drl-parking-lights] for complete specifications

## Power Sources

| Circuit             | Power Source           | Capacity | Load                   |
| :------------------ | :--------------------- | :------- | :--------------------- |
| CT4 Controller      | START battery CONSTANT | 40A      | Powers all CT4 outputs |
| Headlights Low/High | CT4 SW3/SW4            | 10A each | 3.6A / 5.6A            |
| DRL/Parking         | PMU Out 9              | 15A      | ~8A                    |
| Brake Lights        | PMU Out 17             | 7A       | ~3A                    |
| Reverse Lights      | PMU Out 18             | 7A       | ~3A                    |

## Key Features

- **GPS Auto-Cancel:** Turn signals cancel after turns
- **DRL Auto-Off:** PMU programming disables DRL when headlights activate
- **Diode Isolation:** Turn signals and brake lights integrated without backfeed

## Related Documentation

- [Command Touch CT4][command-touch-ct4] - Controller specifications and programming
- [PMU Power Distribution][pmu-power-distribution] - Power management and programming
- [Offroad Lighting][offroad-auxiliary-lighting] - Auxiliary and offroad lighting circuits
- [Control Interfaces Overview][control-interfaces-overview] - All control interfaces

[command-touch-ct4]: ../05-control-interfaces/03-command-touch-ct4.md
[pmu-power-distribution]: ../01-power-systems/04-pmu/index.md
[headlights]: 02-headlights.md
[turn-signals]: 03-turn-signals.md
[tail-brake-reverse-lights]: 04-tail-brake-reverse.md
[drl-parking-lights]: 05-drl-parking.md
[offroad-auxiliary-lighting]: ../04-offroad-lighting/index.md
[control-interfaces-overview]: ../05-control-interfaces/index.md
