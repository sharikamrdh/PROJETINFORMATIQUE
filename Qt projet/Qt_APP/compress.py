#!/usr/bin/python
# -*- coding: utf-8 -*-

import zlib
import os
import sys

def compressFolder(folderPath):
    for filename in os.listdir(folderPath):
        if filename.endswith('.jpeg') or filename.endswith('.png') or filename.endswith('.mp4'):
            file_path = os.path.join(folderPath, filename)
            with open(file_path, 'rb') as f:
                data = f.read()
            print(f"Taille des données avant compression ({filename}): {len(data)} bytes")
            compressed_data = zlib.compress(data)
            print(f"Taille des données après compression ({filename}): {len(compressed_data)} bytes")
            compressed_file_path = os.path.join(folderPath, filename + '.compressed')
            with open(compressed_file_path, 'wb') as f:
                f.write(compressed_data)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python compress.py <folder_path>")
        sys.exit(0)
    folder_to_compress = sys.argv[1]
    compressFolder(folder_to_compress)
