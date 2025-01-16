# src/audio_converter.py
import subprocess

def convert_to_mp3(input_file, output_file):
    command = [
        'ffmpeg',
        '-i', input_file,
        '-vn',
        '-ar', '44100',
        '-ac', '2',
        '-b:a', '192k',
        output_file
    ]
    subprocess.run(command, check=True)
