import requests
import urllib.request

response = requests.get("https://github.com/")

print(response.status_code)
# print(response.content)

# data = {'name': 'Alexa', 'age': 39}

# response = requests.post('https://httpbin.org/post', data=data)

# print(response.status_code)
# print(response.content)


text = "Hello World"

bytes = text.encode('utf-8')

print(bytes)


url = "https://github.com"
response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('utf-8')
print(text)
