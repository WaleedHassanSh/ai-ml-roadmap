# A simple program that calculates the total value of a certain amount of time spent on Bitcoin based on the current price of Bitcoin in USD. The user provides the amount of time as a command-line argument, and the program retrieves the current price of Bitcoin from an API and calculates the total value accordingly.

import sys

import requests

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")

while True:
    try:
        time = float(sys.argv[1])
        break

    except ValueError:
        sys.exit("Command-line argument is not a number")

try:
    response = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin?apiKey=YOUR_API_KEY_HERE"
    )
    response.raise_for_status()

except (requests.RequestException, requests.HTTPError):
    sys.exit("Request error")

o = response.json()

price = float(o["data"]["priceUsd"])

total = price * time

print(f"${total:,.4f}")
