import random

## input howmany stick in the pile
stick_pile = int(input("How many sticks (N) in the pile: "))

print("There are ",stick_pile," sticks in the pile.")

## input name
name = input("What your name : ")


while stick_pile!=0:
    ## ct = computer stick will take
    ct = random.randint(1,2)
    ## input and check number of sticks
    print(name,end='')
    take = int(input(", how many sticks you will take (1 or 2): "))
    if take > 2 : #check if sticks > 2
        print("No you cannot take more than 2 sticks!")
    elif take < 1: #check if sticks < 1
        print("No you cannot take less than 1 sticks!")
    else:
        ## take stick from pile 
        stick_pile = stick_pile - take
        ## check if not enough stick to take
        if stick_pile<0:
            print("There are no enough sticks to take.")
            stick_pile = stick_pile + take
        ## check win condition for computer
        elif stick_pile == 0:          
            print(name,", takes the last stick.")
            print("I, smart computer, win !!!!")
            break
        else: 
            print("There are ",stick_pile," sticks in the pile.")
            stick_pile = stick_pile - ct ## take stick from the pile
            ## start to check condition of smart computer
            if stick_pile == 2: ##condition to make the computer smart
                stick_pile = stick_pile + ct -1
                ct = 1
                print("I, smart computer, takes : ",ct)
                print("There are ",stick_pile," sticks in the pile.") 
            elif stick_pile<=0: ##check win condition for player
                print("I, smart computer, takes the last stick.")
                print(name," win ( I, smart computer, am sad T_T)")
                break
            else:## show howmany sticks that smart compuet take
                print("I, smart computer, takes : ",ct)
                print("There are ",stick_pile," sticks in the pile.") 

        

#sittakon phommee  660631100