import os

# Path to your data folder
data_folder = r"D:\python\Classifier_Model\data"

# Counters
total_files = 0
jpg_count = 0
non_jpg_files = []

# Loop through all files in the folder
for filename in os.listdir(data_folder):
    file_path = os.path.join(data_folder, filename)
    if os.path.isfile(file_path):
        total_files += 1
        print(f"Checking: {filename}")
        if filename.lower().endswith(".jpg"):
            jpg_count += 1
        else:
            non_jpg_files.append(filename)

# Report results
print("\n--- Summary ---")
print(f"Total files checked: {total_files}")
print(f"JPG files: {jpg_count}")
print(f"Non-JPG files: {len(non_jpg_files)}")

if non_jpg_files:
    print("⚠️ Non-JPG files found:")
    for f in non_jpg_files:
        print(f" - {f}")
else:
    print("✅ All files are JPG images.")
