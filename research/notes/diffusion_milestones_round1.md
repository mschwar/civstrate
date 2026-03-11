# Diffusion Milestones Round 1

## Objective

Begin filling defensible `t10_years`, `t25_years`, `t50_years`, and `t75_years` for the current 12 seed profiles without forcing weak estimates into the dataset.

The rule is simple:

- fill milestone fields only when one defensible series can support them
- leave milestone fields blank when the metric, denominator, or source history is too weak

## Method Rules

Use this method for every profile:

1. Freeze one canonical series.
2. Use the same series for all milestone thresholds on that profile.
3. Prefer national U.S. series over local examples.
4. Use direct adoption where possible.
5. Use equivalent exposure only when direct adoption is not meaningful.
6. If the peak or practical saturation point is unstable, leave milestones blank.
7. Record the chosen series and caveat in the profile notes before compiling values into the CSV.

## Priority Tiers

### Tier 1: Fill First

These are the best initial milestone candidates because they have clearer denominators and stronger U.S. historical series.

| Profile | Recommended milestone series | Likely source families | Why first |
| --- | --- | --- | --- |
| `metabolism/electric_grid` | household electrification or customer connection share | Historical Statistics of the United States, Census, DOE | Strong national diffusion history and clear denominator |
| `nervous_system/telephone` | telephones per 100 population or household penetration | Historical Statistics of the United States, Census | Classic adoption curve with strong historical coverage |
| `vascular/railroads` | route miles first, freight ton-miles second | Historical Statistics, DOT, railroad histories | Early national scaling data is relatively tractable |
| `immune_system/municipal_sanitation` | urban population served by sewerage | public-health histories, Census, infrastructure histories | Strong adjacency to the current sanitation profile |
| `immune_system/vaccination_infrastructure` | childhood schedule coverage | CDC historical immunization reports | Modern enough to have clearer national coverage series |
| `nervous_system/internet` | household or adult internet access share | NTIA, Census, Pew, NSF context | Late start date and clearer modern access series |

### Tier 2: Fill If Tier 1 Stabilizes

These are doable, but the series and denominator choice need more judgment.

| Profile | Recommended milestone series | Likely source families | Main difficulty |
| --- | --- | --- | --- |
| `metabolism/electricity` | retail electricity sales per capita or household electrification | Historical Statistics, DOE, Census | overlaps with `electric_grid`, so scope must stay clean |
| `vascular/containerization` | TEUs handled in U.S. ports | MARAD, port statistics, trade histories | TEUs are strong later, weaker for early normalization |
| `nervous_system/telegraph` | line miles or message volume | Historical Statistics, telecom histories | adoption threshold is less intuitive than household technologies |
| `metabolism/oil_refining` | refining capacity or throughput | EIA, historical energy statistics | capacity is strong, but “adoption” is really industrial exposure |

### Tier 3: Likely Leave Blank For Now

These should not be forced in the first milestone pass.

| Profile | Why defer |
| --- | --- |
| `metabolism/bessemer_steel` | the process itself was later superseded, so milestone interpretation is unstable |
| `nervous_system/semiconductors` | indirect GDP exposure is the right lens, but the milestone method is not yet stable enough |

## Recommended Working Order

1. `metabolism/electric_grid`
2. `nervous_system/telephone`
3. `immune_system/municipal_sanitation`
4. `immune_system/vaccination_infrastructure`
5. `vascular/railroads`
6. `nervous_system/internet`
7. `metabolism/electricity`
8. `vascular/containerization`
9. `nervous_system/telegraph`
10. `metabolism/oil_refining`
11. `metabolism/bessemer_steel`
12. `nervous_system/semiconductors`

This order moves from:

- cleaner denominators to messier ones
- direct adoption to equivalent exposure
- likely-fill rows to likely-defer rows

## Output Rules

For each profile worked in this round:

- add the chosen series to the profile notes or evidence pack
- fill milestone years only if the threshold calculation is defensible
- if not defensible, leave the CSV blanks and write a one-line reason in the profile or evidence note

## Done Condition For Round 1

Round 1 is done when:

- Tier 1 has been attempted fully
- any filled milestones are source-backed and reproducible
- any deferred milestones are explicitly deferred, not silently ignored
- the CSV can be regenerated with the new milestone fields through the compiler
