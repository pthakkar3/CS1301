#Pranshav Thakkar 903079725
#pthakkar7@gatech.edu
# I worked on this assignment alone, using only this semester's course materials and resources.
from Myro import *
init()
def seeing_red():
    pic = makePicture("Firestorm.png")
    picList =[]

    for i in range(5):
        copy = copyPicture(pic)
        increment = 30
        for pixel in getPixels(pic):
            r,g,b = getRGB(pixel)
            setRed(pixel, r +increment)
        increment = increment + 40    
        picList.append(copy)
    
    savePicture(picList, "red.gif",2,True)


def fade():
    pic = makePicture("Firestorm.png")
    picList = []
    r = 1
    g = 1
    b = 1   
    while r>0 and g>0 and b>0:
        copy = copyPicture(pic)
        decrement = 10
        for pixel in getPixels(pic):
            r,g,b = getRGB(pixel)
            setRed(pixel, r - decrement)
            setGreen(pixel, g - decrement)
            setBlue(pixel, b - decrement)
        decrement = decrement + 40    
        picList.append(copy)
    savePicture(picList, "fade.gif",1,True)
    
    
def multiple_exposure():
    p = takePicture()
    turnRight(1,1)
    p1 = takePicture()
    copy = copyPicture(p)
    width = getWidth(p)
    height = getHeight(p)
    for x in range(width):
        for y in range(height):
            pix = getPixel(p,x,y)
            pix1 = getPixel(p1,x,y)
            pixcopy = getPixel(copy,x,y)
            r,g,b = getRGB(pix)
            r1,g1,b1 = getRGB(pix1)
            setRed(pixcopy,(r+r1)//2)
            setGreen(pixcopy,(g+g1)//2)
            setBlue(pixcopy,(b+b1)//2)
    savePicture(copy, "Multiple Exposure.jpg")    
            
def splitscreen():
    picList = []
    i = 0
    while i< 3:
        p = takePicture()
        turnRight(1,1)
        p1 = takePicture()
        copy = copyPicture(p)
        width = getWidth(p)
        height = getHeight(p)
        for x in range(width//2):
            for y in range(height):
                pix = getPixel(p,x,y)          
                pixcopy = getPixel(copy,x,y)
                r,g,b = getRGB(pix) 
                setRed(pixcopy,r)
                setGreen(pixcopy,g)
                setBlue(pixcopy,b)    
        for x in range(width//2,width):
            for y in range(height):
                pix1 = getPixel(p1,x,y)          
                pixcopy = getPixel(copy,x,y)
                r1,g1,b1 = getRGB(pix1) 
                setRed(pixcopy,r1)
                setGreen(pixcopy,g1)
                setBlue(pixcopy,b1)
        picList.append(copy) 
        i = i + 1
    savePicture(picList, "Split Screen.gif",1,True) 