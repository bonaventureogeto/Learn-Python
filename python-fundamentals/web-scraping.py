# web scraping
import requests
from bs4 import BeautifulSoup
import csv
import re

url = "https://hojaleaks.com/building-a-dynamic-weather-application-using-the-javascript-dom"
response = requests.get(url)
# html_content = response.text

soup = BeautifulSoup(response.content, "html.parser")

headings = soup.find_all('h1')

# with open('hoja_headings.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['Heading'])
#     for heading in headings:
#         writer.writerow([heading.text])

# email pattern
# email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# emails = re.findall(email_pattern, soup.text)
# print(emails)

# url pattern
url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
urls = re.findall(url_pattern, soup.text)
print(urls)
