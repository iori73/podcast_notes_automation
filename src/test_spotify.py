# src/test_spotify.py
from spotify import SpotifyClient

def test_spotify():
    client = SpotifyClient()
    # テスト用のSpotifyポッドキャストエピソードURL
    test_url = "SpotifyのポッドキャストエピソードのURL"
    episode_info = client.get_episode_info(test_url)
    print(f"タイトル: {episode_info['name']}")
    print(f"説明: {episode_info['description']}")

if __name__ == "__main__":
    test_spotify()
