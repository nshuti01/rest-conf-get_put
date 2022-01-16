import json
import requests
requests.packages.urllib3.disable_warnings() #disable ssl certificate

api_url = "https://192.168.0.129/restconf/data/ietf-interfaces:interfaces"

# dicitionary variable 
headers = { "Accept": "application/yang-data+json",
 "Content-type":"application/yang-data+json"
 }

#authenticatie
basicauth = ("cisco", "cisco123!")

#send request and store json data
resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)

print(resp)

#variable to convert json data
response_json = resp.json()

#json data weergeven
print (response_json)

#perify data
print(json.dumps(response_json, indent=4))
