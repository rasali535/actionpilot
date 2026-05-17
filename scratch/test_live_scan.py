import requests
import json
import time

base_url = "http://216.128.155.55:8000/api/trading"

print("--- Triggering Autonomous Scan ---")
res_scan = requests.post(f"{base_url}/scan")
print("SCAN Response:")
print(json.dumps(res_scan.json(), indent=2))

print("\n--- Waiting 2 seconds ---")
time.sleep(2)

print("\n--- Fetching Boardroom History ---")
res_boardroom = requests.get(f"{base_url}/boardroom")
print("Boardroom Response:")
print(json.dumps(res_boardroom.json(), indent=2))
