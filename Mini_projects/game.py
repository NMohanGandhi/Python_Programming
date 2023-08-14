import random

print("welcome to the Game")

print("###########################################################")

user_a=input("do you want to playing the game(yes/no) ")

print("###########################################################")

print("**********************Lets start*********************")

def mygame():
    # computer generates some random data 
    computer_data=random.randint(1,6)
    global user_a
    # we will give four chances to the user to play the game
    for i in range(4):
        user_data = int(input("enter your value(1, 6) :-"))
        if computer_data  == user_data:
                        print("You won the game , congrats")
                        print("#################################################################")
                        user_a=input("do you want to playing the game(yes/no) ")
                        #return user_a
                        break
                        
        else:
            print("you have one more choice, enter your data again")
            
    else:
        print("##################################################################")
        print("Sorry, You lost the game")
        user_a=input("do you want to playing the game(yes/no) ")

    return user_a


while True:
    if user_a == "yes":
        print("playng now")
        print("************")
        mygame()   
    else:
        print("###############################################################")
        print("Thanks for playing, we will expect you soon ")
        break
   



           
