import requests
import sys

code = input("Enter currency code :")
resp = requests.get(f"https://restcountries.eu/rest/v2/currency/{code}")

if resp.status_code != 200:
    print(f"Sorry!  Could not get details due to some error!")
    sys.exit(1)

countries = resp.json()
for c in countries:
    print(f"{c['name']}")
