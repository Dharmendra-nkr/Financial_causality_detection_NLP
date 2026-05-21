"""
Convert Phase-5.ipynb to Google Colab format

This script:
1. Reads your local Phase-5.ipynb
2. Adds Colab setup cells at the beginning
3. Replaces all local paths with Google Drive paths
4. Saves as Phase-5_Colab.ipynb

Usage:
    python convert_to_colab.py
"""

import json
import os

# Paths
INPUT_NOTEBOOK = "Phase-5.ipynb"
OUTPUT_NOTEBOOK = "Phase-5_Colab.ipynb"

# Load original notebook
print(f"Loading {INPUT_NOTEBOOK}...")
with open(INPUT_NOTEBOOK, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Create new cells to insert at the beginning
colab_setup_cells = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# ⚠️ GOOGLE COLAB SETUP\\n",
            "\\n",
            "**BEFORE RUNNING:** Make sure you have uploaded these files to Google Drive:\\n",
            "```\\n",
            "My Drive/NLP_Phase5/\\n",
            "├── label_shifted_fin_causality_dataset.csv\\n",
            "└── multimodal_model_20260221_141142.pkl.zip\\n",
            "```\\n",
            "\\n",
            "**Runtime Settings:**\\n",
            "- Go to: Runtime → Change runtime type\\n",
            "- Set: Hardware accelerator = GPU\\n",
            "- Save\\n",
            "\\n",
            "---"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Mount Google Drive\\n",
            "from google.colab import drive\\n",
            "drive.mount('/content/drive')\\n",
            "\\n",
            "# Verify files\\n",
            "import os\\n",
            "BASE_PATH = '/content/drive/MyDrive/NLP_Phase5'\\n",
            "\\n",
            "required_files = [\\n",
            "    f'{BASE_PATH}/label_shifted_fin_causality_dataset.csv',\\n",
            "    f'{BASE_PATH}/multimodal_model_20260221_141142.pkl.zip'\\n",
            "]\\n",
            "\\n",
            "print('Checking files...')\\n",
            "all_found = True\\n",
            "for file in required_files:\\n",
            "    exists = os.path.exists(file)\\n",
            "    print(f'  {os.path.basename(file)}: {'✅' if exists else '❌'}')\\n",
            "    if not exists:\\n",
            "        all_found = False\\n",
            "\\n",
            "if all_found:\\n",
            "    print('\\\\n✅ All files found! Ready to proceed.')\\n",
            "else:\\n",
            "    print(f'\\\\n❌ Missing files! Please upload to: {BASE_PATH}/')\\n",
            "    raise FileNotFoundError('Required files not found in Google Drive')"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Install required packages\\n",
            "!pip install -q transformers==4.37.2 nltk accelerate>=0.20.0\\n",
            "\\n",
            "# Download NLTK data\\n",
            "import nltk\\n",
            "nltk.download('wordnet', quiet=True)\\n",
            "nltk.download('omw-1.4', quiet=True)\\n",
            "\\n",
            "print('✅ Packages installed!')"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "---\\n",
            "# Phase 5: Ablation & Robustness Analysis\\n",
            "*(Original notebook content starts below)*"
        ]
    }
]

# Path replacements
path_replacements = {
    r"D:\NLP_ResearchPaper_work\label_shifted_fin_causality_dataset.csv": 
        "/content/drive/MyDrive/NLP_Phase5/label_shifted_fin_causality_dataset.csv",
    
    r"D:\NLP_ResearchPaper_work\model_extracted": 
        "/content/model_extracted",
    
    r"D:\NLP_ResearchPaper_work\multimodal_model_reconstructed.pkl": 
        "/content/multimodal_model_reconstructed.pkl",
    
    r"D:\NLP_ResearchPaper_work\multimodal_model_20260221_141142.pkl.zip":
        "/content/drive/MyDrive/NLP_Phase5/multimodal_model_20260221_141142.pkl.zip",
    
    # Escaped backslashes version
    "D:\\\\NLP_ResearchPaper_work\\\\label_shifted_fin_causality_dataset.csv": 
        "/content/drive/MyDrive/NLP_Phase5/label_shifted_fin_causality_dataset.csv",
    
    "D:\\\\NLP_ResearchPaper_work\\\\model_extracted": 
        "/content/model_extracted",
    
    "D:\\\\NLP_ResearchPaper_work\\\\multimodal_model_reconstructed.pkl": 
        "/content/multimodal_model_reconstructed.pkl",
    
    "D:\\\\NLP_ResearchPaper_work\\\\multimodal_model_20260221_141142.pkl.zip":
        "/content/drive/MyDrive/NLP_Phase5/multimodal_model_20260221_141142.pkl.zip",
}

# Process all cells
print("Replacing paths in cells...")
for cell in nb['cells']:
    if 'source' in cell:
        # Handle both string and list sources
        if isinstance(cell['source'], list):
            source_text = ''.join(cell['source'])
        else:
            source_text = cell['source']
        
        # Apply all path replacements
        for old_path, new_path in path_replacements.items():
            source_text = source_text.replace(old_path, new_path)
        
        # Update source
        cell['source'] = source_text

# Insert Colab setup cells at the beginning
nb['cells'] = colab_setup_cells + nb['cells']

# Update metadata for Colab
nb['metadata'] = {
    "accelerator": "GPU",
    "colab": {
        "gpuType": "T4",
        "provenance": []
    },
    "kernelspec": {
        "display_name": "Python 3",
        "name": "python3"
    },
    "language_info": {
        "name": "python"
    }
}

# Save converted notebook
print(f"Saving {OUTPUT_NOTEBOOK}...")
with open(OUTPUT_NOTEBOOK, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)

print(f"✅ Successfully created {OUTPUT_NOTEBOOK}!")
print(f"\nNext steps:")
print(f"1. Upload these to Google Drive at 'My Drive/NLP_Phase5/':")
print(f"   - label_shifted_fin_causality_dataset.csv")
print(f"   - multimodal_model_20260221_141142.pkl.zip (create this from model_extracted folder)")
print(f"2. Upload {OUTPUT_NOTEBOOK} to Google Colab")
print(f"3. Set Runtime to GPU")
print(f"4. Run all cells")
