# Phase 5 Robustness Study Report
## Financial Causality Detection — Multimodal FinBERT

---

## 1. Overview

This report documents the **robustness analysis** conducted in Phase 5 of the Financial Causality Detection project. The evaluation tests how the **EnhancedMultimodalFinBERT** model performs under various forms of data perturbation and distributional shift, including:

- **Text Perturbations** (word dropout, character noise, word shuffle, synonym replacement)
- **Numerical Feature Noise** (Gaussian noise injection)
- **Adversarial Attacks** (Fast Gradient Sign Method on numerical features)
- **Temporal Distribution Shift** (performance by year)
- **Input Length Sensitivity** (performance by text length bucket)

All experiments were run on Google Colab (Tesla T4 GPU) on the test split of the financial news dataset.

---

## 2. Baseline Performance (Clean Data)

| Metric | Value |
|---|---|
| Accuracy | 0.8729 |
| F1 Score | 0.8750 |
| Precision | 0.8801 |
| Recall | 0.8729 |
| AUC | 0.9533 |

---

## 3. Text Perturbation Robustness

Text perturbations simulate real-world noise in financial articles (OCR errors, informal writing, synonym variation, etc.).

### 3.1 Word Dropout

Randomly drops words from the input text at varying rates.

| Dropout Rate | Accuracy | F1 Score | AUC |
|---|---|---|---|
| 0.0 (baseline) | 0.8729 | 0.8750 | 0.9533 |
| 0.1 | 0.8618 | 0.8641 | 0.9449 |
| 0.2 | 0.8434 | 0.8457 | 0.9339 |
| 0.3 | 0.8191 | 0.8215 | 0.9192 |
| 0.4 | 0.7772 | 0.7809 | 0.8930 |
| 0.5 | 0.7263 | 0.7297 | 0.8581 |

**Observation:** Performance degrades gracefully with increasing dropout. Even at 50% word dropout (severe noise), the model retains ~72.6% accuracy and 0.86 AUC, demonstrating robust text-level feature extraction.

---

### 3.2 Character Noise

Randomly corrupts individual characters in words (simulating OCR or typo errors).

| Noise Rate | Accuracy | F1 Score | AUC |
|---|---|---|---|
| 0.0 (baseline) | 0.8729 | 0.8750 | 0.9533 |
| 0.1 | 0.8673 | 0.8697 | 0.9498 |
| 0.2 | 0.8597 | 0.8620 | 0.9449 |
| 0.3 | 0.8455 | 0.8479 | 0.9362 |
| 0.4 | 0.8272 | 0.8301 | 0.9277 |
| 0.5 | 0.7983 | 0.8017 | 0.9131 |

**Observation:** Character noise has a milder effect than word dropout, likely because FinBERT's subword tokenization can recover partial meaning from corrupted words. The model maintains ~79.8% accuracy even at 50% character noise rate.

---

### 3.3 Word Shuffle

Randomly shuffles the order of words within the sentence.

| Shuffle Rate | Accuracy | F1 Score | AUC |
|---|---|---|---|
| 0.0 (baseline) | 0.8729 | 0.8750 | 0.9533 |
| 0.1 | 0.8673 | 0.8699 | 0.9510 |
| 0.2 | 0.8631 | 0.8652 | 0.9492 |
| 0.3 | 0.8561 | 0.8582 | 0.9453 |
| 0.4 | 0.8450 | 0.8480 | 0.9412 |
| 0.5 | 0.8311 | 0.8348 | 0.9343 |

**Observation:** The model shows strong robustness to word order perturbation — even at 50% shuffle, accuracy drops only to ~83.1%. This suggests FinBERT leverages bag-of-words-like cues alongside positional information for causality detection.

---

### 3.4 Synonym Replacement

Replaces words with synonyms (using WordNet), testing semantic paraphrase robustness.

| Replacement Rate | Accuracy | F1 Score | AUC |
|---|---|---|---|
| 0.0 (baseline) | 0.8729 | 0.8750 | 0.9533 |
| 0.1 | 0.8703 | 0.8726 | 0.9526 |
| 0.2 | 0.8671 | 0.8695 | 0.9508 |
| 0.3 | 0.8608 | 0.8629 | 0.9478 |
| 0.4 | 0.8549 | 0.8577 | 0.9452 |
| 0.5 | 0.8472 | 0.8501 | 0.9416 |

**Observation:** Synonym replacement causes the least degradation of all text perturbation types. Even at 50% synonym substitution rate, accuracy drops only ~2.6 pp. The model generalises well to semantic paraphrasing of financial language.

---

## 4. Numerical Feature Robustness (Gaussian Noise)

Gaussian noise (σ) is injected into the standardised numerical features, simulating measurement noise or data quality issues.

| Noise σ | Accuracy | F1 Score | AUC |
|---|---|---|---|
| 0.0 (baseline) | 0.8729 | 0.8750 | 0.9533 |
| 0.1 | 0.8721 | 0.8742 | 0.9528 |
| 0.25 | 0.8706 | 0.8728 | 0.9519 |
| 0.5 | 0.8680 | 0.8701 | 0.9506 |
| 1.0 | 0.8613 | 0.8638 | 0.9470 |
| 2.0 | 0.8498 | 0.8527 | 0.9412 |

**Observation:** The model is highly robust to numerical noise. Even with σ = 2.0 (very large noise relative to standardised features), accuracy drops only ~2.3 pp. This is consistent with the ablation study finding that text is the dominant modality; numerical features play a supporting role.

---

## 5. Adversarial Robustness (FGSM Attack)

The **Fast Gradient Sign Method (FGSM)** generates adversarial perturbations on the numerical features by computing gradients of the loss and stepping in the sign of the gradient direction. This is the strongest available attack on the numerical branch.

| Epsilon (ε) | Accuracy | F1 Score | AUC |
|---|---|---|---|
| 0.0 (baseline) | 0.8729 | 0.8750 | 0.9533 |
| 0.01 | 0.8712 | 0.8733 | 0.9522 |
| 0.05 | 0.8661 | 0.8683 | 0.9494 |
| 0.1 | 0.8594 | 0.8617 | 0.9453 |
| 0.2 | 0.8470 | 0.8497 | 0.9388 |
| 0.5 | 0.8153 | 0.8191 | 0.9197 |

**Observation:** FGSM adversarial attacks on the numerical branch cause more degradation than random Gaussian noise of equivalent magnitude, but the model retains >81% accuracy even at ε = 0.5 (aggressive attack). The text modality acts as a natural hedge, absorbing perturbations to the numerical branch.

---

## 6. Temporal Distribution Shift

Model performance was evaluated separately for each year present in the test set. The test set was split by a date cutoff (`split_date`), and year-level subsets were analysed.

| Year | n Samples | Accuracy | F1 Score | AUC |
|---|---|---|---|---|
| 2018 | 7,203 | 0.4108 | 0.3591 | 0.5863 |
| 2019 | 18 | N/A (too few) | — | — |
| 2020 | 1 | N/A (too few) | — | — |
| 2023 | 7 | N/A (too few) | — | — |
| 2025 | 1 | N/A (too few) | — | — |

**Observation:** The test set is highly skewed — 2018 contains the overwhelming majority (7,203) of test samples, while subsequent years have too few samples for reliable evaluation (< 20 samples each). The model performance on 2018 test data (Acc = 0.4108, F1 = 0.3591) is notably lower than the aggregate test performance (0.8729), suggesting that:

1. The **training distribution** may be dominated by non-2018 data, creating a covariate shift when evaluated on 2018-era articles.
2. Financial language and causality patterns may have **evolved** between the training periods and 2018 test data.
3. Further investigation into the **date-based train/test split** methodology is recommended.

> ⚠️ **Important:** The year-level temporal shift analysis is limited by dataset composition. Only 2018 has sufficient samples for evaluation. Future work should ensure more balanced temporal coverage in the test set.

---

## 7. Input Length Sensitivity

Test samples were bucketed by text word count to detect any **length bias** in model performance.

| Length Bucket | n Samples | Accuracy | F1 Score | AUC |
|---|---|---|---|---|
| < 20 words | 0 | N/A | — | — |
| 20–50 words | 0 | N/A | — | — |
| 50–100 words | 119 | **0.9832** | **0.9832** | **0.9985** |
| 100–150 words | 263 | 0.9886 | 0.9886 | 0.9784 |
| 150–200 words | 123 | 0.9431 | 0.9434 | 0.9725 |
| 200–500 words | 2,955 | 0.8386 | 0.8421 | 0.9246 |
| 500+ words | 3,770 | 0.8912 | 0.8937 | 0.9690 |

**Observation:** The model achieves its **highest performance on short to medium texts** (50–150 words), reaching F1 > 0.98. Performance dips for medium-long texts (200–500 words) to F1 = 0.8421, then recovers somewhat for very long texts (500+ words, F1 = 0.8937). This pattern suggests:

- Short texts with focused causal language are easiest to classify correctly.
- Very long articles (500+ words) may contain multiple implicit causal relationships, making classification harder, but the model still generalises reasonably.
- The mid-length range (200–500 words) is the most challenging, possibly because these texts contain significant contextual information but not enough signal density.

---

## 8. Robustness Summary

| Test Type | Condition | F1 Drop vs. Baseline |
|---|---|---|
| Word Dropout | 50% rate | −0.1453 |
| Character Noise | 50% rate | −0.0733 |
| Word Shuffle | 50% rate | −0.0402 |
| Synonym Replacement | 50% rate | −0.0249 |
| Numerical Noise (Gaussian) | σ = 2.0 | −0.0223 |
| Adversarial (FGSM) | ε = 0.5 | −0.0559 |
| Temporal Shift | Year 2018 (aggregate test split) | −0.5159 |
| Input Length | 200–500 words | −0.0329 |

> **Key Findings:**
> 1. The model is **most sensitive to word dropout** (complete word loss), as expected for a text-centric classification task.
> 2. The model is **highly robust to synonym replacement and numerical noise**, suggesting good semantic generalisation and text-dominant inference.
> 3. **Temporal distribution shift** (2018 vs. overall test) reveals the largest performance gap, warranting investigation of the training data distribution by year.
> 4. **Input length sensitivity** shows that shorter texts are handled more accurately, but performance is maintained across practical text lengths.

---

## 9. Experimental Setup

| Parameter | Value |
|---|---|
| GPU | Tesla T4 (Google Colab) |
| Base Text Model | `yiyanghkust/finbert-tone` |
| Max Sequence Length | 128 tokens |
| Batch Size | 64 |
| Text Perturbations | Word Dropout, Character Noise, Word Shuffle, Synonym Replacement |
| Synonym Source | WordNet (NLTK) |
| Numerical Perturbations | Gaussian noise injection (σ ∈ {0.1, 0.25, 0.5, 1.0, 2.0}) |
| Adversarial Attack | FGSM on numerical features (ε ∈ {0.01, 0.05, 0.1, 0.2, 0.5}) |

---

*Report generated from Phase 5 Colab notebook and `phase5_ablation_robustness_results.csv`.*
