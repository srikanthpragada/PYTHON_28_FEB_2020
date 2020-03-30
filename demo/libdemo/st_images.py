import requests
from bs4 import BeautifulSoup

resp = requests.get("http://www.srikanthtechnologies.com")
bs = BeautifulSoup(resp.text, 'html.parser')

for t in bs.find_all('img'):
    print(t['src'])
