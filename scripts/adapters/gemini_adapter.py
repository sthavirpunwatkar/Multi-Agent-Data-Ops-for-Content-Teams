import os
import google.generativeai as genai
from scripts.utils import read_env

class GeminiClient:
    def __init__(self):
        # Configure Gemini API
        api_key = read_env("GEMINI_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def completions_create(self, messages, **kwargs):
        """
        Mimics the ChatClient interface from OpenAI but uses Gemini.
        `messages` expects a list of dicts with 'role' and 'content'.
        """
        # Gemini does not use "system", "user" structure in exactly the same way
        # For simplicity, we combine the system and user messages into a single prompt string
        prompt = ""
        for msg in messages:
            prompt += f"{msg['role'].upper()}:\n{msg['content']}\n\n"

        response = self.model.generate_content(prompt)

        # Return in the same mocked dict structure expected by the agents
        return {
            "choices": [
                {
                    "message": {
                        "content": response.text
                    }
                }
            ]
        }

ChatClient = GeminiClient()
