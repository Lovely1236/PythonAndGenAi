import requests
import time
def fetch_with_retry(url, retries=3):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Success after {attempt+1} attempts")
                return response.json()
            else:
                raise Exception("API Error")
        except Exception:
            time.sleep(2 ** attempt)
    print("Failed after retries")