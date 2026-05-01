import requests

def fetch_data():
    url = "https://api.example.com/data"
    response = requests.get(url)
    return response.json()
print(fetch_data())

