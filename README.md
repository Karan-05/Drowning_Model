# Drowning Detection System

A cleaned up snapshot of my LRCN (Long-term Recurrent Convolutional Network)
based drowning detection project. The repository now bundles the original
reports, demo photos and research notebook in a tidy structure, plus a helper
script for painting the initials **KA** on a GitHub contribution graph.

## Repository layout

- `notebooks/drowning_detection_lrcn.ipynb` – end-to-end experiments for
  training and evaluating the LRCN model on pool surveillance footage.
- `docs/` – the supporting research reports (DOCX/PDF) that explain the problem
  framing, dataset collection and model design choices.
- `media/reference_photos/` – reference stills from the recorded drowning
  simulations, renamed sequentially for easier browsing.
- `scripts/ka_commit_art.py` – utility to generate backdated commits that draw
  "KA" on the GitHub contribution heatmap.

## Getting started

1. Create a virtual environment (Python 3.9+ recommended) and install the
   dependencies you need for running the notebook (TensorFlow / PyTorch,
   OpenCV, NumPy, etc.). The exact framework mix depends on how you want to
   re-run the experiments, so use the versions that work best on your machine.
2. Launch JupyterLab or VS Code, open
   `notebooks/drowning_detection_lrcn.ipynb`, and step through the workflow:
   preprocessing → sequence generation → LRCN training → evaluation.
3. The `docs/` folder contains narratives and diagrams that complement the
   notebook.

## Painting "KA" on your contribution graph

Use `scripts/ka_commit_art.py` to create a KA monogram using backdated empty
commits. The script purposely works with any repo so you can paint on a
throwaway clone.

```bash
python scripts/ka_commit_art.py \
  --repo /path/to/repo \
  --start-date 2023-05-14 \
  --message "KA art" \
  --intensity 3
```

- `--start-date` must be the Sunday for the top-left cell where you want the K
  to begin. Adjust it (±7 days) until the design sits inside the current
  52-week window on GitHub.
- `--intensity` controls how dark each lit cell becomes (more commits → darker
  green). Keep it between 1 and 10.
- Add `--dry-run` if you want to preview the dates before creating commits.

After the script finishes run `git push` to sync with GitHub, wait ~1 minute and
refresh your contributions page – "KA" should now be proudly displayed.
