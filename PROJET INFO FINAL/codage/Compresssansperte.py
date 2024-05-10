
import os
import zlib

def compress_folder(folder_path):
    """
    Compresses files within a specified folder that are JPEG, PNG, or MP4 format.

    Args:
        folder_path (str): The path to the folder containing files to compress.
    """
    # Iterate over each file in the folder
    for filename in os.listdir(folder_path):
        # Check if the file has one of the supported extensions
        if filename.endswith(('.jpeg', '.png', '.mp4')):
            # Construct the full path to the file
            file_path = os.path.join(folder_path, filename)
            
            # Open the file in binary read mode
            with open(file_path, 'rb') as f:
                # Read the contents of the file
                data = f.read()
                
                # Compress the data using zlib
                compressed_data = zlib.compress(data)
                
                # Construct the path for the compressed file
                compressed_file_path = os.path.join(folder_path, filename + '.compressed')
                
                # Write the compressed data to a new file
                with open(compressed_file_path, 'wb') as compressed_file:
                    compressed_file.write(compressed_data)


folder_to_compress = '/Users/lauramridha/Documents/compression image'
compress_folder(folder_to_compress)
