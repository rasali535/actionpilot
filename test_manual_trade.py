import requests
import json

base_url = "http://216.128.155.55:8000/api/trading"

try:
    # 1. Place a manual BUY order
    print("--- Placing Manual BUY of 0.05 AAPL/USD ---")
    res_buy = requests.post(f"{base_url}/manual", json={"action": "BUY", "pair": "AAPL/USD", "volume": 0.05})
    print("BUY Status Code:", res_buy.status_code)
    print("BUY Response:", res_buy.json())
    
    # 2. Check status to see updated balance and holdings
    print("\n--- Fetching Status after BUY ---")
    res_status1 = requests.get(f"{base_url}/status")
    data1 = res_status1.json()
    print("Balance USD:", data1["balance"]["USD"])
    print("Holdings:", data1["balance"]["holdings"])
    
    # 3. Place a manual SELL order to liquidate position
    print("\n--- Placing Manual SELL of 0.05 AAPL/USD ---")
    res_sell = requests.post(f"{base_url}/manual", json={"action": "SELL", "pair": "AAPL/USD", "volume": 0.05})
    print("SELL Status:", res_sell.json())
    
    # 4. Verify balance went back
    print("\n--- Fetching Status after SELL ---")
    res_status2 = requests.get(f"{base_url}/status")
    data2 = res_status2.json()
    print("Balance USD:", data2["balance"]["USD"])
    print("Holdings:", data2["balance"]["holdings"])

except Exception as e:
    print("Failed:", e)
