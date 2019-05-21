#Pranshav Thakkar 
#pthakkar7@gatech.edu
# My partner, Chika Okonkwo, and I worked on this assignment alone and used only this semester's course materials.
from Myro import *

def onlySixths(aList):
    newList = []
    for x in aList:
        if x%6==0:
            newList.append(x)
    return newList
            
            
def union(list1,list2):
    list3 = []
    list3 = list1 + list2
    list3.sort()
    newList = []
    for x in list3:
        if x not in newList:
            newList.append(x)
    return newList   
    
    
def multiplyNums(aList):
    plier = 1
    for i in range(len(aList)):
        if type(aList[i])==int or type(aList[i])==float:
            plier = plier * aList[i]
        elif type(aList[i])==list:
            plier = plier * multiplyNums(aList[i])
    return plier


def abbreviator(string):
    newString = ""
    for char in string:
        if char.isupper() == True:
            newString = newString + char
        if char.isdigit():
            newString = newString +char
        else:
            pass
    return newString
    
    
def parse(string,delim):
    string = string + delim
    newList = []
    aStr = ""
    finalList = []
    for x in string:
        if x!=delim:
            aStr = aStr + x
        if x == delim:
            newList.append(aStr)
            aStr = ""
    for x in newList:
        if x!= "":
            finalList.append(x)
    return finalList


def lightStats():
    light = getLight()
    left = light[0]
    center = light[1]
    right = light[2]
    print("Left:",left)
    print("Center:",center)
    print("Right:",right)
    mean = (left + center + right)/3
    light.sort()
    median = light[1]
    ran = light[2] - light[0]
    stats = [mean,median,ran]
    return stats           
