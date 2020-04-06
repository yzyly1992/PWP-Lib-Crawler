import os, datetime, re, time
import pymongo
from PIL import Image
import math
import json

# pngItems = os.listdir()
plants = []
idNum = 0
testDir = '/Volumes/Library/PWP-LIBRARY/CUTOUTS/PLANTS/AUSSIE NZ Collection'
currentDir = os.getcwd()
thumbDir = './Thumbnails/'
if not os.path.isdir(thumbDir):
    try:
        os.mkdir(thumbDir)
    except OSError:
        print("Creation of the directory %s failed" % thumbDir)


def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

# for item in pngItems:
#     if re.match(r'.*\.png', item):
#         if re.match(r'^Tree', item):
#             trees.append(item)
#         elif re.match(r'^Shrub', item):
#             shrubs.append(item)

def createPngDict(root, name):
    if not re.match(r'.*\.png', name):
        return
    path = os.path.join(root, name)
    try:
        im = Image.open(path)
    except IOError:
        print("failed to identify", path)
    else:
        if re.match(r'.*?tree.*\.png', name, flags=re.IGNORECASE):
            category = "Tree"
        elif re.match(r'.*?shrub.*\.png', name, flags=re.IGNORECASE):
            category = "Shrub"
        elif re.match(r'.*?flower.*\.png', name, flags=re.IGNORECASE):
            category = "Flower"
        elif re.match(r'.*?grass.*\.png', name, flags=re.IGNORECASE):
            category = "Grass"
        elif re.match(r'.*?groundcover.*\.png', name, flags=re.IGNORECASE):
            category = "Groundcover"
        else:
            category = "Other"
        global idNum
        idNum = idNum + 1
        imageSize = im.size
        fullName = name.split(".png")[0].replace('-', ' ').replace('_', ' ')
        dataType = "2D Cutout"
        keyWords = fullName.split()
        fileSize = convert_size(os.path.getsize(path))
        createTime = time.ctime(os.path.getmtime(path))
        thumbName150 = fullName + " " + str(idNum) + " 150p.jpg"
        thumbName300 = fullName + " " + str(idNum) + " 300p.jpg"
        thumb150path = os.path.join(thumbDir, thumbName150)
        thumb300path = os.path.join(thumbDir, thumbName300)

        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, im)
        bg.thumbnail((300,300))
        bg.save(thumb300path)
        bg.thumbnail((150,150))
        bg.save(thumb150path)

        return plants.append({
        "id": idNum,
        "name": fullName,
        "category": category,
        "path": path, 
        "dataType": dataType, 
        "keyWords": keyWords,
        "fileSize": fileSize,
        "createTime": createTime,
        "imageSize": imageSize,
        "thumb150path": thumb150path,
        "thumb300path": thumb300path})

for root, dirs, files in os.walk(currentDir, topdown=True):
    for name in files:
        createPngDict(root, name)

# print("Trees: " + ', '.join(trees) + "\n")
# print("Shrubs: " + ', '.join(shrubs) + "\n")

with open('plants.json', 'w') as f:
    json.dump(plants, f)
    

# print(trees)