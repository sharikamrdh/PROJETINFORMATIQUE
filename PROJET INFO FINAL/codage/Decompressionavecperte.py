import os
from PIL import Image
import subprocess

def decompress_image(compressed_file_path, output_path):
    """
    Decompresses a compressed image file using Pillow (PIL).

    Args:
        compressed_file_path (str): Path to the compressed image file.
        output_path (str): Path to save the decompressed image.
    """
    try:
        img = Image.open(compressed_file_path)
        img.save(output_path)  # Decompression may involve no additional processing for lossy formats
        print(f"Decompression successful for {compressed_file_path}.")
    except Exception as e:
        print(f"Decompression failed for {compressed_file_path}: {e}")

def decompress_audio(compressed_file_path, output_path):
    """
    Decompresses a compressed audio file using ffmpeg.

    Args:
        compressed_file_path (str): Path to the compressed audio file.
        output_path (str): Path to save the decompressed audio.
    """
    try:
        subprocess.run(['ffmpeg', '-i', compressed_file_path, output_path])
        print(f"Decompression successful for {compressed_file_path}.")
    except Exception as e:
        print(f"Decompression failed for {compressed_file_path}: {e}")

def decompress_folder(folder_path):
    """
    Decompresses files in a folder based on their types.

    Args:
        folder_path (str): Path to the folder containing compressed files.
    """
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        output_path = os.path.join(folder_path, os.path.splitext(filename)[0])  # Remove file extension
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            decompress_image(file_path, output_path)
        elif filename.lower().endswith(('.mp3', '.wav')):
            decompress_audio(file_path, output_path)
        # Add more conditions for other data types as needed


folder_to_decompress = '/path/to/compressed/files'
decompress_folder(folder_to_decompress)
