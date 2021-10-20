
import json
import requests
from prettytable import PrettyTable

x = PrettyTable()
x.field_names = ["Canandian COVID Data", "Results"]

url = "https://api.covid19tracker.ca/summary"

payload = { 'signUp.email': 'skanaje@umich.edu'}
headers = {
'content-type': "text/xml"
}

response = requests.request("GET", url, data=payload, headers=headers)

#print(response.text)
json_format = json.loads(response.text)
#print(json_format)

for i in json_format:
   #print(i)
   if(i=='data'):
    #print(json_format[i][0])
    for j in json_format[i][0]:
        #print(j+" "+json_format[i][0][j])
        x.add_row([j,json_format[i][0][j]])
print(x)

