def parse_url(url):
    parts = url.split("/", 3)
    base_url = parts[0] + "//" + parts[2]
    path = "/" + parts[3]
    print("Base URL:", base_url)
    print("Path:", path)
parse_url("https://example.com/products/item1")