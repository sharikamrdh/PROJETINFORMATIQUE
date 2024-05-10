import os
import zlib

def compress_file(file_path):
    """
    Compresses a file using zlib compression algorithm.

    Args:
        file_path (str): The path to the file to be compressed.
    """
    try:
        # Read the file content
        with open(file_path, 'rb') as f:
            data = f.read()
            # Compress the file content
            compressed_data = zlib.compress(data)
        
        # Write the compressed data to a new file with .zlib extension
        compressed_file_path = f'{file_path}.zlib'
        with open(compressed_file_path, 'wb') as f_out:
            f_out.write(compressed_data)
        
        print(f"File '{file_path}' compressed successfully.")
    
    except Exception as e:
        print(f"Failed to compress file '{file_path}': {e}")

def generate_compression_report(directory_path):
    """
    Generates a compression report for files in a directory.

    Args:
        directory_path (str): The path to the directory containing files to compress.
    """
    num_files = 0
    original_size = 0
    compressed_size = 0
    
    # Traverse the directory to compress files and calculate sizes
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            num_files += 1
            file_path = os.path.join(root, file)
            original_size += os.path.getsize(file_path)
            
            # Compress the file and update compressed size
            compress_file(file_path)
            compressed_file_path = f'{file_path}.zlib'
            if os.path.exists(compressed_file_path):
                compressed_size += os.path.getsize(compressed_file_path)

    # Check if any files were found for compression
    if num_files == 0:
        print("No files found for compression.")
        return
    
    # Calculate compression ratio
    compression_ratio = compressed_size / original_size
    
    # Print compression report
    print(f'Number of files compressed: {num_files}')
    print(f'Original size: {original_size} bytes')
    print(f'Compressed size: {compressed_size} bytes')
    print(f'Compression ratio: {compression_ratio:.2f}')

if __name__ == '__main__':
    # Get directory path from user input
    directory_path = input("Enter the directory path: ")
    
    # Generate compression report for the specified directory
    generate_compression_report(directory_path)
