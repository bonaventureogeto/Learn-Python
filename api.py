import requests

api_key = "cbdca0e689dcf8e94ed5633cc78e03d4"

location = input("Enter location: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

# url2 = "https://jsonplaceholder.typicode.com/photos"

response = requests.get(url)

try:
    response.raise_for_status()
except requests.exceptions.HTTPError as error:
    print(f"An error occurred: {error}")

data = response.json()

print(data)
