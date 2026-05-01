def fetch_all_pages():
    page = 1
    total_pages = 3

    while page <= total_pages:
        print(f"Fetching page {page}")
        page += 1

    print("Fetched all pages successfully.")
