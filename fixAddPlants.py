import os, re
import json

with open("plants.json", "r") as jsonFile:
    data = json.load(jsonFile)

i = len(data)
n = 0

while n < i:
    path = data[n]["path"]
    data[n]["mac"] = path.replace("\\", "/").replace("Y:", "/Volumes/Library")
    n += 1

with open("plants.json", "w") as f:
    json.dump(data, f)
