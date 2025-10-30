# 🚀 Panduan Push ke GitHub

Ikuti langkah-langkah berikut untuk meng-upload proyek ini ke GitHub:

## 1️⃣ Persiapan Repository GitHub

### Buat Repository Baru di GitHub
1. Buka [GitHub](https://github.com) dan login
2. Klik tombol **"+"** di pojok kanan atas → **"New repository"**
3. Isi informasi repository:
   - **Repository name**: `fruits-ripeness-classification`
   - **Description**: `Fruit ripeness classification using Baseline CNN and MobileNetV2 Transfer Learning`
   - **Visibility**: Pilih **Public** atau **Private**
   - **JANGAN** centang "Initialize this repository with README" (sudah ada README.md)
4. Klik **"Create repository"**

## 2️⃣ Inisialisasi Git di Folder Lokal

Buka **Command Prompt** atau **Git Bash** di folder proyek, lalu jalankan:

```bash
cd "c:\Users\Dandy\Documents\My Career\fruits-ripeness-classification"
```

### Inisialisasi Git Repository
```bash
git init
```

### Tambahkan semua file (kecuali yang di .gitignore)
```bash
git add .
```

### Commit perubahan
```bash
git commit -m "Initial commit: Fruits Ripeness Classification Project"
```

## 3️⃣ Hubungkan dengan GitHub Repository

Ganti `yourusername` dengan username GitHub Anda:

```bash
git remote add origin https://github.com/yourusername/fruits-ripeness-classification.git
```

### Verifikasi remote URL
```bash
git remote -v
```

## 4️⃣ Push ke GitHub

### Push ke branch main
```bash
git branch -M main
git push -u origin main
```

Jika diminta username dan password:
- **Username**: Username GitHub Anda
- **Password**: **Gunakan Personal Access Token** (bukan password biasa)

### Cara Membuat Personal Access Token (PAT)
1. Buka GitHub → **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
2. Klik **"Generate new token"** → **"Generate new token (classic)"**
3. Isi **Note**: `Git access for fruits-ripeness-classification`
4. Centang **repo** (semua sub-options)
5. Klik **"Generate token"**
6. **COPY TOKEN** dan simpan (tidak akan ditampilkan lagi!)
7. Gunakan token ini sebagai password saat push

## 5️⃣ Verifikasi Upload

1. Buka repository GitHub Anda di browser
2. Refresh halaman
3. Pastikan file-file berikut ter-upload:
   - ✅ `README.md`
   - ✅ `requirements.txt`
   - ✅ `LICENSE`
   - ✅ `DATASET_INFO.md`
   - ✅ `.gitignore`
   - ✅ Folder `notebooks/`
   - ✅ Folder `results/`
   - ✅ Folder `models/` (hanya struktur, tanpa file .keras)
   - ❌ Folder `dataset_fix/` (TIDAK ter-upload, sesuai .gitignore)

## 6️⃣ Update README.md (Opsional)

Setelah upload, edit `README.md` untuk menambahkan:

### Update URL GitHub Anda
Cari baris ini di README.md:
```markdown
**Dandy**
- GitHub: [@yourusername](https://github.com/yourusername)
```

Ganti `yourusername` dengan username GitHub Anda.

### Commit dan Push Perubahan
```bash
git add README.md
git commit -m "Update GitHub profile links in README"
git push
```

## 📝 Tips Tambahan

### Cek Status Git
```bash
git status
```

### Lihat File yang Diabaikan
File yang diabaikan oleh `.gitignore`:
- Dataset (`dataset_fix/`)
- Model checkpoints (`.keras`, `.h5`)
- Python cache (`__pycache__/`, `*.pyc`)
- Jupyter checkpoint (`.ipynb_checkpoints/`)

### Push Update Selanjutnya
Setelah melakukan perubahan:
```bash
git add .
git commit -m "Deskripsi perubahan yang Anda lakukan"
git push
```

### Clone Repository (di Komputer Lain)
```bash
git clone https://github.com/denndoy/fruits-ripeness-classification.git
cd fruits-ripeness-classification

# Install dependencies
pip install -r requirements.txt

# Download dataset dari Google Drive
# Link: https://drive.google.com/drive/folders/1FGkJ69pB4AXY69pGwN_OsHsF7xyuRycW?usp=sharing
# Ekstrak ke folder dataset_fix/
```

## ⚠️ PENTING: Jangan Upload Dataset!

Dataset **TIDAK** di-upload ke GitHub karena:
1. Ukuran file terlalu besar
2. GitHub membatasi ukuran file (>100MB akan ditolak)
3. Sudah di-ignore di `.gitignore`

Pengguna lain harus menyiapkan dataset sendiri sesuai petunjuk di `DATASET_INFO.md`.

---

## 🆘 Troubleshooting

### Error: "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/yourusername/fruits-ripeness-classification.git
```

### Error: "fatal: not a git repository"
```bash
git init
```

### Error: File terlalu besar (>100MB)
Pastikan `.gitignore` sudah benar dan file besar (dataset, model) tidak ter-add:
```bash
git rm --cached nama-file-besar
git commit -m "Remove large file"
```

### Ingin Mengupload Model (.keras) ke GitHub
Jika model kecil (<100MB), edit `.gitignore` dan hapus baris:
```
models/model_checkpoints/*.keras
```
Lalu:
```bash
git add models/model_checkpoints/*.keras
git commit -m "Add trained model checkpoints"
git push
```

---

📧 **Butuh bantuan?** Buka GitHub Issues di repository Anda!

✅ **Selamat! Proyek Anda sudah di GitHub!** 🎉
