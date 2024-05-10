#COMPRESSION AVEC PERTE DE DONNÉES

import os
from PIL import Image
import librosa
from pydub import AudioSegment
import gzip
import shutil
import subprocess

# Function to compress images using PIL
def compress_image(file_path, output_path):
    img = Image.open(file_path)
    # Specify a compatible image format for saving, such as JPEG
    img.save(output_path, format='JPEG', quality=50)  # Adjust quality parameter as needed



# Function to compress audio using librosa
def compress_audio(file_path, output_path):
    y, sr = librosa.load(file_path)
    librosa.output.write_wav(output_path, y, sr, norm=False)  # Adjust normalization as needed


# Function to compress other audio formats using pydub
def compress_other_audio(file_path, output_path):
    sound = AudioSegment.from_file(file_path)


# Function to compress text files using gzip
def compress_text(file_path, output_path):
    with open(file_path, 'rb') as f_in:
        with gzip.open(output_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


# Function to compress video files using ffmpeg
def compress_video(file_path, output_path):
    subprocess.call(['ffmpeg', '-i', file_path, '-c:v', 'libx264', '-crf', '23', '-c:a', 'aac', '-b:a', '128k', output_path])


# Function to compress PDF files using ghostscript
def compress_pdf(file_path, output_path):
    subprocess.call(['gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4', '-dPDFSETTINGS=/ebook', '-dNOPAUSE', '-dQUIET', '-dBATCH', '-sOutputFile=' + output_path, file_path])


# Function to compress Microsoft Office files using unoconv (requires unoconv to be installed)
def compress_office(file_path, output_path):
    subprocess.call(['unoconv', '-f', 'pdf', '--stdout', file_path, '|', 'gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4', '-dPDFSETTINGS=/ebook', '-dNOPAUSE', '-dQUIET', '-dBATCH', '-sOutputFile=' + output_path, '-'])


# Function to compress files in a folder
def compress_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        output_path = os.path.join(folder_path, filename + '.compressed')

        """if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            compress_image(file_path, output_path)
        elif filename.lower().endswith(('.mp3', '.wav')):
            compress_audio(file_path, output_path)
        """
        if filename.lower().endswith('.txt'):
            compress_text(file_path, output_path)
        elif filename.lower().endswith(('.mp4', '.avi', '.mov')):
            compress_video(file_path, output_path)
        elif filename.lower().endswith('.pdf'):
            compress_pdf(file_path, output_path)
        elif filename.lower().endswith(('.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx')):
            compress_office(file_path, output_path)

folder_to_compress = '/Users/lauramridha/Documents/Bulletin'
compress_folder(folder_to_compress)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python compress.py <folder_path>")
        sys.exit(0)
    file_path = sys.argv[1]
    compress_folder(folder_to_compress)