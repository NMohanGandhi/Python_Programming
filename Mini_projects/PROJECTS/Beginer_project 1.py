import random
print("Welcome to the Rainbow colour prediction Game ")
print("#############%$$$$&**********************************************")
user_input  = input(" Do you want to play the Game (yes/no) ")
def mygame():
    colours = ["Blue","Red","Violet","Yellow","Orange","Green","Indigo"]
    computers_data = random.choice(colours)
    global user_input
    #print(computers_data)
    for i in range(4):
        user_data = input("Enter your Colour name ")
        if (computers_data ) == user_data :
            print("Winner")
            user_input= input("Do you want to play the Game (yes/no) ")
            break
        else:
            print("one more chance")
            
    else:
        print("loose your game ")
        user_input  = input(" Do you want to play the Game (yes/no) ")
        return user_input
while True:
    if user_input=="yes":
        print("playing")
        mygame()
    else:
        print("Thanks for playing ")
        break
        
        


