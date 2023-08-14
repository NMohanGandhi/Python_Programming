import random
print("welcome to the game")
print("#############################################################")
user_a=input("do you want play the game(yes/no)")
def mygame():
    colours=["blue","red","violet","yellow","orange","green","indigo"]
    computers_data=random.choice(colours)
    global user_a
    for i in range(4):
        user_data=input("enter your colour name")
        if computers_data==user_data:
            print("winner")
            user_a=input("do you wnat play the game(yes/no)")
            break
        else:
            print("one more chance")
    else:
       print("loos your game")
       user_a=input("do you want to play the game(yes/no)")
    return user_a
while True:
    if user_a=="yes":
        print("playing")
        mygame()
    else:
        print("thanks for playing")
        break
