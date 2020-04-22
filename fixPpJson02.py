import os, re
import json

with open("people.json", "r") as jsonFile:
    data = json.load(jsonFile)

i = len(data)
n = 0

while n < i:
    name = data[n]["name"]
    path = data[n]["path"]
    if re.match(r'.*?diverse.*?', path, flags=re.IGNORECASE):
            data[n]["name"] = "Diverse " + str(data[n]["id"])
    if data[n]["category"] == "Indian":
            data[n]["name"] = "Indian " + str(data[n]["id"])
    n += 1

with open("people.json", "w") as f:
    json.dump(data, f)