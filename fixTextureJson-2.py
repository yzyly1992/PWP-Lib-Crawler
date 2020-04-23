import os, re
import json

with open("texture.json", "r") as jsonFile:
    data = json.load(jsonFile)

i = len(data)
n = 0

while n < i:
    path = data[n]["path"]
    name = data[n]["name"]
    if len(path.split("\\")) == 6:
            if re.match(r'(.*?stone.*|.*?cobble.*)', name, flags=re.IGNORECASE):
                data[n]["category"] = "Stone"
            elif re.match(r'(.*?grass.*|.*?tree.*|.*?moss.*)', name, flags=re.IGNORECASE):
                data[n]["category"] = "Plant"
            elif re.match(r'(.*?metal.*|.*?grate.*|.*?steel.*)', name, flags=re.IGNORECASE):
                data[n]["category"] = "Metal"
            elif re.match(r'.*?glass.*', name, flags=re.IGNORECASE):
                data[n]["category"] = "Glass"
            elif re.match(r'.*?concrete.*', name, flags=re.IGNORECASE):
                data[n]["category"] = "Concrete"
            else:
                data[n]["category"] = "Other"

    data[n]["name"] = name.replace("+", " ").replace(".", " ")
    data[n]["name"] = " ".join([i for i in name.split() if not i.isdigit()])
    
    n += 1

with open("texture.json", "w") as f:
    json.dump(data, f)