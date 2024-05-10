import os
import zlib

def decompress_file(compressed_file_path):
    """
    Decompresses a single compressed file.

    Args:
        compressed_file_path (str): Path to the compressed file.

    Returns:
        bytes: Decompressed data if successful, None otherwise.
    """
    try:
        with open(compressed_file_path, 'rb') as f:
            compressed_data = f.read()
            decompressed_data = zlib.decompress(compressed_data)
            return decompressed_data
    except zlib.error as e:
        print("Error during decompression:", e)
        return None

def decompress_folder(folder_path):
    """
    Decompresses all files with '.compressed' extension in a folder.

    Args:
        folder_path (str): Path to the folder containing compressed files.
    """
    for filename in os.listdir(folder_path):
        if filename.endswith('.compressed'):
            compressed_file_path = os.path.join(folder_path, filename)
            decompressed_file_path = os.path.join(folder_path, os.path.splitext(filename)[0])  # Remove file extension
            decompressed_data = decompress_file(compressed_file_path)
            if decompressed_data:
                with open(decompressed_file_path, 'wb') as f:
                    f.write(decompressed_data)
                print(f"Decompression successful for {filename}.")
            else:
                print(f"Decompression failed for {filename}.")

def main():
    folder_to_decompress = '/home/zaineb/Desktop/cats'
    if not os.path.exists(folder_to_decompress):
        print(f"Folder '{folder_to_decompress}' does not exist.")
        return
    decompress_folder(folder_to_decompress)


