# src/test_summary.py
import google.generativeai as genai
from utils import load_config

def generate_podcast_summary(text):
    config = load_config()
    genai.configure(api_key=config['gemini']['api_key'])
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = f"""
    以下のポッドキャストの内容を要約してください。
    フォーマット:
    - 概要（100文字程度）
    - 主要なポイント（箇条書き3-5個）
    
    テキスト:
    {text}
    """
    
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    # テスト用のサンプルテキスト
    sample_text = """
    今回のポッドキャストでは、AI技術の最新動向について議論しました。
    特に機械学習の応用例や、企業での実装事例について詳しく説明しています。
    また、今後の展望についても触れ、特に倫理的な課題について深く掘り下げました。
    """
    
    summary = generate_podcast_summary(sample_text)
    print(summary)
