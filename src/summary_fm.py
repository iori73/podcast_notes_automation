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
import google.generativeai as genai
from utils import load_config


class SummaryFMProcessor:
    def __init__(self):
        self.setup_driver()
        # Gemini APIの設定
        config = load_config()
        genai.configure(api_key=config["gemini"]["api_key"])
        self.model = genai.GenerativeModel("gemini-pro")

    def setup_driver(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--dns-prefetch-disable")
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )
        self.wait = WebDriverWait(self.driver, 60)

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
            self.wait.until(EC.url_to_be("https://podcastranking.jp/dashboard"))

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

    def translate_to_english(self, text, sentence_count=10):
        """日本語テキストを英語に翻訳"""
        try:
            # テキストをセンテンスで分割
            sentences = text.split("。")
            translated_sentences = []

            for i in range(0, len(sentences), sentence_count):
                chunk = "。".join(sentences[i : i + sentence_count])
                if not chunk.strip():
                    continue

                prompt = f"""
                以下の日本語テキスト「## **文字起こし**」を英語に翻訳してください。
                元のテキストの意味と文脈を保持しながら、自然な英語に翻訳してください。
                読みやすいように改行を適切に使用してください。日本語テキストに忠実に英訳してください。

                テキスト:
                {chunk}
                """
                # prompt = f"""
                # Translate the following Japanese text into English, preserving its meaning and context:

                # {chunk}
                # """
                try:
                    response = self.model.generate_content(prompt)
                    translated_sentences.append(response.text)
                    # APIレート制限を避けるため少し待機
                    time.sleep(1)
                except Exception as e:
                    print(f"段落の翻訳エラー: {str(e)}")
                    translated_sentences.append(f"[Translation Error: {str(e)}]")

            # 翻訳したセンテンスを結合
            return "。".join(translated_sentences)

        except Exception as e:
            print(f"翻訳エラー: {str(e)}")
            return None

    # def process_audio(
    #     self,
    #     mp3_path=None,
    #     spotify_url=None,
    #     release_date=None,
    #     duration=None,
    #     language="Japanese",
    # ):
    #     try:
    #         self.login_and_navigate()

    #         # MP3ファイルのパスが指定されている場合はそれを使用
    #         if mp3_path:
    #             audio_file = Path(mp3_path)
    #         else:
    #             # パスが指定されていない場合は最新のファイルを使用
    #             mp3_files = list(Path("downloads").glob("*.mp3"))
    #             if not mp3_files:
    #                 raise Exception("No MP3 files found in downloads directory")
    #             audio_file = max(mp3_files, key=lambda x: x.stat().st_mtime)

    #         print(f"アップロードするファイル: {audio_file}")

    #         # ファイルアップロード
    #         file_input = self.wait.until(
    #             EC.presence_of_element_located((By.ID, "inputs-audio-file"))
    #         )
    #         absolute_path = str(audio_file.resolve())
    #         file_input.send_keys(absolute_path)

    #         # 言語選択
    #         language_select = self.wait.until(
    #             EC.presence_of_element_located((By.ID, "language"))
    #         )
    #         select = Select(language_select)
    #         select.select_by_value(language)  # "Japanese" または "English"

    #         submit_button = self.wait.until(
    #             EC.element_to_be_clickable((By.CSS_SELECTOR, "button.inputs-submit"))
    #         )
    #         submit_button.click()

    #         print("ファイルアップロード完了。文字起こし処理を待機中...")

    #         # 結果生成を待機
    #         time.sleep(90)

    #         # 結果を取得
    #         text_result = self.driver.find_element(
    #             By.ID, "transcribe-result-section-text"
    #         ).text
    #         summary_result = self.driver.find_element(
    #             By.ID, "summary-result-section-text"
    #         ).text
    #         timestamp_result = self.driver.find_element(
    #             By.ID, "timestamp-result-section-text"
    #         ).text

    #         # MP3ファイル名からフォルダ名を取得
    #         folder_name = audio_file.stem

    #         # エピソード用のディレクトリを作成
    #         output_dir = Path("outputs") / folder_name
    #         output_dir.mkdir(parents=True, exist_ok=True)

    #         with open(output_dir / "episode_summary.md", "w", encoding="utf-8") as f:
    #             f.write("## **基本情報**\n\n")
    #             if spotify_url:
    #                 f.write(f"- Spotify URL：[エピソードリンク]({spotify_url})\n")
    #             else:
    #                 f.write("- Spotify URL：[エピソードリンク]()\n")
    #             f.write(f"- 公開日：{release_date if release_date else ''}\n")
    #             f.write(f"- 長さ：{duration if duration else ''}\n")
    #             f.write("- LISTEN URL：\n\n")

    #             f.write("## **要約**\n\n")
    #             f.write(summary_result)
    #             f.write("\n\n")

    #             f.write("## **目次**\n\n")
    #             timestamps = timestamp_result.split("\n")
    #             for timestamp in timestamps:
    #                 if timestamp.strip():
    #                     f.write(f"{timestamp}\n\n")
    #             f.write("\n")

    #             f.write("## **文字起こし**\n\n")
    #             f.write(text_result)
    #             f.write("\n")

    #             # 日本語の場合のみ英訳セクションを追加
    #             if language == "Japanese":
    #                 english_summary = self.translate_to_english(summary_result)
    #                 if english_summary:
    #                     f.write("\n## **English Summary**\n\n")
    #                     f.write(english_summary)
    #                     f.write("\n\n")

    #                 if english_text := self.translate_to_english(text_result):
    #                     f.write("\n## **English Transcription**\n\n")
    #                     f.write(english_text)
    #                     f.write("\n\n")

    #         print(f"結果を {output_dir} に保存しました")

    #         return {
    #             "transcription": text_result,
    #             "summary": summary_result,
    #             "timestamps": timestamp_result,
    #             "english_transcription": (
    #                 self.translate_to_english(text_result)
    #                 if language == "Japanese"
    #                 else None
    #             ),
    #             "english_summary": (
    #                 self.translate_to_english(summary_result)
    #                 if language == "Japanese"
    #                 else None
    #             ),
    #         }

    #     except Exception as e:
    #         print(f"処理エラー: {str(e)}")
    #         raise

    # def process_audio(self, mp3_path=None, spotify_url=None, release_date=None, duration=None, language="Japanese"):
    #     try:
    #         print(f"📢 処理開始: {mp3_path} (言語: {language})")

    #         self.login_and_navigate()
    #         print("✅ ログイン成功")

    #         # ファイルアップロード
    #         file_input = self.wait.until(
    #             EC.presence_of_element_located((By.ID, "inputs-audio-file"))
    #         )
    #         absolute_path = str(Path(mp3_path).resolve())
    #         file_input.send_keys(absolute_path)
    #         print(f"✅ ファイルアップロード完了: {absolute_path}")

    #         # 言語選択
    #         language_select = self.wait.until(
    #             EC.presence_of_element_located((By.ID, "language"))
    #         )
    #         select = Select(language_select)
    #         select.select_by_value(language)
    #         print(f"✅ 言語設定完了: {language}")

    #         submit_button = self.wait.until(
    #             EC.element_to_be_clickable((By.CSS_SELECTOR, "button.inputs-submit"))
    #         )
    #         submit_button.click()
    #         print("✅ 文字起こし処理開始")

    #         # 文字起こし結果の取得
    #         time.sleep(90)  # 処理待機
    #         try:
    #             text_result = self.driver.find_element(By.ID, "transcribe-result-section-text").text
    #             print(f"✅ 文字起こし取得成功: {text_result[:50]}")  # 最初の50文字を表示
    #         except Exception as e:
    #             print(f"❌ 文字起こし取得失敗: {str(e)}")
    #             text_result = "Error: Unable to retrieve transcription"

    #         try:
    #             summary_result = self.driver.find_element(By.ID, "summary-result-section-text").text
    #             print(f"✅ 要約取得成功: {summary_result[:50]}")
    #         except Exception as e:
    #             print(f"❌ 要約取得失敗: {str(e)}")
    #             summary_result = "Error: Unable to retrieve summary"

    #         try:
    #             timestamp_result = self.driver.find_element(By.ID, "timestamp-result-section-text").text
    #             print(f"✅ タイムスタンプ取得成功: {timestamp_result[:50]}")
    #         except Exception as e:
    #             print(f"❌ タイムスタンプ取得失敗: {str(e)}")
    #             timestamp_result = "Error: Unable to retrieve timestamps"

    #         # 結果を保存
    #         folder_name = Path(mp3_path).stem
    #         output_dir = Path("outputs") / folder_name
    #         output_dir.mkdir(parents=True, exist_ok=True)

    #         with open(output_dir / "episode_summary.md", "w", encoding="utf-8") as f:
    #             f.write("## **基本情報**\n\n")
    #             f.write(f"- 公開日：{release_date if release_date else ''}\n")
    #             f.write(f"- 長さ：{duration if duration else ''}\n")
    #             f.write("\n## **要約**\n\n")
    #             f.write(summary_result)
    #             f.write("\n\n## **目次**\n\n")
    #             f.write(timestamp_result)
    #             f.write("\n\n## **文字起こし**\n\n")
    #             f.write(text_result)
    #             f.write("\n")

    #         print(f"✅ 結果を {output_dir} に保存しました")

    #         return {
    #             "transcription": text_result,
    #             "summary": summary_result,
    #             "timestamps": timestamp_result,
    #         }

    #     except Exception as e:
    #         print(f"❌ 文字起こし処理エラー: {str(e)}")
    #         raise

    def process_audio(self, mp3_path=None, spotify_url=None, release_date=None, duration=None, language="Japanese"):
        try:
            print(f"📢 処理開始: {mp3_path} (言語: {language})")

            self.login_and_navigate()
            print("✅ ログイン成功")

            # ファイルアップロード
            file_input = self.wait.until(
                EC.presence_of_element_located((By.ID, "inputs-audio-file"))
            )
            absolute_path = str(Path(mp3_path).resolve())
            file_input.send_keys(absolute_path)
            print(f"✅ ファイルアップロード完了: {absolute_path}")

            # 言語選択
            language_select = self.wait.until(
                EC.presence_of_element_located((By.ID, "language"))
            )
            select = Select(language_select)
            select.select_by_value(language)
            print(f"✅ 言語設定完了: {language}")

            submit_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.inputs-submit"))
            )
            submit_button.click()
            print("✅ 文字起こし処理開始")

            # 文字起こし結果の取得
            time.sleep(90)  # 処理待機
            try:
                text_result = self.driver.find_element(By.ID, "transcribe-result-section-text").text
                print(f"✅ 文字起こし取得成功: {text_result[:50]}")  # 最初の50文字を表示
            except Exception as e:
                print(f"❌ 文字起こし取得失敗: {str(e)}")
                text_result = "Error: Unable to retrieve transcription"

            try:
                summary_result = self.driver.find_element(By.ID, "summary-result-section-text").text
                print(f"✅ 要約取得成功: {summary_result[:50]}")
            except Exception as e:
                print(f"❌ 要約取得失敗: {str(e)}")
                summary_result = "Error: Unable to retrieve summary"

            try:
                timestamp_result = self.driver.find_element(By.ID, "timestamp-result-section-text").text
                print(f"✅ タイムスタンプ取得成功: {timestamp_result[:50]}")
            except Exception as e:
                print(f"❌ タイムスタンプ取得失敗: {str(e)}")
                timestamp_result = "Error: Unable to retrieve timestamps"

            # 結果を保存
            folder_name = Path(mp3_path).stem
            output_dir = Path("outputs") / folder_name
            output_dir.mkdir(parents=True, exist_ok=True)

            with open(output_dir / "episode_summary.md", "w", encoding="utf-8") as f:
                f.write("## **基本情報**\n\n")
                f.write(f"- 公開日：{release_date if release_date else ''}\n")
                f.write(f"- 長さ：{duration if duration else ''}\n")
                f.write("\n## **要約**\n\n")
                f.write(summary_result)
                f.write("\n\n## **目次**\n\n")
                f.write(timestamp_result)
                f.write("\n\n## **文字起こし**\n\n")
                f.write(text_result)
                f.write("\n")

                # 🔹 日本語の場合、英訳を追加
                if language == "Japanese":
                    print("✅ 日本語のエピソードなので英訳を追加します")

                    english_summary = self.translate_to_english(summary_result)
                    print(f"✅ 英訳された English Summary: {english_summary}")

                    if english_summary and english_summary.strip():
                        f.write("\n## **English Summary**\n\n")
                        f.write(english_summary)
                        f.write("\n\n")
                    else:
                        print("⚠️ English Summary の翻訳が失敗したか空です")

                    english_text = self.translate_to_english(text_result)
                    print(f"✅ 英訳された English Transcription: {english_text}")

                    if english_text and english_text.strip():
                        f.write("\n## **English Transcription**\n\n")
                        f.write(english_text)
                        f.write("\n\n")
                    else:
                        print("⚠️ English Transcription の翻訳が失敗したか空です")

            print(f"✅ 結果を {output_dir} に保存しました")

            return {
                "transcription": text_result,
                "summary": summary_result,
                "timestamps": timestamp_result,
            }

        except Exception as e:
            print(f"❌ 文字起こし処理エラー: {str(e)}")
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
