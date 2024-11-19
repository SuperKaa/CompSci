import requests

def convert(from1, to):
    url = f"https://api.frankfurter.app/latest?from={from1}&to={to}"
    request = requests.get(url)
    data = request.json()
    
    if "rates" in data:
        rate = data["rates"][to]
        print(f"current {from1} to {to} rate: {rate}")
    else:
        print("error getting exchange rate")

from1 = input("enter what to convert from ").upper()
to = input("enter what currency to convert to ").upper()

convert(from1, to)
