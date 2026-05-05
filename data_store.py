import json

class DataStore:
    def __init__(self, path="sample_data.json"):
        with open(path, "r") as f:
            self.data = json.load(f)

    def search(self, query: str):
        results = []
        for item in self.data:
            if query.lower() in item["content"].lower() or query.lower() in item["title"].lower():
                results.append(item)

        return results