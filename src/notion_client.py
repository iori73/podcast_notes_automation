# import requests
# import json
# from config import NOTION_API_KEY, NOTION_DATABASE_ID  # config.py から読み込む

# class NotionClient:
#     def __init__(self):
#         self.token = NOTION_API_KEY
#         self.database_id = NOTION_DATABASE_ID
#         self.headers = {
#             "Authorization": f"Bearer {self.token}",
#             "Content-Type": "application/json",
#             "Notion-Version": "2022-06-28"
#         }

#     def create_page(self, title, markdown_content):
#         """Notion データベースにエピソード情報を追加"""
#         url = "https://api.notion.com/v1/pages"
#         data = {
#             "parent": {"database_id": self.database_id},
#             "properties": {
#                 "Name": {
#                     "title": [{"text": {"content": title}}]
#                 }
#             },
#             "children": [
#                 {
#                     "object": "block",
#                     "type": "paragraph",
#                     "paragraph": {
#                         "rich_text": [{"text": {"content": markdown_content}}]
#                     }
#                 }
#             ]
#         }

#         response = requests.post(url, headers=self.headers, data=json.dumps(data))
#         if response.status_code == 200:
#             print(f"✅ Notion に追加成功: {title}")
#         else:
#             print(f"❌ Notion 追加エラー: {response.status_code}, {response.text}")


import requests
import json
from config import NOTION_API_KEY, NOTION_DATABASE_ID

class NotionClient:
    def __init__(self):
        self.token = NOTION_API_KEY
        self.database_id = NOTION_DATABASE_ID
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }

    def create_page(self, title, markdown_content):
        """Notion データベースにエピソード情報を追加"""
        url = "https://api.notion.com/v1/pages"

        # 📌 Markdown を Notion の `children` 用のフォーマットに変換
        notion_blocks = self.format_markdown_to_notion(markdown_content)

        data = {
            "parent": {"database_id": self.database_id},
            "properties": {
                "Name": {"title": [{"text": {"content": title}}]}
            },
            "children": notion_blocks  # 📌 修正：適切にフォーマットされた Markdown を渡す
        }

        response = requests.post(url, headers=self.headers, data=json.dumps(data))
        if response.status_code == 200:
            print(f"✅ Notion に追加成功: {title}")
        else:
            print(f"❌ Notion 追加エラー: {response.status_code}, {response.text}")

    def format_markdown_to_notion(self, markdown_content):
        """Markdown を Notion API の `children` 用フォーマットに変換"""
        blocks = []
        paragraphs = []  # 長文用のバッファ

        def flush_paragraph():
            """バッファ内のパラグラフをまとめてブロックに変換"""
            if paragraphs:
                text = "\n".join(paragraphs)
                while len(text) > 2000:  # 2000 文字制限を超えないように分割
                    blocks.append({
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {"rich_text": [{"text": {"content": text[:2000]}}]}
                    })
                    text = text[2000:]
                blocks.append({
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {"rich_text": [{"text": {"content": text}}]}
                })
                paragraphs.clear()

        for line in markdown_content.split("\n"):
            line = line.strip()
            if not line:
                continue  # 空行をスキップ

            if line.startswith("## "):  # 📌 見出し (H2)
                flush_paragraph()
                blocks.append({
                    "object": "block",
                    "type": "heading_2",
                    "heading_2": {"rich_text": [{"text": {"content": line[3:]}}]}
                })
            elif line.startswith("- "):  # 📌 箇条書き (Bullet List)
                flush_paragraph()
                blocks.append({
                    "object": "block",
                    "type": "bulleted_list_item",
                    "bulleted_list_item": {"rich_text": [{"text": {"content": line[2:]}}]}
                })
            else:  # 📌 通常の段落
                paragraphs.append(line)

        # 残った段落を追加
        flush_paragraph()
        return blocks

