import requests

# # get request
# response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# print(response.status_code)
# print(response.json())

import json

data = {'title': 'Foo', 'body': 'Bar', 'userId': 1}
headers = {'content-type': 'application/json'}

response = requests.post('https://jsonplaceholder.typicode.com/posts', data=json.dumps(data), headers=headers)

print(response.status_code)
print(response.json())
