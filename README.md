# FACE-1
Predicts age, gender, and ethnicity from face images using a multi-output CNN trained on the UTKFace dataset. Supports real-time webcam inference, with preprocessing, early stopping, and learning rate scheduling for optimized performance.

# Future Considerations
Could implement Batch Normalization to help stabilize and accelerate training, and update the image resizing to higher resolutions such as 224×224 <-> 512×512 to capture more facial details.


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
├─ data/                        # raw UTKFace images (not included in the repository)
├─ data_clean/                  # cleaned valid images (not included in the repository)
│
├─ data_cleaning_scripts/       # python scripts for validating and cleaning the dataset
│   ├─ data_naming_validation.py
│   ├─ jpg_check.py
│   └─ size_check.py
│
├─ models/
│   ├─ face1_model.h5           # trained model 1
│   ├─ face1_model.h5           # optional duplicate (newer saved format)
│   └─ upcoming_models...       # trained model n
│
├─ test_imgs/
│   ├─ Jensen_Huang.jpg         # test image
│   └─ ....jpg                  # test images
│
├─ Human_Classifier.ipynb       # training + exploration notebook
├─ try_me_out.py                # testing/inference script
└─ README.md
```

# Setup
1. Install dependencies:
pip install tensorflow keras numpy pandas matplotlib opencv-python scikit-learn pillow

2. Run in Terminal
  - 2a. Go to correct directory
    - cd ~/<file_path>/Classifier_Model
  - 2b. Run command
    - Static image test (if image exists in directory)
      - py try_me_out.py --mode static --image "test_imgs/<FirstName_LastName>.jpg"
    - Live webcam test (no boxes)
      - py try_me_out.py --mode live
    - Live webcam test (with face detection boxes)
      - py try_me_out.py --mode live_box

# Dataset
Dataset: UTKFace - Age, Gender, and Ethnicity Dataset
- Kaggle Source: https://www.kaggle.com/datasets/nipunarora8/age-gender-and-ethnicity-face-data-csv
- Original Website: https://susanqq.github.io/UTKFace/
- Google Drive Download Link: https://drive.google.com/drive/folders/1HROmgviy4jUUUaCdvvrQ8PcqtNg2jn3G