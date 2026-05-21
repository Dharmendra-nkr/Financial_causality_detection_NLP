# 🎯 Google Colab Setup - Quick Start Guide

## ✅ What I've Created For You

I've created 3 files to help you run Phase-5 on Google Colab:

1. **Phase-5_Colab.ipynb** - Your notebook ready for Colab (automatically converted!)
2. **Google_Colab_Setup_Instructions.md** - Detailed instructions
3. **convert_to_colab.py** - Script I used to convert the notebook (for reference)

---

## 📋 What You Need to Do (Step-by-Step)

### Step 1: Prepare Files on Your Computer

#### File 1: CSV Dataset ✓ (Already ready)
- **File**: `label_shifted_fin_causality_dataset.csv`
- **Location**: `D:\NLP_ResearchPaper_work\label_shifted_fin_causality_dataset.csv`
- **Action**: **No action needed** - this file is ready to upload

#### File 2: Model ZIP (You need to create this)
- **Source folder**: `D:\NLP_ResearchPaper_work\model_extracted\multimodal_model_20260221_141142\`
- **Action**: Create a ZIP file

**How to create the ZIP:**
```
1. Open File Explorer
2. Navigate to: D:\NLP_ResearchPaper_work\model_extracted\
3. Right-click on the folder: multimodal_model_20260221_141142
4. Select "Send to" → "Compressed (zipped) folder"
   OR if you have 7-Zip: Right-click → "7-Zip" → "Add to archive..."
5. Name it: multimodal_model_20260221_141142.pkl.zip
6. The ZIP file should contain:
   - byteorder (file)
   - version (file)
   - data/ (folder with numbered files 0, 1, 2, ..., 224)
```

---

### Step 2: Upload to Google Drive

1. **Go to**: [Google Drive](https://drive.google.com)

2. **Create folder**: Click "New" → "Folder" → Name it exact `NLP_Phase5`

3. **Upload files** to the `NLP_Phase5` folder:
   - Upload `label_shifted_fin_causality_dataset.csv`
   - Upload `multimodal_model_20260221_141142.pkl.zip` (the ZIP you just created)

4. **Verify** your Google Drive structure looks like this:
   ```
   My Drive/
   └── NLP_Phase5/
       ├── label_shifted_fin_causality_dataset.csv  ✓
       └── multimodal_model_20260221_141142.pkl.zip ✓
   ```

---

### Step 3: Upload Notebook to Google Colab

1. **Go to**: [Google Colab](https://colab.research.google.com/)

2. **Upload notebook**:
   - Click "File" → "Upload notebook"
   - Click "Browse" and select: `Phase-5_Colab.ipynb` (from this folder)
   - OR drag and drop `Phase-5_Colab.ipynb` into Colab

3. **Set GPU runtime**:
   - Click "Runtime" at top
   - Click "Change runtime type"
   - Set "Hardware accelerator" to **GPU**
   - Click "Save"

---

### Step 4: Run the Notebook

1. **Run cells in order**:
   - Click "Runtime" → "Run all"
   - OR press Ctrl+F9

2. **First cell will ask permission**:
   - It will show: "Permit this notebook to access your Google Drive files?"
   - Click "Connect to Google Drive"
   - Choose your Google account
   - Click "Allow"

3. **Wait for completion**:
   - The notebook will take ~1-2 hours to complete on free Colab GPU
   - You'll see progress bars for each section

---

## 🔍 Expected Results

The notebook will generate:

### Experiments Run:
1. ✅ Baseline model evaluation
2. ✅ Component ablation (4 variants: Text-Only, Numerical-Only, No Gate, CLS Pooling)
3. ✅ Feature ablation (test each numerical feature)
4. ✅ Text perturbation robustness (word dropout, char noise, shuffle, synonyms)
5. ✅ Numerical noise robustness (Gaussian noise)
6. ✅ Adversarial robustness (FGSM attacks)
7. ✅ Temporal distribution shift
8. ✅ Input length sensitivity

### Output Files:
- `ablation_comparison.png` - Bar charts comparing all ablation results
- `robustness_sensitivity_curves.png` - 4-panel robustness plot
- `robustness_heatmap.png` - Heatmap of robustness scores
- `phase5_ablation_robustness_results.csv` - All results in CSV format

---

## ⚠️ Troubleshooting

### Problem: "Files not found" error
**Solution**: 
- Check folder name is exactly: `NLP_Phase5` (case-sensitive!)
- Check files are directly in that folder, not in a subfolder

### Problem: "CUDA out of memory"
**Solution**: 
- The notebook already has optimized batch size (64)
- If still happens, reconnect with a new session (Runtime → Factory reset runtime)

### Problem: "GPU not available"
**Solution**: 
- Make sure you selected GPU in Runtime settings
- Free Colab occasionally runs out of GPU quota
- Try again in a few hours OR upgrade to Colab Pro

### Problem: Session disconnects
**Solution**: 
- Colab free tier disconnects after ~12 hours or 30 min idle
- Keep browser tab open and active
- Or run in shorter sessions (sections 1-8, then 9-19)

### Problem: Training too slow
**Expected times on free Colab T4 GPU:**
- Baseline evaluation: ~2-3 minutes
- Each ablation variant: ~5-10 minutes  
- Full notebook: ~1-2 hours

If much slower, check:
- GPU is enabled (should see "GPU 0: Tesla T4" when you run cell 1)
- No other heavy Colab notebooks running

---

## 💡 Tips

### Save Results to Drive
Add this cell at the very end of notebook:
```python
# Save results to Google Drive
!cp *.png /content/drive/MyDrive/NLP_Phase5/
!cp *.csv /content/drive/MyDrive/NLP_Phase5/
print(" Results saved to Google Drive!")
```

### Download Results
After completion:
- Click folder icon on left sidebar
- Right-click files → Download

### Resume from checkpoint
If disconnected, just run cell 1-3 again, then continue from where you stopped

---

## 📊 What's Different from Local Version?

| Local Notebook | Colab Notebook |
|---|---|
| Runs on your RTX 3050 | Runs on Google Tesla T4/V100 |
| Uses local paths (`D:\...`) | Uses Google Drive paths (`/content/drive/...`) |
| Conda environment | Pre-installed packages + pip |
| Faster (your GPU) | Slightly slower (shared GPU) |
| No time limit | Free tier: ~12 hours max |

---

## ✨ Summary Checklist

- [ ] Created ZIP of model folder
- [ ] Uploaded CSV to Google Drive `NLP_Phase5/`
- [ ] Uploaded ZIP to Google Drive `NLP_Phase5/`
- [ ] Uploaded `Phase-5_Colab.ipynb` to Colab
- [ ] Set Runtime to GPU
- [ ] Clicked "Run all"
- [ ] Granted Google Drive access
- [ ] Waiting for results (~1-2 hours)

---

**You're all set!** 🚀

If you have any issues, check the detailed instructions in `Google_Colab_Setup_Instructions.md`.

The notebook is self-contained - all the code from your local Phase-5.ipynb is there, 
just with updated paths for Google Colab environment.
