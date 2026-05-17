import requests
import json
import time

base_url = "http://216.128.155.55:8000/api/trading"

print("--- Placing Manual BUY of 0.001 BTC/USD ---")
res_buy = requests.post(f"{base_url}/manual", json={
    "action": "BUY",
    "pair": "BTC/USD",
    "volume": 0.001
})
print("BUY Response:")
print(json.dumps(res_buy.json(), indent=2))

print("\n--- Waiting 2 seconds ---")
time.sleep(2)

print("\n--- Fetching Status after BUY ---")
res_status = requests.get(f"{base_url}/status")
status_data = res_status.json()
print(json.dumps(status_data, indent=2))

print("\n--- Placing Manual SELL of 0.001 BTC/USD ---")
res_sell = requests.post(f"{base_url}/manual", json={
    "action": "SELL",
    "pair": "BTC/USD",
    "volume": 0.001
})
print("SELL Response:")
print(json.dumps(res_sell.json(), indent=2))

print("\n--- Waiting 2 seconds ---")
time.sleep(2)

print("\n--- Fetching Status after SELL ---")
res_status2 = requests.get(f"{base_url}/status")
status_data2 = res_status2.json()
print(json.dumps(status_data2, indent=2))
