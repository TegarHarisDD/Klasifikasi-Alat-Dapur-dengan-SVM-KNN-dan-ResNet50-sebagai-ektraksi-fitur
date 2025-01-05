import os
import shutil

# Tentukan path folder dataset
dataset_dir = 'dataset_preprocessed'

# Daftar kelas yang ada
class_names = [
    'alat_kupas', 'centong_nasi', 'garpu', 'gunting', 
    'pisau', 'sendok'
]

#class_names = [
#   'BOTTLE_OPENER', 'BREAD_KNIFE', 'CAN_OPENER', 'DESSERT_SPOON', 
#   'DINNER_FORK', 'DINNER_KNIFE', 'FISH_SLICE', 'KITCHEN_KNIFE'
#]

# Untuk setiap kelas, pindahkan gambar augmentasi ke folder kelas
for class_name in class_names:
    augmentasi_dir = os.path.join(dataset_dir, class_name, 'augmented')
    class_dir = os.path.join(dataset_dir, class_name)

    # Pastikan folder class dir ada
    os.makedirs(class_dir, exist_ok=True)

    # Cek apakah folder augmentasi ada
    if os.path.exists(augmentasi_dir):
        # Pindahkan semua gambar di folder augmentasi ke folder kelas
        for image_name in os.listdir(augmentasi_dir):
            image_path = os.path.join(augmentasi_dir, image_name)
            if os.path.isfile(image_path):
                # Pindahkan gambar
                shutil.move(image_path, os.path.join(class_dir, image_name))

        # Hapus folder augmentasi setelah dipindahkan
        os.rmdir(augmentasi_dir)
    else:
        print(f"Folder augmentasi untuk {class_name} tidak ditemukan.")
