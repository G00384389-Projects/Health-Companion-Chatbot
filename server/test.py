import requests
import json

#   Code to test the api is being called
url = "http://localhost:5000/answer"
data = {"message": "Hello, AI!"}
headers = {"Content-Type": "application/json"}

response = requests.post(url, data=json.dumps(data), headers=headers)

print("Status code:", response.status_code)
print("Response text:", response.text)

try:
    print("Response JSON:", response.json())
except json.JSONDecodeError:
    print("No JSON could be decoded from the response.")