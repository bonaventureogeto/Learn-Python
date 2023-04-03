import requests

api_key = "YOUR-API-KEY"
url = f"http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid={api_key}"

response = requests.get(url)
data = response.json()

print(data)
