import requests
import sys

def main():
    try:
        n_bitcoins = float(sys.argv[1])
    except:
        print("Wrong number of bitcoins")
        exit(1)

    url = "https://api.coindesk.com/v1/bpi/currentprice.json"

    try:
        data = requests.get(url).json()
    except:
        print("An error occurred")
        exit(1)

    usd_price = data["bpi"]["USD"]["rate_float"]

    print(f"The {n_bitcoins} bitcoins in USD is: {n_bitcoins*usd_price:,.4f}$")

if __name__ == "__main__":
    main()