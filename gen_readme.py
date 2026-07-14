#!/usr/bin/env python3
"""Generate README.md for the awesome list from papers.json."""
import json, collections, os

HERE = os.path.dirname(os.path.abspath(__file__))
rows = json.load(open(os.path.join(HERE, "papers.json")))

# 1-indexed -> row
P = {i + 1: r for i, r in enumerate(rows)}

# Category -> ordered list of paper indices (each paper appears exactly once)
CATS = [
    ("single-cell-foundation-models", "🧬 Single-cell & RNA Foundation Models",
     "Transcriptome-scale pretrained models for single-cell RNA-seq, multi-omics and mRNA sequences.",
     [76, 75, 80, 81, 77, 82, 78, 79, 84]),
    ("pathology-foundation-models", "🔬 Pathology Foundation Models (Knowledge Distillation & Multimodal)",
     "Slide-level pathology FMs built via knowledge distillation from expert vision models "
     "(GPFM) and via multimodal knowledge injection from gene expression + pathology reports (mSTAR).",
     [11, 2]),
    ("spatial-foundation-models", "🗺️ Spatial-omics Foundation Models",
     "Foundation models built natively for spatial transcriptomics / proteomics.",
     [70, 41, 35, 24]),
    ("histology-to-gene-expression", "🖼️➡️🧬 Histology → Gene Expression Prediction",
     "Predicting spatial / bulk gene expression directly from H&E whole-slide images (a.k.a. H2ST).",
     [83, 40, 85, 72, 4, 19, 27, 46, 47, 29, 61, 54, 55, 57, 51, 52, 53, 59, 56, 73]),
    ("spatial-transcriptomics-analysis", "📈 Spatial Transcriptomics Analysis",
     "Denoising, imputation, representation learning, niche & region modeling on ST data.",
     [69, 71, 18, 25, 65, 64, 63, 49, 67]),
    ("single-cell-analysis", "🔎 Single-cell Analysis & Dynamics",
     "Trajectories, gene regulatory networks, generation, perturbation and continual learning.",
     [42, 21, 32, 23, 22, 44, 66, 60, 68]),
    ("computational-pathology-wsi", "🧫 Computational Pathology (WSI)",
     "Multiple-instance learning, survival, retrieval, segmentation and image generation on slides.",
     [1, 9, 16, 17, 34, 31, 20, 3, 7, 10, 15, 58, 38]),
    ("multimodal-histo-genomics", "🔗 Multimodal Histo-Genomic Fusion & Prognosis",
     "Fusing pathology images with genomics / proteomics for molecular prediction and prognosis.",
     [8, 14, 48, 50]),
    ("agents-and-reasoning", "🤖 LLM Agents & Reasoning",
     "Agentic and reasoning systems for pathology, spatial omics and single-cell analysis.",
     [37, 30, 26, 36]),
    ("interpretability-sae", "💡 Interpretability & Sparse Autoencoders",
     "Concept discovery and mechanistic interpretability of pathology / bio foundation models.",
     [5, 28, 62, 74]),
    ("genomic-language-models", "🧩 Genomic / DNA Language Models",
     "Tokenization, representation and evaluation of DNA / genomic foundation models.",
     [43, 45]),
    ("benchmarks-datasets-tools", "🏁 Benchmarks, Datasets & Toolkits",
     "Open benchmarks, multicentric datasets and data-processing toolkits.",
     [33, 39]),
    ("surveys-and-perspectives", "📚 Surveys & Perspectives",
     "Review articles and perspectives on the field.",
     [13, 6, 12]),
]


def norm(s):
    return " ".join((s or "").split())


def is_code(url):
    return "github.com" in (url or "")


def links_md(r):
    """Render up to two badges: a paper link and a code link.

    `link` holds the primary URL (paper or code); `Git repository` may add a
    separate code repo, so an entry can show both a paper and a code badge.
    """
    link = norm(r.get("link"))
    git = norm(r.get("Git repository"))
    paper_url = "" if is_code(link) else link
    code_url = link if is_code(link) else ""
    if git and is_code(git):
        code_url = git
    parts = []
    if paper_url:
        parts.append(f"[[paper]]({paper_url})")
    if code_url:
        parts.append(f"[![code](https://img.shields.io/badge/code-black?logo=github)]({code_url})")
    return " ".join(parts) if parts else "—"


def clean_kw(r):
    """Keyword chips, dropping author/curation tags."""
    drop = {"Hao Chen", "Mahmood", "Outstanding", "Core AI", "Microsoft"}
    ks = [k.strip() for k in (r.get("Key word") or "").split(",")]
    ks = [k for k in ks if k and k not in drop]
    return ", ".join(ks)


# ---- stats ----
total = len(rows)
n_code = sum(1 for r in rows if is_code(r.get("link")))
venues = collections.Counter(r.get("Journal", "").strip() or "—" for r in rows)

out = []
out.append("# Awesome Pathology & Spatial-Omics AI [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)")
out.append("")
out.append("> A curated list of papers on **artificial intelligence for computational pathology, "
           "spatial transcriptomics, and single-cell genomics** — with a focus on "
           "**predicting gene expression from histology images (H2ST)**, multimodal "
           "histo-genomic modeling, foundation models, and biomedical reasoning agents.")
out.append("")
out.append("![papers](https://img.shields.io/badge/papers-%d-blue) "
           "![with%%20code](https://img.shields.io/badge/with%%20code-%d-brightgreen) "
           "[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-orange.svg)](CONTRIBUTING.md) "
           "[![License: CC0](https://img.shields.io/badge/License-CC0-lightgrey.svg)](LICENSE)"
           % (total, n_code))
out.append("")
out.append("Papers span venues including ICML, CVPR, ICLR, NeurIPS, AAAI, Nature / Nature Communications, "
           "Science and more (mostly 2025–2026). Each entry links to the paper or its official code. "
           "Contributions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).")
out.append("")

# ---- Contents ----
out.append("## Contents")
out.append("")
for slug, title, _desc, ids in CATS:
    out.append(f"- [{title}](#{slug}) ({len(ids)})")
out.append("")
out.append("---")
out.append("")

# ---- Sections ----
for slug, title, desc, ids in CATS:
    out.append(f'<a id="{slug}"></a>')
    out.append("")
    out.append(f"## {title}")
    out.append("")
    out.append(f"*{desc}*")
    out.append("")
    out.append("| Title | Venue | Year | Topics | Links |")
    out.append("|---|:--:|:--:|---|:--:|")
    for i in ids:
        r = P[i]
        t = norm(r.get("Title"))
        url = norm(r.get("link"))
        title_cell = f"[{t}]({url})" if url else t
        venue = r.get("Journal", "").strip() or "—"
        year = r.get("Year") or "—"
        kw = clean_kw(r)
        out.append(f"| {title_cell} | {venue} | {year} | {kw} | {links_md(r)} |")
    out.append("")
    out.append("[⬆ back to top](#contents)")
    out.append("")

# ---- Footer ----
out.append("---")
out.append("")
out.append("## Legend")
out.append("")
out.append("- **H2ST** — *Histology-to-Spatial-Transcriptomics*: predicting spatial gene expression from H&E images.")
out.append("- **WSI** — Whole-Slide Image. **FM** — Foundation Model. **SAE** — Sparse Autoencoder.")
out.append("- ![code](https://img.shields.io/badge/code-black?logo=github) marks entries with an official code release.")
out.append("")
out.append("## Contributing")
out.append("")
out.append("Found a missing paper or a broken link? Please open a pull request or issue. "
           "See [CONTRIBUTING.md](CONTRIBUTING.md) for the entry format.")
out.append("")
out.append("## License")
out.append("")
out.append("[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](LICENSE)")
out.append("")
out.append("To the extent possible under law, the maintainers have waived all copyright and related "
           "or neighboring rights to this work.")
out.append("")

readme = "\n".join(out)
with open(os.path.join(HERE, "README.md"), "w") as f:
    f.write(readme)

# sanity: every paper used exactly once
used = [i for _, _, _, ids in CATS for i in ids]
assert sorted(used) == list(range(1, total + 1)), \
    f"coverage mismatch: dup={ [x for x in used if used.count(x)>1] } missing={ set(range(1,total+1))-set(used) }"
print(f"README.md written: {len(readme)} chars, {total} papers, all covered once.")
print("Venues:", dict(venues.most_common()))
