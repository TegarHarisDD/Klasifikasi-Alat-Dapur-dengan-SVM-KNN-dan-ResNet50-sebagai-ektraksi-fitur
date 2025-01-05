import os
from PIL import Image #PIL: 11.0.0 (pip install Pillow==11.0.0)

def resize_images_in_folder(input_folder, output_folder, target_size=(224, 224)):
    # Traverse the folder structure
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(('.jpg', '.jpeg', '.png')):
                # Get the full path to the image file
                img_path = os.path.join(root, file)
                
                # Open and resize the image
                with Image.open(img_path) as img:
                    img_resized = img.resize(target_size)
                    
                    # Save the resized image to the output folder
                    class_folder = os.path.relpath(root, input_folder)
                    output_class_folder = os.path.join(output_folder, class_folder)
                    os.makedirs(output_class_folder, exist_ok=True)
                    
                    # Save the image
                    img_resized.save(os.path.join(output_class_folder, file))

input_folder = 'dataset_raw'  # Path to the original dataset folder
output_folder = 'dataset_preprocessed'  # Path to save the resized images
target_size = (224, 224)  # Desired image size (width, height)

resize_images_in_folder(input_folder, output_folder, target_size)
