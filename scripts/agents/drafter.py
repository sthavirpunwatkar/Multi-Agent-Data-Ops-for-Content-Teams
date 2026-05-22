from scripts.adapters.openai_adapter import ChatClient
from scripts.utils import save_text
import json

class DrafterAgent:
    def run(self, outline_data, out_path="data/draft.md"):
        # Construct messages to send to LLM
        messages = [
            {"role": "system", "content": "You are an expert content writer. You turn outlines into engaging, comprehensive drafts."},
            {"role": "user", "content": f"Based on the following outline, write a full draft.\n\nOutline:\n{json.dumps(outline_data)}\n\nWrite the content in Markdown."}
        ]

        # Call the chat client
        response = ChatClient.completions_create(
            model="gpt-4",
            messages=messages
        )

        draft_content = response["choices"][0]["message"]["content"]

        save_text(draft_content, out_path)

        return draft_content
