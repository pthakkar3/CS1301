#Pranshav Thakkar 
#pthakkar7@gatech.edu
#I worked on this assignment alone, using only this semester's course resources.

import string

def applyToTech(reading,math,writing):
    total = reading + math + writing
    if 680 <= reading <= 800 and 690<= math <=800 and 650<= writing <= 800 and 2060<= total <=2400:
        return "Congratulations, you have been admitted to Georgia Tech. Go Jackets!"
    if reading>800 or math>800 or writing>800:
        return "Invalid scores. Please try again."
    if reading <680 or math<690 or writing<650 or total<2060:
        return "I am sorry to inform you we cannot offer you admission to Tech."
        
        
def guessAge(age):
    answer = (input("Guess the Age"))
    i = 0
    while i<6:
        if answer == "Quit" or answer == "quit" or answer == "QUIT":
            print("Don't give up! You can do it!")
            i = 7 
        elif answer == str(age):
            print("Great Job! It took you",i,"unsuccesful tries to guess the age")
            i = 7
        else:
            if i == 5:
                print("You have exceeded the maximum number of tries.")
                i=7
            else:
                answer = (input("Try Again. Guess the Age"))
                i = i+1   
    print("Thanks for Playing!")
    
    
def encryptMessage(secretMsg):
        encrypt = ""
        for letter in secretMsg:
            if letter in string.ascii_uppercase:
                letter = letter.lower()+ '^'
            elif letter in string.ascii_lowercase:
                letter = letter
            elif letter == '1':
                letter = '@'
            elif letter == '2':
                letter = '#'
            elif letter == '3':
                letter = '$'
            else:
                letter = '*'
            encrypt = encrypt + letter
        return encrypt


def numberPyramid(num):
    for i in range(num,0,-1):  
        left = str(i) * i
        right = str(i) * i
        spaces = int(num - i)
        line = left + spaces * '  ' + right
        print(line)
        
                                    
def reverseMultiTable(n):
    for i in range(n,0,-1):
        for x in range(n,0,-1):
            print(i*x, end = '\t')
        print()                

       
def enoughFor():    
    letter = input("What letter grade would you like to get?(A-D)")
    if letter == 'A' or  letter =='a':
        desired = 90
    elif letter == 'B' or letter == 'b':
        desired = 80
    elif letter == 'C' or letter == 'c':
        desired = 70
    elif letter == 'D' or letter =='d':
        desired = 60
    else:    
        my_error = ValueError("{0} is an invalid input".format(letter))    
        raise my_error
    current = int(input("What is your current grade in the class?(in %)"))
    w = int(input("How much is the final worth?"))  
    final = (100*desired - (100-w)*current)/w
    if final > 100:
        print("It's impossible for you to get this grade.")
    else:
        print("You need",final,"in the final to get a",letter,"in the class.")                        
