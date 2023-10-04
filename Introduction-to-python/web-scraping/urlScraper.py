import requests, re
from bs4 import BeautifulSoup

url = "https://hojaleaks.com"
response = requests.get(url)
html_content = response.text


url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
urls = re.findall(url_pattern, html_content)

for url in urls:
    print(url)
