
print("welcome to my project")
print("*******************************************************************")
print("choice 1 -  Addtion", "\n", "choice 2 - Multiplication","\n", "choice 3 -  division", "\n","choice 4 -  Subtraction")

choice  = int(input("please enter your choice of operation "))

num1=int(input("enter the value "))
num2=int(input("enter the value "))

def add(m,s):
    c=m+s
    print(m+s)

def mul(m,s):
    c=m*s
    print(m*s)

def div(m,s):
    c=m/s
    print(c)

def sub(x,y):
    d=x-y
    print(d)

if choice==1:
              print(add(num1,num2))
elif choice==2:
    print(mul(num1,num2))
elif choice==3:
    print(div(num1,num2))
else:
    print(sub(num1,num2))

