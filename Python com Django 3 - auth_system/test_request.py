import requests

url = "http://127.0.0.1:8000/auth/register/"
data = {"username": "meuuser", "password": "minhasenha"}

response = requests.post(url, json=data)

print(response.json())
