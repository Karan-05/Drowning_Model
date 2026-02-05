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
