from scripts.adapters.ddg_adapter import SearchClient as SerpClient
from scripts.adapters.gemini_adapter import ChatClient
from scripts.utils import save_json

class ResearcherAgent:
    def run(self, prd_text, out_path="data/sources.json", n_sources=3):
        results = SerpClient.search(prd_text, num_results=n_sources)
        save_json(results, out_path)
        return results
