import requests
import json
import time

base_url = "http://216.128.155.55:8000/api/trading"

print("--- Triggering Invoice Processing ---")
start_time = time.time()
try:
    res = requests.post(f"{base_url}/invoice", timeout=30)
    end_time = time.time()
    print(f"Status Code: {res.status_code}")
    print(f"Time Taken: {end_time - start_time:.2f} seconds")
    print("Response:")
    print(json.dumps(res.json(), indent=2))
except Exception as e:
    print(f"Failed: {e}")
