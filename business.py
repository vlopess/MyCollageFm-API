import math
import os
import random
import requests
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from cell import Cell

from model import Model

def downloadImg(model: Model):
    c = 0
    urlList = model.cellList
    for j in range(0, len(urlList)):
        image_url = urlList[j].urlImage
        img_data = requests.get(image_url).content
        with open('temporary/{}_{}.jpg'.format(model.id,c), 'wb') as handler:
            handler.write(img_data)
        c = c + 1
    
def getFontSize(lenght, size):
    x = 2 if size == 240 else 4.5 if size == 300 else 8
    if(lenght < 33): 
        return x + 14
    if(lenght < 45): 
        return x + 12
    if(lenght < 55): 
        return x + 10
    if(lenght < 65): 
        return x + 8       
    return x + 6

def createImg(model: Model):
    size = getSize(model.size)
    new = Image.new("RGBA", (1200,1200))
    c = 0
    for i in range(0,1200,size):
        for j in range(0,1200,size):
            img = Image.open("temporary/{}_{}.jpg".format(model.id, c))
            img = img.resize((size,size))
            I1 = ImageDraw.Draw(img)
            position = ((size/2) - 30, size - 35)
            text = model.cellList[c].name
            c = c + 1
            lenghtText = len(text)
            pixels = (10 * len(text))
            x = (size - pixels) / 2
            position = (0, size - 35)
            fontSize = getFontSize(lenght=lenghtText,size=size)
            # max = 70
            font = ImageFont.truetype('fonts/Barlow-Light.ttf',fontSize)
            left, top, right, bottom  = I1.textbbox(position,text,font=font)
            I1.rectangle((left-5, top-5, right+5, bottom+5), fill="black")
            I1.text(position, text, font=font,fill =(255, 255, 255),align="center"),             
            new.paste(img, (j,i))            
    filename = "temporary/{}_collage.pdf".format(model.id)
    new.save(filename)
    return filename

def getSize(size):
    if size == 3: return 400
    if size == 4: return 300
    if size == 5: return 240

def deleteFilesRequest(id : int):
    cwd = os.getcwd()
    path = '{}/{}'.format(cwd, 'temporary')
    arr = os.listdir(path)
    for file in arr:
        fileID = file.split('_')
        if id == fileID[0]:
            filePath = '{}/{}'.format(path, file)
            os.remove(filePath)
        


