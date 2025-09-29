import random

class MockOpenAIChat:
    def completions_create(self, model, messages, **kwargs):
        responses = [
            "Mock summary: friendly blog about baking.",
            "Mock draft: intro, 3 steps, troubleshooting tips.",
            "Mock idea: include equipment list and recipe."
        ]
        return {"choices": [{"message": {"content": random.choice(responses)}}]}

class MockOpenAIEmbeddings:
    def create(self, model, input, **kwargs):
        if isinstance(input, list):
            data = [{"embedding": [0.1] * 10} for _ in input]
        else:
            data = [{"embedding": [0.1] * 10}]
        return {"data": data}
