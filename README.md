# Amazing GitHub Research Repo

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16950343.svg)](https://doi.org/10.5281/zenodo.16950343)

This tiny project showcases a clean, reproducible layout for research code using Python. It demonstrates:

* The files you should always have present to allow others to reuse and cite your project, namely a `LICENSE` and a `CITATION.cff`.
* How you should configure your `.gitignore` file to never commit potentially sensitive research data.
* How to share the project dependencies (aka requirements).
* How to instruct others on how to set up their system and how to rerun your code.
* How you can use [Issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues) and [Pull Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) to manage your project and collaborate with others.
* How you can run unit tests every time you push new code to the repository so that you can spot issues early.
* How you can safely back up your code to Zenodo whenever you create a release.
* How you can register your project on RSD to link your project to a paper and other work.

## What this code does

You shouldn't get hung up on what the code actually does, since this repository is focused on the "meta" stuff, i.e. good Research Software Management. But the code is a very simple example of a typical data science project you might come across in the wild in academia.

The code performs a quick little correlation analysis for a synthetic dataset of workers of different ages, genders, education levels, years of experience, and salary. The dataset also contains Likert-style responses on job satisfaction, mental health, and stress at work rating their job. Please note that, just as you would expect in reality, the dataset is **not** included in the repository, as it could be too sensitive to share publicly.

The code performs the following steps:

1. **Data cleaning** by removing rows with missing fields and removing participants outside the 18–70 age range.
2. **Data Analysis** by calculating Pearson correlation of `mental_health` with `job_satisfaction`, `stress_at_job`, `salary`, and `years_experience`, respectively.
3. **Data Plotting** where we get a bar chart of mean `mental_health` per `education` with side-by-side bars for `gender`.

The outputs are written to `python/outputs/` and `R/outputs/` respectively.

---

## Quick start

### 1) Get the code

```bash
git clone https://github.com/StefKirsch/amazing_github_research_repo.git
```

### 2) Create and activate a virtual environment for the dependencies

Navigate into the project folder:

```bash
cd amazing_github_research_repo
```

Create the virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

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

The outputs will be stored in:

* `python/outputs/mental_health_correlations.csv`
* `python/outputs/mental_health_by_education_gender.png`

## Continuous Integration

This repository includes **GitHub Actions** workflows that run on every push and pull. You can find the logic for that in `.github/workflows/python-tests.yml`.

You can also run the tests locally by running:

```bash
pytest -q
```

## How to create and set up your own repository this way

Like what you see? Excellent! You can very easily store and manage your own code in this way. And remember, your software project doesn't need to be fancy! Even a small script that helps others reproduce your paper's results can (and probably should) be managed this way.

Here are some step-by-step instructions on how to set up your own [FAIR](https://fair-software.nl/) and reproducible software project.

1. Start using git, ideally right from the start of your project. This is the only step in this list that has quite a learning curve and can be a little daunting at first. To get started, we recommend following the tutorial from the [Turing Way](https://book.the-turing-way.org/reproducible-research/vcs).
2. If you haven't already, create a [GitHub account](https://book.the-turing-way.org/collaboration/github-novice/github-novice-firststeps). We also recommend [anonymizing](https://docs.github.com/en/account-and-profile/how-tos/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address) your commit e-mail address.
3. Create a `.gitignore` file and configure it so that you don't commit any large or sensitive research data. This is crucial, because git and GitHub are not designed to handle large files. Also, because of the open nature of GitHub you should never put sensitive data on there! This is also why it's always important to keep a keen eye on the changes you are committing between versions.

> [!CAUTION]
> Make sure to **NEVER** commit files or data that you don't want to have on GitHub. Even when you delete these files later and commit the deletions, the files will remain somewhere in the version history and will still be pushed to the remote repository. If you are unsure, it's always better to start fresh by copying your code files into a new folder and reinitialize git. Don't worry about these slip-ups, it will happen [a lot](https://xkcd.com/1597/) in the beginning!

4. Create a new [repository on GitHub](https://book.the-turing-way.org/collaboration/github-novice/github-novice-firststeps).
5. Sync your project with the GitHub remote repository. The way you need to do this depends on whether you started with a local project or with the GitHub repository. You can find more information in [this guide](https://book.the-turing-way.org/reproducible-research/vcs/vcs-github#rr-vcs-github-online).
6. Add a `LICENSE` for your project. GitHub offers a handy [license picker](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) and you can find more information on which license to choose [here](https://choosealicense.com/).

> [!CAUTION]
> From a legal point of view, not choosing a license means that nobody except you can download, rerun, or alter your code. This prevents your code from being FAIR by definition.

7. Add a `CITATION.cff` file. You can find more information on how to populate this file [here](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files).

> [!TIP]
> If you have a `LICENSE` and `CITATION.cff` file in the root of your repository's file structure, GitHub will automatically add links in the sidebar of your project's page. Nice!

8. Enable the dependency management technique of choice that is compatible with your programming language of choice. You can find some tips to get you started [here](https://gitlab.uvt.nl/coding-caf/dependency-management).

> [!TIP]
> You should not commit and push your entire virtual environment. Instead, you should generate and share the instructions to build the environment in the form of a `requirements.txt` (Python) or a `renv.lock` (R) file.

9. Write a nice README.md for your project and include the instructions on how to download your code, recreate the dependencies, and run your code.

> [!TIP]
> Since the license for reusing your code and the instructions on how to cite it are neatly tucked away in the specialized files we created earlier, you don't need to mention those things again in your README.

10. Start working with Issues (even when you are working alone) and [Pull Requests](https://www.atlassian.com/blog/git/written-unwritten-guide-pull-requests) (as soon as you are working together with others).

> [!TIP]
> You can auto-close Issues by mentioning `Closes #[issue number]` in the body of your commit message.

> [!TIP]
> Issues and Pull Requests are not only super useful for yourself and your team, but also offer the community a way to give feedback and ask questions on your work. For example, check out a project like [pandas](https://github.com/pandas-dev/pandas/issues) that has thousands of Issues and Pull Requests submitted by the community.
> 
> This means that you can also submit issues on open source software that you are working with yourself! You will be surprised how often you will get a swift reply to your questions from the maintainers of these projects.
> 
> And by the way, if you find a bug in an open source project, you can even suggest a fix yourself by opening an issue, forking the repository, and then working in your own copy of it. Find out more [here](https://github.com/gabrieldemarmiesse/getting_started_open_source).

11. Add [unit tests](https://book.the-turing-way.org/reproducible-research/testing.html) to your code and set up [GitHub Actions](https://book.the-turing-way.org/reproducible-research/ci/ci-github-actions). An AI chatbot of your choice is a great way to set up those actions.

12. Link your repository to [Zenodo](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content) to get a DOI for your software.

> [!TIP]
> Check out the source code of this README to see how you can embed the Zenodo DOI in your own README.

13. Register your project in the [Research Software Directory](https://research-software-directory.org/documentation/users/adding-projects/).

What you find in this repository is (or rather should be) very much the bread and butter of effective and professional research software management. Even if you only have a small piece of code that meaningfully contributes to your research output, you can follow the formula above! 🙌

## Extra bits

Believe it or not, GitHub has many more features that are perfect for research projects. GitHub Actions are extremely versatile and they offer a lot of freedom. On top of that, you can host your own static website with GitHub Pages. Check out the [CAFE Playbook](https://github.com/code-cafes-nl/cafe_playbook) for a nice little [example](https://code-cafes-nl.github.io/cafe_playbook/). You can even use this feature to leverage Quarto to publish your manuscripts in different formats at the same time (without changing a line of code in the source!). This is a nice little [example project](https://cwickham.github.io/manuscript-showcase/) with the source being available [here](https://github.com/cwickham/manuscript-showcase).

## Statement of AI use

The above text and software code in this repository has been generated and/or refined using chatGPT 5. All AI-output has been verified for correctness, 
accuracy and completeness, adapted where needed, and approved by the author. The author takes responsibility for any mistakes and inaccuracies.