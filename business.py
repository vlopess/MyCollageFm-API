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
    x = 0 if size == 300 else 2.5 if size == 375 else 6.5
    print(x)
    if(lenght < 35): 
        return x + 20
    if(lenght < 45): 
        return x + 16
    if(lenght < 55): 
        return x + 14
    if(lenght < 65): 
        return x + 12
        
    return x + 10

def createImg(model: Model):
    #downloadImg()
    # 5x5 = 300
    # 4x4 = 375
    # 3x3 = 500
    size = 500
    new = Image.new("RGBA", (1500,1500))
    c = 0
    for i in range(0,1500,size):
        for j in range(0,1500,size):
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
            new.paste(img, (i,j))            
    new.save("temporary/collage.png")
    return "temporary/collage.png"

def removeImg():
    os.remove('temporary/collage.png')


