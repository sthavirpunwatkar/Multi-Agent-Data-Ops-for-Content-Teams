from scripts.utils import read_env
from scripts.mocks.mock_serpapi import MockSerpAPI

USE_MOCKS = read_env("USE_MOCKS", "true").lower() == "true"

if USE_MOCKS:
    SerpClient = MockSerpAPI()
else:
    import requests
    class RealSerpClient:
        def __init__(self):
            self.api_key = read_env("SERPAPI_API_KEY")
        def search(self, query, num_results=5):
            url = "https://serpapi.com/search.json"
            params = {"engine":"google","q":query,"api_key":self.api_key,"num":num_results}
            r = requests.get(url, params=params, timeout=15)
            return r.json().get("organic_results", [])
    SerpClient = RealSerpClient()
