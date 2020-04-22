import os, re
import json

with open("people.json", "r") as jsonFile:
    data = json.load(jsonFile)

i = len(data)
n = 0

while n < i:
    name = data[n]["name"]
    path = data[n]["path"]
    thumb150path = data[n]["thumb150path"]
    thumb300path = data[n]["thumb300path"]
    data[n]["thumb150path"]=thumb150path[1:]
    data[n]["thumb300path"]=thumb300path[1:]
    if re.match(r'.*?bike.*?', name, flags=re.IGNORECASE):
            data[n]["category"] = "Bike"
    if re.match(r'.*?indian.*?', path, flags=re.IGNORECASE):
            data[n]["category"] = "Indian"
    if data[n]["category"] == "Indian":
            data[n]["name"] = "Indian" + str(data[n]["id"])
    n += 1

with open("people.json", "w") as f:
    json.dump(data, f)