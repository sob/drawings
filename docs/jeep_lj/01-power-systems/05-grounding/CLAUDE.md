# Grounding Architecture - Navigation Guide

## What's Here

Documents complete grounding system including direct battery connections and ground bus bars.

## Files

### `index.md` - Grounding Overview

**Contains:** Grounding principles, architecture overview, testing procedures

**Use when:** Understanding overall grounding strategy

### `01-starter-battery-ground.md` - Starter Battery Ground

**Contains:** Direct starter battery negative terminal connections

**Use when:** Finding what connects directly to starter battery negative

### `02-aux-battery-ground.md` - Aux Battery Ground

**Contains:** Direct aux battery negative terminal connections

**Use when:** Finding what connects directly to aux battery negative

### `03-engine-bay-ground-bus.md` - Engine Bay Ground Bus

**Contains:** Engine bay ground bus bar specifications and connections

**Use when:** Finding engine bay ground bus connections

### `04-firewall-stud-bus.md` - Firewall Ground Bus

**Contains:** Cabin electronics ground bus bar specifications and connections

**Use when:** Finding firewall/cabin ground bus connections

### `05-switchpros-ground-bus.md` - SwitchPros Ground Bus

**Contains:** Lighting/accessories ground bus bar specifications and connections

**Use when:** Finding SwitchPros ground bus connections

## Cross-Section References

**To Battery Distribution (1.2, 1.3):** Battery negative terminals

**To Power Generation (1.1):** Alternator, BCDC grounding

**To All Sections:** Ground connection locations for all components

## Navigation Scenarios

**"Where does [component] ground?"** → Check appropriate ground file

**"What grounds directly to battery negative?"** → `01-starter-battery-ground.md` or `02-aux-battery-ground.md`

**"What connects to engine bay ground bus?"** → `03-engine-bay-ground-bus.md`

**"Where are the ground buses located?"** → `index.md` overview

## When Updating

**Adding component with direct battery ground:**

1. Update `01-starter-battery-ground.md` or `02-aux-battery-ground.md`
2. Update battery distribution docs (1.2 or 1.3)

**Adding component to ground bus:**

1. Update appropriate bus file (03, 04, or 05)
2. Verify bus bar stud availability

**Moving ground connection:**

1. Update old ground location file
2. Update new ground location file
3. Update component's primary documentation
