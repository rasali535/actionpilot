import requests
import json

url = "http://216.128.155.55:8000/api/trading/status"
try:
    print(f"Requesting GET {url}...")
    res = requests.get(url, timeout=15)
    print("Status Code:", res.status_code)
    print("Response JSON:")
    print(json.dumps(res.json(), indent=2))
except Exception as e:
    print("Failed:", e)
