from Myro import *
picList = []
for x in range(35):
    forward(0.25,0.25)
    pic = takePicture()
    picList.append(pic)
for x in range(10):
    turnLeft(0.25,0.25)
    pic = takePicture()
    picList.append(pic)
for x in range(15):
    forward(0.25,0.25)
    pic = takePicture()
    picList.append(pic)
for x in range(20):
    pic = takePicture()
    picList.append(pic)    
savePicture(picList,"movie.gif",1,True)
