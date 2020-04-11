import os, re
import json

with open("plants.json", "r") as jsonFile:
    data = json.load(jsonFile)

i = len(data)
n = 0
while n < i:
    tmpS = data[n]['thumb150path']
    tmpL = data[n]['thumb300path']
    data[n]['thumb150path'] = tmpS[1:]
    data[n]['thumb300path'] = tmpL[1:]
    if data[n]['keyWords'][0] == 'Aquatic':
        data[n]['category'] = 'Aquatic'
        tmpN = data[n]['name']
        data[n]['name'] = tmpN.replace('Aquatic', '')
    elif data[n]['keyWords'][0] == 'Succulent':
        data[n]['category'] = 'Succulent'
        tmpN = data[n]['name']
        data[n]['name'] = tmpN.replace('Succulent', '')
    elif data[n]['category'] == 'Tree':
        tmpN = data[n]['name']
        data[n]['name'] = tmpN.replace('Tree', '')
    elif data[n]['category'] == 'Shrub':
        tmpN = data[n]['name']
        data[n]['name'] = tmpN.replace('Shrub', '')
    elif data[n]['category'] == 'Flower':
        tmpN = data[n]['name']
        data[n]['name'] = tmpN.replace('Flower', '')
    elif data[n]['category'] == 'Groundcover':
        tmpN = data[n]['name']
        data[n]['name'] = tmpN.replace('Groundcover', '')
    elif data[n]['category'] == 'Grass':
        tmpN = data[n]['name']
        data[n]['name'] = tmpN.replace('Grass', '')
    n += 1

with open("plants.json", "w") as f:
    json.dump(data, f)