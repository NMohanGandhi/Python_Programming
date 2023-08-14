#print("choice1 : registration","choice2  :  login ")


#user_choice = input("enter your choice")

user_input = input("enter your valid e_mail id ")

# @ and .
#
flag  =  True

for i in user_input:
    
    if i=="@":
        k = user_input.index(".") - user_input.index(i) 
        print(k)

        if k >=2:
            print("valid mail id")
            flag  =  True
            break
            
        
        else:
            flag  = False
    else:
        flag  = False                                                                   
        

if flag  == False:
     print("please enter the valid mail id" )
    



        
        
        

        

