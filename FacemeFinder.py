import datetime, re, time, os
from PIL import Image
import math
import json
from ConfigWin import cutoutPathPlants

# pngItems = os.listdir()
people = []
idNum = 0
currentDir = os.getcwd()
thumbDir = ".\\Thumbnails-Faceme\\"
pngDir = ".\\Thumbnails-Faceme-PNG\\"

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
    if not re.match(r'.*\.skp', name, flags=re.IGNORECASE):
        return
    else:
        path = os.path.join(root, name)
        pngName = name.replace("skp", "png")
        pngPath = os.path.join(pngDir, pngName)

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

        # category = path.split("\\")[-2].replace('-', ' ').replace('_', ' ').replace('+', ' ')
        global idNum
        idNum = idNum + 1
        imageSize = [300, 300]
        fullName = re.split('\.skp', name, flags=re.IGNORECASE)[0].replace('-', ' ').replace('_', ' ').replace('+', ' ')
        dataType = "Face-me"
        fileSize = convert_size(os.path.getsize(path))
        createTime = time.ctime(os.path.getmtime(path))
        thumbName150 = fullName + " " + str(idNum) + " 150p.jpg"
        thumbName300 = fullName + " " + str(idNum) + " 300p.jpg"
        thumb150path = os.path.join(thumbDir, thumbName150)[1:]
        thumb300path = os.path.join(thumbDir, thumbName300)[1:]

        mac = path.replace("\\", "/").replace("Y:", "/Volumes/Library")

        try:
            im = Image.open(pngPath)
        except IOError:
            print("failed to identify", pngPath)

        if  im.mode == "RGBA":
            bg = Image.new("RGB", im.size, (255, 255, 255))
            bg.paste(im, mask=im)
            bg.thumbnail((300,300), Image.ANTIALIAS)
            bg.save(thumb300path)
            bg.thumbnail((150,150), Image.ANTIALIAS)
            bg.save(thumb150path)

        else:
            im.thumbnail((300,300), Image.ANTIALIAS)
            im.save(thumb300path)
            im.thumbnail((150,150),  Image.ANTIALIAS)
            im.save(thumb150path)

        return people.append({
            "id": idNum,
            "name": fullName,
            "category": category,
            "path": path, 
            "dataType": dataType, 
            "fileSize": fileSize,
            "createTime": createTime,
            "imageSize": imageSize,
            "thumb150path": thumb150path,
            "thumb300path": thumb300path,
            "mac": mac})

for rootPath in cutoutPathPlants:
    for root, dirs, files in os.walk(rootPath, topdown=True):
        for name in files:
            createPngDict(root, name)
            # try:
            #     createPngDict(root, name)
            # except Exception as e:
            #     print(e)

with open('faceme.json', 'w') as f:
    json.dump(people, f)