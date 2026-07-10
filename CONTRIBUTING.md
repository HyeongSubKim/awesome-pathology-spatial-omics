# Contributing

Thanks for helping keep this list useful and up to date!

## How to add a paper

1. Find the right section in [`README.md`](README.md) (or propose a new one if none fits).
2. Add a row to that section's table, keeping entries roughly newest-first:

   ```
   | [Paper Title](paper-or-code-url) | Venue | Year | topic1, topic2 | [[paper]](url) or code badge |
   ```

3. Prefer the **official code repository** as the primary link when one exists; otherwise link the paper (arXiv / publisher / OpenReview).
4. Keep topic tags short and consistent with existing ones (e.g. `spatial transcriptomics`, `WSI`, `H2ST`, `sc RNA-seq`, `Proteomics`, `FM`, `Reasoning`).

## Regenerating the README

The `README.md` is generated from [`papers.json`](papers.json) by [`gen_readme.py`](gen_readme.py):

```bash
python3 gen_readme.py
```

You may edit `README.md` directly for small fixes, or update `papers.json` + the
category map in `gen_readme.py` and regenerate for larger changes. The generator
asserts that **every paper is assigned to exactly one category**, so it will fail
loudly if a paper is duplicated or dropped.

## Quality bar

- The paper should be relevant to AI for computational pathology, spatial
  transcriptomics, single-cell genomics, or closely related foundational ML.
- No dead links. Verify the URL resolves before submitting.
- One paper per row; no duplicates across sections.

## Pull request checklist

- [ ] Entry placed in the most relevant section
- [ ] Link resolves and points to paper or official code
- [ ] Topic tags reuse existing vocabulary where possible
- [ ] `python3 gen_readme.py` runs without error (if you touched `papers.json`)
