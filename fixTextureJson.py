import os, re
import json

with open("texture.json", "r") as jsonFile:
    data = json.load(jsonFile)

i = len(data)
n = 0

while n < i:
    thumb150path = data[n]["thumb150path"]
    thumb300path = data[n]["thumb300path"]
    data[n]["thumb150path"]=thumb150path[1:]
    data[n]["thumb300path"]=thumb300path[1:]
    n += 1

with open("texture.json", "w") as f:
    json.dump(data, f)