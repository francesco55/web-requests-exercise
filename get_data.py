# get_data.py

import requests

print("REQUESTING SOME DATA FROM THE INTERNET...")

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/1.json"
print(request_url)
response = requests.get(request_url)
print(response.status_code)
print(response.text)