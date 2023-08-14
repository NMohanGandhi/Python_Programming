print("WELCOME TO THE UPCOMING MUTHYALAMMA JATHARA")

House_number = [i for  i in range(1,3001)]

Name  = [""]*300

Amount = [0]*300

collection = input("are you go to collect money in next house(YES/NO)")

while collection =="YES":

    print("enter your details below")

    House_number = int(input("enter your correct house number "))

    donar_Name = input("enter your correct name as per adhar or voter card ")

    Amount_donate  = int(input("enter your giving amount"))

    Name.insert(House_number-1,donar_Name)
    Amount.insert(House_number-1,Amount_donate)
    print(Name)
    print(Amount)
    collection = input("are you go to collect money in next house(YES/NO)")

amount =  0
for i in Amount:
    amount+=i                                                           
print(amount)
insufficent_amount_donar =[]
excess_amount_donar=[]
for i in range(len(Amount)):
    if Amount[i]>300:
        data = i
        print(data)
        people=Name[data]
        excess_amount_donar.append(people)
    else:
        insufficent_amount_donar+=Amount[i]

        
    
        
        
        
    
print(Amount)
print("whose paid  less_than 300,notify me")
print(insufficent_amount_donar)
print(excess_amount_donar)
#print("to added all donars amount",300*300)
TOTAL = 300*300
print(TOTAL)
data3 = TOTAL-amount
print(data3)









    
    
1
