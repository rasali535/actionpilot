import requests
import json

url = "http://216.128.155.55:8000/api/trading/scan"

try:
    print(f"Triggering scan via POST {url}...")
    res = requests.post(url, timeout=45)
    print("Status Code:", res.status_code)
    print("Response JSON:")
    print(json.dumps(res.json(), indent=2))
except Exception as e:
    print("Scan failed:", e)
