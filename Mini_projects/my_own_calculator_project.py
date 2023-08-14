print("@@@@@@@@***************@@@@@@@@*************&&&&&&&&&&&&&&")
print("******#welcome to python, i am creating my first and simple project - by MoHAn*** YADAv ########")
print("my project manager is RAMESH SIR")

print(" luck 1 - mohan" ,"\n","luck 2 - chiru","\n","luck 3 - moon","\n","luck 4 - fan","\n")

luck=int(input("enter you lucky number "))
y=int(input("enter the integer number1 "))
g=int(input("enter the integer number2 "))

def mohan(p,m):
    sir=p+m
    print(sir)
#mohan(y,g)
def chiru(j,k):
    mam=(j-k)
    print(mam)
#chiru(y,g)   
def moon(u,v):
    sunny=(u*v)
    print(sunny)
#moon(y,g)
def fan(a,b):
    light=(a/b)
    print(light)
#fan(y,g)
if luck==1:
    print(mohan(y,g))
elif luck==2:
    print(chiru(y,g))
elif luck==3:
    print(moon(y,g))
else:
    print(fan(y,g))

