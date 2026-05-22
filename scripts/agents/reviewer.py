from scripts.adapters.gemini_adapter import ChatClient
from scripts.utils import save_text

class ReviewerAgent:
    def run(self, draft_content, prd_text, out_path="data/reviewed_draft.md"):
        # Construct messages to send to LLM
        messages = [
            {"role": "system", "content": "You are an expert editor. You review drafts against PRDs to ensure tone, goals, and accuracy are met."},
            {"role": "user", "content": f"Please review and refine the following draft based on the original PRD.\n\nPRD:\n{prd_text}\n\nDraft:\n{draft_content}\n\nProvide the final refined draft in Markdown format."}
        ]

        # Call the chat client
        response = ChatClient.completions_create(
            model="gpt-4",
            messages=messages
        )

        reviewed_content = response["choices"][0]["message"]["content"]

        save_text(reviewed_content, out_path)

        return reviewed_content
