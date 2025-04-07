import requests
import sys

if (len(sys.argv) < 2):
    sys.exit("Missing command-line argument")

if sys.argv[1].isalpha():
    sys.exit("Command-line argument is not a number")

try:
    res = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=5a1bb68201a50f91707f986e829a815634d15402cee9c36da4bc0a4209e3c255').json()
    cost = float(res['data']['priceUsd']) * float(sys.argv[1])
    output = "$"+"{:,.4f}".format(cost)

    print(output)

except requests.RequestException:
    print("idk what to type here")
