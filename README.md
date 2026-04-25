# Proyek-Analisis-Bike-Sharing-Dataset

Berikut adalah draf isi berkas `README.md` yang sudah disusun dengan rapi dan profesional. Kamu bisa langsung *copy* seluruh teks di dalam blok kode di bawah ini dan *paste* ke dalam file `README.md` milikmu.

```markdown
# Bike Sharing Data Analysis Dashboard 🚲

Dashboard ini dibuat menggunakan **Streamlit** untuk memvisualisasikan hasil analisis data eksploratif (EDA) dari dataset *Bike Sharing*. Dashboard ini berfokus untuk menyajikan *insight* bisnis terkait pola perilaku pengguna berdasarkan kondisi suhu udara dan tipe hari (hari kerja vs akhir pekan).

## 📁 Struktur Direktori
Pastikan struktur folder Anda terlihat seperti ini sebelum menjalankan aplikasi:
```text
submission/
├── dashboard/
│   ├── main_data.csv
│   └── dashboard.py
├── notebook.ipynb
├── README.md
└── requirements.txt
```

## 🛠️ Setup Environment

Sangat disarankan untuk menjalankan aplikasi ini di dalam *virtual environment* agar dependensi tidak bentrok dengan proyek lain.

### 1. Menggunakan Conda
Jika Anda menggunakan Conda, jalankan perintah berikut di terminal:
```bash
conda create --name dicoding-bike python=3.9
conda activate dicoding-bike
pip install -r requirements.txt
```

### 2. Menggunakan Venv (Bawaan Python)
Jika Anda menggunakan Venv standar, jalankan perintah berikut:

**Windows:**
```bash
python -m venv dicoding-bike
dicoding-bike\Scripts\activate
pip install -r requirements.txt
```

**Mac/Linux:**
```bash
python3 -m venv dicoding-bike
source dicoding-bike/bin/activate
pip install -r requirements.txt
```

## 🚀 Cara Menjalankan Dashboard

1. Buka Terminal atau Command Prompt.
2. Aktifkan environment yang telah dibuat sebelumnya (`dicoding-bike`).
3. Navigasikan direktori terminal Anda ke dalam folder `dashboard`:
   ```bash
   cd letak/folder/submission/dashboard
   ```
4. Jalankan perintah Streamlit berikut:
   ```bash
   streamlit run dashboard.py
   ```
5. Tunggu beberapa saat, dan dashboard akan secara otomatis terbuka di *browser* default Anda (biasanya pada alamat lokal `http://localhost:8501`).
```
