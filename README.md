# 🚀 Multi-Agent Content Data Ops

A powerful, modular, and **cost-optimized** multi-agent pipeline designed for content teams. This system automates the entire content creation lifecycle—from raw research to final expert-reviewed drafts—using a collaborative swarm of specialized AI agents.

## 🌟 Why This Project? (Best Features)

Compared to standard AI writing tools or simple single-agent scripts, this project offers:

1.  **Swarm Intelligence:** Unlike a single prompt, our workflow uses 4 specialized agents (**Researcher, Outliner, Drafter, Reviewer**) that critique and build upon each other's work, resulting in higher accuracy and better structure.
2.  **Zero-Cost Research Integration:** Built-in **DuckDuckGo Search** adapter provides real-time web data without requiring expensive SerpApi or Google Search API keys.
3.  **Advanced Rate-Limit Resilience:** Custom **Exponential Backoff** logic specifically tuned for Gemini's free tier, ensuring the pipeline completes even under heavy traffic.
4.  **Plug-and-Play Adapters:** A modular architecture allows you to swap between **Gemini**, **OpenAI**, and various search providers simply by changing a single line of code.
5.  **Interactive Streamlit UI:** A professional dashboard to visualize the research process, edit PRDs in real-time, and download final results.

---

## 🛠️ The Agent Swarm

-   **🔍 Researcher Agent:** Scours the web using DuckDuckGo to find the most relevant and up-to-date sources.
-   **📝 Outliner Agent:** Synthesizes research into a logical, hierarchical structure.
-   **✍️ Drafter Agent:** Transforms the outline into a comprehensive, engaging Markdown draft.
-   **🧐 Reviewer Agent:** Acts as an editor-in-chief, refining the draft against the original PRD for tone, accuracy, and goal alignment.

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.9+
- A Google Gemini API Key ([Get it here](https://aistudio.google.com/))

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/sthavirpunwatkar/Multi-Agent-Data-Ops-for-Content-Teams.git
cd Multi-Agent-Data-Ops-for-Content-Teams

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4. Run the UI
```bash
streamlit run app.py
```

---

## 🧪 Testing
The project includes a comprehensive suite of integration tests to verify API connectivity and agent logic:
```bash
$env:PYTHONPATH="."; pytest test/
```

## 📜 License
MIT License. Free to use and modify.
