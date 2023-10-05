import requests, re
from bs4 import BeautifulSoup

url = "https://zinduaschool.com/blog/"
response = requests.get(url)
html_content = response.text


date_pattern = r'\d{1,2}\s+([A-Z][a-z]+)\s+\d{4}' # "2 October 2023"
dates = re.findall(date_pattern, html_content)

soup = BeautifulSoup(response.content, 'html.parser')

headings = soup.find_all('h2')
for heading in headings:
    print(heading.text)

for date in dates:
    print(date)
