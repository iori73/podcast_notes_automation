# src/main.py
import google.generativeai as genai
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import load_config
import time
import requests

class PodcastAutomation:
    def __init__(self):
        self.config = load_config()
        self.setup_gemini()
        self.setup_driver()

    def setup_gemini(self):
        genai.configure(api_key=self.config['gemini']['api_key'])
        self.model = genai.GenerativeModel('gemini-pro')

    def setup_driver(self):
        options = Options()
        options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.wait = WebDriverWait(self.driver, 60)

    def generate_summary(self, text):
        prompt = f"以下のポッドキャストの内容を要約してください：\\n\\n{text}"
        response = self.model.generate_content(prompt)
        return response.text

if __name__ == "__main__":
    automation = PodcastAutomation()
    try:
        # テスト用のテキスト
        test_text = "これはテスト用のポッドキャストテキストです。"
        summary = automation.generate_summary(test_text)
        print(summary)
    finally:
        automation.driver.quit()
