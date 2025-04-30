# Batik Classification with Resnet (Google Colab ver)
This project implements deep learning models using the ResNet architecture to classify 25 traditional Indonesian batik patterns. It is optimized to run on **Google Colab** with automatic data splitting, training, and evaluation.

---

## 📁 Dataset Structure

Each subfolder represents one batik class. The script will split them into:

// will be added later
- 80% training
- 10% validation
- 10% testing

---

## ⚙️ Features

- ✅ Automatic dataset splitting using `splitfolders`
- ✅ Multiple ResNet architectures (ResNet18–152, ResNet110 custom)
- ✅ Data augmentation during training
- ✅ Model evaluation with:
  - Accuracy
  - Precision
  - Recall
  - F1-Score
  - Confusion Matrix
- ✅ Saves training history plots and best model
- ✅ Export performance summary to CSV

---

## 🧠 Notes
- `ResNet110` is manually constructed using stacked `BasicBlock` layers.
- Number of classes is inferred from the training directory.
- You can adjust hyperparameters like:
  - `BATCH_SIZE`
  - `NUM_EPOCHS`
  - `learning_rate`

---

## 📌 Credits

This project was developed as part of my thesis on classifying traditional Indonesian batik patterns using deep learning. The model will also be adapted for mobile deployment.
Special thanks to my thesis advisor and colleagues for their support and feedback throughout the development process <3.

---

## 📬 Contact
For inquiries or feedback, please contact: [nexuszeoviennazabrizkie@gmail.com]
Insta: @hydie.exe
