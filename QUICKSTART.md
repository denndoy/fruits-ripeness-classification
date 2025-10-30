# 🚀 Quick Start Guide - Real-time Detection

Panduan cepat untuk menjalankan aplikasi deteksi kematangan buah secara real-time.

## ⚡ Langkah Cepat (5 Menit)

### 1. Install Dependencies
```bash
pip install opencv-python tensorflow numpy
```

### 2. Jalankan Aplikasi
```bash
cd app
python webcam_detector.py
```

### 3. Gunakan Aplikasi
- Arahkan webcam ke buah (apel atau pisang)
- Lihat hasil prediksi real-time
- Tekan `Q` untuk keluar

---

## 📋 Checklist Persiapan

Sebelum menjalankan, pastikan:

- [ ] ✅ Python 3.8+ terinstall
- [ ] ✅ Webcam berfungsi dengan baik
- [ ] ✅ Model sudah dilatih (`mobilenetv2_best.keras` ada di `models/model_checkpoints/`)
- [ ] ✅ Dependencies sudah terinstall

---

## 🧪 Test Kamera

Cek apakah kamera terdeteksi:

```bash
cd app
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

---

## 🎮 Kontrol Aplikasi

| Tombol | Fungsi |
|--------|--------|
| `Q` atau `ESC` | Keluar dari aplikasi |
| `P` | Toggle tampilan probabilitas |
| `S` | Screenshot (simpan gambar) |

---

## 💡 Tips Untuk Hasil Terbaik

1. **Pencahayaan** ☀️
   - Gunakan cahaya yang cukup terang
   - Hindari backlight (cahaya dari belakang)

2. **Jarak** 📏
   - Jarak ideal: 20-50 cm dari kamera
   - Buah harus terlihat jelas di frame

3. **Background** 🎨
   - Background polos lebih baik
   - Hindari background yang ramai

4. **Fokus** 🎯
   - Pastikan buah dalam fokus kamera
   - Satu buah per prediksi untuk akurasi optimal

---

## ❌ Troubleshooting Cepat

### Problem: "Tidak dapat membuka webcam"
```bash
# Cek kamera available
python utils.py

# Jika ada multiple kamera, edit webcam_detector.py:
# Ganti camera_index=0 menjadi 1, 2, dst
```

### Problem: "Model tidak ditemukan"
```bash
# Pastikan Anda sudah melatih model di notebook
# Cek apakah file ada:
ls ../models/model_checkpoints/mobilenetv2_best.keras
```

### Problem: FPS rendah / lag
```bash
# Solusi: Nonaktifkan probability display
# Tekan 'P' saat aplikasi berjalan
```

---

## 🎬 Demo Video

Hasil yang diharapkan:

```
┌────────────────────────────────────┐
│  Apel Matang                       │
│  Confidence: 94.3%                 │
│  ✅ MATANG (SIAP KONSUMSI)         │
│                                    │
│  [====Webcam Feed Here====]        │
│                                    │
│  FPS: 28.5                         │
│  [████████████████░░░░░░] 94%      │
└────────────────────────────────────┘
```

---

## 📚 Dokumentasi Lengkap

Untuk fitur advanced dan customization, baca:
- **`app/README.md`** - Dokumentasi lengkap aplikasi
- **Main `README.md`** - Dokumentasi proyek keseluruhan

---

## 🆘 Butuh Bantuan?

1. Baca troubleshooting di `app/README.md`
2. Cek GitHub Issues
3. Test utilities dengan `python utils.py`

---

**Selamat mencoba! 🎉**
