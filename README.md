# Amazing GitHub Research Repo (Dummy Project)

This tiny project showcases a clean, reproducible layout for research code using **both Python and R**. It demonstrates:

- A single dataset (`data/survey_data.csv`)
- One core **cleaning function** in each language
- A handful of simple analyses (correlations and a grouped bar plot)
- **Unit tests** that run automatically on GitHub Actions
- Lightweight **environment management** (Python `venv` + `requirements.txt`; R `renv` + `renv.lock`)

## What it does
1. **Cleans data** (remove rows with missing fields; keep ages 18–70 inclusive).
2. **Correlations**: Pearson correlation of `mental_health` with available variables among
   `job_satisfaction`, `stress_at_job`, `salary`, `years_experience`.
3. **Plot**: Bar chart of mean `mental_health` per `education` with side‑by‑side bars for `gender`.

Outputs are written to `python/outputs/` and `R/outputs/` respectively.

---

## Quick start

### 1) Get the code
```bash
# clone your repo (example)
git clone <your-repo-url>.git
cd <your-repo>
````

### 2) Python environment (via `venv`)

```bash
python -m venv .venv
# Activate
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate

pip install -r requirements.txt

# Run the Python analysis
python python/src/analysis.py
```

Outputs:

* `python/outputs/mental_health_correlations.csv`
* `python/outputs/mental_health_by_education_gender.png`

### 3) R environment (via `renv`)

Open the `.Rproj` in RStudio **or** run in R:

```r
install.packages("renv")
renv::restore()  # uses renv.lock to install deps

# Run the R analysis from project root
source("R/src/analysis.R")
```

Outputs:

* `R/outputs/mental_health_correlations.csv`
* `R/outputs/mental_health_by_education_gender.png`

---

## Continuous Integration

This repo includes **GitHub Actions** workflows that run on every push / pull request:

* `python-tests.yml` runs Python unit tests with `pytest`.
* `r-tests.yml` runs R unit tests with `testthat` and `renv::restore()`.
