import os
import json
from dotenv import load_dotenv

load_dotenv()

def save_json(obj, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)

def load_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def read_env(key, default=None):
    return os.environ.get(key, default)
