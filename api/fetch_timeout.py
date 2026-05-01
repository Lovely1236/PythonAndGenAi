import requests
def fetch_with_timeout():
    url = "https://api.example.com/payment"

    try:
        requests.get(url, timeout=5)
    except requests.exceptions.Timeout:
        print("Request Timeout: Retrying...")