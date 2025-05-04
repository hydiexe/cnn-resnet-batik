import os
import shutil
import random
from pathlib import Path

# CONFIGURATIONS
SOURCE_DIR = "raw_dataset"            # Folder asli yang berisi 20 subfolder kelas
OUTPUT_DIR = "dataset_split"          # Folder keluaran
TRAIN_RATIO = 0.7                     # 70% train
VAL_RATIO = 0.15                      # 15% val
TEST_RATIO = 0.15                     # 15% test
SEED = 42

random.seed(SEED)

# Buat folder keluaran
splits = ['train', 'val', 'test']
for split in splits:
    os.makedirs(os.path.join(OUTPUT_DIR, split), exist_ok=True)

# Mulai proses split
for class_name in os.listdir(SOURCE_DIR):
    class_path = os.path.join(SOURCE_DIR, class_name)
    if not os.path.isdir(class_path):
        continue

    images = os.listdir(class_path)
    random.shuffle(images)

    n_total = len(images)
    n_train = int(n_total * TRAIN_RATIO)
    n_val = int(n_total * VAL_RATIO)

    train_images = images[:n_train]
    val_images = images[n_train:n_train + n_val]
    test_images = images[n_train + n_val:]

    for split, img_list in zip(splits, [train_images, val_images, test_images]):
        split_class_dir = os.path.join(OUTPUT_DIR, split, class_name)
        os.makedirs(split_class_dir, exist_ok=True)
        for img_name in img_list:
            src = os.path.join(class_path, img_name)
            dst = os.path.join(split_class_dir, img_name)
            shutil.copy2(src, dst)

    print(f"{class_name}: {len(train_images)} train, {len(val_images)} val, {len(test_images)} test")

print("✅ Dataset split selesai.")
