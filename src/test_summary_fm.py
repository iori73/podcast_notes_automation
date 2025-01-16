# src/test_summary_fm.py
from summary_fm import SummaryFMProcessor


def test_summary_fm():
    processor = SummaryFMProcessor()
    results = processor.process_audio()
    
    if results:
        print("\n=== 文字起こし ===")
        print(results["transcription"][:200] + "...")  # 最初の200文字のみ表示
        
        print("\n=== 要約 ===")
        print(results["summary"])
        
        print("\n=== タイムスタンプ ===")
        print(results["timestamps"])

if __name__ == "__main__":
    test_summary_fm()

