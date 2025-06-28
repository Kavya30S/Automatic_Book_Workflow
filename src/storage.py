import chromadb

class VersionStorage:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(name="book_versions")

    def save_version(self, content):
        version_id = "chapter_1_v1"
        self.collection.add(documents=[content], ids=[version_id])
        return version_id

    def get_version(self, version_id):
        result = self.collection.get(ids=[version_id])
        return result["documents"][0] if result["documents"] else "Not found"

if __name__ == "__main__":
    with open("data/processed/reviewed_content.txt", "r", encoding="utf-8") as f:
        content = f.read()
    storage = VersionStorage()
    version_id = storage.save_version(content)
    retrieved = storage.get_version(version_id)
    print(f"Version {version_id} saved and retrieved: {retrieved[:50]}...")