print ("welcome to the file handeling")

file = open("chiru.txt","w")

data1 = input("enter yoour name")

data2 = input("enter your age")

file.write(data1)
file.write(data2)

print("DATA WRITTEN TO THE FILE SUCCESSFULLY")

file.close( )


