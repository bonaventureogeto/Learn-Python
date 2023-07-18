import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.nytimes.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

articles = soup.find_all('section', class_='story-wrapper')
# print(len(articles))
data = []

for article in articles[:10]:
    title = article.find('h3').text.strip()
    # description = article.find(
    #     'p', class_='summary-class').text.strip()
    # data.append({'title': title, 'description': description})
    print(title)

with open('nytimes.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'description'])
    writer.writeheader()
    writer.writerows(data)
