import os, re
import json

with open("faceme.json", "r") as jsonFile:
    data = json.load(jsonFile)

i = len(data)
n = 0

while n < i:
    name = data[n]["name"]
    data[n]["name"] = " ".join([i for i in name.split() if not i.isdigit()])
    n += 1

with open("faceme.json", "w") as f:
    json.dump(data, f)