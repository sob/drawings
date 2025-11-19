# AUX battery Distribution - Navigation Guide

## What's Here

Documents wheel well power distribution from the AUX battery (Odyssey PC1500).

## Files

### `index.md` - AUX battery Overview

**Contains:** AUX battery terminal connection table, direct load connections

**Use when:** Finding what connects to AUX battery positive terminal

### `01-circuit-breakers.md` - Circuit Breakers

**Contains:** All AUX battery circuit breaker specifications and ratings

**Use when:** Finding circuit breaker size for SwitchPros, BODY PDU, or other loads

### `02-constant-bus.md` - CONSTANT Bus Bar

**Contains:** Blue Sea 2104 PowerBar specifications, stud assignments, load distribution

**Use when:** Finding CONSTANT bus bar capacity, available studs, or what connects to the bus

### `04-body-pdu.md` - BODY PDU

**Contains:** Body relay/timer/fuse panel specifications and circuit assignments

**Use when:** Finding BODY PDU specifications or fuse assignments

## Cross-Section References

**To SwitchPros (4.2):** SwitchPros power source via circuit breaker

**To BODY PDU loads:** Audio systems (Section 5), cabin circuits

**To BCDC (1.1.3):** BCDC output connection, charging details

**To Grounding (1.5):** AUX battery negative connections, ground reference cable

**To START battery (1.2):** BCDC input circuit breaker

## Navigation Scenarios

**"What circuit breaker protects SwitchPros?"** → `01-circuit-breakers.md`

**"What connects to AUX battery positive terminal?"** → `index.md` terminal table

**"What connects to the CONSTANT bus bar?"** → `02-constant-bus.md` stud assignments

**"What's powered by BODY PDU?"** → `04-body-pdu.md` circuit assignments

**"How does AUX battery get charged?"** → BCDC (1.1.3)

## When Updating

**Adding new AUX battery load:**

1. Determine if direct battery connection or CONSTANT bus connection
2. Update `index.md` terminal table OR `02-constant-bus.md` stud table
3. Add circuit breaker in `01-circuit-breakers.md` if needed
4. Update grounding files (Section 1.5)

**Changing BODY PDU circuits:**

1. Update `04-body-pdu.md` circuit table
2. Update affected system docs (Section 5)
