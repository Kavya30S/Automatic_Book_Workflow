from transformers import pipeline
import os

class AIProcessor:
    def __init__(self):
        self.spinner = pipeline("text-generation", model="distilgpt2")
        self.reviewer = pipeline("summarization", model="facebook/bart-large-cnn")

    def spin_content(self, content):
        prompt = f"Rewrite this in your own words:\n{content[:500]}"
        spun = self.spinner(prompt, max_length=600, num_return_sequences=1)[0]["generated_text"]
        os.makedirs("data/processed", exist_ok=True)
        with open("data/processed/spun_content.txt", "w", encoding="utf-8") as f:
            f.write(spun)
        return spun

    def review_content(self, content):
        reviewed = self.reviewer(content, max_length=300, min_length=100, do_sample=False)[0]["summary_text"]
        with open("data/processed/reviewed_content.txt", "w", encoding="utf-8") as f:
            f.write(reviewed)
        return reviewed

if __name__ == "__main__":
    with open("data/raw/chapter_1.txt", "r", encoding="utf-8") as f:
        content = f.read()
    processor = AIProcessor()
    spun = processor.spin_content(content)
    reviewed = processor.review_content(spun)
    print("Spinning and reviewing completed.")