#Pranshav Thakkar  
#pthakkar7@gatech.edu 
#Chika Okonkwo and I worked on this assignment alone, using only this semester's course materials.
import math

def square(b):
    y=b*b
    return y
    
def taylorSwift(numFans):
    mins=3*numFans
    if numFans<20:
        print("Taylor Swift is done at 9:{}".format(numFans*3), "PM")
    elif numFans==20:
        print("Taylor Swift is done at 10:00")
    elif numFans>20 and numFans<39:
        print("Taylor Swift is done at 10:{}".format(numFans*3-60), "PM")
    elif  numFans==40:
        print("Taylor Swift is done at 11:00")
    elif numFans>40 and numFans<59:
        print("Taylor Swift is done at 11:{}".format(numFans*3-120), "PM")
    elif numFans==60:
        print("Taylor Swift is done at 12:00")
       
        
def girlScoutCookies():
    boxes=int(input("How many boxes do you want?"))
    money=int(input("How much money do you have?"))
    cost=boxes*4
    diff=abs(money-cost)
    if diff<money:
        print("You have", diff, "dollars left.")
    if cost>money:
        print("You still need", diff, "dollars")
    
def conversionTime(metersPerSecond):
    mph=(metersPerSecond*3600*3.28084)/5280
    mph_final=round((mph),2)
    feet=(metersPerSecond*3.28084)
    feet_final=round((feet),2)
    km=(metersPerSecond*3600)/1000
    km_final=round((km),2)
    
    print("You have {0:.2f} miles per hour, {1:.2f} feet per second, {2:.2f} kilometers per hour.".format(mph_final,feet_final, km))
    
def tipCalculator():
    bill=int(input("What was the bill?"))
    tip=int(input("What percentage tip would you like to pay?"))
    coupon=int(input("Did you have any coupons? (Please enter value)"))
    initial_cost=bill-coupon
    tip_bill=math.ceil(bill*(tip/100))
    tax_bill=initial_cost*.08
    totalCost=round((initial_cost+tip_bill+tax_bill),2)
    totalCost=str("${0:.2f}".format(totalCost))
   
    return totalCost
    
def falafel(falafelBalls,hummus,pitaBread):
    fala=falafelBalls//6
    hum=hummus//2
    if fala<=hum and fala<=pitaBread:
        final=fala
    if hum<=fala and hum<=pitaBread:
        final=hum
    if pitaBread<=fala and pitaBread<=hum:
        final=pitaBread
        
    print("With", falafelBalls, "falafel balls,", pitaBread, "pitas, and", hummus, "hummus, you can make a maximum of",final, "falafels.")
    
