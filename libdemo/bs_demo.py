from bs4 import BeautifulSoup
soup = BeautifulSoup("<h1>Test</h1><h1>Another Test</h1>", 'html.parser')

for h1 in soup.find_all("h1"):
    print(h1.text)