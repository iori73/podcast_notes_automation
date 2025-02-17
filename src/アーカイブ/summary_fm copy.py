# # src/summary_fm.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path
from datetime import datetime
import time
from selenium.webdriver.support.ui import Select



class SummaryFMProcessor:
    def __init__(self):
        self.setup_driver()

    def setup_driver(self):
        options = Options()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument('--dns-prefetch-disable')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.wait = WebDriverWait(self.driver, 300)


    def login_and_navigate(self):
        """ログインして文字起こしページに移動"""
        try:
            # ログインページにアクセス
            self.driver.get("https://podcastranking.jp/login")
            
            # メールアドレス入力
            email_input = self.wait.until(
                EC.presence_of_element_located((By.ID, "email"))
            )
            email_input.send_keys("iori730002204294@gmail.com")
            
            # パスワード入力
            password_input = self.wait.until(
                EC.presence_of_element_located((By.ID, "password"))
            )
            password_input.send_keys("SumFM0607")
            
            # ログインボタンをクリック
            login_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
            )
            login_button.click()
            
            # ダッシュボードページの読み込みを待機
            self.wait.until(
                EC.url_to_be("https://podcastranking.jp/dashboard")
            )
            
            # 文字起こしページに直接移動
            self.driver.get("https://podcastranking.jp/transcribe")
            
            # 文字起こしページの要素が表示されるまで待機
            self.wait.until(
                EC.presence_of_element_located((By.ID, "inputs-audio-file"))
            )
            
            print("ログインと移動が完了しました")
            
        except Exception as e:
            print(f"ログインエラー: {str(e)}")
            raise


    def process_audio(self, mp3_path=None, spotify_url=None, release_date=None, duration=None):
        try:
            self.login_and_navigate()
            
            # MP3ファイルのパスが指定されている場合はそれを使用
            if mp3_path:
                audio_file = Path(mp3_path)
            else:
                # パスが指定されていない場合は最新のファイルを使用
                mp3_files = list(Path('downloads').glob('*.mp3'))
                if not mp3_files:
                    raise Exception("No MP3 files found in downloads directory")
                audio_file = max(mp3_files, key=lambda x: x.stat().st_mtime)
                
            print(f"アップロードするファイル: {audio_file}")
            
            # ファイルアップロード
            file_input = self.wait.until(
                EC.presence_of_element_located((By.ID, "inputs-audio-file"))
            )
            absolute_path = str(audio_file.resolve())
            file_input.send_keys(absolute_path)
            
            # 言語選択とLet'sボタンクリック
            language_select = self.wait.until(
                EC.presence_of_element_located((By.ID, "language"))
            )
            select = Select(language_select)
            select.select_by_value("Japanese")  # または "Japanese"
            
            submit_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.inputs-submit"))
            )
            submit_button.click()            
            
            print("ファイルアップロード完了。文字起こし処理を待機中...")
            
            # 結果生成を待機
            time.sleep(90)
            
            # 結果を取得
            text_result = self.driver.find_element(By.ID, "transcribe-result-section-text").text
            summary_result = self.driver.find_element(By.ID, "summary-result-section-text").text
            timestamp_result = self.driver.find_element(By.ID, "timestamp-result-section-text").text

            # MP3ファイル名からフォルダ名を取得
            folder_name = audio_file.stem

            # エピソード用のディレクトリを作成
            output_dir = Path('outputs') / folder_name
            output_dir.mkdir(parents=True, exist_ok=True)
            
            with open(output_dir / "episode_summary.md", 'w', encoding='utf-8') as f:
                f.write("## **基本情報**\n\n")
                if spotify_url:
                    f.write(f"- Spotify URL：[エピソードリンク]({spotify_url})\n")
                else:
                    f.write("- Spotify URL：[エピソードリンク]()\n")
                f.write(f"- 公開日：{release_date if release_date else ''}\n")
                f.write(f"- 長さ：{duration if duration else ''}\n")
                f.write("- LISTEN URL：\n\n")
                
                f.write("## **要約**\n\n")
                f.write(summary_result)
                f.write("\n\n")
                
                f.write("## **目次**\n\n")
                timestamps = timestamp_result.split('\n')
                for timestamp in timestamps:
                    if timestamp.strip():  # 空行をスキップ
                        f.write(f"{timestamp}\n\n")  # 各タイムスタンプの後に2行の改行を追加
                f.write("\n")
                
                f.write("## **文字起こし**\n\n")
                f.write(text_result)
                f.write("\n")
                
            print(f"結果を {output_dir} に保存しました")
            
            return {
                "transcription": text_result,
                "summary": summary_result,
                "timestamps": timestamp_result
            }
            
        except Exception as e:
            print(f"処理エラー: {str(e)}")
            raise

    def set_language(self, language):
        """
        language: "Japanese" or "English"
        """
        language_select = self.wait.until(
            EC.presence_of_element_located((By.ID, "language"))
        )
        select = Select(language_select)
        select.select_by_value(language)





# # # src/summary_fm.py
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait, Select
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from pathlib import Path
# from datetime import datetime
# import time
# import re


# class SummaryFMProcessor:
#     def __init__(self):
#         self.setup_driver()

#     def setup_driver(self):
#         options = Options()
#         options.add_argument('--start-maximized')
#         options.add_argument('--disable-dev-shm-usage')
#         options.add_argument('--no-sandbox')
#         options.add_argument('--dns-prefetch-disable')
#         self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#         self.wait = WebDriverWait(self.driver, 300)


#     def login_and_navigate(self):
#         """ログインして文字起こしページに移動"""
#         try:
#             # ログインページにアクセス
#             self.driver.get("https://podcastranking.jp/login")
            
#             # メールアドレス入力
#             email_input = self.wait.until(
#                 EC.presence_of_element_located((By.ID, "email"))
#             )
#             email_input.send_keys("iori730002204294@gmail.com")
            
#             # パスワード入力
#             password_input = self.wait.until(
#                 EC.presence_of_element_located((By.ID, "password"))
#             )
#             password_input.send_keys("SumFM0607")
            
#             # ログインボタンをクリック
#             login_button = self.wait.until(
#                 EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
#             )
#             login_button.click()
            
#             # ダッシュボードページの読み込みを待機
#             self.wait.until(
#                 EC.url_to_be("https://podcastranking.jp/dashboard")
#             )
            
#             # 文字起こしページに直接移動
#             self.driver.get("https://podcastranking.jp/transcribe")
            
#             # 文字起こしページの要素が表示されるまで待機
#             self.wait.until(
#                 EC.presence_of_element_located((By.ID, "inputs-audio-file"))
#             )
            
#             print("ログインと移動が完了しました")
            
#         except Exception as e:
#             print(f"ログインエラー: {str(e)}")
#             raise

# # --------------------------------
#     # def detect_language_from_url(self, spotify_url):
#     #     """SpotifyのURLから言語を判定"""
#     #     # デフォルトは日本語
#     #     default_language = "English"
        
#     #     if not spotify_url:
#     #         return default_language
            
#     #     # URLに含まれる言語コードをチェック
#     #     language_mapping = {
#     #         "jp": "English",
#     #         "en": "English",
#     #         # 必要に応じて他の言語を追加
#     #     }
        
#     #     for code, language in language_mapping.items():
#     #         if f"/{code}/" in spotify_url.lower():
#     #             return language
                
#     #     return default_language
#     def detect_language_from_url(self, spotify_url):
#         """SpotifyのURLから言語を判定"""
#         # デフォルトは英語
#         default_language = "English"
        
#         if not spotify_url:
#             return default_language
                
#         # URLが英語っぽい文字列のみで構成されているか確認
#         if spotify_url and re.match(r'^[A-Za-z0-9\s\-_.,!?&()\'\"]+$', spotify_url):
#             return "English"
        
#         return "English"


# # ---

#     def process_audio(self, spotify_url=None, release_date=None, duration=None):
#         try:
#             # まずログインして文字起こしページに移動
#             self.login_and_navigate()
            
#             # downloadsフォルダから最新のMP3ファイルを取得と処理
#             mp3_files = list(Path('downloads').glob('*.mp3'))
#             if not mp3_files:
#                 raise Exception("No MP3 files found in downloads directory")
            
#             latest_mp3 = max(mp3_files, key=lambda x: x.stat().st_mtime)
#             print(f"アップロードするファイル: {latest_mp3}")
            
#             # ファイルアップロード
#             file_input = self.wait.until(
#                 EC.presence_of_element_located((By.ID, "inputs-audio-file"))
#             )
#             absolute_path = str(latest_mp3.resolve())
#             file_input.send_keys(absolute_path)
            
#             # # 言語選択とLet'sボタンクリック
#             # language_select = self.wait.until(
#             #     EC.presence_of_element_located((By.CSS_SELECTOR, "select"))
#             # )
#             # language_select.send_keys("English")
            
            
#             # # URLから言語を判定
#             # detected_language = self.detect_language_from_url(spotify_url)
            
#             # # 言語選択とLet'sボタンクリック
#             # language_select = self.wait.until(
#             #     EC.presence_of_element_located((By.CSS_SELECTOR, "select"))
#             # )
#             # language_select.send_keys(detected_language)
            
            
#             # # 言語選択とLet'sボタンクリック
#             # language_select = self.wait.until(
#             #     EC.presence_of_element_located((By.CSS_SELECTOR, "select"))
#             # )
#             # detected_language = self.detect_language_from_url(spotify_url)
#             # print(f"Detected language: {detected_language}")  # デバッグ用
#             # language_select.send_keys(detected_language)

#             # # 選択が反映されたか確認
#             # selected_value = language_select.get_attribute("value")
#             # print(f"Selected language: {selected_value}")  # デバッグ用

            
            
#             # submit_button = self.wait.until(
#             #     EC.element_to_be_clickable((By.CSS_SELECTOR, "button.inputs-submit"))
#             # )
#             # submit_button.click()
            
#             # 言語選択の部分を修正
#             language_select = self.wait.until(
#                 EC.presence_of_element_located((By.ID, "language"))
#             )
#             # Select要素を使用して適切に言語を選択
#             from selenium.webdriver.support.ui import Select
#             select = Select(language_select)
#             detected_language = self.detect_language_from_url(spotify_url)
#             select.select_by_value(detected_language)  # 検出された言語を使用


#             submit_button = self.wait.until(
#                 EC.element_to_be_clickable((By.CSS_SELECTOR, "button.inputs-submit"))
#             )
#             submit_button.click()

            
#             print("ファイルアップロード完了。文字起こし処理を待機中...")
            
#             # 結果生成を待機
#             time.sleep(90)
            
        
#             # 結果を取得
#             text_result = self.driver.find_element(By.ID, "transcribe-result-section-text").text
#             summary_result = self.driver.find_element(By.ID, "summary-result-section-text").text
#             timestamp_result = self.driver.find_element(By.ID, "timestamp-result-section-text").text

#             # MP3ファイル名からフォルダ名を取得
#             folder_name = latest_mp3.stem
            
#             # エピソード用のディレクトリを作成
#             output_dir = Path('outputs') / folder_name
#             output_dir.mkdir(parents=True, exist_ok=True)
           
        
            
#             with open(output_dir / "episode_summary.md", 'w', encoding='utf-8') as f:
#                 f.write("## **基本情報**\n\n")
#                 if spotify_url:
#                     f.write(f"- Spotify URL：[エピソードリンク]({spotify_url})\n")
#                 else:
#                     f.write("- Spotify URL：[エピソードリンク]()\n")
#                 f.write(f"- 公開日：{release_date if release_date else ''}\n")
#                 f.write(f"- 長さ：{duration if duration else ''}\n")
#                 f.write("- LISTEN URL：\n\n")
                
#                 # 要約セクション
#                 f.write("## **要約**\n\n")
#                 f.write(summary_result)
#                 f.write("\n\n")
                
#                 # 目次セクション
#                 f.write("## **目次**\n\n")
#                 timestamps = timestamp_result.split('\n')
#                 for timestamp in timestamps:
#                     if timestamp.strip():  # 空行をスキップ
#                         f.write(f"{timestamp}\n\n")  # 各タイムスタンプの後に2行の改行を追加
#                 f.write("\n")
                
#                 # 文字起こしセクション
#                 f.write("## **文字起こし**\n\n")
#                 f.write(text_result)
#                 f.write("\n")


          
                            
                
#             print(f"結果を {output_dir} に保存しました")
            
#             return {
#                 "transcription": text_result,
#                 "summary": summary_result,
#                 "timestamps": timestamp_result
#             }
            
#         except Exception as e:
#             print(f"処理エラー: {str(e)}")
#             raise

