import httpx
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("FEATHERLESS_API_KEY")
url = "https://api.featherless.ai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
}

models = [
    "Qwen/Qwen2.5-72B-Instruct",
    "deepseek-ai/DeepSeek-V3.2"
]

for model in models:
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello! Say hi."}
        ],
        "temperature": 0.7,
        "max_tokens": 100
    }
    try:
        print(f"Testing model {model}...")
        res = httpx.post(url, headers=headers, json=payload, timeout=10.0)
        print("Status:", res.status_code)
        print("Response:", res.text[:200])
    except Exception as e:
        print("Error:", e)
