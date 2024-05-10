import os
from PIL import Image
import librosa
from pydub import AudioSegment
import gzip
import shutil
import subprocess

def compress_image(file_path, output_path, quality=50):
    """
    Compresses an image file using PIL.

    Args:
        file_path (str): The path to the input image file.
        output_path (str): The path to save the compressed image.
        quality (int): Compression quality, a value between 0 and 100 (default: 50).
    """
    img = Image.open(file_path)
    img.save(output_path, format='JPEG', quality=quality)

def compress_audio(file_path, output_path, format='wav', bitrate="64k"):
    """
    Compresses an audio file using librosa or pydub.

    Args:
        file_path (str): The path to the input audio file.
        output_path (str): The path to save the compressed audio.
        format (str): Output audio format, 'wav' or 'mp3' (default: 'wav').
        bitrate (str): Audio bitrate for MP3 format (default: "64k").
    """
    if format == 'wav':
        y, sr = librosa.load(file_path)
        librosa.output.write_wav(output_path, y, sr, norm=False)
    elif format == 'mp3':
        sound = AudioSegment.from_file(file_path)
        sound.export(output_path, format="mp3", bitrate=bitrate)

def compress_text(file_path, output_path):
    """
    Compresses a text file using gzip.

    Args:
        file_path (str): The path to the input text file.
        output_path (str): The path to save the compressed text file.
    """
    with open(file_path, 'rb') as f_in:
        with gzip.open(output_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

def compress_video(file_path, output_path):
    """
    Compresses a video file using ffmpeg.

    Args:
        file_path (str): The path to the input video file.
        output_path (str): The path to save the compressed video.
    """
    subprocess.run(['ffmpeg', '-i', file_path, '-c:v', 'libx264', '-crf', '23', '-c:a', 'aac', '-b:a', '128k', output_path])

def compress_pdf(file_path, output_path):
    """
    Compresses a PDF file using ghostscript.

    Args:
        file_path (str): The path to the input PDF file.
        output_path (str): The path to save the compressed PDF file.
    """
    subprocess.run(['gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4', '-dPDFSETTINGS=/ebook', '-dNOPAUSE', '-dQUIET', '-dBATCH', '-sOutputFile=' + output_path, file_path])

def compress_office(file_path, output_path):
    """
    Converts and compresses a Microsoft Office file to PDF using unoconv and ghostscript.

    Args:
        file_path (str): The path to the input Microsoft Office file.
        output_path (str): The path to save the compressed PDF file.
    """
    subprocess.run(['unoconv', '-f', 'pdf', '--stdout', file_path, '|', 'gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4', '-dPDFSETTINGS=/ebook', '-dNOPAUSE', '-dQUIET', '-dBATCH', '-sOutputFile=' + output_path, '-'])

def compress_folder(folder_path):
    """
    Compresses files in a folder based on their types.

    Args:
        folder_path (str): The path to the folder containing files to compress.
    """
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        output_path = os.path.join(folder_path, filename + '.compressed')
        # Identify the file type and apply corresponding compression method
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            compress_image(file_path, output_path)
        elif filename.lower().endswith(('.mp3', '.wav')):
            compress_audio(file_path, output_path)
        elif filename.lower().endswith('.txt'):
            compress_text(file_path, output_path)
        elif filename.lower().endswith(('.mp4', '.avi', '.mov')):
            compress_video(file_path, output_path)
        elif filename.lower().endswith('.pdf'):
            compress_pdf(file_path, output_path)
        elif filename.lower().endswith(('.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx')):
            compress_office(file_path, output_path)

# Example usage
folder_to_compress = '/home/zaineb/Desktop/animals'
compress_folder(folder_to_compress)
