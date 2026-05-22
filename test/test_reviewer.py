from scripts.agents.reviewer import ReviewerAgent
import os

def test_reviewer_integration():
    # Only run if API key is present
    if not os.environ.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY") == "your_actual_gemini_api_key_here":
        import pytest
        pytest.skip("Gemini API key not configured")

    agent = ReviewerAgent()
    prd_text = "Goal: Write a professional blog post about AI."
    draft_content = "AI is cool. It helps people do things faster. The end."
    
    result = agent.run(draft_content, prd_text, out_path="data/test_reviewed_draft.md")
    
    assert isinstance(result, str)
    assert len(result) > len(draft_content) # Reviewer should expand/refine
