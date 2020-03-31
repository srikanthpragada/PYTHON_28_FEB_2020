import requests
from bs4 import BeautifulSoup

resp = requests.get("http://www.srikanthtechnologies.com/rss.xml")
bs = BeautifulSoup(resp.text, 'xml')    # Use XML Parser of lxml

for c in bs.find_all("item"):
    print(c.find('title').text.strip())
    print(c.find('link').text.strip())
    print(c.find('pubDate').text.strip())
    print("-" * 80)
