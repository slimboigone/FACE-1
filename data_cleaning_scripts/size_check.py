# Output:
# Total images checked: 24106
# Minimum size: 87x69
# Maximum size: 8198x8739

# No images smaller than 64x64 found.

import os
from PIL import Image

# Path to your dataset
data_path = r"D:\python\Classifier_Model\data"

# Initialize min/max trackers
min_width, min_height = float('inf'), float('inf')
max_width, max_height = 0, 0

# Optional: keep track of very small images
small_images = []

# Scan all jpg files
image_files = [f for f in os.listdir(data_path) if f.lower().endswith(".jpg")]

for file in image_files:
    file_path = os.path.join(data_path, file)
    try:
        img = Image.open(file_path)
        w, h = img.size

        # Update min/max
        min_width = min(min_width, w)
        min_height = min(min_height, h)
        max_width = max(max_width, w)
        max_height = max(max_height, h)

        # Optional: check for tiny images
        if w < 64 or h < 64:
            small_images.append(file)

    except Exception as e:
        print(f"Error opening {file}: {e}")

# Print results
print(f"Total images checked: {len(image_files)}")
print(f"Minimum size: {min_width}x{min_height}")
print(f"Maximum size: {max_width}x{max_height}")

if small_images:
    print(f"\nImages smaller than 64x64 ({len(small_images)} found):")
    for f in small_images:
        print(f" - {f}")
else:
    print("\nNo images smaller than 64x64 found.")

# Output:
# Total images checked: 24106
# Minimum size: 87x69
# Maximum size: 8198x8739

# No images smaller than 64x64 found.