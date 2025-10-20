import os
import shutil

# Paths
data_path = r"D:\python\Classifier_Model\data"
clean_path = r"D:\python\Classifier_Model\data_clean"
os.makedirs(clean_path, exist_ok=True)

# Counters
valid_count = 0
invalid_count = 0

for file in os.listdir(data_path):
    if not file.lower().endswith(".jpg"):
        continue

    name_only = file.split(".")[0]
    parts = name_only.split("_")

    # Assume file is invalid unless all checks pass
    is_valid = False

    # Check filename parts
    if len(parts) >= 4:
        try:
            age = int(parts[0])
            gender = int(parts[1])
            race = int(parts[2])
            timestamp = parts[3]

            # Strict UTKFace checks
            if (0 <= age <= 116) and (gender in [0, 1]) and (race in [0, 1, 2, 3, 4]) and timestamp.isdigit():
                is_valid = True

        except ValueError:
            is_valid = False

    if is_valid:
        shutil.copy2(os.path.join(data_path, file), os.path.join(clean_path, file))
        valid_count += 1
    else:
        invalid_count += 1
        # Optionally print invalid files
        print(f"Skipping invalid file: {file}")

print("Filtering complete!")
print(f"Valid images copied: {valid_count}")
print(f"Invalid images skipped: {invalid_count}")
print(f"Clean dataset path: {clean_path}")
