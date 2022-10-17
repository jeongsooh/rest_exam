import requests
import re
import json

URL = "http://127.0.0.1:8000/"

response = requests.get(URL)

# get csrftoken
temp = response.headers['Set-Cookie']
p = re.compile('csrftoken=[A-Za-z0-9]+[A-Za-z0-9]')
xcsrftoken = p.findall(temp)[0][10:]

headers={'x-csrftoken':xcsrftoken}

newItem = {
    "sensor_id":"gresystem002",
    "e_data": "Item #00X"
}

response = requests.post(URL, headers=headers, data=newItem)
print(response.text)