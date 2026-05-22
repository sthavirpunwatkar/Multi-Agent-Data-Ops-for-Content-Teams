from scripts.adapters.gemini_adapter import ChatClient
from scripts.utils import save_json
import json

class OutlinerAgent:
    def run(self, prd_text, sources, out_path="data/outline.json"):
        # Construct messages to send to LLM
        messages = [
            {"role": "system", "content": "You are an expert outliner. You organize research into logical, well-structured outlines."},
            {"role": "user", "content": f"Based on the following PRD and Research Sources, create an outline.\n\nPRD:\n{prd_text}\n\nSources:\n{json.dumps(sources)}\n\nRespond with a structured JSON outline."}
        ]

        # Call the chat client
        response = ChatClient.completions_create(
            model="gpt-4",
            messages=messages
        )

        outline_content = response["choices"][0]["message"]["content"]

        # In a real scenario, we might parse this. For now, we save it as a structured dict
        outline_data = {"outline": outline_content}
        save_json(outline_data, out_path)

        return outline_data
