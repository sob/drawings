---
hide:
  - toc
tags:
  - communication-systems
  - ham-radio
---

# 7.3 Ham Radio (Future) {#ham-radio}

Reserved circuit for future amateur radio installation.

/// html | div.product-info

**Type:** Amateur (Ham) Radio

**Model:** TBD

**Manufacturer:** TBD

**Mounting:** TBD

**Power Source:** PMU OUT12 (15A capacity, CONSTANT - reserved)

///

## Reserved Circuit

PMU OUT12 is reserved for future ham radio installation:

| Spec       |                   Value |
| :--------- | ----------------------: |
| PMU Output |                   OUT12 |
| Capacity   |                     15A |
| Power Mode |                CONSTANT |
| Wire Gauge |                  14 AWG |
| Ground     | START battery neg (14 AWG) |
| Firewall   |                 Grommet |

15A capacity supports up to ~180W output radios (most mobile ham radios are 50-100W).

## License Requirements

Ham radio requires an FCC license:

- **Technician** - VHF/UHF privileges
- **General** - HF privileges added
- **Amateur Extra** - Full privileges

Exam required for each license class.

## Potential Radio Types

**VHF/UHF Mobile (2m/70cm):**

| Spec          |                             Value |
| :------------ | --------------------------------: |
| Frequency     |                 144 MHz / 440 MHz |
| Typical Power |                  50W VHF, 35W UHF |
| Current Draw  |                    ~10A TX, 1A RX |
| Antenna       | Roof-mounted dual-band whip (NMO) |

**HF Mobile (Long Range):**

| Spec          |                                 Value |
| :------------ | ------------------------------------: |
| Frequency     |                              3-30 MHz |
| Typical Power |                                  100W |
| Current Draw  |                      ~15A TX, 1-2A RX |
| Antenna       | Bumper or rack mount (requires tuner) |

## Outstanding Items

- [ ] Determine if/when ham radio will be installed
- [ ] Decide on VHF/UHF vs HF vs both
- [ ] Verify 15A fuse is sufficient for chosen radio
- [ ] Determine antenna mounting location
- [ ] Plan coax cable routing
- [ ] Determine if ham radio will integrate with STX intercom

## Related Documentation

- [Communication Systems Overview][comm-overview]
- [PMU Outputs][pmu-outputs]
- [START Battery Distribution][starter-battery]

[comm-overview]: index.md
[pmu-outputs]: ../01-power-systems/04-pmu/03-pmu-outputs.md
[starter-battery]: ../01-power-systems/02-starter-battery-distribution/index.md
