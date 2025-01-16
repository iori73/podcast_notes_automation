# # src/local_audio.py
# from summary_fm import SummaryFMProcessor
# from pathlib import Path
# from datetime import datetime


# class LocalAudioProcessor:
#     def __init__(self):
#         self.summary_processor = SummaryFMProcessor()

#     def process_local_audio(self, mp3_path, metadata=None):
#         """
#         ローカルのMP3ファイルを処理する
        
#         Args:
#             mp3_path (str): MP3ファイルのパス
#             metadata (dict, optional): メタデータ情報
#                 {
#                     "title": "エピソードタイトル",
#                     "release_date": "2024年1月1日",
#                     "duration": "31:33"
#                 }
#         """
#         try:
#             # MP3ファイルの存在確認
#             audio_file = Path(mp3_path)
#             if not audio_file.exists():
#                 raise FileNotFoundError(f"File not found: {mp3_path}")

#             # メタデータがない場合はファイル情報から生成
#             if metadata is None:
#                 metadata = {
#                     "title": audio_file.stem,
#                     "release_date": datetime.fromtimestamp(audio_file.stat().st_mtime).strftime('%Y年%m月%d日'),
#                     "duration": ""  # MP3の長さを取得する場合は追加実装が必要
#                 }

#             # Summary.fm処理を実行
#             results = self.summary_processor.process_audio(
#                 spotify_url=None,
#                 release_date=metadata.get("release_date", ""),
#                 duration=metadata.get("duration", "")
#             )

#             return results

#         except Exception as e:
#             print(f"ローカルファイル処理エラー: {str(e)}")
#             raise


# src/local_audio.py
from summary_fm import SummaryFMProcessor
from pathlib import Path
from datetime import datetime
from mutagen.mp3 import MP3

class LocalAudioProcessor:
    def __init__(self):
        self.summary_processor = SummaryFMProcessor()

    def get_audio_duration(self, file_path):
        """MP3ファイルの長さを取得"""
        try:
            audio = MP3(file_path)
            seconds = int(audio.info.length)
            minutes = seconds // 60
            remaining_seconds = seconds % 60
            return f"{minutes}:{remaining_seconds:02d}"
        except Exception as e:
            print(f"長さの取得に失敗: {str(e)}")
            return ""

    def process_local_audio(self, mp3_path, metadata=None):
        try:
            # MP3ファイルの存在確認
            audio_file = Path(mp3_path)
            if not audio_file.exists():
                raise FileNotFoundError(f"File not found: {mp3_path}")

            # メタデータがない場合はファイル情報から生成
            if metadata is None:
                duration = self.get_audio_duration(mp3_path)
                metadata = {
                    "title": audio_file.stem,
                    "release_date": datetime.fromtimestamp(audio_file.stat().st_mtime).strftime('%Y年%m月%d日'),
                    "duration": duration
                }

            # Summary.fm処理を実行
            results = self.summary_processor.process_audio(
                spotify_url=None,
                release_date=metadata.get("release_date", ""),
                duration=metadata.get("duration", "")
            )

            return results

        except Exception as e:
            print(f"ローカルファイル処理エラー: {str(e)}")
            raise
