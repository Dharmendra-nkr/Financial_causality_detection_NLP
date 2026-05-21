# Financial Causality Detection NLP

This repository contains the code, notebooks, datasets, and results for a financial causality detection project built around a multimodal FinBERT pipeline. The work progresses through multiple phases, ending with a Phase 5 Colab workflow that evaluates the model, runs ablation studies, and measures robustness under several perturbation settings.

## Project Scope

The main goal of the project is to detect causal relationships in financial text by combining:

- Financial news text encoded with FinBERT
- Numerical financial features
- Multimodal fusion for classification
- Ablation and robustness analysis for model validation

## Repository Layout (organized)

- `notebooks/` - all Jupyter notebooks (Phase notebooks, `flow.ipynb`, Colab variants)
- `scripts/` - Python helper scripts (e.g., `convert_to_colab.py`)
- `docs/` - user-facing documentation and quick-start guides (`COLAB_QUICK_START.md`, `Google_Colab_Setup_Instructions.md`, flowchart)
- `results/` - experiment output and figures (Phase 5 results are under `results/phase5`)
- `model_extracted/` (LOCAL ONLY) - extracted model checkpoint directory (not tracked by git)

Files that were previously in the repository root have been moved into the folders above to keep code and results separated and make navigation easier.

## Phase 5 Outputs

See `results/phase5/` for the Phase 5 artifacts (reports, CSVs, and plots):

- `ablation_report.md`
- `robustness_report.md`
- `phase5_ablation_robustness_results.csv`
- `ablation_comparison.png`
- `robustness_sensitivity_curves.png`
- `robustness_heatmap.png`
- `Phase_5_Colab.ipynb`

## Key Findings

The Phase 5 experiments show that:

- The full multimodal model performs best overall.
- The numerical branch contributes meaningful complementary signal.
- Fusion gating and attention pooling both improve performance.
- The model is most sensitive to word dropout and temporal distribution shift.
- Text remains the dominant modality, while numerical features provide supporting information.

## Colab Workflow

To run the Phase 5 notebook on Google Colab:

1. Upload `label_shifted_fin_causality_dataset.csv` and the model archive to Google Drive.
2. Open `Phase-5_Colab.ipynb` in Colab.
3. Mount Google Drive and set the runtime to GPU.
4. Run the notebook cells in order.

For step-by-step instructions, see:

- `COLAB_QUICK_START.md`
- `Google_Colab_Setup_Instructions.md`

## Notes

- Large artifacts (model checkpoints and full datasets) are kept locally and are excluded from the git repo. See `.gitignore` for excluded patterns.
- If you want to publish the model or datasets, use Git LFS, attach them to a GitHub Release, or store them in cloud storage (Google Drive/Dropbox) and add download instructions to `docs/`.

If you'd like, I can:

1. Move the local model artifacts to `artifacts/` (outside git) and add a small loader script.
2. Configure Git LFS for the model files and re-add them to the repo.
3. Create a short `docs/README-models.md` describing where to find the model and how to re-create the ZIP.

Tell me which option you prefer or if you want me to proceed with one of them.

## Recommended Start Point

If you want the latest end-to-end workflow, start with `Phase-5_Colab.ipynb` and the reports in `collab_results_phase_5/`.
