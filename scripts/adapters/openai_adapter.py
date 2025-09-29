from scripts.utils import read_env
from scripts.mocks.mock_openai import MockOpenAIChat, MockOpenAIEmbeddings

USE_MOCKS = read_env("USE_MOCKS", "true").lower() == "true"

if USE_MOCKS:
    ChatClient = MockOpenAIChat()
    EmbeddingClient = MockOpenAIEmbeddings()
else:
    from openai import OpenAI
    client = OpenAI()
    ChatClient = client.chat
    EmbeddingClient = client.embeddings
