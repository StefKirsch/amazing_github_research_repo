[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16950343.svg)](https://doi.org/10.5281/zenodo.16950343)

# Amazing GitHub Research Repo

This tiny project showcases a clean, reproducible layout for research code using Python. It demonstrates:

- The files you should always have present to allow others to reuse and cite your project, namely a `LICENSE` and a `CITATION.cff`.
- How you should configure your `.gitignore` file to never commit potentially sensitive research data.
- How to share the project dependencies (aka requirements).
- How to instruct other on how to set up their system and how to rerun your code.
- How you can use [Issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues) and [Pull Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) to manage your project and collaborate with others.
- How you can run unit tests every time you push new code to the repository so that you can spot issues early.
- How you can safely back up your code to Zenodo whenever you create a release.
- How you can register your project on RSD to link your project to a paper and other work.

## What this code does

You shouldn't get hung up on what the code actually does, since this repository focused on the "meta" stuff, i.e. good Research Software Management. But the code is a very simple example of a typical data science project you might come across in the wild in academia.

The code performs a quick little correlation analysis for a synthetic dataset of workers of different ages, genders, education levels, years of experience and salary. The dataset also contains Likert-style responses on job satisfaction, mental health and stress at work rating their job. Please note that, just as you would expect in reality, the dataset is **not** included in the repository, as it could be too sensitive to share publicly.

The code performs the following steps

1. **Data cleaning** by removing rows with missing fields and removing participants outside the 18–70 age range.
2. **Data Analysis** by calculating Pearson correlation of `mental_health` with `job_satisfaction`, `stress_at_job`, `salary`, `years_experience`, respectively.
3. **Data Plotting** where we get a bar chart of mean `mental_health` per `education` with side‑by‑side bars for `gender`.

The outputs are written to `python/outputs/` and `R/outputs/` respectively.

---

## Quick start

### 1) Get the code

```bash
git clone https://github.com/StefKirsch/amazing_github_research_repo.git
```

### 2) Create and activate a virtual environment for the dependencies

Navigate into the project folder

```bash
cd amazing_github_research_repo
```

Create the virtual environment

```bash
python -m venv .venv
```

Activate the environment

#### Windows

```bash
.venv\\Scripts\\activate
```

#### macOS/Linux

```bash
source .venv/bin/activate
```

### 3) Install the dependencies

```bash
pip install -r requirements.txt
```

### 4) Run the analysis

```bash
python python/src/analysis.py
```

The outputs will be stored in

- `python/outputs/mental_health_correlations.csv`
- `python/outputs/mental_health_by_education_gender.png`

## Continuous Integration

This repository includes **GitHub Actions** workflows that run on every push and pull. You can find the logic for that in `.github/workflows/python-tests.yml`.

You can also run the tests locally by running

```bash
pytest -q
```
