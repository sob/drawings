# 1.6 - SafetyHub 150 {#safetyhub-150}
**Type:** High-Current Fuse Panel

**Model:** Blue Sea 7748

**Product Page:** [Blue Sea SafetyHub 150](https://www.bluesea.com/products/7748/SafetyHub_150_Fuse_Block)

**Power Source:** CONSTANT bus bar

**Mounting Location:** Engine compartment - TBD specific location

**Ground:** TBD - chassis ground point

## Circuit Configuration

|  Slot  | Size |           Circuit            | Gauge | Power Source |           Routing            | Load |                   Notes                    |
| :----: | :--: | :--------------------------: | :---: | :----------: | :--------------------------: | :--: | :----------------------------------------: |
| MIDI-1 | 60A  | ARB Compressor Motor 1 Power | 10AWG |   CONSTANT   |     To compressor motor 1     | 45A  |           One motor of twin setup           |
| MIDI-2 | 60A  | ARB Compressor Motor 2 Power | 10AWG |   CONSTANT   |     To compressor motor 2     | 45A  |           One motor of twin setup           |
| MIDI-3 |  -   |            SPARE             |   -   |      -       |              -               |  -   |                                            |
| MIDI-4 |  -   |            SPARE             |   -   |      -       |              -               |  -   |                                            |
| ATC-1  | 10A  |   Winch Contactor Trigger    |  TBD  |   CONSTANT   |   From 3-position selector   | ~1A  | Trigger only, main winch power is separate |
| ATC-2  |  -   |            SPARE             |   -   |      -       |              -               |  -   |                                            |
| ATC-3  |  -   |            SPARE             |   -   |      -       |              -               |  -   |                                            |
| ATC-4  |  -   |            SPARE             |   -   |      -       |              -               |  -   |                                            |

## System Architecture

**Philosophy:** SafetyHub provides high-current fused distribution for heavy-load accessories (ARB compressor, winch trigger)

**Power Distribution:**

- **MIDI slots (60A each):** ARB compressor dual motors (120A total)
- **ATC slots (10A each):** Winch contactor trigger
- **Total used:** 3 of 8 slots, 5 spare for future expansion

## Outstanding Items

- [ ] Determine exact SafetyHub mounting location in engine compartment
- [ ] Determine SafetyHub chassis ground point location
- [ ] Determine wire gauge for all SafetyHub circuits (currently TBD)
- [ ] Determine routing for winch contactor trigger from SafetyHub ATC-1 to winch

## Related Documentation

- [Rear Battery Distribution][13-rear-battery-distribution-wheel-well] - CONSTANT bus specifications
- [Air System][air-system-arb-compressor-lockers] - ARB Twin Compressor wiring details
- [Recovery Systems][recovery-systems] - Winch system specifications
- [SwitchPros SP-1200][switchpros-sp-1200-rcr-force-12] - OUTPUT-11 compressor control signal
