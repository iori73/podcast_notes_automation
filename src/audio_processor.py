# src/audio_processor.py
import os
import subprocess
import requests
from pathlib import Path

class AudioProcessor:
    def __init__(self):
        self.download_dir = Path('downloads')
        self.download_dir.mkdir(exist_ok=True)

    def download_audio(self, url, filename):
        """音声ファイルをダウンロード"""
        response = requests.get(url, stream=True)
        filepath = self.download_dir / filename
        
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        return filepath

    def convert_to_mp3(self, input_file):
        """MP4からMP3に変換"""
        output_file = input_file.with_suffix('.mp3')
        command = [
            'ffmpeg',
            '-i', str(input_file),
            '-vn',  # 映像を除外
            '-ar', '44100',  # サンプリングレート
            '-ac', '2',  # ステレオ
            '-b:a', '192k',  # ビットレート
            str(output_file)
        ]
        
        try:
            subprocess.run(command, check=True, capture_output=True)
            return output_file
        except subprocess.CalledProcessError as e:
            print(f"変換エラー: {e.stderr.decode()}")
            raise
