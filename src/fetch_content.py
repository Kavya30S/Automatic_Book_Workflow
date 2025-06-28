from playwright.sync_api import sync_playwright
import os

def fetch_content(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")
        
        # Extract content
        content = page.query_selector("div#mw-content-text").inner_text()
        content = "\n".join(line for line in content.splitlines() if line.strip())
        
        # Save raw content
        raw_path = "data/raw/chapter_1.txt"
        os.makedirs(os.path.dirname(raw_path), exist_ok=True)
        with open(raw_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        # Save screenshot
        screenshot_path = "data/screenshots/chapter_1.png"
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        page.screenshot(path=screenshot_path, full_page=True)
        
        browser.close()
        return content, screenshot_path

if __name__ == "__main__":
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    content, screenshot = fetch_content(url)
    print(f"Content fetched and saved. Screenshot: {screenshot}")