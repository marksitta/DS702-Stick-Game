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
    
    #     ## take stick from pile 
    # stick_pile = stick_pile - hmtake
    # ## check if not enough stick to take
    # if stick_pile<0:
    #     print("There are no enough sticks to take.")
    #     stick_pile = stick_pile + hmtake
    #     ## check win condition for computer
    # elif stick_pile == 0:          
    #     print(name,", takes the last stick.")
    #     print("I, smart computer, win !!!!")
    #     break
    # else: 
    #     print("There are ",stick_pile," sticks in the pile.")
    #     stick_pile = stick_pile - ct ## take stick from the pile
    # ## start to check condition of smart computer
    #     if stick_pile == 2: ##condition to make the computer smart
    #         stick_pile = stick_pile + ct -1
    #         ct = 1
    #         print("I, smart computer, takes : ",ct)
    #         print("There are ",stick_pile," sticks in the pile.") 
    #     elif stick_pile<=0: ##check win condition for player
    #             print("I, smart computer, takes the last stick.")
    #             print(name," win ( I, smart computer, am sad T_T)")
    #             break
    #     else:## show howmany sticks that smart compuet take
    #         print("I, smart computer, takes : ",ct)
    #         print("There are ",stick_pile," sticks in the pile.") 

        

#sittakon phommee 660631100