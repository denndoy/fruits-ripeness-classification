# 🍎🍌 Fruits Ripeness Classification

Proyek klasifikasi kematangan buah menggunakan **Deep Learning** dengan perbandingan antara **Baseline CNN** (Custom Architecture) dan **MobileNetV2 Transfer Learning**.

## 📋 Deskripsi Proyek

Proyek ini bertujuan untuk mengklasifikasikan tingkat kematangan buah (apel dan pisang) ke dalam 6 kategori:
- **Overripe Apple** (Apel Terlalu Matang)
- **Ripe Apple** (Apel Matang)
- **Unripe Apple** (Apel Mentah)
- **Overripe Banana** (Pisang Terlalu Matang)
- **Ripe Banana** (Pisang Matang)
- **Unripe Banana** (Pisang Mentah)

### 🎯 Tujuan
Membandingkan performa antara:
1. **Baseline CNN** - Model convolutional neural network yang dibangun dari awal (from scratch)
2. **MobileNetV2 Transfer Learning** - Memanfaatkan pre-trained model MobileNetV2 dari ImageNet

## 📁 Struktur Folder

```
fruits-ripeness-classification/
│
├── dataset_fix/                      # Dataset gambar buah (tidak di-push ke GitHub)
│   ├── train/                        # Data training (70%)
│   │   ├── overripe_apple/
│   │   ├── overripe_banana/
│   │   ├── ripe_apple/
│   │   ├── ripe_banana/
│   │   ├── unripe_apple/
│   │   └── unripe_banana/
│   ├── validation/                   # Data validasi (15%)
│   │   └── [struktur sama dengan train]
│   └── test/                         # Data testing (15%)
│       └── [struktur sama dengan train]
│
├── notebooks/                        # Jupyter Notebooks
│   └── Baseline_CNN_vs_MobileNetV2.ipynb  # Notebook utama eksperimen
│
├── models/                           # Model yang telah dilatih
│   └── model_checkpoints/            # Checkpoint model terbaik
│       ├── baseline_cnn_best.keras   # Model Baseline CNN terbaik
│       └── mobilenetv2_best.keras    # Model MobileNetV2 terbaik
│
├── results/                          # Hasil evaluasi dan metrik
│   ├── results.csv                   # Ringkasan metrik utama
│   ├── classification_report_baseline.json
│   ├── classification_report_transfer.json
│   ├── confusion_matrix_baseline.csv
│   └── confusion_matrix_transfer.csv
│
├── .gitignore                        # File yang diabaikan Git
└── README.md                         # Dokumentasi proyek (file ini)
```

## 🛠️ Teknologi yang Digunakan

- **Python 3.x**
- **TensorFlow 2.x** / **Keras** - Framework deep learning
- **NumPy** - Operasi numerik
- **Pandas** - Manipulasi data
- **Matplotlib** - Visualisasi
- **Scikit-learn** - Evaluasi metrik
- **PIL/Pillow** - Pemrosesan gambar
- **Jupyter Notebook** - Environment eksperimen

## 📊 Konfigurasi Model

### Hyperparameters
- **Image Size**: 224 × 224 pixels
- **Batch Size**: 32
- **Epochs**: 20 (dengan Early Stopping)
- **Optimizer**: Adam
  - Baseline CNN: Learning Rate = 0.0001
  - MobileNetV2 TL: Learning Rate = 0.0005
- **Loss Function**: Categorical Crossentropy
- **Callbacks**: 
  - Early Stopping (patience=3, monitor='val_loss')
  - ModelCheckpoint (monitor='val_accuracy', save_best_only=True)

### Data Augmentation
Augmentasi diterapkan hanya pada data training:
- Random Rotation (±10°)
- Random Zoom (0.9-1.1×)
- Random Horizontal Flip
- Random Translation (±10%)

### Class Imbalance Handling
- Menggunakan **Class Weights** yang dihitung secara otomatis dengan metode `balanced`
- Membantu model memberikan perhatian lebih pada kelas minoritas

## 🚀 Cara Instalasi

### 1. Clone Repository
```bash
git clone https://github.com/denndoy/fruits-ripeness-classification.git
cd fruits-ripeness-classification
```

### 2. Download Dataset
Download dataset dari Google Drive:
- **Link**: [Google Drive - Fruits Ripeness Dataset](https://drive.google.com/drive/folders/1FGkJ69pB4AXY69pGwN_OsHsF7xyuRycW?usp=sharing)
- Ekstrak dan letakkan di folder `dataset_fix/` di root proyek
- Pastikan struktur folder sesuai dengan dokumentasi

### 3. Install Dependencies
```bash
pip install tensorflow numpy pandas matplotlib scikit-learn pillow jupyter ipywidgets
```

Atau menggunakan file requirements.txt (jika ada):
```bash
pip install -r requirements.txt
```

### 4. Persiapan Dataset
- Download dataset buah Anda
- Susun dataset sesuai struktur folder di atas (`dataset_fix/train`, `validation`, `test`)
- Pastikan setiap folder berisi subfolder untuk setiap kelas

## 📖 Cara Penggunaan

### 1. Training Model
Buka dan jalankan notebook `notebooks/Baseline_CNN_vs_MobileNetV2.ipynb`:
```bash
jupyter notebook notebooks/Baseline_CNN_vs_MobileNetV2.ipynb
```

Jalankan semua cell secara berurutan untuk:
1. Memuat dan menganalisis dataset
2. Melatih Baseline CNN
3. Melatih MobileNetV2 Transfer Learning
4. Evaluasi kedua model pada test set
5. Visualisasi hasil dan perbandingan

### 2. Prediksi Gambar Baru
Di akhir notebook terdapat widget untuk upload dan prediksi gambar baru:
```python
# Jalankan cell terakhir untuk mengaktifkan widget prediksi
# Upload gambar buah
# Klik tombol "Prediksi"
```

### 3. Menggunakan Model yang Sudah Dilatih
```python
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model terbaik
model = tf.keras.models.load_model('models/model_checkpoints/mobilenetv2_best.keras')

# Load dan preprocess gambar
img = Image.open('path/to/image.jpg').convert('RGB').resize((224, 224))
img_array = np.expand_dims(np.array(img), 0)

# Prediksi
predictions = model.predict(img_array)
class_names = ['overripe_apple', 'overripe_banana', 'ripe_apple', 
               'ripe_banana', 'unripe_apple', 'unripe_banana']
predicted_class = class_names[np.argmax(predictions)]
confidence = np.max(predictions) * 100

print(f"Prediksi: {predicted_class} ({confidence:.2f}%)")
```

## 📈 Hasil Eksperimen

### Performa pada Test Set

| Model | Test Accuracy | Precision (Macro) | Recall (Macro) | F1-Score (Macro) |
|-------|---------------|-------------------|----------------|------------------|
| **Baseline CNN** | - | - | - | - |
| **MobileNetV2 TL** | - | - | - | - |

> **Catatan**: Hasil akurasi dan metrik lengkap dapat dilihat di file `results/results.csv` setelah menjalankan eksperimen.

### Analisis
- **MobileNetV2 Transfer Learning** umumnya memberikan performa lebih baik karena:
  - Memanfaatkan feature extraction dari ImageNet
  - Lebih efisien dengan parameter lebih sedikit
  - Konvergensi lebih cepat
  
- **Baseline CNN** cocok untuk:
  - Understanding dan pembelajaran konsep dasar CNN
  - Dataset yang sangat berbeda dari ImageNet
  - Eksperimen arsitektur kustom

### Visualisasi
Notebook menyediakan visualisasi lengkap:
- 📊 Training & Validation Accuracy/Loss curves
- 🔍 Confusion Matrix untuk setiap model
- 📈 Perbandingan side-by-side kedua model
- ⚖️ Analisis overfitting gap

## 🔧 Troubleshooting

### Error: Dataset tidak ditemukan
```
⚠️ Folder dataset_fix tidak ditemukan!
```
**Solusi**: Pastikan dataset sudah disiapkan di folder `dataset_fix/` dengan struktur yang benar.

### Error: Model checkpoint tidak ditemukan
```
⚠️ Gagal memuat model: No such file
```
**Solusi**: Jalankan sel training terlebih dahulu untuk membuat model checkpoint.

### Warning: Class imbalance detected
```
⚠️ IMBALANCE TERDETEKSI! Class weights akan digunakan.
```
**Solusi**: Ini normal. Model otomatis menggunakan class weights untuk menangani imbalance.

## 📝 Catatan Penting

1. **Dataset tidak di-push ke GitHub** karena ukuran file besar
2. **Model checkpoints (.keras)** di-ignore dari Git (ukuran besar)
3. Hasil evaluasi (CSV/JSON) di-push ke GitHub sebagai referensi
4. Pastikan TensorFlow versi terbaru untuk kompatibilitas format `.keras`

## 🤝 Kontribusi

Kontribusi, issues, dan feature requests sangat diterima!

## 📄 Lisensi

[MIT License](LICENSE) - Silakan gunakan untuk keperluan akademis dan komersial.

## 👨‍💻 Author

**Dandy**
- GitHub: [@denndoy](https://github.com/denndoy)
- Repository: [fruits-ripeness-classification](https://github.com/denndoy/fruits-ripeness-classification)

## 🙏 Acknowledgments

- Dataset: [Fruits Ripeness Dataset - Google Drive](https://drive.google.com/drive/folders/1FGkJ69pB4AXY69pGwN_OsHsF7xyuRycW?usp=sharing)
- MobileNetV2: [Google Research](https://arxiv.org/abs/1801.04381)
- TensorFlow/Keras Documentation

---

⭐ Jika proyek ini bermanfaat, silakan berikan star pada repository ini!
