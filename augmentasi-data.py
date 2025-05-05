from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img, save_img
import os
from pathlib import Path
from tqdm import tqdm

# parameters
input_dir = "dataset_split/train"
output_dir = "preprocessing_images"
img_size = (224, 224)  # ukuran gambar yang diinginkan
num_augmented = 3      # jumlah augmentasi per gambar

os.makedirs(output_dir, exist_ok=True)

# augmentasi settings
datagen = ImageDataGenerator(
    rotation_range=30,
    brightness_range=(0.8, 1.2),
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='reflect'
)

class_dirs = [d for d in Path(input_dir).iterdir() if d.is_dir()]

for class_dir in class_dirs:
    class_name = class_dir.name
    output_class_dir = os.path.join(output_dir, class_name)
    os.makedirs(output_class_dir, exist_ok=True)
    
    image_paths = list(class_dir.glob("*.jpg")) + list(class_dir.glob("*.png")) + list(class_dir.glob("*.jpeg"))
    print(f"{class_name}: {len(image_paths)} images")

    for img_path in tqdm(image_paths, desc=f"Processing {class_name}"):
        try:
            img = load_img(img_path, target_size=img_size)
            x = img_to_array(img)
            x = x.reshape((1,) + x.shape)  # reshape untuk ImageDataGenerator

            base_name = img_path.stem

            i = 0
            for batch in datagen.flow(x, batch_size=1):
                filename = f"{base_name}_aug{i}.png"
                save_img(os.path.join(output_class_dir, filename), batch[0])
                i += 1
                if i >= num_augmented:
                    break

            # simpan juga gambar asli (resize)
            save_img(os.path.join(output_class_dir, f"{base_name}_orig.png"), x[0])
        except Exception as e:
            print(f"⚠️ Error on image {img_path}: {e}")

print("✅ Augmentasi selesai dan disimpan di folder 'preprocessing_images'")