# src/test_gemini.py
import google.generativeai as genai
from utils import load_config

def test_gemini():
    config = load_config()
    genai.configure(api_key=config['gemini']['api_key'])
    model = genai.GenerativeModel('gemini-pro')
    
    response = model.generate_content('こんにちは！')
    print(response.text)

if __name__ == "__main__":
    test_gemini()
