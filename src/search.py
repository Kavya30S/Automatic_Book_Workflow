from src.storage import VersionStorage
import random

class RLSearch:
    def __init__(self, storage):
        self.storage = storage

    def search(self, query):
        # Simplified RL: randomly select a version (can be expanded later)
        version_id = "chapter_1_v1"  # Only one version for now
        return self.storage.get_version(version_id)

if __name__ == "__main__":
    storage = VersionStorage()
    searcher = RLSearch(storage)
    result = searcher.search("chapter 1")
    print(f"Search result: {result[:50]}...")