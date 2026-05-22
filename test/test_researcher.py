from scripts.agents.researcher import ResearcherAgent

def test_mock_researcher():
    agent = ResearcherAgent()
    results = agent.run("Artificial Intelligence trends 2024", "data/test_sources.json", n_sources=2)
    assert len(results) == 2
    assert all("title" in r for r in results)
