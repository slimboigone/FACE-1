# FACE-1
Predicts age, gender, and ethnicity from face images using a multi-output CNN trained on the UTKFace dataset. Supports real-time webcam inference, with preprocessing, early stopping, and learning rate scheduling for optimized performance.

# Features
- Predicts age (regression), gender (binary classification), and ethnicity (5-class classification) simultaneously.
  - [age]     → 0–116 (person's age)
  - [gender]  → male, female
  - [race]    → 0 = White, 1 = Black, 2 = Asian, 3 = Indian, 4 = Others
- Supports static image input for testing.
- Supports live webcam input with optional face bounding boxes.
- Uses early stopping and learning rate scheduling to prevent overfitting.
- Handles preprocessing: resizing to 128x128 and normalizing images.

# Project Structure
```
Classifier_Model/
│
├─ data/                        # raw UTKFace images
├─ data_clean/                  # cleaned valid images
│
├─ data_clearing_scripts/       # (typo fix: 'cleaing' → 'clearing')
│   ├─ data_naming_validation.py
│   ├─ jpg_check.py
│   └─ size_check.py
│
├─ test/
│   ├─ Jensen_Huang.jpg         # test image
│   └─ ....jpg                  # test images
│
├─ face1_model.h5               # trained model
├─ face1_model.keras            # optional duplicate (newer saved format)
│
├─ Human_Classifier.ipynb       # training + exploration notebook
├─ try_me_out.py                # testing/inference script
└─ README.md
```

# Setup
1. Install dependencies:
pip install tensorflow keras numpy pandas matplotlib opencv-python scikit-learn pillow

2. Run in Terminal (Options)
- Static image test (if image exists in directory)
  - python try_me_out.py --mode static --image "test/<FirstName_LastName>.jpg"
- Live webcam test (no boxes)
  - python try_me_out.py --mode live
- Live webcam test (with face detection boxes)
  - python try_me_out.py --mode live_box

# Dataset
Dataset: UTKFace - Age, Gender, and Ethnicity Dataset
- Kaggle Source: https://www.kaggle.com/datasets/nipunarora8/age-gender-and-ethnicity-face-data-csv
- Original Website: https://susanqq.github.io/UTKFace/
- Google Drive Download Link: https://drive.google.com/drive/folders/1HROmgviy4jUUUaCdvvrQ8PcqtNg2jn3G
