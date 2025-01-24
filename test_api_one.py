import requests
import json

token = "a601f54b4ec24dba59bc90b1fa9d6f8fe540c311"
city = "Bangkok"

airq_api_url = "http://api.waqi.info/feed/#city#/?token=a601f54b4ec24dba59bc90b1fa9d6f8fe540c311"
requests_url = airq_api_url.replace("#city#", city)

print(requests_url)

response = requests.get(requests_url)
json_data = response.json()['data']

print(f"{json_data['city']['name']} has current pollution level: {json_data['aqi']}")

 