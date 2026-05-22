import os
import time
import google.generativeai as genai
from google.api_core import exceptions
from scripts.utils import read_env

class GeminiClient:
    def __init__(self):
        # Configure Gemini API
        api_key = read_env("GEMINI_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.0-flash")

    def completions_create(self, messages, max_retries=5, **kwargs):
        """
        Mimics the ChatClient interface from OpenAI but uses Gemini.
        Includes a retry mechanism for Rate Limit (429) errors.
        """
        prompt = ""
        for msg in messages:
            role = msg['role'].upper()
            content = msg['content']
            prompt += f"{role}:\n{content}\n\n"
        
        for attempt in range(max_retries):
            try:
                response = self.model.generate_content(prompt)
                
                return {
                    "choices": [
                        {
                            "message": {
                                "content": response.text
                            }
                        }
                    ]
                }
            except exceptions.ResourceExhausted as e:
                if attempt < max_retries - 1:
                    wait_time = (2 ** attempt) + 2  # Exponential backoff: 3s, 4s, 6s, 10s...
                    print(f"Rate limit hit. Retrying in {wait_time}s... (Attempt {attempt + 1}/{max_retries})")
                    time.sleep(wait_time)
                else:
                    raise e
            except Exception as e:
                # Handle other potential transient errors
                if "429" in str(e) and attempt < max_retries - 1:
                    wait_time = (2 ** attempt) + 2
                    time.sleep(wait_time)
                else:
                    raise e

ChatClient = GeminiClient()
