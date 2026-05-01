import requests
def fetch_with_token():
    token = "abc123"
    headers = {'Authorization': f'Bearer {token}'}

    response = requests.get("https://api.example.com/secure", headers=headers)

    if response.status_code == 200:
        print("Request Authorized")