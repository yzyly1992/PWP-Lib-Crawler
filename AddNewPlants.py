import datetime, re, time, os
from PIL import Image
import math
import json

# pngItems = os.listdir()
plants = []
idNum = 0

thumbDir = ".\\Thumbnails\\"
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


def createPngDict(root, name):
    if not re.match(r'.*\.png', name):
        return
    path = os.path.join(root, name)
    try:
        im = Image.open(path)
    except IOError:
        print("failed to identify", path)
    else:
        if re.match(r'.*?tree.*?', name, flags=re.IGNORECASE):
            category = "Tree"
            name = name.replace('Tree', '')
        elif re.match(r'.*?shrub.*?', name, flags=re.IGNORECASE):
            category = "Shrub"
            name = name.replace('Shrub', '')
        elif re.match(r'.*?flower.*?', name, flags=re.IGNORECASE):
            category = "Flower"
            name = name.replace('Flower', '')
        elif re.match(r'.*?grass.*?', name, flags=re.IGNORECASE):
            category = "Grass"
            name = name.replace('Grass', '')
        elif re.match(r'.*?groundcover.*?', name, flags=re.IGNORECASE):
            category = "Groundcover"
            name = name.replace('Groundcover', '')
        elif re.match(r'.*?aquatic.*?', name, flags=re.IGNORECASE):
            category = "Aquatic"
            name = name.replace('Aquatic', '')
        elif re.match(r'.*?succulent.*?', name, flags=re.IGNORECASE):
            category = "Succulent"
            name = name.replace('Succulent', '')
        else:
            category = "Other"


        global idNum
        idNum = idNum + 1
        realId = 2242 + idNum
        imageSize = im.size
        fullName = name.split(".png")[0].replace('-', ' ').replace('_', ' ')
        dataType = "2D Cutout"
        fileSize = convert_size(os.path.getsize(path))
        createTime = time.ctime(os.path.getmtime(path))
        thumbName150 = fullName + " " + str(realId) + " 150p.jpg"
        thumbName300 = fullName + " " + str(realId) + " 300p.jpg"
        thumb150path = os.path.join(thumbDir, thumbName150)
        thumb300path = os.path.join(thumbDir, thumbName300)
        thumbName150Png = fullName + " " + str(realId) + " 150p.png"
        thumbName300Png = fullName + " " + str(realId) + " 300p.png"
        thumb150pathPng = os.path.join(thumbDir, thumbName150Png)
        thumb300pathPng = os.path.join(thumbDir, thumbName300Png)

        if im.mode == "RGBA":
            bg = Image.new("RGB", im.size, (255, 255, 255))
            bg.paste(im, mask=im)
            bg.thumbnail((300,300))
            bg.save(thumb300path)
            bg.thumbnail((150,150))
            bg.save(thumb150path)
            return plants.append({
                "id": realId,
                "name": fullName,
                "category": category,
                "path": path, 
                "dataType": dataType, 
                "fileSize": fileSize,
                "createTime": createTime,
                "imageSize": imageSize,
                "thumb150path": thumb150path[1:],
                "thumb300path": thumb300path[1:]})
        else:
            im.thumbnail((300,300), Image.ANTIALIAS)
            im.save(thumb300pathPng, "PNG")
            im.thumbnail((150,150),  Image.ANTIALIAS)
            im.save(thumb150pathPng, "PNG")
            return plants.append({
                "id": realId,
                "name": fullName,
                "category": category,
                "path": path, 
                "dataType": dataType, 
                "fileSize": fileSize,
                "createTime": createTime,
                "imageSize": imageSize,
                "thumb150path": thumb150pathPng[1:],
                "thumb300path": thumb300pathPng[1:]})

addPath = "Y:\\PWP-LIBRARY\\CUTOUTS\\PLANTS\\TROPICAL Collection\\"
for file in os.listdir(addPath):
    createPngDict(addPath, file)

# print("Trees: " + ', '.join(trees) + "\n")
# print("Shrubs: " + ', '.join(shrubs) + "\n")

with open('plants.json', 'a') as f:
    json.dump(plants, f)
    

# print(trees)