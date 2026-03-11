# Dependency Slug QA Round 1

## Scope

This pass reviewed dependency slugs across:

- `data/processed/substrates_master.csv`
- the current profile IDs in `research/profiles/`

## Summary

- Compiled rows reviewed: `24`
- Declared dependency edges reviewed: `66`
- Dependency slugs with invalid format: `0`
- Dependency slugs that resolve to an existing profile ID: `27`
- Dependency slugs that do **not** resolve to an existing profile ID: `39`

Conclusion:

- slug formatting is clean
- dependency resolution is not clean
- the repo is currently mixing two different things in one field:
  - canonical dependencies that point to real substrate profiles
  - conceptual prerequisites that only have placeholder slugs

This is the core issue. `SCHEMA.md` currently describes `primary_dependencies` as a semicolon-delimited list of prerequisite technology slugs, which implies resolvable substrate IDs. The current CSV does not satisfy that contract consistently.

## Severity

### P1: Contract Mismatch

The `primary_dependencies` field currently looks like a resolvable graph field, but many values are placeholders rather than real profile IDs.

Examples:

- `metabolism/crude_oil_supply`
- `metabolism/industrial_distillation`
- `metabolism/precision_materials`
- `vascular/roads_and_highways`
- `immune_system/public_health_agencies`

Impact:

- graphing dependencies will produce broken edges
- any compiler or validator that assumes slug resolution will either fail or silently produce a misleading graph
- future agents cannot tell which dependencies are canonical and which are shorthand

### P1: Mixed Granularity

Some unresolved slugs are candidate future substrate profiles, while others are not really substrate rows at all.

Likely future profile candidates:

- `vascular/roads_and_highways`
- `metabolism/steam_power`
- `nervous_system/vacuum_tubes`
- `metabolism/steel_pipe`
- `immune_system/biologics_manufacturing`

Likely conceptual or non-profile placeholders:

- `immune_system/municipal_governance`
- `immune_system/public_health_agencies`
- `vascular/poles_and_rights_of_way`
- `vascular/heavy_transport`
- `nervous_system/standardized_protocols`

Impact:

- the field is currently carrying both profile IDs and abstract prerequisites
- there is no explicit way to distinguish one class from the other

### P2: Alias / Near-Duplicate Naming

Some unresolved slugs appear to be aliases or close variants of likely or existing concepts rather than cleanly chosen canonical IDs.

Examples:

- `vascular/cold_chain_logistics` vs existing profile `vascular/refrigerated_logistics_cold_chain`
- `immune_system/communications_networks` vs dependencies that likely live in `Nervous_System`
- `metabolism/construction_materials` as a broad catch-all rather than a distinct substrate row

Impact:

- even if future profiles are added, inconsistent naming will fragment the dependency graph

## Unresolved Dependency Slugs

### Likely Future Profile Candidates

- `immune_system/biologics_manufacturing`
- `immune_system/piped_water_networks`
- `immune_system/vital_statistics`
- `metabolism/battery_power`
- `metabolism/coke_fuel`
- `metabolism/crude_oil_supply`
- `metabolism/industrial_chemicals`
- `metabolism/industrial_heat`
- `metabolism/industrial_ice_and_refrigeration`
- `metabolism/ironmaking`
- `metabolism/limestone_quarrying`
- `metabolism/precision_materials`
- `metabolism/steam_power`
- `metabolism/steam_turbines`
- `metabolism/steel_pipe`
- `nervous_system/vacuum_tubes`
- `vascular/port_infrastructure`
- `vascular/roads_and_highways`
- `vascular/warehousing`

### Conceptual Placeholders That Should Probably Not Be Treated As Canonical Slugs

- `immune_system/communications_networks`
- `immune_system/municipal_governance`
- `immune_system/public_health_agencies`
- `metabolism/aggregate_supply`
- `metabolism/construction_materials`
- `metabolism/electrical_signaling_apparatus`
- `metabolism/industrial_distillation`
- `metabolism/machine_tools`
- `metabolism/metallurgy`
- `metabolism/precision_glass`
- `metabolism/precision_instrumentation`
- `metabolism/pumping_power`
- `nervous_system/computer_architecture`
- `nervous_system/standardized_protocols`
- `vascular/fuel_distribution`
- `vascular/heavy_transport`
- `vascular/long_haul_telecom_infrastructure`
- `vascular/poles_and_rights_of_way`

### Alias / Naming Problems Requiring Normalization

- `vascular/cold_chain_logistics`

This one is especially notable because there is already an existing profile with the likely intended meaning:

- existing profile: `vascular/refrigerated_logistics_cold_chain`

## Recommended Fix Order

1. Decide the contract for `primary_dependencies`.
   Choose one of:
   - only canonical profile IDs
   - canonical profile IDs plus explicit conceptual placeholders in a separate field

2. Do not keep mixing both classes in one field.

3. Normalize alias cases first.
   Start with:
   - `vascular/cold_chain_logistics`

4. Split unresolved dependencies into:
   - `candidate future profiles`
   - `conceptual prerequisites`

5. Update `SCHEMA.md` once the contract is decided.

## Recommended Short-Term Rule

Until the schema is changed, treat `primary_dependencies` in the compiled CSV as:

- canonical profile IDs where available
- unresolved placeholders only when no canonical row exists yet

And when a placeholder is used, record that explicitly in the `notes` field rather than pretending it is already a resolvable substrate ID.
