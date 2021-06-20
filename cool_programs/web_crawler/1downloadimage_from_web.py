import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_file_name = str(name) + ".jpg"         #format: 500.jpg
    urllib.request.urlretrieve(url, full_file_name)

download_web_image("your_url")