import json
import xml.etree.ElementTree as ET

day_temp=dict()
day_temp_json=dict()

tree = ET.parse('temp.xml')
data=tree.getroot()


for children in data:
    for child in children:
        date = children.text.strip()
        temp=int((child[1].text).strip())
        day_temp.setdefault(date,[]).append(temp)

print("From XML Files")
for i in day_temp:
    sum_temp=sum(day_temp[i])
    len_temp=len(day_temp[i])
    print("Average temp of day "+i+" "+str(sum_temp/len_temp))

with open("temp.json", encoding="utf8") as f:
    data = json.load(f)

for line in data['weather']:
    day_temp_json.setdefault(line['date'], []).append(line['temperature'])
print("From JSON File")
print(day_temp_json)
for day in day_temp_json:
    sum_temp_json=sum(day_temp_json[day])
    len_temp_json=len(day_temp_json[day])
    print("Average temp of day " + i + " " + str(sum_temp_json / len_temp_json))



