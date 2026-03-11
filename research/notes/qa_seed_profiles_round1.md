# Seed Profile QA Round 1

This note records the first adjudication pass over the 12 seed profiles. All profiles below are `PASS` after normalization of the few disputed boundaries that were too loose in the initial draft.

## PASS

- `metabolism/electricity`
  Notes: kept separate from `metabolism/electric_grid`; retained `1831` invention and `1882` U.S. commercial launch.

- `metabolism/electric_grid`
  Notes: retained `1882` for both invention and U.S. commercial launch because the practical grid and paid service network coincide at Pearl Street.

- `metabolism/oil_refining`
  Notes: retained `1854` invention and `1859` U.S. commercial launch; kerosene-era vs motor-fuel-era refinement remains a later analytical split, not a blocker.

- `metabolism/bessemer_steel`
  Notes: retained `1856` invention and `1865` U.S. commercial launch; `1864` remains a minor normalization alternative in the profile notes.

- `nervous_system/telegraph`
  Notes: normalized U.S. commercial launch from `1844` to `1845` so T0 reflects paid public/company operation rather than the government demonstration line.

- `nervous_system/telephone`
  Notes: retained `1876` invention and `1878` U.S. commercial launch; `1877` company formation remains a precursor milestone only.

- `nervous_system/semiconductors`
  Notes: retained `1947` invention and `1951` U.S. commercial launch; `1954` remains a later normalization alternative, but not strong enough to displace the current T0.

- `nervous_system/internet`
  Notes: normalized U.S. commercial launch from `1989` to `1991` to align with NSF's explicit public/commercial opening boundary.

- `vascular/railroads`
  Notes: retained `1830` for both invention and U.S. commercial launch within the repo's U.S.-scoped substrate framing.

- `vascular/containerization`
  Notes: retained `1956` for both invention and U.S. commercial launch; later ISO standardization is treated as a maturity milestone, not T0.

- `immune_system/municipal_sanitation`
  Notes: tightened the boundary to `1855` invention and `1856` U.S. public deployment, anchored to Chicago's comprehensive sewer planning and buildout.

- `immune_system/vaccination_infrastructure`
  Notes: normalized both invention and U.S. commercial launch to `1962`, tied to the Vaccination Assistance Act and CDC grant-backed delivery system.

## Corrections Applied During QA

- `telegraph`: moved T0 to `1845`
- `internet`: moved T0 to `1991`
- `municipal_sanitation`: split invention `1855` from T0 `1856`
- `vaccination_infrastructure`: moved T0 to `1962`

## Compile Decision

All 12 profiles are eligible for inclusion in the first `data/processed/substrates_master.csv`.
