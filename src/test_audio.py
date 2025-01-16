# # src/test_audio.py
# from audio_processor import AudioProcessor

# def test_audio_conversion():
#     processor = AudioProcessor()
    
#     # テスト用の音声ファイルURL（実際のURLに置き換えてください）
#     test_url = "https://example.com/test.mp4"
    
#     try:
#         # ダウンロード
#         print("ファイルをダウンロード中...")
#         input_file = processor.download_audio(test_url, "test.mp4")
        
#         # 変換
#         print("MP3に変換中...")
#         output_file = processor.convert_to_mp3(input_file)
        
#         print(f"変換完了: {output_file}")
        
#     except Exception as e:
#         print(f"エラーが発生しました: {str(e)}")

# if __name__ == "__main__":
#     test_audio_conversion()


# src/test_audio.py
from pathlib import Path
from audio_processor import AudioProcessor
import os

def test_audio_conversion():
    processor = AudioProcessor()
    
    # ダウンロードしたMP4ファイルのパスを指定
    input_file = Path('downloads/test_1.mp4')  # ここにダウンロードしたファイルを配置
    
    try:
        # 変換
        print("MP3に変換中...")
        output_file = processor.convert_to_mp3(input_file)
        
        print(f"変換完了: {output_file}")
        
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")

if __name__ == "__main__":
    test_audio_conversion()
