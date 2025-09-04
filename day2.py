'''day=int(input())
year=day//365
if day>0:
    remaining_days=(day%365)
    month=remaining_days//30
    remaining_days=remaining_days%30
    print(year,month,remaining_days)
    
    

 #if
amount=int(input())
if(amount<500):
    amount=amount+40
print(amount) 


#if else
amount=int(input())
if(amount<500):
    amount=amount+40
else:
    print("No delivery charges")
print(amount) 



#multi way selection
n=int(input())
if n>0:
    print(n,"is positive")
elif n<0:
    print(n,"is negative")
else:
    print(n,"is zero")
    

i=input()
if (i=='n' or i=='N'):
    print("north")
elif (i=='e' or i=='E'):
    print("east")
elif (i=='w' or i=='W'):
    print("west")
elif (i=='s' or i=='S'):
    print("south")
else:
    print("invalid")
    
a=10
print(a==30 or 40 or 60)


c=0   
print(c!=8 or c) 

for i in range(25,10,-2):
    print(i)



for i in range (50,101,1):
    if i%7==0 and i%3==0:
        print(i,end=' ')
        

for i in range (50,101,1):
    if i%7==0 or i%3==0:
        print(i,end=' ')
        

        
usr1='peter'
pwd1='123'
usr2=input("enter name:")
pwd2=input("enter pwd")
if usr2== usr1 and pwd2==pwd1:
        print("welcome")
    
else:
        print("Try Again")
    '''

usr1='peter'
pwd1='123'
i=1
while (i<4):
    usr2=input("enter name:")
    pwd2=input("enter pwd")
    if usr2== usr1 and pwd2==pwd1:
        print("welcome")
        exit()
    
    else:
        print("Try Again")
        i=i+1
light_color=input("Enter the traffic light color (red/yellow/green): ")
if light_color=="red":
    print("Stop!The light is red.")
elif light_color=="yellow":
    print("Caution!The light is yellow.")
elif light_color=="green":
    print("Go!The light is green.")
else:
    print("Invalid color! Please enter 'red','yellow', or'green'.")
    
    
data_used = float(input("Enter the data you have used today (in GB): "))
if data_used >= 1:
    print("Data is over!")
elif data_used == 0.5:
    print("ALERT:You have used 500 MB of data today.")
else:
    print("You are within your data limit for today.")

if purchased_item:
        return 0  
    elif hours_parked <= 2:
        return 0 
    else:
        return (hours_parked - 2) * 5 


fee = calculate_parking_fee(hours, purchased_item)
print(f"Parking Fee: {fee} units")

