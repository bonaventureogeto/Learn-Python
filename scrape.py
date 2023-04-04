import requests
from bs4 import BeautifulSoup
import csv

url = 'https://hojaleaks.com/series/python'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

headings = soup.find_all('h1')


with (open('hojaleaks_headings.csv', 'w')) as file:
    writer = csv.writer(file)
    writer.writerow(['Headings'])
    for heading in headings:
        writer.writerow([heading.text])
