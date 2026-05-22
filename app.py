import streamlit as st
import os
import json
from scripts.agents.researcher import ResearcherAgent
from scripts.agents.outliner import OutlinerAgent
from scripts.agents.drafter import DrafterAgent
from scripts.agents.reviewer import ReviewerAgent
from scripts.utils import load_text, save_text

# Page configuration
st.set_page_config(page_title="Multi-Agent Content Ops", layout="wide")

st.title("🚀 Multi-Agent Content Data Ops")
st.markdown("Use this interface to run the full content generation pipeline powered by **Gemini** and **DuckDuckGo**.")

# Initialize data directory
os.makedirs("data", exist_ok=True)
default_prd_path = "data/prd_example.md"

if not os.path.exists(default_prd_path):
    with open(default_prd_path, "w") as f:
        f.write("# Sample PRD\n\nGoal: Write a blog post about the benefits of Multi-Agent Systems in 2024.\nTarget Audience: Technical Project Managers.")

# Sidebar - Settings
with st.sidebar:
    st.header("Settings")
    prd_content = st.text_area("Edit PRD Content", value=load_text(default_prd_path), height=300)
    if st.button("Save PRD"):
        save_text(prd_content, default_prd_path)
        st.success("PRD Saved!")

# Main Area
col1, col2 = st.columns(2)

with col1:
    st.header("1. Research & Outline")
    if st.button("Run Pipeline"):
        # Reset data for a clean run
        save_text(prd_content, default_prd_path)
        
        # Step 1: Research
        with st.status("🔍 Researching...", expanded=True) as status:
            researcher = ResearcherAgent()
            sources = researcher.run(prd_content)
            st.write(f"Found {len(sources)} sources.")
            st.json(sources)
            status.update(label="Research Complete!", state="complete")

        # Step 2: Outline
        with st.status("📝 Creating Outline...", expanded=True) as status:
            outliner = OutlinerAgent()
            outline = outliner.run(prd_content, sources)
            st.write("Outline generated.")
            st.json(outline)
            status.update(label="Outline Complete!", state="complete")

        # Step 3: Draft
        with st.status("✍️ Drafting Content...", expanded=True) as status:
            drafter = DrafterAgent()
            draft = drafter.run(outline)
            st.markdown("### Initial Draft")
            st.markdown(draft)
            status.update(label="Drafting Complete!", state="complete")

        # Step 4: Review
        with st.status("🧐 Reviewing & Refining...", expanded=True) as status:
            reviewer = ReviewerAgent()
            reviewed_draft = reviewer.run(draft, prd_content)
            st.session_state['final_result'] = reviewed_draft
            status.update(label="Review Complete!", state="complete")
            st.balloons()

with col2:
    st.header("2. Final Result")
    if 'final_result' in st.session_state:
        st.markdown(st.session_state['final_result'])
        st.download_button(
            label="Download Final Draft",
            data=st.session_state['final_result'],
            file_name="final_content.md",
            mime="text/markdown"
        )
    else:
        st.info("Run the pipeline to see the final output here.")
