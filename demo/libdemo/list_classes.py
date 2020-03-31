import requests
from bs4 import BeautifulSoup

resp = requests.get("http://www.srikanthtechnologies.com/")
bs = BeautifulSoup(resp.text, 'html.parser')

classes = set()  # Empty set
for t in bs.find_all():
    if t.has_attr('class'):
        for c in t['class']:
            classes.add(c)

for c in sorted(classes):
    print(c)
