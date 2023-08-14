import random

print("WELCOME TO THE RAIN_BOW COLOUR PREDICTION GAME")

print("***************************=***+*****************************************")

user_input=input("ARE U INTRESTING FOR PLAYING rain_BOW COLOUR PREDICTION GAME(YES/NO)")
def mygame():
    rainbow_colours   =   ["red","orange","yellow","green","blue","indigo","violet"]

    print("&&&&&&&&&&&*************************@@@@@@@@@@@@@@@@@@*********##########***$$$$$$")

    computers_data    =   random.choice(rainbow_colours)
    global user_input
    for i in range(5):
        user_a=input("please GUEES your COLOUR NAME  ")
        if computers_data==user_a:
            print("congrats , dear MADAM/SIR  you won the  RAINBOOW colour  prediction  game")
            user_input=input("ARE U INTRESTING FOR PLAYING rain_BOW colour prediction GAME(YES/NO)")
            break
        else:
            print("sorry dear loss your game ,BUT i am giving one more chance to cover your loss")
    else:
       print ("loos your game,you dont have any life lines to continue my game,you have only one option quit into my game ")
       user_input=input("are u intresting playing my game (YES/NO)")
       return user_input
while True:
    if user_input=="YES":
        print("TNAKYOU for INTRESTING TO PLAYING MY GAME")
        print("##############################################################################")
        mygame()
    else:
        print("SORRY you dont  allow to PLAY MY GAME")
        print("@@@@@@@@@@@@@@@@@@@*********************************************************************")
        break


    

        

    

