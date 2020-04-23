import datetime, re, time, os
from PIL import Image
import math
import json
from ConfigWin import cutoutPathTexture

# pngItems = os.listdir()
people = []
idNum = 0
currentDir = os.getcwd()
thumbDir = ".\\Thumbnails-Texture\\"
thumbDirReal = ".\\Thumbnails-Texture\\"
if not os.path.isdir(thumbDirReal):
    try:
        os.mkdir(thumbDirReal)
    except OSError:
        print("Creation of the directory %s failed" % thumbDirReal)


def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def createPngDict(root, name):
    if not re.match(r'.*\.png|.*\.jpg', name, flags=re.IGNORECASE):
        return
    path = os.path.join(root, name)
    try:
        im = Image.open(path)
    except IOError:
        print("failed to identify", path)
    else:
        if len(path.split("\\")) == 6:
            if re.match(r'(.*?stone.*|.*?cobble.*)', name, flags=re.IGNORECASE):
                category = "Stone"
            elif re.match(r'(.*?grass.*|.*?tree.*|.*?moss.*)', name, flags=re.IGNORECASE):
                category = "Plant"
            elif re.match(r'(.*?metal.*|.*?grate.*|.*?steel.*)', name, flags=re.IGNORECASE):
                category = "Metal"
            elif re.match(r'.*?glass.*', name, flags=re.IGNORECASE):
                category = "Glass"
            else:
                category = "Other"
        else:
            category = path.split("\\")[5]
        global idNum
        idNum = idNum + 1
        imageSize = im.size
        fullName = re.split('\.png|\.jpg', name, flags=re.IGNORECASE)[0].replace('-', ' ').replace('_', ' ')
        dataType = "Texture"
        fileSize = convert_size(os.path.getsize(path))
        createTime = time.ctime(os.path.getmtime(path))
        thumbName150 = fullName + " " + str(idNum) + " 150p.jpg"
        thumbName300 = fullName + " " + str(idNum) + " 300p.jpg"
        thumb150path = os.path.join(thumbDir, thumbName150)
        thumb300path = os.path.join(thumbDir, thumbName300)
        thumbName150Png = fullName + " " + str(idNum) + " 150p.png"
        thumbName300Png = fullName + " " + str(idNum) + " 300p.png"
        thumb150pathPng = os.path.join(thumbDir, thumbName150Png)
        thumb300pathPng = os.path.join(thumbDir, thumbName300Png)
        mac = path.replace("\\", "/").replace("Y:", "/Volumes/Library")

        if  im.mode == "RGBA":
            bg = Image.new("RGB", im.size, (255, 255, 255))
            bg.paste(im, mask=im)
            bg.thumbnail((300,300), Image.ANTIALIAS)
            bg.save(thumb300path)
            bg.thumbnail((150,150), Image.ANTIALIAS)
            bg.save(thumb150path)
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
        elif im.mode == "RGB":
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
        else:
            im.thumbnail((300,300), Image.ANTIALIAS)
            im.save(thumb300pathPng, "PNG")
            im.thumbnail((150,150),  Image.ANTIALIAS)
            im.save(thumb150pathPng, "PNG")
            return people.append({
                "id": idNum,
                "name": fullName,
                "category": category,
                "path": path, 
                "dataType": dataType, 
                "fileSize": fileSize,
                "createTime": createTime,
                "imageSize": imageSize,
                "thumb150path": thumb150pathPng,
                "thumb300path": thumb300pathPng,
                "mac": mac})


for root, dirs, files in os.walk(cutoutPathTexture, topdown=True):
    for name in files:
        try:
            createPngDict(root, name)
        except Exception:
            pass

with open('texture.json', 'w') as f:
    json.dump(people, f)