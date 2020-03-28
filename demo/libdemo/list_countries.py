import requests
import sys

resp = requests.get("https://restcountries.eu/rest/v2/all")

if resp.status_code != 200:
    print(f"Sorry!  Could not get details due to some error!")
    sys.exit(1)

countries = resp.json()
for c in sorted(countries, key=lambda c: c['population'], reverse=True):
    print(f"{c['name']:50} {c['capital']:30}  {c['region']:10}  {c['population']:10}")
