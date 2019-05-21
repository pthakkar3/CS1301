#Pranshav Thakkar 903079725
#pthakkar7@gatech.edu
#I worked on this assignment alone, using only this semester's course materials.
def robopics():
    p = takePicture()
    show(p)
    width = getWidth(p)#width is 427
    height = getHeight(p)#height is 266
    redhor = 0
    bluehor = 0
    redvert = 0
    bluevert = 0
    for y in range(0,height):
        pix = getPixel(p,0,y)
        r = getRed(pix)
        g = getGreen(pix)
        b = getBlue(pix)
        if r>150 and b<100:
            redhor = redhor + 1
            print("Red horizontal added")
        if b>100 and r<150:
            bluehor = bluehor + 1     
            print("Blue horizontal added")  
        
    if redhor >=1:
        print("Red Horizontal")
        turnLeft(1,1)
        turnRight(1,1)
        beep(2,800)
        return
    elif bluehor >=1:
        print("Blue Horizontal")
        turnLeft(1,1)
        turnRight(1,1)
        beep(2,800)
        wait(2)
        beep(2,800)
        return
        
    for x in range(0,width):
        pix = getPixel(p,x,0)
        r = getRed(pix)
        g = getGreen(pix)
        b = getBlue(pix)
        if r>150 and b<100:
            redvert = redvert + 1
            print("Red Vert added")
        if b>100 and r<150:
            bluevert = bluevert + 1  
            print("Blue Vert added")
        
    if redvert >=1:
        print("Red Vertical")
        forward(1,1)
        backward(1,1)
        beep(2,800)
        return
    elif bluevert >=1:
        print("Blue Vertical")
        forward(1,1)
        backward(1,1)
        beep(2,800)
        wait(2)
        beep(2,800)
        return        

