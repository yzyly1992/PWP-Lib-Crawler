import os, re
import json

with open("3d.json", "r") as jsonFile:
    data = json.load(jsonFile)


i = len(data)
n = 0
e = 2051
new3dJson = []
addFaceJson = []

while n < i:
    if data[n]["id"] in range(2604, 3634):
        data[n]["category"] = "People"
        e += 1
        data[n]["id"] = e
        data[n]["dataType"] = "Face-me"
        addFaceJson.append(data[n])
    else:
        new3dJson.append(data[n])
    n += 1

with open("3d.json", "w") as f:
    json.dump(new3dJson, f)

with open("faceme.json", "a") as jsonFace:
    json.dump(addFaceJson, jsonFace)
