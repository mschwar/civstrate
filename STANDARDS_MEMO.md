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
