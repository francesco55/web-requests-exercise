
import requests
import json
import statistics

print("REQUESTING SOME DATA FROM THE INTERNET...")

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json"
print(request_url)
response = requests.get(request_url)
print(response.status_code)
print(response.text)

parsed_response = json.loads(response.text)
#print(parsed_response["name"])
#new_list = [d["name"] for d in parsed_response]
#print(new_list)

finalGrade_list = [d["finalGrade"] for d in parsed_response["students"]]
#length = len(finalGrade_list)
#sum = 0
#for l in finalGrade_list
#    sum = sum +l
#average = sum/l
print(statistics.mean(finalGrade_list))
print(finalGrade_list)