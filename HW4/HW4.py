#Pranshav Thakkar  903079725
#pthakkar7@gatech.edu
#I worked on this assignment alone using only this semester's course materials.

from Myro import *

init()

def theme():
    for t in timer(15):
        beep(0.4,659.26)
        beep(0.3,783.99)
        beep(0.25,880)
        wait(0.5)
        beep(0.25,880)
        beep(0.3,783.99)
        beep(0.4,659.26)
        wait(0.5)
        beep(0.25,659.26)
        beep(0.25,783.99)
        beep(0.2,880)
        beep(0.2,880)
        beep(0.2,783.99)
        beep(0.25,880)
        beep(0.25,783.99)
        beep(0.25,659.26)
        wait(0.25)
    
    
def signatureAbility():
    #Spidey!! (agility)
    theme()
    for t in timer(10):
        translate(1,1)
        rotate(45,0.5)
        translate(-1,1)
        rotate(180,1)
    stop()
    print(getName())
    
    
def secondAbility():
    #Flash (spins)
    for t in timer(10):
        translate(1)
        rotate(0.9)
    stop()
    
    
def thirdAbility():
    #Daredevil (detects)
    for seconds in timer(10):
        L,R = getIR()
        if L == 0 or R == 0:
            rotate(90, 0.5)
        else:
            backward(1)
    stop()
              
              
def battleMenu():
    switch = True
    while switch == True:
        option = int(input("1. One Ability\n2. Two Abilities\n3. Three Abilities\n4. Exit\nWhich option would you like?"))
        if option == 1:
            signatureAbility()
        elif option == 2:
            signatureAbility()
            secondAbility()
        elif option == 3:
            signatureAbility()
            secondAbility()
            thirdAbility()
        elif option == 4:
            print("You won the battle!")
            switch = False
        else:
            print("I'm sorry, that's an invalid input")              