import requests
import csv
from bs4 import BeautifulSoup

url = "https://hojaleaks.com"
response = requests.get(url)

# print(response)

soup = BeautifulSoup(response.content, 'html.parser')

# print(soup)

headings = soup.find_all('h1')

with open('headings.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['HEADINGS'])
    for heading in headings:
        writer.writerow([heading.text])
