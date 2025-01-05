# Proyek Klasifikasi Gambar dengan Augmentasi Data dan Transfer Learning

Repositori ini berisi pipeline lengkap untuk klasifikasi gambar menggunakan augmentasi data, transfer learning, dan algoritma machine learning tradisional (SVM dan KNN).

## Gambaran Proyek

Proyek ini mengikuti proses berurutan dengan file bernomor untuk kemudahan eksekusi:

### 0. Pengubahan Ukuran Gambar (resize_images.py)
- Mengubah ukuran gambar dari folder "dataset_raw" menjadi 224x224 piksel
- Membuat folder baru "dataset_preprocessed" yang berisi gambar yang telah diubah ukurannya
- Mempertahankan struktur folder asli

### 1. Tahap Augmentasi Pertama (augmentation_1.py)
Menerapkan pipeline augmentasi berikut menggunakan imgaug:
- Penyesuaian kecerahan acak (Multiply: 0.5-1.0)
- Penyesuaian kontras acak (LinearContrast: 0.5-1.5)
- Blur Gaussian (sigma: 0.0-1.0)
- Rotasi acak (-25° sampai 25°)
- Penskalaan acak (0.8-1.2)
- Noise Gaussian aditif (skala: 0-0.05*255)
- Pemotongan acak (0-10%)
- Transformasi affine bertahap acak (skala: 0.01-0.05)

### 2. Tahap Augmentasi Kedua (augmentation_2.py)
Menambahkan transformasi berikut:
- Pembalikan horizontal
- Pembalikan vertikal

### 3. Tahap Augmentasi Ketiga (augmentation_3.py)
Menambahkan konversi grayscale:
- Konversi lengkap ke grayscale (alpha=1.0)

### 4. Penggabungan Dataset (merge_datasets.py)
- Menggabungkan gambar hasil augmentasi dari semua tahap
- Membuat struktur dataset terpadu
- Catatan: Sesuaikan class_names dengan kelas di dataset Anda

### 5. Klasifikasi (classification.py)
Mengimplementasikan klasifikasi gambar menggunakan:
- Ekstraksi fitur dengan transfer learning ResNet50
- Pengklasifikasi SVM dan KNN
- Evaluasi dan analisis model

## Persyaratan

### Lingkungan Pengembangan
- VSCode: [Unduh](https://code.visualstudio.com/download)
- Python 3.10.11: [Unduh](https://www.python.org/downloads/release/python-31011/)

### Pustaka Python
```
numpy==1.26.4
tensorflow==2.9.3
scikit-learn==1.5.2
seaborn==0.13.2
matplotlib==3.9.2
imgaug
```

## Struktur Dataset
Dataset Anda harus mengikuti struktur ini:
```
dataset_raw/
    ├── class1/
    │   ├── image1.jpg
    │   ├── image2.jpg
    │   └── ...
    ├── class2/
    │   ├── image1.jpg
    │   └── ...
    └── ...
```

## Instalasi

1. Klon repositori:
```bash
git clone [url-repositori]
cd [nama-repositori]
```

2. Buat dan aktifkan virtual environment (direkomendasikan):
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Instal paket yang diperlukan:
```bash
pip install -r requirements.txt
```

## Penggunaan

Jalankan file secara berurutan:

1. Ubah ukuran gambar:
```bash
python 0_resize_images.py
```

2. Jalankan tahap augmentasi:
```bash
python 1_augmentation_1.py
python 2_augmentation_2.py
python 3_augmentation_3.py
```

3. Gabungkan dataset hasil augmentasi:
```bash
python 4_merge_datasets.py
```

4. Jalankan klasifikasi:
```bash
python 5_classification.py
```

## Struktur Output

Setelah menjalankan semua script, Anda akan memiliki struktur direktori berikut:
```
project/
    ├── dataset_raw/
    ├── dataset_preprocessed/
    ├── augmented_1/
    ├── augmented_2/
    ├── augmented_3/
    ├── merged_dataset/
    └── results/
        ├── models/
        └── evaluation/
```

## Lisensi

[Tentukan lisensi Anda di sini]

## Kontributor

[Informasi nama/tim Anda]

## Kontak

[Informasi kontak Anda]
