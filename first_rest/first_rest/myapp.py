# import requests
# URL='http://127.0.0.1:8000/stuinfo'
# r=requests.get(url=URL)
# data=r.json()
# print(data)


import requests
import json
URL="http://127.0.0.1:8000/student_create/"
data={
    'id':5,
    'name':'sonom',
    'roll':101,
    'city':'Bhavnagar'
}

json_data = json.dumps(data) 


r = requests.post(url = URL, data = json_data) 
print("****************",r)
data=r.json() 

print(data) 