import requests
import json
URL="http://127.0.0.1:8000/stucreate/"

data={
    'name':'Akhand',
    'roll':101,
    'city':'Pisawan'
}

json_data=json.dumps(data)

r=requests.post(url=URL,data=json_data)
data=r.json()
print(data)