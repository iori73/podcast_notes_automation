# # src/test_local_audio.py
# from local_audio import LocalAudioProcessor

# def test_local_audio():
#     processor = LocalAudioProcessor()
    
#     # テスト用のメタデータ
#     metadata = {
#         "title": "テストエピソード",
#         "release_date": "2024年1月1日",
#         "duration": "30:00"
#     }
    
#     # MP3ファイルのパスを指定して処理
#     results = processor.process_local_audio(
#         "path/to/your/audio.mp3",
#         metadata=metadata
#     )
    
#     if results:
#         print("\n=== 文字起こし ===")
#         print(results["transcription"][:200] + "...")
        
#         print("\n=== 要約 ===")
#         print(results["summary"])
        
#         print("\n=== タイムスタンプ ===")
#         print(results["timestamps"])

# if __name__ == "__main__":
#     test_local_audio()


# src/test_local_audio.py
from local_audio import LocalAudioProcessor
from pathlib import Path

def test_local_audio():
    processor = LocalAudioProcessor()
    
    # 対象のMP3ファイルのパス
    mp3_path = Path("downloads/起承転結を忘れろ！TEDが起こしたプレゼンテーション革命【第79号音声版】#79.mp3")
    
    # MP3ファイルのパスを指定して処理
    results = processor.process_local_audio(str(mp3_path))
    
    if results:
        print("\n=== 文字起こし ===")
        print(results["transcription"][:200] + "...")
        
        print("\n=== 要約 ===")
        print(results["summary"])
        
        print("\n=== タイムスタンプ ===")
        print(results["timestamps"])

if __name__ == "__main__":
    test_local_audio()
