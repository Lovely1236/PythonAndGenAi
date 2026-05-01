import requests
import json
def safe_json_parse():
    url = "https://api.example.com/data"

    try:
        response = requests.get(url)
        data = response.json()
        return data
    except json.decoder.JSONDecodeError:
        print("Error: Invalid JSON response")
