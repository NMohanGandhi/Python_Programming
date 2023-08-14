import random
#data=random.randint(1,6)
user_input=input("do you want to play the dice game (yes/no)")
while True:
    if user_input=="yes":
        #print(data)
        print(random.randint(1,6))
        user_input=input("do you wnat to play the dice game(yes/no)")
    else:
        print("thank you for playing game")
        break
