import os, re
import json

with open("plants.json", "r") as jsonFile:
    data = json.load(jsonFile)

i = len(data)
n = 0

while n < i:
    macPath = data[n]["mac"]
    winPath = data[n]["path"]
    data[n]["mac"] = macPath.replace("/PLANTS", "/PLANTS/COLLECTIONS") 
    data[n]["path"] = winPath.replace("\\PLANTS", "\\PLANTS\\COLLECTIONS")
    n += 1

with open("plants.json", "w") as f:
    json.dump(data, f)