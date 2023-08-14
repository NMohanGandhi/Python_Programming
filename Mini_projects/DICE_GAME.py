print("WELCOME TO THE DICE GAME")
print("######@@@@@@####$$@@@@$$$")
import random
user1=input("do you ROLE THE DICE(yes/no)")
while True:
    if user1=="yes":
        print(random.randint(1,6))
        user1=input("do you ROLE THE DICE AGAIN (yes/no)")
    else:
        print("thank you for palying game")
        break
