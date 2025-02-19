# SPOTIFY_CLIENT_ID="your_spotify_client_id"
# SPOTIFY_CLIENT_SECRET="your_spotify_client_secret"
# LISTEN_NOTES_API_KEY="your_listen_notes_api_key"
# GEMINI_API_KEY="your_gemini_api_key" 
# NOTION_API_KEY="your_notion_api_key" 

from pathlib import Path
import yaml

# 正しい config.yaml のパスを設定
CONFIG_PATH = Path(__file__).parent.parent / "config/config.yaml"

def load_config():
    """YAML から設定をロード"""
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

# 設定をロード
config = load_config()

# Notion の API 設定
NOTION_API_KEY = config.get("notion", {}).get("api_key", "")
NOTION_DATABASE_ID = config.get("notion", {}).get("database_id", "")

# その他の API 設定
SPOTIFY_CLIENT_ID = config.get("spotify", {}).get("client_id", "")
SPOTIFY_CLIENT_SECRET = config.get("spotify", {}).get("client_secret", "")
LISTEN_NOTES_API_KEY = config.get("listen_notes", {}).get("api_key", "")
GEMINI_API_KEY = config.get("gemini", {}).get("api_key", "")

# デバッグ: 読み込んだ設定を確認
print(f"✅ CONFIG_PATH: {CONFIG_PATH}")
print(f"✅ NOTION_DATABASE_ID: {NOTION_DATABASE_ID}")
print(f"✅ NOTION_API_KEY: {NOTION_API_KEY[:10]}... (トークンの一部表示)")
