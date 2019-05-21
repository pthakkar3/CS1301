#Pranshav Thakkar 903079725
#pthakkar7@gatech.edu
#I worked on this assignment alone, using only this semester's course resources and materials.
def machToFPS(machList):
    map(lambda x : print(x,"mach is equivalent to",x*1116.4370079,"feet per second"),machList)
    
    
def sqPyramidVolume(baseHeightList,volumeList):
    correctList = map(lambda x: (x[0]*x[0]*x[1])//3 , baseHeightList)
    correctList = filter(lambda x: x in volumeList, correctList)
    return correctList
    
    
def makeChange(changeList):
    changeList[0] = changeList[0] * 100
    changeList[1] = changeList[1] * 25
    changeList[2] = changeList[2] * 10
    changeList[3] = changeList[3] * 5
    changeList[4] = changeList[4] * 1
    totalValue = reduce(lambda x,y : x+y, changeList)
    return totalValue