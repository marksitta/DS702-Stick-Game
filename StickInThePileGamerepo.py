#Sittakon Phommee
#660631100
#26/7/2023
#StickInThePileGame

import random

## input name of Human
name = input("What your name : ")
print("")

#define function to check input number of sticks in the pile
def st_pile_input():
    while True:
        num = input("How many sticks (N) in the pile: ")
        try:
            number = int(num)
            return number
        except ValueError:
            print("Please input number of sticks in the pile")
            print("")

## input howmany stick in the pile
stick_pile = st_pile_input()
print("")

## set number of stick can take
num_take = 2

# input and check condution function
def hm_input_stick():
    stick = num_take+1
    if stick_pile>num_take:
        while stick not in range (1,num_take+1):
            print(name,end='')
            stick = int(input(", how many sticks you will take : "))
            if stick > num_take : 
                print("No you cannot take more than",num_take,"sticks!")
                print("")
            elif stick < 1: 
                print("No you cannot take less than 1 sticks!")
                print("")
    else:
        while stick >stick_pile or stick<1:
            print(name,end='')
            stick = int(input(", how many sticks you will take : "))
            if stick not in range(1,stick_pile):
                print("Have",stick_pile,"sticks you can take!")
                print("")
    return stick   
            
 


#define ai brain 
def ai_brain():
    if stick_pile%(num_take + 2) in range(1,num_take+1):
        if stick_pile == num_take:
            a=num_take-1
        else:
            a=stick_pile%(num_take + 2)
    else:
        if stick_pile== num_take+1:
            a=stick_pile-1
        else:
            a=random.randrange(1,num_take)
    return a


#game start
while stick_pile != 0:
    print("There are ",stick_pile," sticks in the pile.")
    #Ai turn
    ai_stick = ai_brain()
    stick_pile = stick_pile - ai_stick
    #win condition for human
    if stick_pile == 0:
        print("I take the last stick,")
        print("You WON (",name,"WON)")
        break
    else:
        print("I take",ai_stick,"stick, there are",stick_pile,"sticks in the pile.")
        print("")
    #Human turn
    hmtake = hm_input_stick()
    stick_pile = stick_pile - hmtake
    #win condition for ai
    if stick_pile < 1:
        print("You take the last stick,")
        print("I WON (Python WON)")
        break
    
        