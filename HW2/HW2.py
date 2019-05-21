#Pranshav Thakkar 
#pthakkar7@gatech.edu
#My partner, Chikanma Okonkwo, and I worked on this assignment alone, using only this semester's course materials.

import math

def square(base):
    result = base ** 2
    return result
    
def taylorSwift(numFans):
    time = numFans*3
    hours = 9
    minutes = 0
    if time < 60:
        hours = 9
        minutes = time
        print("Taylor will be done by {}:{:02d} P.M.".format(hours,minutes))
    if time >= 60 and time < 120:
        hours = 10
        minutes = time - 60
        print("Taylor will be done by {}:{:02d} P.M.".format(hours,minutes))    
    if time >= 120 and time < 180:
        hours = 11
        minutes = time - 120
        print("Taylor will be done by {}:{:02d} P.M.".format(hours,minutes))
    if time >= 180:
        print("Sorry! Taylor has already left!")
    
def girlScoutCookies():
    boxes = int(input("How many boxes do you want?"))
    money = int(input("How much money do you have"))
    owed = boxes*4
    if money >= owed:
        remaining = money - owed
        remaining = str(remaining)
        print("You have $"+remaining,"left")
    else:
        remaining = owed - money
        remaining = str(remaining)
        print("You still need $"+remaining)
        
def conversionTime(metersPerSecond):
    milesPerHour = (metersPerSecond *3600*3.28084)/(5280)
    feetPerSecond = (metersPerSecond)*3.28084
    kmPerHour = (metersPerSecond * 3600)/(1000)
    print("You have {0:.2f} mph, {1:.2f} feet per second, and {2:.2f} kilometers per hour.".format(milesPerHour, feetPerSecond, kmPerHour))        


def tipCalculator():
    bill = float(input("How much was your bill?"))
    tip = float(input("How much would you like to tip?"))
    coupons = float(input("Do you have any coupons?(Please enter value)"))
    tip= tip*0.01
    tipped = bill * tip
    math.ceil(tipped)
    discounted = bill - coupons
    tax = discounted * 0.08
    totalCost = discounted + tipped + tax
    totalCost = str("${0:.2f}".format(totalCost))
    return totalCost
    
def falafel(falafelBalls,pitaBread,hummus):
    fB = int(falafelBalls/6)
    hum = int(hummus/2)
    pB = int(pitaBread/1)
    if fB <= hum and fB <= pB:
        print("With",falafelBalls,"falafel ball(s),",pitaBread,"pita(s) and",hummus,"hummus, you can make a maximum of",fB,"falafels.")
    if hum <= fB and hum <= pB:
        print("With",falafelBalls,"falafel ball(s),",pitaBread,"pita(s) and",hummus,"hummus, you can make a maximum of",hum,"falafels.")   
    if pB <= fB and pB <= hum:
        print("With",falafelBalls,"falafel ball(s),",pitaBread,"pita(s) and",hummus,"hummus, you can make a maximum of",pB,"falafel(s).")
