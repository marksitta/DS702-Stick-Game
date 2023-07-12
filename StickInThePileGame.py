## input howmany stick in the pile
stick_pile = int(input("How many sticks (N) in the pile: "))

print("There are ",stick_pile," sticks in the pile.")

## input name
name = input("What your name : ")

time= 0

while stick_pile!=0:
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
        ## check if 0 stick in the pile
        elif stick_pile == 0:
            time+=1 #keep how many times that take stick
            print("OK. There is no stick left in the pile. You spent ",time," times.")
            break
        else:
            time+=1 #keep how many times that take stick
            print("There are ",stick_pile," sticks in the pile.")
            
