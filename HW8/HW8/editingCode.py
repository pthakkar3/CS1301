from Myro import *

picList = loadPictures("movie1.gif")
pikachu = makePicture("Pikachu.png")
splitscreen = []
for p in range(60,71):
    pic = picList[p]
    copy = copyPicture(pic)
    width = getWidth(pic)
    height = getHeight(pic)
    for x in range(width//2):
        for y in range(height):
            pix = getPixel(pic,x+75,y)          
            pixcopy = getPixel(copy,x,y)
            r,g,b = getRGB(pix) 
            setRed(pixcopy,r)
            setGreen(pixcopy,g)
            setBlue(pixcopy,b)    
    for x in range(width//2,width):
        for y in range(height):
            pix1 = getPixel(pikachu,x,y)          
            pixcopy = getPixel(copy,x,y)
            r1,g1,b1 = getRGB(pix1) 
            setRed(pixcopy,r1)
            setGreen(pixcopy,g1)
            setBlue(pixcopy,b1)
    picList[p] = copy



seeingred = []
for p in range(71,76):
    pic = picList[p]
    copy = copyPicture(pic)
    increment = 30
    for pixel in getPixels(copy):
        r,g,b = getRGB(pixel)
        setRed(pixel, r +increment)
        increment = increment + 40    
    picList[p] = copy


fade = []
pic = picList[79]
   
for i in range(30):
    copy = copyPicture(pic)
    decrement = 10
    for pixel in getPixels(pic):
        r,g,b = getRGB(pixel)
        setRed(pixel, r - decrement)
        setGreen(pixel, g - decrement)
        setBlue(pixel, b - decrement)
    decrement = decrement + 70    
    picList.append(copy)
    
savePicture(picList,"movie2.gif",1,True)