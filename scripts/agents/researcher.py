from scripts.adapters.ddg_adapter import SearchClient
from scripts.utils import save_json

class ResearcherAgent:
    def run(self, prd_text, out_path="data/sources.json", n_sources=3):
        results = SearchClient.search(prd_text, num_results=n_sources)
        save_json(results, out_path)
        return results
