# Research Standards & Adjudication Rules

To prevent AI hallucination and ensure rigorous historical data, all agents must adhere to the following standards:

## 1. Defining "Invention" vs. "Commercial Launch (T0)"
* **Invention:** Must be a *working prototype or practical demonstration*, not merely a theoretical paper or scientific discovery. (e.g., Nuclear power invention is the first artificial fission reactor, not Einstein's E=mc^2).
* **T0 (Commercial Launch):** Must be the year ordinary citizens, firms, or municipalities in the U.S. could *purchase or utilize* the technology. A lab demo does not count. 

## 2. Direct vs. Indirect Adoption
If a technology is a component (e.g., Semiconductors, Electric Grid, Portland Cement), do not track direct consumer ownership. 
* *Incorrect:* "Consumers who own a semiconductor."
* *Correct:* "U.S. GDP exposure to semiconductor-dependent sectors" OR "Input-Output capital stock of IT equipment."

## 3. Sourcing Hierarchy
All date and metric claims must prioritize:
1. U.S. Statistical Abstract (Historical statistics).
2. Bureau of Economic Analysis (BEA) Input-Output tables.
3. Authoritative institutional histories (e.g., IEEE, DOE, Santa Fe Institute, NBER).

## 4. Dispute Logging
If historical consensus is split (e.g., "Who invented the radio?"), agents must log both dates in their scratchpad, select the most defensible U.S.-relevant date, and write a 1-sentence justification.

## 5. Substrate Inclusion Cutoff
To qualify as an in-scope substrate, a candidate technology must satisfy all three gate conditions:

1. **Post-1800 Practicality:** It has a workable invention date after 1800 and a defensible U.S. commercial or public deployment date.
2. **Measurable U.S. Reach:** It has a plausible U.S. adoption, exposure, capacity, or infrastructure metric that can be sourced from authoritative records.
3. **System-Layer Role:** It functions as an enabling layer for production, logistics, coordination, computation, or public health capacity rather than as a branded product, a short-lived feature, or a pure scientific discovery.

If the gate conditions are met, include the technology only if it also passes at least **three of the following five tests**:

1. **Cross-Sector Impact:** It materially changes how multiple industries, municipalities, or households operate.
2. **Dependency Depth:** Later technologies or institutions clearly depend on it.
3. **Durability:** It remains relevant for at least two decades or permanently alters the architecture of the system.
4. **Substrate Character:** It is infrastructure, a critical material, a coordination layer, or a health-capacity layer rather than a downstream consumer application.
5. **Analytical Separability:** It can be analyzed as a distinct substrate rather than a minor feature of a parent substrate.

### Default Exclusions
- branded end-user products
- narrow industrial methods that do not create broader dependency chains
- pure scientific discoveries without deployment
- short-lived interface standards or protocols that are better treated as components of a larger substrate
- firm-specific services that do not become economy-wide enabling layers

### Protocol And Standard Exception
Protocols, standards, and coordination rules may be included only when they operate as a durable, economy-scale substrate in their own right and can be measured as such. Otherwise, capture them inside the parent technology profile instead of creating a standalone row.

## 6. Citation And Evidence Format
Profiles should use the citation pattern seen in the newest Google DeepMind white papers:

- numbered citations inline in the prose
- a numbered `References` section at the end of the profile
- numbering based on citation order
- stable URLs for reports, papers, and web sources when available

Example claim style:

- The electric grid diffused more slowly than consumer electronics because it required coordinated physical rollout across utilities and municipalities [1, 2].

Repo decision:
To keep adjudication local to each technology, the project stores these references directly in each profile instead of relying on a separate global bibliography during Phase 1.

## 7. Diffusion Milestone Methodology (T10, T25, T50, T75)

To ensure comparability and rigor, agents must calculate the years to reach 10%, 25%, 50%, and 75% adoption thresholds using these standardized steps:

### 1. Select a Canonical Series
*   **Single-Source Rule:** Use exactly one time-series for all four milestone thresholds. Do not "stitch" multiple series together unless they are historically reconciled.
*   **National Scope:** Prioritize U.S. national-level series (e.g., U.S. Statistical Abstract, Census).
*   **Denominator Alignment:** The series must use the same `denominator` (Households, Population, etc.) defined in the profile metadata.

### 2. Define the Adoption Metric
*   **Direct Adoption:** For consumer-facing or household infrastructure, use the percentage of the denominator that has adopted or is connected (e.g., % of households).
*   **Exposure / Capacity:** For industrial substrates, use the share of total sector output, capacity, or work performed (e.g., % of total freight ton-miles).

### 3. Determine the Milestone Year
*   **First Crossing:** The milestone year is the **first calendar year** in which the recorded value meets or exceeds the threshold (10%, 25%, 50%, or 75%).
*   **Observation vs. Interpolation:** Use the first observed year in the source data. If data is sparse, do not interpolate; record the first observed year above the threshold and note the data gap.
*   **T0 Boundary:** A milestone year must be greater than or equal to the `us_commercial_launch_year` (T0).

### 4. Calculate "Years Since Launch"
*   The fields `t10_years`, `t25_years`, etc., store the **number of years** since the `us_commercial_launch_year`.
*   *Formula:* `Milestone Year - us_commercial_launch_year = Threshold Year Value`.
*   *Example:* If T0 is 1900 and 10% adoption is reached in 1912, `t10_years` = 12.

### 5. Adjudication for Missing Data/Proxies
If direct adoption metrics are missing, agents may propose an indirect proxy:
*   **Justify Proxy:** Provide a clear, one-sentence justification for the chosen proxy in the profile's notes.
*   **Stability Check:** Ensure the proxy is stable across the entire diffusion period.

### 6. Peak and Supersession Rules
*   **Stable Peak:** Milestones should only be filled if the technology has a stable or predictable saturation point.
*   **Supersession:** If a technology was superseded (e.g., Bessemer Steel) before reaching a threshold, that milestone field MUST remain blank.

### 7. Documentation
*   Every filled milestone must be supported by a reference in the `## References` section.
*   Record the specific series and caveats in the `notes` field or the profile's `Diffusion Milestones` section.

## 8. Confidence Scoring Model

Every technology profile must assign a qualitative confidence score (`high`, `medium`, `low`) to its data and claims based on the following rubric:

### High Confidence
*   **Sourcing:** Supported by multiple primary or authoritative statistical sources (e.g., Census, Historical Statistics of the U.S.).
*   **Consensus:** Dates and metrics are well-established with no significant historical disputes.
*   **Metric Clarity:** Uses a direct adoption metric with a stable, well-defined denominator.
*   **Milestones:** Diffusion milestones are derived from a single, continuous, high-quality time series.

### Medium Confidence
*   **Sourcing:** Supported by at least two reliable secondary sources or one authoritative institutional history.
*   **Consensus:** Minor disputes may exist (e.g., +/- 2 years on launch), but one date is clearly more defensible for the U.S. context.
*   **Metric Clarity:** Uses a reasonable proxy for adoption or exposure where direct metrics are unavailable.
*   **Milestones:** Milestone thresholds are reached, but the series may have minor gaps or require slight normalization.

### Low Confidence
*   **Sourcing:** Relies on limited or fragmented sources with significant data gaps.
*   **Consensus:** Primary dates (Invention or T0) are highly disputed or conceptual boundaries are blurry.
*   **Metric Clarity:** Adoption metrics are purely speculative or based on very weak proxies.
*   **Milestones:** Milestones are mostly blank or based on extremely sparse observations.

*Note: If a profile is marked `low` confidence, the `notes` field MUST explain the specific data risks or historical disputes that led to the rating.*
