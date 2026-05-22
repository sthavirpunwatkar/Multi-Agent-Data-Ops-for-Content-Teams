from ddgs import DDGS

class DuckDuckGoClient:
    @staticmethod
    def search(query, num_results=3):
        results = []
        try:
            with DDGS() as ddgs:
                # Use DDGS.text() and fetch max_results
                ddg_results = list(ddgs.text(query, max_results=num_results))

                # Transform results into the exact mocked output format expected by the system
                for r in ddg_results:
                    results.append({
                        "title": r.get("title", ""),
                        "link": r.get("href", ""),
                        "snippet": r.get("body", "")
                    })
        except Exception as e:
            print(f"DDG Search error: {e}")
        return results

SearchClient = DuckDuckGoClient()
