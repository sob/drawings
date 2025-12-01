# Audit Installation Checklist

Analyze a documentation section and create/update its installation checklist.

**Argument:** `$ARGUMENTS` - Section number or name (e.g., "01", "power-systems", "03", "lighting-systems")

## Section Mapping

| Input | Section Path | Checklist File |
|-------|--------------|----------------|
| `01`, `power-systems` | `docs/jeep_lj/01-power-systems/` | `09-installation/02-power-systems-checklist.md` |
| `02`, `engine-systems` | `docs/jeep_lj/02-engine-systems/` | `09-installation/03-engine-systems-checklist.md` |
| `03`, `lighting-systems` | `docs/jeep_lj/03-lighting-systems/` | `09-installation/04-lighting-systems-checklist.md` |
| `04`, `offroad-lighting` | `docs/jeep_lj/04-offroad-lighting/` | `09-installation/05-offroad-lighting-checklist.md` |
| `05`, `control-interfaces` | `docs/jeep_lj/05-control-interfaces/` | `09-installation/06-control-interfaces-checklist.md` |
| `06`, `audio-systems` | `docs/jeep_lj/06-audio-systems/` | `09-installation/07-audio-systems-checklist.md` |
| `07`, `communication-systems` | `docs/jeep_lj/07-communication-systems/` | `09-installation/08-communication-systems-checklist.md` |
| `08`, `exterior-systems` | `docs/jeep_lj/08-exterior-systems/` | `09-installation/09-exterior-systems-checklist.md` |

## Process

### Step 1: Analyze Section Documentation

Read all `.md` files in the section directory (excluding CLAUDE.md). Extract:

1. **Components** - Each product/system documented
2. **Wiring connections** - Sources, destinations, wire gauges, colors
3. **Mounting locations** - Physical installation points
4. **Configuration requirements** - Programming, settings, calibration
5. **Testing requirements** - Verification steps, expected values

### Step 2: Check for Existing Checklist

- If checklist exists: Compare against section docs, identify missing items
- If checklist doesn't exist: Create new file with all discovered tasks

### Step 3: Generate/Update Checklist

**Task Phrasing (as confirmations for amateur mechanic):**

| Type | Pattern | Example |
|------|---------|---------|
| Wiring | "Confirm [source] is connected to [destination] ([gauge] [color])" | "Confirm PMU OUT1+10 connected to iBooster main power (10 AWG red)" |
| Mounting | "Ensure [component] is mounted at [location], torqued to [spec]" | "Ensure iBooster mounted at factory location, bolts torqued to 25 ft-lb" |
| Testing | "Verify [condition] ([expected value])" | "Verify 12V present at iBooster with ignition OFF and ON" |
| Configuration | "Confirm [setting] is configured in [system]" | "Confirm PMU output combining configured for OUT1+10" |
| Ground | "Confirm [component] grounded to [location] ([gauge])" | "Confirm radio grounded to START battery negative (14 AWG)" |

**Organization:**
- Group by subsystem or component
- Order by installation sequence (mount → wire → configure → test)
- Include cross-references to source documentation

### Step 4: Update Index and Nav (if new file)

If creating a new checklist file:

1. **Add to `docs/jeep_lj/09-installation/index.md`:**
   ```markdown
   - **[9.X - Section Name Checklist][section-checklist]** - Section X installation tasks

   [section-checklist]: 0X-section-name-checklist.md
   ```

2. **Add to `mkdocs.yml` nav under Installation:**
   ```yaml
   - 9.X - Section Name Checklist: jeep_lj/09-installation/0X-section-name-checklist.md
   ```

3. **Update `docs/jeep_lj/09-installation/CLAUDE.md`** with new file entry

## Output Format

Present findings:

1. **Components found** - List of systems/products in section
2. **Tasks identified** - Grouped checklist items
3. **Missing from existing checklist** (if applicable)
4. **Files to create/modify** - List all changes needed

Then apply changes after user approval.

## Checklist File Template

```markdown
# Section X: [Name] - Installation Checklist

Organized by installation order for efficient build workflow.

---

## [Subsystem 1]

### [Component A]

- [ ] Confirm [task 1]
- [ ] Ensure [task 2]
- [ ] Verify [task 3]

### [Component B]

- [ ] Confirm [task 1]
...

---

## Related Documentation

- [Component A][component-a] - Full specifications
- [Component B][component-b] - Wiring details

[component-a]: ../0X-section/component-a.md
[component-b]: ../0X-section/component-b.md
```
