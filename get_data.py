# get_data.py

import requests
import json

print("REQUESTING SOME DATA FROM THE INTERNET...")

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"
print(request_url)
response = requests.get(request_url)
print(response.status_code)
print(response.text)

parsed_response = json.loads(response.text)
#print(parsed_response["name"])
new_list = [d["name"] for d in parsed_response]
print(new_list)
