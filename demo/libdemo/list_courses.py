import requests
from bs4 import BeautifulSoup

f = open("courses.xml")
bs = BeautifulSoup(f.read(), 'xml')    # Use XML Parser of lxml

for c in bs.find_all("course"):
    print(f"{c.find('name').text:25} {c.find('stdate').text}")