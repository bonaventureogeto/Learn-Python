import requests
from bs4 import BeautifulSoup
import csv

url = 'https://hojaleaks.com/series/python'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

headings = soup.find_all('h1', class_='blog-post-card-title')

# for image in images:
#     print(image['src'])

# with (open('hojaleaks_images.csv', 'w')) as file:
#     writer = csv.writer(file)
#     writer.writerow(['images'])
#     for image in images:
#         writer.writerow(image['src'])

with (open('hojaleaks_headings.csv', 'w')) as file:
    writer = csv.writer(file)
    writer.writerow(['Headings'])
    for heading in headings:
        writer.writerow([heading.text])
