from scripts.agents.outliner import OutlinerAgent
import os

def test_outliner_integration():
    # Only run if API key is present
    if not os.environ.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY") == "your_actual_gemini_api_key_here":
        import pytest
        pytest.skip("Gemini API key not configured")

    agent = OutlinerAgent()
    prd_text = "Goal: Write a blog post about AI. Audience: Developers."
    sources = [{"title": "AI Trends", "link": "http://example.com", "snippet": "AI is growing."}]
    
    result = agent.run(prd_text, sources, out_path="data/test_outline.json")
    
    assert "outline" in result
    assert isinstance(result["outline"], str)
    assert len(result["outline"]) > 0
