import requests
from bs4 import BeautifulSoup


def getText(a):
    if len(a.text) > 0:
        return a.text
    else:
        return ''


resp = requests.get("http://www.srikanthtechnologies.com")
soup = BeautifulSoup(resp.text, "html.parser")
anchors = soup.findAll("a")
for a in anchors:
    print(getText(a))
    print(a['href'])
