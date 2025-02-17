# # src/test_integration.py
from spotify import SpotifyClient
from listen_notes import ListenNotesClient
from summary_fm import SummaryFMProcessor
from datetime import datetime


def test_podcast_fetch():
    spotify_url = "https://open.spotify.com/episode/0YIfdfNxGbGnDEzM017W5x"

    try:
        spotify_client = SpotifyClient()
        episode_info = spotify_client.get_episode_info(spotify_url)
        print(f"Spotifyエピソード情報: {episode_info['title']}")

        ln_client = ListenNotesClient()
        ln_url = ln_client.get_episode_url(episode_info['title'])
        print(f"Listen Notes URL: {ln_url}")


        if ln_url:
            try:
                downloaded_file = ln_client.download_episode(
                    episode_url=ln_url,
                    episode_title=episode_info['title']
                )
                print(f"ダウンロードしたファイル: {downloaded_file}")
                
                # Spotifyから追加情報を取得
                duration_min = episode_info['duration_ms'] // (1000 * 60)
                duration_sec = (episode_info['duration_ms'] // 1000) % 60
                # Spotifyから追加情報を取得
                duration = f"{episode_info['duration_ms'] // (1000 * 60)}:{(episode_info['duration_ms'] // 1000) % 60:02d}"
                release_date = datetime.strptime(episode_info['release_date'], '%Y-%m-%d').strftime('%Y年%m月%d日')

                
                # Summary.fm処理
                summary_processor = SummaryFMProcessor()
                results = summary_processor.process_audio(
                    spotify_url=spotify_url,
                    release_date=release_date,
                    duration=duration
                )



            except Exception as e:
                print(f"ダウンロードエラー: {str(e)}")
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")



if __name__ == "__main__":
    test_podcast_fetch()



# --------------------------------------------


# # src/test_integration.py
# from spotify import SpotifyClient
# from listen_notes import ListenNotesClient
# from summary_fm import SummaryFMProcessor
# from datetime import datetime
# import os
# import sys
# import pandas as pd


# def process_podcast_urls(urls=None):
#     # デフォルトのURLリスト
#     default_urls = [
#         "https://open.spotify.com/episode/1xbQhe5qok8Wmnm7LjL7e4",
#         # 他の番組のURLも追加可能
#     ]
    
#     # URLが指定されていない場合はデフォルトを使用
#     urls_to_process = urls if urls else default_urls

#     # 単一のURLの場合はリストに変換
#     if isinstance(urls_to_process, str):
#         urls_to_process = [urls_to_process]

#     if not urls_to_process:
#         print("処理するURLが見つかりません")
#         return

#     for spotify_url in urls_to_process:
#         try:
#             spotify_client = SpotifyClient()
#             episode_info = spotify_client.get_episode_info(spotify_url)
#             print(f"Spotifyエピソード情報: {episode_info['title']}")

#             ln_client = ListenNotesClient()
#             ln_url = ln_client.get_episode_url(episode_info['title'])
#             print(f"Listen Notes URL: {ln_url}")

#             if ln_url:
#                 try:
#                     downloaded_file = ln_client.download_episode(
#                         episode_url=ln_url,
#                         episode_title=episode_info['title']
#                     )
#                     print(f"ダウンロードしたファイル: {downloaded_file}")

#                     duration = f"{episode_info['duration_ms'] // (1000 * 60)}:{(episode_info['duration_ms'] // 1000) % 60:02d}"
#                     release_date = datetime.strptime(episode_info['release_date'], '%Y-%m-%d').strftime('%Y年%m月%d日')

#                     summary_processor = SummaryFMProcessor()
#                     results = summary_processor.process_audio(
#                         spotify_url=spotify_url,
#                         release_date=release_date,
#                         duration=duration
#                     )

#                 except Exception as e:
#                     print(f"ダウンロードエラー: {str(e)}")
#         except Exception as e:
#             print(f"エラーが発生しました: {str(e)}")

# # if __name__ == "__main__":
# #     # 直接URLリストを指定して実行
# #     process_podcast_urls()

# def get_urls_from_csv():
#     current_dir = os.path.dirname(os.path.abspath(__file__))
#     csv_path = os.path.join(current_dir, '..', '..', 'BIAS', 'data', 'processed_episodes.csv')
#     try:
#         df = pd.read_csv(csv_path)
#         return df['URL'].tolist()
#     except Exception as e:
#         print(f"CSVからのURL取得エラー: {e}")
#         return None


# if __name__ == "__main__":
#     urls = get_urls_from_csv()
#     process_podcast_urls(urls)

def process_spotify_podcast():
    spotify_url = "https://open.spotify.com/episode/..."
    
    # 1. Spotifyから情報取得
    spotify_client = SpotifyClient()
    episode_info = spotify_client.get_episode_info(spotify_url)
    
    # 2. Listen Notesで対応する音声を検索・ダウンロード
    ln_client = ListenNotesClient()
    ln_url = ln_client.get_episode_url(episode_info['title'])
    downloaded_file = ln_client.download_episode(ln_url, episode_info['title'])
    
    # 3. 音声処理と要約生成
    summary_processor = SummaryFMProcessor()
    results = summary_processor.process_audio(
        spotify_url=spotify_url,
        release_date=episode_info['release_date'],
        duration=f"{episode_info['duration_ms'] // (1000 * 60)}:{(episode_info['duration_ms'] // 1000) % 60:02d}"
    )
