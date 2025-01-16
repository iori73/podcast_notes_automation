# src/test_listen_notes.py
from listen_notes import ListenNotesClient

def test_download():
    client = ListenNotesClient()
    # テスト用のLISTEN NOTESのエピソードURLを指定
    test_url = "エピソードのダウンロードURL"
    
    try:
        filepath = client.download_episode(test_url)
        print(f"ダウンロード完了: {filepath}")
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")

if __name__ == "__main__":
    test_download()
