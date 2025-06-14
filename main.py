import requests
import json
from datetime import datetime
import matplotlib.pyplot as plt
import os

# Your Tiingo API tok
# en
API_TOKEN = os.getenv("API_MUFFIN")
if not API_TOKEN: 
    print("❌ API token not found. Please set the API_MUFFIN environment variable.")
    exit()

# --- getting the current date ---
Today_date = datetime.today().date()
Investment_date = datetime.strptime(Today_date, "%d/%m/%Y").date()

#--- User Input ---
Company = input("Which company did you invest in? ")
Date = input("When did you invest into this company? ")
Amount = int(input("How much did you invest into this company? "))
if Amount < 0:
    print("❌ Invalid amount. Please enter a positive number.")
    exit()

# --- getting the current date ---
Date = input("When did you invest into this company? ")
Today_date = datetime.today().date()
Investment_date = datetime.strptime(Date, "%d/%m/%Y").date()
if Investment_date > Today_date:
    print("Sorry! How did you invest from the future?")
    exit()
if ValueError:
    print("❌ Sorry that isn't a valid date. Please use dd/mm/yyyy format and make sure the date is a real date.")
    exit()
# --- Bright Data Proxy Gateway Config ---
PROXY_HOST = "brd.superproxy.io"
PROXY_PORT = "port"
PROXY_USER = "user_name"
PROXY_PASS = "password"

# --- Build proxy config for requests ---
proxy_url = f"http://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}"
proxies = {"http": proxy_url, "https": proxy_url}

# --- Yahoo Finance API config ---
Date_str = Investment_date  # dd/mm/yyyy format

# Convert string to datetime object
dt = datetime.strptime(Date_str, "%d/%m/%Y")

# Now it's a datetime object, so we can call .timestamp()
timestamp = int(dt.timestamp())

print(timestamp)
symbol = f"{Company.upper()}"
interval = "1d"
url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?range={range_}&interval={interval}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# --- Make request through Bright Data proxy ---
try:
    print(f"🔄 Fetching stock data for {symbol} through Bright Data proxy...")
    response = requests.get(url, headers=headers, proxies=proxies, timeout=60)

    print("✅ Status Code:", response.status_code)
    print("📄 Response Preview:")

    data = response.json()
    print(json.dumps(data, indent=2))

    # --- Extract and format data ---
    result = data["chart"]["result"][0]
    dates = result["timestamp"]
    closes = result["indicators"]["quote"][0]["close"]

    # Convert Unix timestamps to dates
    #dates = [datetime.fromtimestamp(ts).strftime('%Y-%m-%d') for ts in timestamps]

    # --- Plotting ---
    plt.figure(figsize=(10, 5))
    plt.plot(dates, closes, marker='o')
    plt.title(f"{symbol} Closing Prices ({range})")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    plt.tight_layout()
    plt.savefig("stock_chart.png")

except requests.exceptions.RequestException as e:
    print(f"❌ Proxy request failed: {e}")
except (KeyError, IndexError, TypeError) as e:
    print(f"❌ Data parsing failed: {e}")
