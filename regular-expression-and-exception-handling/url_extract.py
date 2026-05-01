import re
def extract_urls(text):
    urls = re.findall(r'https?://\S+', text)
    print(urls)

extract_urls("Visit https://google.com and http://github.com")