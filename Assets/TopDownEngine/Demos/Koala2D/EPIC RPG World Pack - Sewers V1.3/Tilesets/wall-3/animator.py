# Python program to read
# json file

import json
import re

pixelsPerFrame = 32
currentPixel = 0


for i in range(1, pixelsPerFrame):
    baseName = "water-tiles"
    og = open('./{baseName}-0.asset'.format(baseName=baseName), 'r')
    totalFrames = 8

    
    # Opening JSON file
    f = open('./{baseName}.json'.format(baseName=baseName))
    g = open('./{baseName}-{currentPixel}.asset'.format(baseName=baseName, currentPixel=currentPixel+1), 'w+')
    # print(f.read())
    # returns JSON object as m
    # a dictionary
    data = json.load(f)
    target = og.read()

    # print(data[0])
    matches = re.findall('- {fileID:(.*?),',target)

    def findRelativeTile(name, skip):
        baseName = re.findall('(.*?)_', name)[0]
        currentValue = re.findall('[^_]+$', name)[0]
        # print(currentValue,'basename')
        newValue = int(currentValue) + skip
        newName = baseName+"_"+str(newValue)
        newId = 0

        for item in data:
            # print(item["second"],newName,"new id")
            if(item["second"].strip() == newName.strip()):
                newId = item["id"]
                # print(item["id"],newName,"new id")


        return {"name":newName, "id": newId}
            

    # for m in matches:
    print(matches)
    for m in matches:
        for item in data:
            if(item["id"].strip() == m.strip()):
                newTile = findRelativeTile(item["second"], i) 
                print(currentPixel, newTile["name"]) 
                target = target.replace(item["id"], newTile["id"]) 

    g.seek(0)
    g.write(target)

    currentPixel += 1


# Closing file
f.close()