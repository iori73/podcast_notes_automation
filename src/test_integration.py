# # src/test_integration.py
from spotify import SpotifyClient
from listen_notes import ListenNotesClient
from summary_fm import SummaryFMProcessor
from datetime import datetime


def test_podcast_fetch():
    spotify_url = "https://open.spotify.com/episode/1xbQhe5qok8Wmnm7LjL7e4?si=3da54362355d4aee"

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
                # duration = f"{duration_min}:{duration_sec:02d}"
                # release_date = datetime.strptime(episode_info['release_date'], '%Y-%m-%d').strftime('%Y年%m月%d日')
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
