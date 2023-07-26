import random

## input howmany stick in the pile
stick_pile = int(input("How many sticks (N) in the pile: "))
print("There are ",stick_pile," sticks in the pile.")
## input name
name = input("What your name : ")
ai_stick = 0

#define input and check function
def hm_input_stick():
    stick = 3
    if stick_pile>2:
        while stick not in {1,2}:
            print(name,end='')
            stick = int(input(", how many sticks you will take (1 or 2): "))
            if stick > 2 : #check if sticks > 2
                print("No you cannot take more than 2 sticks!")
            elif stick < 1: #check if sticks < 1
                print("No you cannot take less than 1 sticks!")
    else:
        while stick !=1:
            print(name,end='')
            stick = int(input(", how many sticks you will take (1 or 2): "))
            if stick!=1:
                print("No you can take 1 stick!")
            
    return stick 

#hm take

#define ai brain 
def ai_brain():
    if stick_pile%4 == 3:
        if stick_pile < 4:
            ai_stick = 2
        else:
            ai_stick = 1
    elif stick_pile%4 == 2: #clear
        if stick_pile<4:
            ai_stick = 1
        else:
            ai_stick =2
    elif stick_pile%4 == 1: #clear
        ai_stick = 1
    else :               #clear
        ai_stick = 1
    return ai_stick

#game start1
while stick_pile != 0:
    print("There are ",stick_pile," sticks in the pile.")
    ai_stick = ai_brain()
    stick_pile = stick_pile - ai_stick
    if stick_pile == 0:
        print("I take the last stick,")
        print("You WON (",name,"WON)")
        break
    else:
        print("I take",ai_stick,"stick, there are",stick_pile,"sticks in tje pile.")
    hmtake = hm_input_stick()
    stick_pile = stick_pile - hmtake
    if stick_pile < 1:
        print("You take the last stick,")
        print("I WON (Python WON)")
        break
    
        

#sittakon phommee 660631100