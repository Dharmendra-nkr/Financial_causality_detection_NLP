# Phase 5 Ablation Study Report
## Financial Causality Detection — Multimodal FinBERT

---

## 1. Overview

This report documents the **ablation study** conducted in Phase 5 of the Financial Causality Detection project. The goal is to quantify the contribution of each architectural component of the **EnhancedMultimodalFinBERT** model by systematically removing or replacing individual modules and measuring the impact on classification performance.

All experiments were conducted on Google Colab using a **Tesla T4 GPU**. The dataset consists of financial news articles along with numerical financial features (e.g., stock-related statistics).

---

## 2. Baseline Model: `EnhancedMultimodalFinBERT`

The full baseline model integrates:

| Component | Description |
|---|---|
| **Text Encoder** | `yiyanghkust/finbert-tone` (pretrained FinBERT) |
| **Attention Pooling** | Learnable attention over token outputs (replaces CLS-only pooling) |
| **Numerical Branch** | Two-layer MLP processing scaled numerical features |
| **Fusion Gate** | Sigmoid-gated combination of text and numerical representations |
| **Classifier Head** | Linear layer → output logits |

Numerics were scaled using a fitted `StandardScaler`. The model was trained and evaluated on a held-out test split (split by date: `split_date` cutoff).

---

## 3. Ablation Variants

| Model | Description |
|---|---|
| `EnhancedMultimodalFinBERT` | **Baseline** — full multimodal model with attention pooling & fusion gate |
| `TextOnlyFinBERT` | Text encoder + attention pooling; **no numerical branch** |
| `NumericalOnlyClassifier` | MLP on numerical features only; **no text** |
| `MultimodalNoGate` | Multimodal (text + numeric) but **no fusion gate** (simple concatenation) |
| `MultimodalCLSPooling` | Multimodal with **CLS token pooling** instead of attention pooling |

---

## 4. Results

### 4.1 Full Results Table (from `phase5_ablation_robustness_results.csv`)

| Experiment | Model / Variant | Accuracy | F1 Score | Precision | Recall | AUC |
|---|---|---|---|---|---|---|
| Component Ablation | Baseline (Full Multimodal) | **0.8729** | **0.8750** | 0.8801 | 0.8729 | **0.9533** |
| Component Ablation | No Attention Pooling (CLS) | 0.8661 | 0.8682 | 0.8746 | 0.8661 | 0.9498 |
| Component Ablation | No Fusion Gate | 0.8653 | 0.8677 | 0.8737 | 0.8653 | 0.9484 |
| Component Ablation | No Numerical Branch | 0.8579 | 0.8601 | 0.8690 | 0.8579 | 0.9441 |
| Architectural Ablation | Text Only | 0.8576 | 0.8594 | 0.8683 | 0.8576 | 0.9447 |
| Architectural Ablation | Numerical Only | 0.4101 | 0.3652 | 0.6671 | 0.4101 | 0.5701 |

---

### 4.2 Component Ablation Analysis

**Removing the Numerical Branch** has the largest single-component impact, reducing F1 by ~1.5 percentage points (0.8750 → 0.8601). This confirms that numerical features carry complementary information beyond what can be extracted from text alone.

**Removing the Fusion Gate** (reverting to simple concatenation) reduces F1 by ~0.7 pp (0.8750 → 0.8677). The gate dynamically balances text and numerical signals; without it, the model loses this adaptive weighting capability.

**Replacing Attention Pooling with CLS Pooling** reduces F1 by ~0.7 pp (0.8750 → 0.8682). Attention pooling aggregates contextual representations across all tokens, capturing richer sentence-level semantics than the single CLS token.

---

### 4.3 Architectural Ablation Analysis

**Text-Only Model** achieves F1 = 0.8594, confirming that financial text (processed by FinBERT) is the dominant signal for causal classification. The 1.6 pp gap vs. the full multimodal model demonstrates the added value of integrating numerical features.

**Numerical-Only Model** achieves F1 = 0.3652 and AUC = 0.5701, barely above random. This shows that numerical financial features alone are insufficient for causal event detection — the task is fundamentally language-driven.

---

## 5. Summary of Component Contributions

| Component Removed | ΔF1 vs. Baseline | Interpretation |
|---|---|---|
| Numerical Branch | −0.0149 | Numerics add meaningful complementary signal |
| Fusion Gate | −0.0073 | Adaptive gating improves text–numeric fusion |
| Attention Pooling | −0.0068 | Token-level attention captures richer context |

> **Key Takeaway:** Every architectural component contributes to final performance. The numerical branch has the largest individual impact, followed by the fusion gate and attention pooling, both of roughly equal importance.

---

## 6. Experimental Setup

| Parameter | Value |
|---|---|
| GPU | Tesla T4 (Google Colab) |
| Base Text Model | `yiyanghkust/finbert-tone` |
| Max Sequence Length | 128 tokens |
| Batch Size | 64 |
| Numerical Features | Financial statistics (scaled via `StandardScaler`) |
| Optimizer | AdamW |
| Evaluation | Accuracy, Macro F1, Precision, Recall, AUC-ROC |

---

*Report generated from Phase 5 Colab notebook and `phase5_ablation_robustness_results.csv`.*
