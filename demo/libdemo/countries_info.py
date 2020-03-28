import requests
import sys

code = input("Enter country code :")
resp = requests.get(f"https://restcountries.eu/rest/v2/alpha/{code}")

if resp.status_code != 200:
    print(f"Sorry!  Could not get details due to some error!")
    sys.exit(1)

country = resp.json()
for k, v in country.items():
    print(f"{k:20} - {v}")
