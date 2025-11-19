# 1.5 - Body RTMR {#body-rtmr}
**Type:** Relay/Fuse Panel (Body Power Distribution)

**Model:** TBD - need to determine part number

**Power Source:** Mix of CONSTANT and SWITCHED buses

**Mounting Location:** Under dash - passenger side

**Ground:** TBD

## Circuit Configuration

| Slot | Size |              Circuit               | Gauge | Power Source |                Routing                | Load |                  Notes                  |
| :--: | :--: | :--------------------------------: | :---: | :----------: | :-----------------------------------: | :--: | :-------------------------------------: |
|  F1  | 10A  |           **SPARE**                |   -   |      -       |                   -                   |  -   | Previously Dakota Digital (moved to PMU Out 14) |
|  F2  | 5A   |  Fusion Radio (memory)             | 18AWG |   CONSTANT   |    Memory/clock retention only        | ~1A  | Memory power when ignition off          |
|  F3  | 15A  |  Fusion Radio (amplifier)          | 14AWG |   CONSTANT   |    Amplifier main power               | ~15A | Remote wire from deck triggers on/off   |
|  F4  | 20A  |    USB Charging Ports              | 14AWG |   CONSTANT   | 2x Powerwerx PanelUSB-75W             | ~13A | Always-on phone/GPS charging            |
|  F5  | 10A  |    WolfBox Camera/Mirror           | 16AWG |   CONSTANT   | Dash cam + backup camera              | ~10A | Ignition wire triggers active recording |
|  F6  | 15A  |    Driver Heated Seat              | 14AWG |   SWITCHED   | via On/Off Switch                     | 15A  | Heated seat only                        |
|  F7  | 15A  |    Passenger Heated Seat           | 14AWG |   SWITCHED   | via On/Off Switch                     | 15A  | Heated seat only                        |
|  F8  | 15A  |    **SPARE**                       |   -   |      -       | -                                     |  -   | Ham Radio moved to SafetyHub            |
|  F9  | 10A  |           **SPARE**                |   -   |      -       |                   -                   |  -   | Future expansion                        |
| F10  | 10A  |           **SPARE**                |   -   |      -       |                   -                   |  -   | Future expansion                        |
| F11  | 10A  |           **SPARE**                |   -   |      -       |                   -                   |  -   | Future expansion                        |
| F12  | 10A  |           **SPARE**                |   -   |      -       |                   -                   |  -   | Previously cargo + BCDC (moved to PMU/SwitchPros) |

## System Architecture

**Philosophy:** Body RTMR provides fused power distribution for cabin convenience systems only

**Power Distribution:**

- **CONSTANT circuits:** USB charging (20A), radio memory (5A), radio amplifier (15A), WolfBox (10A) = 50A total
- **SWITCHED circuits:** Heated seats (30A) = 30A total
- **Total used:** 5 of 12 slots, 7 spare for future expansion

**System Changes:**

- **Critical systems moved to PMU:** Dakota Digital cluster (Out 14), BCDC signal (ignition sense tap)
- **Cargo light moved to SwitchPros:** OUTPUT-13 (user-controlled)
- **Communication devices moved to SafetyHub:** G1 GMRS (15A), STX Intercom (5A), Ham Radio future (25A)

**Trigger Wire Control:**

- Amplifier: Remote wire from deck triggers on/off (on CONSTANT power)
- WolfBox: Ignition trigger wire activates recording (on CONSTANT power)

## Outstanding Items

- [ ] Determine specific Body RTMR part number
- [ ] Determine Body RTMR ground connection location
- [ ] Confirm wire gauge specifications for all circuits (currently specified)
- [ ] Verify actual current draw for Fusion radio memory and amplifier circuits
- [ ] Determine specific WolfBox camera/mirror model and verify 10A fuse is sufficient
- [ ] Route CONSTANT power feed from rear battery CONSTANT bus to Body RTMR
- [ ] Route SWITCHED power feed from front battery SWITCHED bus (via PMU or relay) to Body RTMR
- [ ] Route heated seat on/off switch wiring to Body RTMR F6/F7
- [ ] Verify heated seat current draw is 15A per seat (PRP EnduroTrek specification)

## Related Documentation

- [Front Battery Distribution][zone-1-front-battery-tray--primary-distribution-engine-bay] - SWITCHED bus specifications
- [Rear Battery Distribution][13-rear-battery-distribution-wheel-well] - CONSTANT bus specifications
- [Dashboard Controls][dashboard-physical-controls] - Physical switch panel layout
- [Audio Systems][audio-systems] - Fusion radio specifications
