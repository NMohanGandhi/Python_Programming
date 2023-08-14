
file = open("donations.txt",'a+') 
#lines  =  file.readlines()

inp  =  input("welcome to muthyalamma festival trust, enter (yes/no) if there is anyone's donations to enter  :")

#inp = "yes"


while inp == "yes":
    
    data = {}
    #print(data)
    name  =  input("please enter their name :")
    amt     = input("please enter the donation :")

    data[name] = amt
    print(data)
    #file.write(data)
    for key,val in data.items():
        file.write("%s:%s\n"%(key,val))
    inp  =  input("are you going to add anyone , to add donations (yes/no):")
    
else:

    print("thank you, now count the donations and check whether anyone has not yet donated ")


while True:
    next_line = file.readline()

    if not next_line:
        break;
    print(next_line.strip())

#file.close()
