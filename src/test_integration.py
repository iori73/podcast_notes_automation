# # # src/test_integration.py
# from spotify import SpotifyClient
# from listen_notes import ListenNotesClient
# from summary_fm import SummaryFMProcessor
# from datetime import datetime
# import sys


# def test_podcast_fetch():
#     spotify_url = (
#         "https://open.spotify.com/episode/6FAgvuhKf5CWoUMogrji1s?si=bc802a0fa1e84e36"
#     )

#     try:
#         # Spotifyからメタデータを取得
#         spotify_client = SpotifyClient()
#         episode_info = spotify_client.get_episode_info(spotify_url)
#         print(f"Spotifyエピソード情報: {episode_info['title']}")

#         # 言語を検出（episode_infoから言語情報を取得）
#         # language = episode_info.get("language", "ja")  # デフォルトは日本語
#         language = episode_info.get("language", "ja").split("-")[0]  # "en-US" → "en"
#         print(f"検出された言語: {language}")

#         # Listen Notesクライアントの言語を設定
#         ln_client = ListenNotesClient()
#         # ISO 639-1コード（'en', 'ja'など）をListen Notes用の形式に変換
#         ln_language = "English" if language == "en" else "Japanese"
#         ln_client.set_language(ln_language)

#         ln_url = ln_client.get_episode_url(episode_info["title"])
#         print(f"Listen Notes URL: {ln_url}")

#         if ln_url:
#             try:
#                 downloaded_file = ln_client.download_episode(
#                     episode_url=ln_url, episode_title=episode_info["title"]
#                 )
#                 print(f"ダウンロードしたファイル: {downloaded_file}")

#                 duration = f"{episode_info['duration_ms'] // (1000 * 60)}:{(episode_info['duration_ms'] // 1000) % 60:02d}"
#                 release_date = datetime.strptime(
#                     episode_info["release_date"], "%Y-%m-%d"
#                 ).strftime("%Y年%m月%d日")

#                 # Summary.fmの言語設定も更新
#                 summary_processor = SummaryFMProcessor()
#                 # results = summary_processor.process_audio(
#                 #     spotify_url=spotify_url,
#                 #     release_date=release_date,
#                 #     duration=duration,
#                 #     language=ln_language,  # 言語情報を渡す
#                 # )
#                 results = summary_processor.process_audio(
#                     spotify_url=spotify_url,
#                     release_date=release_date,
#                     duration=duration,
#                     language=ln_language,  # 言語情報を渡す
#                 )

#                 print("🔍 取得結果:", results)



#             except Exception as e:
#                 print(f"ダウンロードエラー: {str(e)}")
#         else:
#             print("Listen Notesで対応するポッドキャストが見つかりませんでした。")
#             print("test_local_audio.pyを使用して処理してください。")
#             sys.exit(1)

#     except Exception as e:
#         print(f"エラーが発生しました: {str(e)}")


# if __name__ == "__main__":
#     test_podcast_fetch()










# # # # src/test_integration.py
# from spotify import SpotifyClient
# from listen_notes import ListenNotesClient
# from summary_fm import SummaryFMProcessor
# from datetime import datetime
# import sys


# def test_podcast_fetch():
#     spotify_url = "https://open.spotify.com/episode/1oilteqtA0P5W8j7Lniw4p?si=d305b88ef34b4fb2"

#     try:
#         # **Spotifyからメタデータを取得**
#         spotify_client = SpotifyClient()
#         episode_info = spotify_client.get_episode_info(spotify_url)
#         title = episode_info["title"]
#         print(f"🎧 Spotifyエピソード情報: {title}")

#         # **言語を検出**
#         language = episode_info.get("language", "ja").split("-")[0]  # "en-US" → "en"
#         ln_language = "English" if language == "en" else "Japanese"
#         print(f"🌍 検出された言語: {ln_language}")

#         # **Listen Notes クライアントを初期化**
#         ln_client = ListenNotesClient()
#         ln_client.set_language(ln_language)

#         # **Listen Notes でエピソード URL を取得**
#         ln_url = ln_client.get_episode_url(title)
#         print(f"🔗 Listen Notes URL: {ln_url}")

#         # **MP3ファイルのダウンロード**
#         downloaded_file = None
#         if ln_url:
#             try:
#                 downloaded_file = ln_client.download_episode(episode_url=ln_url, episode_title=title)
#                 print(f"✅ Listen Notesからダウンロード成功: {downloaded_file}")
#             except Exception as e:
#                 print(f"❌ Listen Notes ダウンロードエラー: {str(e)}")

#         # **Listen Notesで見つからなかった場合は Spotify からダウンロード**
#         if not downloaded_file:
#             print("⚠️ Listen Notesでエピソードが見つかりませんでした。")
#             print("📥 代わりにSpotifyから直接ダウンロードします。")
#             try:
#                 downloaded_file = spotify_client.download_episode(spotify_url)
#                 print(f"✅ Spotifyからダウンロード成功: {downloaded_file}")
#             except Exception as e:
#                 print(f"❌ Spotify ダウンロードエラー: {str(e)}")
#                 sys.exit(1)  # Spotifyでも取得できない場合は終了

#         # **MP3 ファイルのメタデータを取得**
#         duration = f"{episode_info['duration_ms'] // (1000 * 60)}:{(episode_info['duration_ms'] // 1000) % 60:02d}"
#         release_date = datetime.strptime(episode_info["release_date"], "%Y-%m-%d").strftime("%Y年%m月%d日")

#         # **文字起こし処理**
#         summary_processor = SummaryFMProcessor()
#         results = summary_processor.process_audio(
#             mp3_path=downloaded_file,
#             spotify_url=spotify_url,
#             release_date=release_date,
#             duration=duration,
#             language=ln_language,
#         )

#         print("🔍 取得結果:", results)

#     except Exception as e:
#         print(f"❌ エラー発生: {str(e)}")
#         sys.exit(1)


# if __name__ == "__main__":
#     test_podcast_fetch()




from spotify import SpotifyClient
from listen_notes import ListenNotesClient
from summary_fm import SummaryFMProcessor
from datetime import datetime
import sys


def test_podcast_fetch():
    spotify_url = "https://open.spotify.com/episode/1DHZTc6ZvoHQ1UgiVTduKB?si=3697f486a6f443d5&nd=1&dlsi=6448aeab96114782"

    try:
        # **Spotifyからメタデータを取得**
        spotify_client = SpotifyClient()
        episode_info = spotify_client.get_episode_info(spotify_url)
        title = episode_info["title"]
        print(f"🎧 Spotifyエピソード情報: {title}")

        # **言語を検出**
        language = episode_info.get("language", "ja").split("-")[0]  # "en-US" → "en"
        ln_language = "English" if language == "en" else "Japanese"
        print(f"🌍 検出された言語: {ln_language}")

        # **Listen Notes クライアントを初期化**
        ln_client = ListenNotesClient()
        ln_client.set_language(ln_language)

        # **Listen Notes でエピソード URL を取得**
        ln_url = ln_client.get_episode_url(title)
        print(f"🔗 Listen Notes URL: {ln_url}")

        # **MP3ファイルのダウンロード**
        downloaded_file = None
        if ln_url:
            try:
                downloaded_file = ln_client.download_episode(episode_url=ln_url, episode_title=title)
                print(f"✅ Listen Notesからダウンロード成功: {downloaded_file}")
            except Exception as e:
                print(f"❌ Listen Notes ダウンロードエラー: {str(e)}")

        # **Listen Notesで見つからなかった場合は Spotify からダウンロード**
        if not downloaded_file:
            print("⚠️ Listen Notesでエピソードが見つかりませんでした。")
            print("📥 代わりにSpotifyから直接ダウンロードします。")
            try:
                downloaded_file = spotify_client.download_episode(spotify_url)
                print(f"✅ Spotifyからダウンロード成功: {downloaded_file}")
            except Exception as e:
                print(f"❌ Spotify ダウンロードエラー: {str(e)}")
                sys.exit(1)  # Spotifyでも取得できない場合は終了

        # **MP3 ファイルのメタデータを取得**
        duration = f"{episode_info['duration_ms'] // (1000 * 60)}:{(episode_info['duration_ms'] // 1000) % 60:02d}"
        release_date = datetime.strptime(episode_info["release_date"], "%Y-%m-%d").strftime("%Y年%m月%d日")

        # **文字起こし処理**
        summary_processor = SummaryFMProcessor()
        results = summary_processor.process_audio(
            mp3_path=downloaded_file,
            spotify_url=spotify_url,
            release_date=release_date,
            duration=duration,
            language=ln_language,
        )

        print("🔍 取得結果:", results)

    except Exception as e:
        print(f"❌ エラー発生: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    test_podcast_fetch()
