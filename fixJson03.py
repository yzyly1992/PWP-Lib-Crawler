import os, re
import json

with open("plants.json", "r") as jsonFile:
    data = json.load(jsonFile)

i = len(data)
n = 0

while n < i:
    path = data[n]["mac"]
    data[n]["mac"] = path.replace("/Volumes", "/Volumes/Library") 
    print(data[n]["mac"])
    n += 1

with open("plants.json", "w") as f:
    json.dump(data, f)