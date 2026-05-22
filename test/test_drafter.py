from scripts.agents.drafter import DrafterAgent
import os

def test_drafter_integration():
    # Only run if API key is present
    if not os.environ.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY") == "your_actual_gemini_api_key_here":
        import pytest
        pytest.skip("Gemini API key not configured")

    agent = DrafterAgent()
    outline_data = {"outline": "1. Introduction to AI\n2. Benefits\n3. Conclusion"}
    
    result = agent.run(outline_data, out_path="data/test_draft.md")
    
    assert isinstance(result, str)
    assert len(result) > 0
