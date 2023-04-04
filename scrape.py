import requests
from bs4 import BeautifulSoup
import csv

url = 'https://hojaleaks.com/series/python'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

images = soup.find_all('img', class_='post-cover')

# for image in images:
#     print(image['src'])

with (open('hojaleaks_images.csv', 'w')) as file:
    writer = csv.writer(file)
    writer.writerow(['images'])
    for image in images:
        writer.writerow(image['src'])

# with (open('hojaleaks_headings.csv', 'w')) as file:
#     writer = csv.writer(file)
#     writer.writerow(['Headings'])
#     for heading in headings:
#         writer.writerow([heading.text])
