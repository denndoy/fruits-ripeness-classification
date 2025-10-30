# 📊 Cara Update Hasil Eksperimen di README

Setelah menjalankan eksperimen, update tabel hasil di `README.md` dengan data aktual dari file `results/results.csv`.

## Langkah-langkah:

### 1. Buka file `results/results.csv`
Anda akan melihat data seperti ini:
```csv
Model,Test_Accuracy,Test_Precision_Macro,Test_Recall_Macro,Test_F1_Score_Macro,...
Baseline CNN,0.8523,0.8456,0.8498,0.8476,...
MobileNetV2 Transfer Learning,0.9156,0.9089,0.9112,0.9100,...
```

### 2. Update Tabel di README.md

Cari bagian ini di `README.md`:

```markdown
| Model | Test Accuracy | Precision (Macro) | Recall (Macro) | F1-Score (Macro) |
|-------|---------------|-------------------|----------------|------------------|
| **Baseline CNN** | - | - | - | - |
| **MobileNetV2 TL** | - | - | - | - |
```

Ganti dengan hasil aktual (contoh):

```markdown
| Model | Test Accuracy | Precision (Macro) | Recall (Macro) | F1-Score (Macro) |
|-------|---------------|-------------------|----------------|------------------|
| **Baseline CNN** | 0.8523 | 0.8456 | 0.8498 | 0.8476 |
| **MobileNetV2 TL** | 0.9156 | 0.9089 | 0.9112 | 0.9100 |
```

### 3. Tambahkan Insight di Section Analisis

Tambahkan analisis hasil di bagian `### Analisis`:

```markdown
### Analisis

**Hasil Eksperimen:**
- MobileNetV2 Transfer Learning mencapai akurasi **91.56%**, lebih tinggi **6.33%** dari Baseline CNN
- Precision, Recall, dan F1-Score MobileNetV2 juga lebih tinggi di semua metrik
- Baseline CNN mencapai akurasi **85.23%**, cukup baik untuk model yang dibangun from scratch

**Kesimpulan:**
- **MobileNetV2 Transfer Learning** memberikan performa terbaik untuk klasifikasi kematangan buah
- Pre-trained weights dari ImageNet membantu model belajar lebih cepat dan akurat
- Untuk deployment production, disarankan menggunakan MobileNetV2
```

### 4. (Opsional) Tambahkan Screenshot Confusion Matrix

Tambahkan gambar confusion matrix di folder `results/`:
1. Save confusion matrix dari notebook sebagai PNG
2. Upload ke folder `results/` dengan nama `confusion_matrix_baseline.png` dan `confusion_matrix_transfer.png`
3. Tambahkan di README:

```markdown
### Confusion Matrix

**Baseline CNN:**
![Confusion Matrix - Baseline CNN](results/confusion_matrix_baseline.png)

**MobileNetV2 Transfer Learning:**
![Confusion Matrix - MobileNetV2](results/confusion_matrix_transfer.png)
```

### 5. Commit dan Push Update

```bash
git add README.md results/
git commit -m "Update hasil eksperimen dan analisis"
git push
```

---

## 📝 Template Analisis Lengkap

Gunakan template ini untuk menulis analisis yang comprehensive:

```markdown
## 📈 Hasil Eksperimen

### Performa pada Test Set

| Model | Test Accuracy | Precision (Macro) | Recall (Macro) | F1-Score (Macro) | Epochs Trained |
|-------|---------------|-------------------|----------------|------------------|----------------|
| **Baseline CNN** | X.XXXX | X.XXXX | X.XXXX | X.XXXX | XX |
| **MobileNetV2 TL** | X.XXXX | X.XXXX | X.XXXX | X.XXXX | XX |

### Analisis Performa

**Kelebihan MobileNetV2 Transfer Learning:**
- ✅ Akurasi lebih tinggi (+X.XX%)
- ✅ Konvergensi lebih cepat (X epochs vs XX epochs)
- ✅ Lebih stabil (gap overfitting lebih kecil)
- ✅ Model lebih ringan dan efisien

**Kelebihan Baseline CNN:**
- ✅ Lebih mudah dipahami dan di-customize
- ✅ Tidak memerlukan pre-trained weights
- ✅ Lebih fleksibel untuk arsitektur custom

### Analisis Per-Kelas

Kelas dengan performa terbaik:
- **[Nama Kelas]**: Precision XX%, Recall XX%

Kelas yang challenging:
- **[Nama Kelas]**: Precision XX%, Recall XX% (sering dikelirukan dengan [Kelas Lain])

### Rekomendasi

1. **Untuk Production**: Gunakan **MobileNetV2 Transfer Learning**
2. **Untuk Pembelajaran**: Mulai dengan **Baseline CNN**
3. **Improvement Ideas**:
   - Fine-tuning beberapa layer terakhir MobileNetV2
   - Menambah data augmentation
   - Menggunakan ensemble dari kedua model
```

---

✅ **Dokumentasi yang baik membuat proyek Anda lebih profesional dan mudah dipahami!**
