import requests
from bs4 import BeautifulSoup

url = 'https://hojaleaks.com/series/python'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

headings = soup.find_all('h1')

for heading in headings:
    print(heading.text)
