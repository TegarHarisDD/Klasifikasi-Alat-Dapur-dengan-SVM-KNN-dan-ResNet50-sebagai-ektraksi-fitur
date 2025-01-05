# Klasifikasi-Alat-Dapur-dengan-SVM-KNN-dan-ResNet50-sebagai-ektraksi-fitur

Image Classification Pipeline
Repository ini berisi pipeline untuk preprocessing, augmentasi, dan klasifikasi gambar menggunakan pendekatan berbasis transfer learning dengan ResNet50. Berikut adalah urutan langkah-langkah untuk menjalankan file dalam repository ini:

0. Resize Dataset
File: 0_resize.py

Fungsi: Mengubah ukuran semua gambar di dataset raw Anda menjadi resolusi 224x224.
Input: Folder dataset raw (default: dataset_raw), dapat diganti sesuai nama dan path dataset Anda.
Output: Folder dataset yang telah diproses dengan nama dataset_preprocessed.
1. Augmentasi Tahap 1
File: 1_augmentasi1.ipynb

Menggunakan imgaug, augmentasi gambar dilakukan dengan pipeline berikut:

Ubah kecerahan secara acak.
Ubah kontras secara acak.
Tambahkan Gaussian blur.
Rotasi gambar secara acak.
Skala gambar secara acak.
Tambahkan noise Gaussian.
Potong gambar secara acak.
Transformasi affine secara acak.
2. Augmentasi Tahap 2
File: 2_augmentasi2.ipynb

Menambahkan dua augmentasi tambahan:

Flip horizontal penuh.
Flip vertikal penuh.
3. Augmentasi Tahap 3
File: 3_augmentasi3.ipynb

Menambahkan konversi penuh ke grayscale (grayscale alpha 1.0).

4. Merge Dataset
File: 4_merge.py

Fungsi: Menggabungkan semua hasil augmentasi ke dalam folder Augmented sesuai dengan kelas dataset.
Catatan: Pastikan Anda menyesuaikan variabel class_names agar sesuai dengan kelas di dataset Anda.
5. Klasifikasi Gambar
File: 5_classification.ipynb

Tahapan klasifikasi dilakukan dengan langkah berikut:

Persiapan dataset: Membagi dataset menjadi train-test split dan melakukan preprocessing.
Ekstraksi fitur: Menggunakan model pre-trained ResNet50 untuk mendapatkan representasi fitur dari gambar.
Klasifikasi: Implementasi algoritma SVM dan KNN untuk klasifikasi berbasis fitur.
Evaluasi: Melakukan evaluasi akurasi dan analisis hasil klasifikasi.
Persyaratan Sistem
VSCode: Download VSCode
Python 3.10.11: Download Python
Library yang Dibutuhkan
Pastikan Anda menginstal library berikut:

NumPy: 1.26.4
TensorFlow: 2.9.3
Scikit-learn: 1.5.2
Seaborn: 0.13.2
Matplotlib: 3.9.2
Struktur Dataset
Dataset harus memiliki struktur sebagai berikut:

markdown
Copy code
dataset/
    ├── class1/
    │   ├── image1.jpg
    │   ├── image2.jpg
    │   └── ...
    ├── class2/
    └── ...
