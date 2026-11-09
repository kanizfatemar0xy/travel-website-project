# WanderGallery — Responsive Travel Website & Developer Portfolio

**[Live travel website](https://kanizfatemar0xy.github.io/travel-website-project/)** · **[Developer portfolio](https://kanizfatemar0xy.github.io/travel-website-project/portfolio.html)** · **[Portfolio project index](PORTFOLIO.md)**

[![Static site checks](https://github.com/kanizfatemar0xy/travel-website-project/actions/workflows/site-checks.yml/badge.svg)](https://github.com/kanizfatemar0xy/travel-website-project/actions/workflows/site-checks.yml)

A responsive, accessible-by-design frontend demonstration built by **Kaniz Fatema Roxy**. The repository also hosts my developer portfolio, which links to Python, data analysis, research, web and Android projects.

## What you'll find

| Page | What it shows | Link |
| --- | --- | --- |
| Travel gallery | Responsive cards, photos and destinations | [Open live website](https://kanizfatemar0xy.github.io/travel-website-project/) |
| Developer portfolio | Skills, selected projects, live demos and contact links | [View portfolio](https://kanizfatemar0xy.github.io/travel-website-project/portfolio.html) |
| Project index | Technical descriptions and links to source, tests and caveats | [Read PORTFOLIO.md](PORTFOLIO.md) |
| GitHub profile template | An introduction prepared for the GitHub profile README | [View template](PROFILE_README_TEMPLATE.md) |

## Technologies

HTML5 · CSS3 · responsive layout · semantic landmarks · keyboard navigation · GitHub Pages · Python standard-library site tests · GitHub Actions.

## Run locally

No backend or credentials are required. Open `index.html` or serve the directory:

```bash
python -m http.server 8000
```

Then open http://localhost:8000 for the travel site, or http://localhost:8000/portfolio.html for the portfolio.

To run automated source checks, **open a separate terminal** in the same directory and execute:

```bash
python -m unittest discover -s tests -v
```

The workflow checks local navigation, image files, basic accessibility markup and the absence of unsafe demo forms. Visual QA, browser/device coverage and professional accessibility audits have not been completed.

## Scope and attribution

The travel gallery is a student **frontend demonstration only**. It does not book travel, process payment or store user information. Illustrative images were retained from the original exercise; image permissions should be checked before commercial reuse.

**Developer:** [Kaniz Fatema Roxy](https://github.com/kanizfatemar0xy) · [LinkedIn](https://www.linkedin.com/in/kaniz-fatema-roxy)
