from src.fetch_content import fetch_content
from src.ai_process import AIProcessor
from src.storage import VersionStorage
from src.search import RLSearch

def main():
    # Fetch content
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    content, screenshot = fetch_content(url)
    print("Content fetched.")

    # Process with AI
    processor = AIProcessor()
    spun_content = processor.spin_content(content)
    reviewed_content = processor.review_content(spun_content)
    print("AI processing completed.")

    # Human-in-the-loop edit
    print("Original content:", reviewed_content[:200])
    human_edit = input("Enter your edits (or press Enter to keep as is): ")
    final_content = reviewed_content if not human_edit else f"{reviewed_content}\nHuman Edit: {human_edit}"

    # Store and retrieve
    storage = VersionStorage()
    version_id = storage.save_version(final_content)
    searcher = RLSearch(storage)
    retrieved = searcher.search("chapter 1")
    print(f"Final content stored as {version_id} and retrieved: {retrieved[:200]}...")

if __name__ == "__main__":
    main()