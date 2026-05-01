import requests
def authenticate():
    url = "https://api.example.com/login"
    data = {'username': 'alex', 'password': '1234'}

    response = requests.post(url, json=data)

    if response.status_code == 200:
        print("Login successful")
    else:
        print(f"Authentication Failed: {response.status_code}")
