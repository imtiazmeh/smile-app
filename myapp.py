import requests
import json
URL = 'http://127.0.0.1:8000/student/create/'
data = {
    'name': 'Sonia',
    'roll_no': '2',
    'city': 'Lahore'
}
json_data = json.dumps(data)
res = requests.post(url=URL, data=json_data)
print(res.json())
