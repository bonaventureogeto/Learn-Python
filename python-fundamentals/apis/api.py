import requests
import os

# working with openweathermap api
api_key = os.environ.get('API_KEY')
location = input("Enter Location: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
response = requests.get(url)

response = requests.get(url)

try:
    response.raise_for_status()
    data = response.json()
    print(data)
    print("Success!")
except requests.exceptions.HTTPError as error:
    print(f"An error occurred: {error}")


# print(data['main'])

# url = "https://jsonplaceholder.typicode.com/posts"
# data = {
#     "userId": 3457,
#     "id": 1,
#     "title": "To make a POST request in Python, you would use the following code",
#     "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
# }

# response = requests.post(url, data=data)

# print(response.text)
