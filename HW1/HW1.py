#Pranshav Thakkar
#CS1301 Section A
# pthakkar7@gatech.edu
# I worked on this assignment alone, using only this semester's course resources.

print("First, we will convert speed in machs to feet per second.")

def machToFPS():
     mach = float(input("Enter speed in machs"))
     FPS = mach *  1116.4370079
     print("Your speed in Feet/Second is:", FPS, "feet/second")

#machToFPS()

print("Now, we will calculate the volume of a square pyramid.")

def sqPyramidVolume():
    base = float(input("Please enter the length of the base in inches"))
    height = float(input("Please enter the height of the pyramid in inches"))                  
    volume = (base * base * height)/3
    print("The volume of the square pyramid is",volume,"inches cubed")
     
#sqPyramidVolume()     

print("Next, we will convert any number of cents entered into dollars, quarters, dimes, nickels and pennies.")

def makeChange():
    cents = int(input("Enter the number of cents"))
    dollars = int(cents/100)
    cents1 = int(cents%100)
    quarters = int(cents1/25)
    cents2 = int(cents1%25)
    dimes = int(cents2/10)
    cents3 = int(cents2%10)
    nickels = int(cents3/5)
    pennies = int(cents3%5)
    print("You have",dollars,"dollar(s),",quarters,"quarter(s),",dimes,"dime(s),",nickels,"nickel(s),and",pennies,"penny(ies).")

#makeChange()        

print("Finally, we will calculate your PPI ratio.")

def PPIIndex():
    weight = float(input("Please enter your weight in pounds"))
    height = float(input("Please enter your height in inches"))
    PPI = (weight/height)*1.125
    print("Your corrected PPI is {0:.1f}.".format(PPI))

#PPIIndex()

    
