# Google Colab Setup Instructions for Phase-5 Ablation Analysis

## 📋 Prerequisites

You'll need to upload these files to your Google Drive to run Phase-5 analysis on Google Colab.

## 🗂️ Step 1: Create Folder Structure in Google Drive

In your Google Drive, create this folder:

```
My Drive/
└── NLP_Phase5/
```

## 📤 Step 2: Upload Required Files

Upload these 2 files to the `NLP_Phase5` folder in your Google Drive:

### File 1: Dataset
- **Filename**: `label_shifted_fin_causality_dataset.csv`
- **Location on your PC**: `D:\NLP_ResearchPaper_work\label_shifted_fin_causality_dataset.csv`
- **Size**: ~few MB
- **Action**: Simply upload this file as-is to Google Drive folder

### File 2: Model Checkpoint (ZIP)
- **Filename**: `multimodal_model_20260221_141142.pkl.zip`
- **Location on your PC**: You need to create this ZIP file
- **How to create**:
  
  1. Navigate to: `D:\NLP_ResearchPaper_work\model_extracted\multimodal_model_20260221_141142\`
  
  2. This folder contains:
     ```
     multimodal_model_20260221_141142/
     ├── byteorder
     ├── version
     └── data/
         ├── 0
         ├── 1
         ├── 2
         ... (many numbered files)
     ```
  
  3. **Create ZIP file:**
     - Right-click on the `multimodal_model_20260221_141142` folder
     - Select "Send to" → "Compressed (zipped) folder"
     - OR use 7-Zip/WinRAR: Right-click → "Add to archive"
     - Name it: `multimodal_model_20260221_141142.pkl.zip`
  
  4. Upload this ZIP file to `My Drive/NLP_Phase5/` in Google Drive

## ✅ Step 3: Verify Your Google Drive Structure

Your Google Drive should now look like this:

```
My Drive/
└── NLP_Phase5/
    ├── label_shifted_fin_causality_dataset.csv
    └── multimodal_model_20260221_141142.pkl.zip
```

## 🚀 Step 4: Run on Google Colab

### Option A: Create Notebook from Scratch
1. Go to [Google Colab](https://colab.research.google.com/)
2. Create a new notebook
3. Copy all cells from `Phase-5.ipynb` but modify paths:
   - Change all `D:\NLP_ResearchPaper_work\` to `/content/drive/MyDrive/NLP_Phase5/`
   - Add Google Drive mount at the beginning

### Option B: Use the Pre-configured Colab Notebook (Recommended)

I'll create a simplified Colab-ready notebook for you. The key differences from your local notebook:

#### Changes needed in code:

1. **Add at the very beginning:**
```python
from google.colab import drive
drive.mount('/content/drive')
```

2. **Change paths:**
```python
# OLD (local):
DATA_PATH = r"D:\NLP_ResearchPaper_work\label_shifted_fin_causality_dataset.csv"

# NEW (Colab):
DATA_PATH = '/content/drive/MyDrive/NLP_Phase5/label_shifted_fin_causality_dataset.csv'
```

3. **Install packages first:**
```python
!pip install -q transformers==4.37.2 nltk accelerate
```

4. **Set runtime to GPU:**
   - In Colab: Runtime → Change runtime type → GPU → Save

## 📝 Full Colab Notebook Template

Since the full notebook is too large to display here, I'll create just the key setup cells you need to add to your existing Phase-5.ipynb:

### Cell 0 (Add at beginning): Mount Drive & Install Packages

```python
# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Install required packages
!pip install -q transformers==4.37.2 nltk accelerate

# Download NLTK data
import nltk
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)

print("✅ Setup complete!")
```

### Cell 0.5: Verify Files

```python
import os

BASE_PATH = '/content/drive/MyDrive/NLP_Phase5'
DATA_FILE = f'{BASE_PATH}/label_shifted_fin_causality_dataset.csv'
MODEL_ZIP = f'{BASE_PATH}/multimodal_model_20260221_141142.pkl.zip'

print("Checking files...")
print(f"Dataset exists: {os.path.exists(DATA_FILE)}")
print(f"Model ZIP exists: {os.path.exists(MODEL_ZIP)}")

if os.path.exists(DATA_FILE) and os.path.exists(MODEL_ZIP):
    print("\n✅ All files found! Ready to proceed.")
else:
    print("\n❌ Missing files! Please upload them to:", BASE_PATH)
```

### Update paths in existing cells:

Find and replace in your Phase-5.ipynb:
- `D:\\NLP_ResearchPaper_work\\label_shifted_fin_causality_dataset.csv` → `/content/drive/MyDrive/NLP_Phase5/label_shifted_fin_causality_dataset.csv`
- `D:\\NLP_ResearchPaper_work\\model_extracted` → `/content/model_extracted`
- `D:\\NLP_ResearchPaper_work\\multimodal_model_reconstructed.pkl` → `/content/multimodal_model_reconstructed.pkl`

## ⚡ Performance Tips for Colab

1. **Use GPU**: Make sure Runtime → GPU is enabled
2. **Colab GPU Options**:
   - Free: T4 (~15GB VRAM) - should be sufficient
   - Colab Pro: V100/A100 - much faster

3. **Expected Training Time** (on T4):
   - Full baseline evaluation: ~2-3 minutes
   - Each ablation variant: ~5-10 minutes
   - Total notebook run: ~1-2 hours

## 🔧 Troubleshooting

### Issue: "No module named transformers"
**Solution**: Run the install cell again:
```python
!pip install transformers==4.37.2
```

### Issue: "CUDA out of memory"
**Solution**: Reduce batch size in the code:
```python
BATCH_SIZE = 32  # Change from 64 to 32
```

### Issue: "Files not found"
**Solution**: Check your folder structure exactly matches:
```
My Drive/NLP_Phase5/
```
NOT: `MyDrive` or `My_Drive` or any other variation

### Issue: Session disconnects
**Solution**: 
- Colab free tier sessions timeout after ~12 hours or 30 min idle
- Keep browser tab active
- Or upgrade to Colab Pro for longer sessions

## 💾 Saving Results

Results will be saved to `/content/` which is temporary. To keep them:

Add this at the end of notebook:
```python
# Copy results to Google Drive
!cp /content/*.png /content/drive/MyDrive/NLP_Phase5/
!cp /content/*.csv /content/drive/MyDrive/NLP_Phase5/
print("✅ Results saved to Google Drive!")
```

## 📊 What Will Run on Colab

All sections from Phase-5 will run:
1. ✅ Baseline Evaluation
2. ✅ Component Ablation (4 variants)
3. ✅ Feature Ablation
4. ✅ Text Perturbation Robustness
5. ✅ Numerical Noise Robustness
6. ✅ Adversarial (FGSM) Attacks
7. ✅ Temporal Distribution Shift
8. ✅ Input Length Sensitivity
9. ✅ Visualizations (all plots)

Expected total runtime: **1-2 hours on free Colab T4 GPU**

---

## 🎯 Quick Start Checklist

- [ ] Upload `label_shifted_fin_causality_dataset.csv` to Google Drive
- [ ] Create ZIP of model folder and upload to Google Drive
- [ ] Verify both files are in `My Drive/NLP_Phase5/`
- [ ] Open existing Phase-5.ipynb locally
- [ ] Add Colab setup cells at the beginning
- [ ] Find-Replace all local paths with Colab paths
- [ ] Upload modified notebook to Colab
- [ ] Set Runtime to GPU
- [ ] Run all cells

---

**Need Help?**: If you encounter issues, the most common problem is incorrect file paths. 
Double-check that your Google Drive folder is named exactly `NLP_Phase5` and that path matches in the code.
