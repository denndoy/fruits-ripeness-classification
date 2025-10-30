# Dataset Information

## 📊 Dataset Overview

Dataset ini berisi gambar buah (apel dan pisang) dengan berbagai tingkat kematangan yang digunakan untuk klasifikasi menggunakan Deep Learning.

## 📁 Struktur Dataset

```
dataset_fix/
├── train/           # Data untuk training (70%)
├── validation/      # Data untuk validasi (15%)
└── test/            # Data untuk testing (15%)
```

Setiap folder (`train`, `validation`, `test`) memiliki 6 subfolder:

### Kelas Dataset
1. **overripe_apple** - Apel yang terlalu matang
2. **ripe_apple** - Apel yang matang (siap dikonsumsi)
3. **unripe_apple** - Apel yang masih mentah
4. **overripe_banana** - Pisang yang terlalu matang
5. **ripe_banana** - Pisang yang matang (siap dikonsumsi)
6. **unripe_banana** - Pisang yang masih mentah

## 📝 Cara Menggunakan Dataset

### 1. Persiapan Dataset

Dataset **TIDAK DISERTAKAN** dalam repository GitHub karena ukuran file yang besar. Anda perlu menyiapkan dataset sendiri dengan struktur berikut:

```
dataset_fix/
├── train/
│   ├── overripe_apple/
│   │   ├── image1.jpg
│   │   ├── image2.jpg
│   │   └── ...
│   ├── overripe_banana/
│   ├── ripe_apple/
│   ├── ripe_banana/
│   ├── unripe_apple/
│   └── unripe_banana/
├── validation/
│   └── [struktur sama dengan train]
└── test/
    └── [struktur sama dengan train]
```

### 2. Format Gambar
- **Format yang didukung**: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`, `.tiff`
- **Ukuran**: Gambar akan otomatis di-resize menjadi 224×224 pixels
- **Channel**: RGB (3 channels)

### 3. Rekomendasi Split Data
- **Training**: 70% dari total data
- **Validation**: 15% dari total data
- **Testing**: 15% dari total data

Pastikan distribusi kelas seimbang di setiap split untuk hasil optimal.

## 🔄 Data Augmentation

Data augmentation diterapkan **HANYA** pada data training untuk meningkatkan generalisasi model:

- **Random Rotation**: ±10°
- **Random Zoom**: 0.9-1.1×
- **Random Horizontal Flip**: 50% probabilitas
- **Random Translation**: ±10% (horizontal dan vertikal)

Data validation dan test **TIDAK** menggunakan augmentation untuk evaluasi yang fair.

## ⚖️ Class Imbalance

Jika terjadi imbalance (ketidakseimbangan jumlah gambar antar kelas):
- Model secara otomatis menghitung **Class Weights**
- Menggunakan metode `balanced` dari scikit-learn
- Class dengan sampel lebih sedikit akan mendapat bobot lebih tinggi

## 📌 Catatan Penting

1. **Path Dataset**: Pastikan path di notebook sudah benar (`./dataset_fix`)
2. **Naming Convention**: Gunakan nama folder persis seperti yang tercantum di atas
3. **Quality**: Gunakan gambar berkualitas baik untuk hasil optimal
4. **Variasi**: Tambahkan variasi kondisi pencahayaan, sudut pandang, dan background

## 🔗 Sumber Dataset

Dataset yang digunakan dalam proyek ini tersedia di:
- **Link Dataset**: [Google Drive - Fruits Ripeness Dataset](https://drive.google.com/drive/folders/1FGkJ69pB4AXY69pGwN_OsHsF7xyuRycW?usp=sharing)
- **Format**: Gambar JPG/PNG terorganisir dalam folder per kelas
- **Akses**: Public (dapat diakses siapa saja)

### Cara Download Dataset
1. Klik link Google Drive di atas
2. Download folder `dataset_fix` atau download per subfolder
3. Ekstrak dan letakkan di root folder proyek dengan nama `dataset_fix/`
4. Pastikan struktur folder sesuai dengan yang dijelaskan di dokumentasi ini

---

📧 Untuk pertanyaan terkait dataset, silakan hubungi author melalui GitHub Issues.
