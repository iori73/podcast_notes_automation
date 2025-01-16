# # src/spotify.py
# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
# from utils import load_config
# import re
# from datetime import datetime


# class SpotifyClient:
#     def __init__(self):
#         config = load_config()
#         auth_manager = SpotifyClientCredentials(
#             client_id=config['spotify']['client_id'],
#             client_secret=config['spotify']['client_secret']
#         )
#         self.sp = spotipy.Spotify(auth_manager=auth_manager)
    
    
#     def _get_episode_id(self, url):
#         """SpotifyのURLからエピソードIDを抽出"""
#         try:
#             # URLからIDを抽出（最後の/以降の?より前の部分）
#             if '?' in url:
#                 episode_id = url.split('/')[-1].split('?')[0]
#             else:
#                 episode_id = url.split('/')[-1]
#             return episode_id
#         except Exception as e:
#             print(f"エピソードID抽出エラー: {str(e)}")
#             return None



    
#     # def get_episode_info(self, spotify_url):
#     #     # URLからエピソードIDを抽出
#     #     episode_id = re.search(r'episode/([a-zA-Z0-9]+)', spotify_url).group(1)
#     #     episode = self.sp.episode(episode_id)
        
#     #     return {
#     #         'title': episode['name'],
#     #         'description': episode['description'],
#     #         'duration_ms': episode['duration_ms'],
#     #         'release_date': episode['release_date']
#     #     }
#     def get_episode_info(self, url):
#         try:
#             episode_id = self._get_episode_id(url)
#             episode = self.spotify.episode(episode_id)
            
#             # ミリ秒を分:秒形式に変換
#             duration_ms = episode['duration_ms']
#             duration_min = duration_ms // (1000 * 60)
#             duration_sec = (duration_ms // 1000) % 60
#             duration = f"{duration_min}:{duration_sec:02d}"
            
#             # 公開日をフォーマット
#             release_date = datetime.strptime(episode['release_date'], '%Y-%m-%d').strftime('%Y年%m月%d日')
            
#             return {
#                 'title': episode['name'],
#                 'description': episode['description'],
#                 'release_date': release_date,
#                 'duration': duration
#             }
#         except Exception as e:
#             print(f"エピソード情報の取得に失敗: {str(e)}")
#             return None



# src/spotify.py
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from utils import load_config
from datetime import datetime

class SpotifyClient:
    def __init__(self):
        config = load_config()
        auth_manager = SpotifyClientCredentials(
            client_id=config['spotify']['client_id'],
            client_secret=config['spotify']['client_secret']
        )
        self.sp = spotipy.Spotify(auth_manager=auth_manager)
    
    def _get_episode_id(self, url):
        """SpotifyのURLからエピソードIDを抽出"""
        try:
            if '?' in url:
                episode_id = url.split('/')[-1].split('?')[0]
            else:
                episode_id = url.split('/')[-1]
            return episode_id
        except Exception as e:
            print(f"エピソードID抽出エラー: {str(e)}")
            return None

    # def get_episode_info(self, url):
    #     try:
    #         episode_id = self._get_episode_id(url)
    #         episode = self.sp.episode(episode_id)
            
    #         # ミリ秒を分:秒形式に変換
    #         duration_ms = episode['duration_ms']
    #         duration_min = duration_ms // (1000 * 60)
    #         duration_sec = (duration_ms // 1000) % 60
    #         duration = f"{duration_min}:{duration_sec:02d}"
            
    #         # 公開日をフォーマット
    #         release_date = datetime.strptime(episode['release_date'], '%Y-%m-%d').strftime('%Y年%m月%d日')
            
    #         return {
    #             'title': episode['name'],
    #             'description': episode['description'],
    #             'release_date': release_date,
    #             'duration': duration
    #         }
    #     except Exception as e:
    #         print(f"エピソード情報の取得に失敗: {str(e)}")
    #         return None
    
    def get_episode_info(self, url):
        try:
            episode_id = self._get_episode_id(url)
            episode = self.sp.episode(episode_id)
            
            # 公開日をフォーマット
            release_date = episode['release_date']  # 元のフォーマットのまま保持
            
            return {
                'title': episode['name'],
                'description': episode['description'],
                'release_date': release_date,  # フォーマット前の日付を返す
                'duration': f"{episode['duration_ms'] // (1000 * 60)}:{(episode['duration_ms'] // 1000) % 60:02d}",
                'duration_ms': episode['duration_ms']
            }
        except Exception as e:
            print(f"エピソード情報の取得に失敗: {str(e)}")
            return None





# src/listen_notes.py
import requests
from pathlib import Path
from utils import load_config
import urllib.parse

class ListenNotesClient:
    def __init__(self):
        self.config = load_config()
        self.base_url = "https://www.listennotes.com/api/v2"
        
    def search_episode(self, title):
        """タイトルからエピソードを検索"""
        # タイトルをURLエンコード
        encoded_title = urllib.parse.quote(title)
        search_url = f"{self.base_url}/search?q={encoded_title}&type=episode"
        
        # APIリクエストを送信
        response = requests.get(search_url, headers={
            "X-ListenAPI-Key": self.config['listen_notes']['api_key']
        })
        
        if response.status_code == 200:
            results = response.json()
            # 最も関連性の高いエピソードを返す
            if results['results']:
                return results['results'][0]
        return None

    def get_episode_url(self, spotify_title):
        """SpotifyのタイトルからListen NotesのURLを取得"""
        episode = self.search_episode(spotify_title)
        if episode:
            return f"https://www.listennotes.com/podcasts/{episode['podcast_id']}/episodes/{episode['id']}"
        return None
