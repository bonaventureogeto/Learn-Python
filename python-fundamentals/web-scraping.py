# web scraping
import requests
from bs4 import BeautifulSoup
import csv

url = "https://hojaleaks.com"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

headings = soup.find_all('h1')

with open('hoja_headings.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Heading'])
    for heading in headings:
        writer.writerow([heading.text])
