# 1.3 Rear Battery Distribution (Wheel Well) {#13-rear-battery-distribution-wheel-well}
## Components

- **Location:** Passenger side rear wheel well, custom compartment with access panel
- **Battery:** Odyssey ODX-34/78-AGM (see [Section 1.1][# 1.1 Power Generation & Storage {#11-power-generation-storage}])
- **Charger:** RedArc BCDC Alpha 50 (see [Section 1.1][# 1.1 Power Generation & Storage {#11-power-generation-storage}])
- **CONSTANT Bus Bar:** Always powered, feeds all accessory circuits (150A+ capacity required)

!!! info "Detailed Specifications"
    See [Section 1.1 - Battery System][# 1.1 Power Generation & Storage {#11-power-generation-storage}] for complete battery and BCDC Alpha 50 specifications.

## Circuit Breakers

| Circuit | Rating | Source | Destination | Loads |
|---------|--------|--------|-------------|-------|
| CONSTANT Bus | 100A | Rear Battery+ | CONSTANT bus bar | All accessory circuits |
| SwitchPros | 150A | CONSTANT bus | SwitchPros RCR-Force 12 | Auxiliary lighting, lockers, compressor |
| SafetyHub | 100A | CONSTANT bus | SafetyHub 150 | ARB compressor (dual 60A), winch trigger (10A) |

## Power Distribution

```
REAR BATTERY+ (Passenger Wheel Well - Odyssey ODX-34/78-AGM)
│
├─ BCDC Alpha 50 Output (50A DC-DC charging)
│   Input: 4 AWG from front battery (70A CB, per Redarc spec)
│   Signal: Body RTMR F12 (12V trigger when engine running)
│
├─ [Blue Sea 100A CB] → CONSTANT Bus Bar
│   │
│   ├─ [Blue Sea 150A CB] → SwitchPros RCR-Force 12
│   │   Roof lights: 31A + 12A + 12A = 55A
│   │   Fog/ditch/rock: 9A + 12A + 3A = 24A
│   │   Party/chase/rear: 6A + 6A + 5A = 17A
│   │   Dome lights: 4A
│   │   ARB lockers: 2A + 2A = 4A
│   │   ARB compressor control: OUTPUT-11, 15A max
│   │
│   ├─ [Blue Sea 100A CB] → SafetyHub 150
│   │   ARB Compressor Motor 1: MIDI-1, 60A
│   │   ARB Compressor Motor 2: MIDI-2, 60A
│   │   Winch trigger: ATC-1, 10A (from dash switch)
│   │
│   └─ Body RTMR (CONSTANT circuits only)
│       F5: Rearview mirror camera, 10A
│       F6: *OPEN*
│       F7: *OPEN*
│       F8: Ham radio, 15A (future)
│       F9: USB charging, 10A
│       F10: Heated/cooled seats, 20A
│       F11: Heated/cooled seats, 20A
│       F12: Cargo lights + BCDC signal, 15A
│           **WARNING:** BCDC signal must be isolated from cargo lights
│
└─ Jump Start Assist (BCDC Alpha 50 automatic mode when front battery low)

REAR BATTERY-
├─ Rear frame rail ground (2/0 AWG)
├─ SwitchPros direct ground (2/0 AWG, per manufacturer)
├─ BCDC Alpha 50 ground (2/0 AWG)
└─ Ground reference from front battery (2/0 AWG)
```

## Inter-Battery Wiring

### Front to Rear Power Cables

| Cable | Gauge | Source | Destination | Protection | Length | Notes |
|-------|-------|--------|-------------|------------|--------|-------|
| BCDC Input | 2/0 or 4/0 AWG | Front battery+ | BCDC input | 50-60A CB at front | ~10-12 ft | 4/0 AWG recommended for voltage drop |
| Ground Reference | 2/0 AWG | Front battery- | Rear battery- | None | ~10-12 ft | Critical for BCDC operation |
| BCDC Signal | 14-16 AWG | Body RTMR F12 | BCDC trigger | Fused at source | Varies | Clean SWITCHED signal, isolated from cargo lights |

**Routing:** Engine bay → under vehicle along frame rail → rear wheel well

## Outstanding Items

- [ ] Body RTMR F12: Isolate BCDC trigger signal from cargo lights circuit
- [ ] Confirm exact wire gauges for all inter-battery wiring (2/0 vs 4/0 AWG)
- [ ] Confirm exact cable lengths for all inter-battery runs
- [ ] Determine exact routing path for cables (under vehicle vs through cabin)
- [ ] Determine exact physical mounting locations for bus bars in rear wheel well
- [ ] Confirm winch 2/0 AWG cable routing through front bumper

## References

- [BCDC Alpha BT Instruction Manual](https://cdn.intelligencebank.com/au/share/yE9N/zJpl/Dra9X/original/BCDC+Alpha+BT+Instruction+Manual+EN) - Wire sizing, installation, specifications
