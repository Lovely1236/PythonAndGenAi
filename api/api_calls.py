import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
def fetch_endpoint(endpoint):
    url = f"https://api.example.com{endpoint}"
    response = requests.get(url)
    return response.status_code

def parallel_calls():
    endpoints = ['/users', '/products', '/orders']
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(fetch_endpoint, ep) for ep in endpoints]

        for _ in as_completed(futures):
            pass

    print("Fetched 3 APIs in parallel.")