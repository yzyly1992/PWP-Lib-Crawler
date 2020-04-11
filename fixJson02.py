import os, re
import json

with open("plants.json", "r") as jsonFile:
    data = json.load(jsonFile)

i = len(data)
n = 0
newList = []
while n < i:
    path = data[n]["path"]
    data[n]["mac"] = path.replace("\\", "/").replace("Y:", "/Volumes")
    del data[n]["keyWords"]
    name = data[n]["name"]
    data[n]["name"] = " ".join([i for i in name.split() if not i.isdigit()])
    if not "copy" in data[n]["name"]:
        newList.append(data[n])
    n += 1

with open("plants.json", "w") as f:
    json.dump(newList, f)


