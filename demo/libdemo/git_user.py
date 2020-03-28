
import requests
import sys

user = "srikanthpragada123"
resp = requests.get(f"https://api.github.com/users/{user}")

if resp.status_code == 404:
    print(f"Sorry!  {user} not found!")
    sys.exit(1)

if resp.status_code != 200:
    print(f"Sorry!  Could not get details due to some error!")
    sys.exit(2)

details = resp.json()
for k,v in details.items():
    print(f"{k:20} -  {v}")