import os, re
import json

with open("faceme.json", "r") as jsonFile:
    data = json.load(jsonFile)

i = len(data)
n = 0

while n < i:
    data[n]["dataType"] = "Face-Me"
    n += 1

with open("faceme.json", "w") as f:
    json.dump(data, f)