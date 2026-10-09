# Global Groundwater Geotoxicity — reproducible research evidence

**Status: curated GitHub staging package; not yet approved for public release.**

This repository supports the Geoscience Frontiers groundwater geotoxicity systematic review (As, F, U, Cr). It consolidates the verified code-generated country research-evidence map with a *minimal* selection of screening, audit and synthesis artifacts from `D:\Water`.

## Included
- `src/`: reproducible Python/Matplotlib code for the integrated global country evidence map.
- `data/GSF_Geography_Country_ResearchIntensity_v1.csv`: frozen country-level research counts (86 entries).
- `data/screening/PRISMA_TITLE_ABSTRACT_FREEZE_SUMMARY.csv`: title/abstract screening summary.
- `data/synthesis/`: four preserved synthesis workbooks (overlap/effects, quantitative-SPM bridge, 892-record domain synthesis, final table/figure specifications).
- `audits/`: summary of the secondary source verification attempt.
- `figures/`: code-generated map (PNG 600dpi, PDF, SVG) and seven historical figure exports, retained for comparison, **not certified as final manuscript figure numbering**.
- `basemap/`: Natural Earth country polygons; **not global aquifer boundaries**.
- `tests/`: country counts, screening summary, and file checksum verification.
- `selection_manifest.csv`: historical selection manifest retained for provenance; its original checksums may differ from current release files.
- `release_manifest_v1.0.0.csv`: current release inventory, file sizes, SHA-256 checksums and provenance categories.

## What the data mean
The 892-record analytical subset is **not** the final review-wide included-study count. The 756 country-counting eligible records underpin the map. Country counts are research-intensity evidence, not contaminant concentration, aquifer risk, exceedance prevalence or groundwater stress. Contaminant categories overlap within publications. Pie sectors are normalised contaminant representations, not mutually exclusive study or sample percentages.

## Not included and why
- 10,260- and 11,280-record bibliographic reconciliation masters and screening ledger: large source metadata and abstract reuse requires rights/provenance review.
- 892-record geography master and 46-record overlap gate: record-level metadata and abstracts require a separate sharing decision.
- Duplicate or provisional figures, copyrighted source PDFs, manuscript drafts and unrelated ArticleC files.

The workbooks and source figure exports are preserved but **scientific consistency and redistribution clearance remain pending**. This repository reproduces the map, **not** the complete screening or quantitative synthesis pipeline. No WHYMAP aquifer polygon layer has been incorporated.

## Reproduce the map
```bash
python -m pip install -r requirements.txt
python src/build_gsf_integrated.py
python tests/check_data.py
python tests/check_package.py
```
Outputs: `figures/GSF_Integrated_Global_Evidence_Code_600dpi.{png,pdf,svg}`.
The `check_data.py` test validates selected country-data invariants
and the existence of the three generated map exports.

The `check_package.py` test validates file sizes and SHA-256
checksums against `release_manifest_v1.0.0.csv`.

These tests do not independently reproduce the complete PRISMA
screening, source verification, dataset-independence adjudication,
or quantitative synthesis.

## Licensing and citation
The MIT licence applies to original software only; it does **not** override source-data or figure rights. Natural Earth geography is public domain (https://www.naturalearthdata.com/about/terms-of-use/). Citation metadata are provisional pending journal publication.
