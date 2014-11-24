import requests
params = "58ccb27930a44373a42588b6342e9315"
r = requests.get('http://developer.cumtd.com/api/v2.1/json/GetStops', params=params)

print(r.json())