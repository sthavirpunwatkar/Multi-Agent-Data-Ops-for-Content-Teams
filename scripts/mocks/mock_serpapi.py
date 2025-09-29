class MockSerpAPI:
    def search(self, query, num_results=5):
        return [
            {"title": f"Mock article about {query}",
             "link": "http://example.com/mock",
             "snippet": f"Snippet about {query}."}
            for _ in range(num_results)
        ]
