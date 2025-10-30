# 🎥 Real-time Fruit Ripeness Detection

Aplikasi deteksi kematangan buah secara **real-time** menggunakan **webcam** dan **Computer Vision**.

![Demo](https://img.shields.io/badge/Status-Ready-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-red)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.10+-orange)

## ✨ Fitur

- ✅ **Real-time Detection** - Deteksi langsung dari webcam
- ✅ **Multi-Class Classification** - 6 kelas (apel & pisang: mentah, matang, terlalu matang)
- ✅ **Confidence Score** - Tampilan persentase keyakinan prediksi
- ✅ **Visual Feedback** - Warna berbeda untuk setiap status kematangan
- ✅ **FPS Counter** - Monitor performa aplikasi
- ✅ **Probability Display** - Lihat probabilitas semua kelas
- ✅ **Screenshot** - Simpan hasil deteksi

## 🎯 Cara Kerja

1. Aplikasi mengambil frame dari webcam
2. Frame di-preprocess (resize, color conversion)
3. Model MobileNetV2 memprediksi kematangan buah
4. Hasil prediksi ditampilkan dengan overlay visual
5. Proses berulang secara real-time (~30 FPS)

## 📦 Instalasi

### 1. Install Dependencies

Pastikan sudah install requirements utama:
```bash
pip install -r ../requirements.txt
```

Atau install manual dependencies untuk aplikasi ini:
```bash
pip install opencv-python opencv-contrib-python tensorflow numpy
```

### 2. Cek Kamera

Test apakah kamera Anda terdeteksi:
```bash
python utils.py
```

Output yang diharapkan:
```
🔍 Testing utilities...

1. Testing camera...
   ✅ Camera OK

2. Available cameras:
   Camera 0: 1280x720 @ 30.0 FPS

✅ Utilities test complete!
```

## 🚀 Cara Menjalankan

### Menjalankan Aplikasi

```bash
cd app
python webcam_detector.py
```

### Kontrol Keyboard

Saat aplikasi berjalan, Anda dapat menggunakan:

| Tombol | Fungsi |
|--------|--------|
| **Q** atau **ESC** | Keluar dari aplikasi |
| **P** | Toggle tampilan probabilitas semua kelas |
| **S** | Screenshot (simpan frame saat ini) |

## 📸 Screenshot dan Output

Screenshot akan disimpan dengan nama `screenshot_1.jpg`, `screenshot_2.jpg`, dst. di folder app.

## 🎨 Visual Guide

### Warna Indikator

Aplikasi menggunakan **color-coding** untuk memudahkan identifikasi:

- 🟢 **HIJAU** → Buah **Matang** (Siap dikonsumsi)
- 🟠 **ORANYE** → Buah **Mentah** (Belum siap)
- 🔴 **MERAH** → Buah **Terlalu Matang** (Overripe)

### Informasi yang Ditampilkan

1. **Nama Kelas** - Label kematangan buah (Apel/Pisang + Status)
2. **Confidence** - Persentase keyakinan model (0-100%)
3. **Status** - Pesan kematangan (✅ MATANG, ⏳ MENTAH, ⚠️ TERLALU MATANG)
4. **Confidence Bar** - Visual bar di bawah layar
5. **FPS** - Frame per second (performa)
6. **Probabilities** (opsional) - Probabilitas semua kelas

## ⚙️ Konfigurasi

Edit `webcam_detector.py` untuk kustomisasi:

### Ganti Model
```python
MODEL_PATH = Path("../models/model_checkpoints/baseline_cnn_best.keras")  # Ganti ke baseline
```

### Ubah Resolusi Kamera
```python
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)   # Full HD width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)  # Full HD height
```

### Gunakan Kamera External
```python
detector.run(camera_index=1)  # Ganti index kamera (0, 1, 2, ...)
```

### Nonaktifkan Probability Display
```python
detector.run(camera_index=0, show_probabilities=False)
```

## 🐛 Troubleshooting

### Problem: "Tidak dapat membuka webcam"

**Solusi:**
1. Pastikan webcam terpasang dan driver terinstall
2. Cek apakah aplikasi lain sedang menggunakan webcam
3. Coba ganti `camera_index` (0, 1, 2)
4. Jalankan `python utils.py` untuk cek kamera available

### Problem: "Model tidak ditemukan"

**Solusi:**
1. Pastikan sudah melatih model di notebook
2. Cek path model benar: `../models/model_checkpoints/mobilenetv2_best.keras`
3. Pastikan file `.keras` ada di folder tersebut

### Problem: FPS rendah / lag

**Solusi:**
1. Gunakan resolusi kamera lebih rendah (640x480)
2. Tutup aplikasi lain yang berat
3. Gunakan GPU jika tersedia (install `tensorflow-gpu`)
4. Nonaktifkan probability display (tekan 'P')

### Problem: Import Error OpenCV

**Solusi:**
```bash
pip uninstall opencv-python opencv-contrib-python
pip install opencv-python==4.8.0.76
```

## 📊 Performa

Pada sistem dengan spesifikasi:
- **CPU**: Intel i5/i7 atau AMD Ryzen 5/7
- **RAM**: 8GB+
- **Webcam**: 720p

Performa yang diharapkan:
- **FPS**: 25-30 FPS
- **Latency**: < 50ms per frame
- **Accuracy**: ~91% (sesuai hasil training)

## 🔧 Advanced Usage

### Integrasi dengan Aplikasi Lain

```python
from webcam_detector import FruitRipenessDetector

# Inisialisasi
detector = FruitRipenessDetector("path/to/model.keras")

# Prediksi single frame
import cv2
frame = cv2.imread("fruit.jpg")
predicted_class, confidence, probs = detector.predict(frame)
print(f"Result: {predicted_class} ({confidence:.1f}%)")
```

### Batch Processing dari Video File

```python
# Ganti VideoCapture source
cap = cv2.VideoCapture("video.mp4")  # Dari video file
```

### Simpan Output ke Video

```python
# Define codec dan buat VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (1280, 720))

# Di dalam loop:
out.write(frame)

# Jangan lupa release
out.release()
```

## 📝 Tips Penggunaan

1. **Pencahayaan** - Gunakan cahaya yang cukup untuk hasil optimal
2. **Jarak** - Jarak ideal: 20-50 cm dari kamera
3. **Background** - Background polos lebih baik untuk akurasi
4. **Fokus** - Pastikan buah dalam fokus kamera
5. **Satu buah** - Model dilatih untuk 1 buah per prediksi

## 🎓 Penjelasan Teknis

### Preprocessing Pipeline
```
Raw Frame (BGR) 
  → Resize (224x224)
  → BGR to RGB
  → Add Batch Dimension
  → Model Prediction
```

### Model Architecture
- **Base**: MobileNetV2 (pre-trained ImageNet)
- **Input**: 224×224×3 RGB image
- **Output**: 6 classes softmax probabilities
- **Inference Time**: ~30-40ms per frame (CPU)

### Color Space
- OpenCV menggunakan **BGR** format
- TensorFlow/Model menggunakan **RGB** format
- Conversion otomatis dilakukan di preprocessing

## 🔮 Future Improvements

Ide untuk pengembangan selanjutnya:

- [ ] Object detection (deteksi multiple buah)
- [ ] Tracking buah yang bergerak
- [ ] Export ke mobile (TFLite Android/iOS)
- [ ] Web deployment dengan WebRTC
- [ ] Histogram analysis untuk ripeness level
- [ ] Integration dengan database/logging
- [ ] Multi-threading untuk performa lebih baik

## 📚 Referensi

- [OpenCV Documentation](https://docs.opencv.org/)
- [TensorFlow Model Inference](https://www.tensorflow.org/guide/inference)
- [Computer Vision Best Practices](https://github.com/microsoft/computervision-recipes)

## 🆘 Butuh Bantuan?

Jika mengalami masalah:
1. Cek [Troubleshooting](#-troubleshooting) di atas
2. Buka **GitHub Issues** di repository
3. Sertakan informasi: OS, Python version, error message

---

**📧 Contact**: [GitHub @denndoy](https://github.com/denndoy)

**⭐ Jika bermanfaat, berikan star di repository!**
