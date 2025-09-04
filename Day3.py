
'''number=int(input()) #23456
e_digit=int(input())#4

#6
product=1
while number>0:            #23456 > 0              #2345>0              #234>0          
    dgt=number%10          #digit 23456%10=6       digit =2345%10=5       digit=234%10     
    if(dgt!=e_digit):      #6!=4=>true             5!=4 True              4!=4 ->false
        product=dgt*product #6*1=>6                 prdt=5*6=30           
    number=number//10       #23456//10=>2345        nmbr=2345//10=>234     234//10=23
print(product)

n=int(input())

msg=0
i=1
while n>0:
    rem=n%10
    if rem%i==0:
        msg=msg+rem
        i=i+1
    n=n//10
   
   
   
#pattern
for i in range(1,4):
    for j in range(1,4):
        print(i,end=" ")
    print()
    
#1 
#1 2 
#1 2 3 
#1 2 3 4 
#1 2 3 4 5 
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print() 

#1 2 3 4 5 
#1 2 3 4 
#1 2 3 
#1 2 
#1 
for i in range(5,0,-1):
    for j in range(1,i + 1):
        print(j,end =' ')
    print()
  
  
  
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end =' ')
    print()
    

for i in range(1,6,1):
    for j in range (1,6,1):
        print("%2d"%(i*j),"\t",end=' ')
    print()
    
# else statement used with loops
for num in range(5):
    print(f"Cuurent number:{num}")
else:
    print("Loop completed normally")
    


#
for num in range(5):
    print(f"Cuurent number:{num}")
    
    if num==3:
        break
else:
    print("Loop completed normally")

 
#else with while
count =0
while count < 10:
    print(f"Current count: {count}")
    count = count+1
else:
    print("Loop completed normally")


count =0
while count < 10:
    print(f"Current count: {count}")
    count = count+1
    if count>5:
        break
    
else:
    print("Loop completed normally")
    
count =0
while count < 10:
   
    count = count+1
    if count>5:
        continue
    print(f"Current count: {count}")
    
   
    
else:
    print("Loop completed normally")
  
    
 #multiline strings
 
print("welcome \
python \
Programmimg")'




print('welcome '
'python '
'Programmimg')

print("""welcome 
python 
Programmimg"""
)


msg="python"
print(msg[-1])
print(msg[0:4])

s="welcome to python programming"
print(s[-11:-17:-1/])



for i in range(0,128):
    print(i,"-->",chr(i),',' ,end=' ')


s="priya"
for i in s:
    print(i,"-->",ord(i))
    
'''


s="program priya python sru "
res=s[0]

print(len(s.split()))
print(s.replace(res,'$'))


user_input = input("Enter some text: ")

greeting = "Hello, " + user_input
print("Concatenated greeting:", greeting)

print("Is alphabetic?", user_input.isalpha())
print("Is digit?", user_input.isdigit())
print("Is alphanumeric?", user_input.isalnum())
print("Is lowercase?", user_input.islower())
print("Is uppercase?", user_input.isupper())

print("Split into words:", user_input.split())
print("Partitioned input:", user_input.partition(" "))

words = user_input.split()
print("Joined words:", ", ".join(words))

print("Uppercase:", user_input.upper())
print("Lowercase:", user_input.lower())
print("Capitalized:", user_input.capitalize())
print("Title case:", user_input.title())
print("Swap case:", user_input.swapcase())

try:
    int_value = int(user_input)
    print("Converted to integer:", int_value)
except ValueError:
    print("Cannot convert to integer.")


print("Type of user input:", type(user_input))

if user_input:
    first_char = user_input[0]
    print("ASCII value of first character:", ord(first_char))
s = "Hello, World"
print(s[:11])
print(s[0:5:2]) 
print(s[0:-5])  
print(s[::-2])
print(s[::-1]) 
print(s[:5])
#start negative
print(s[-1:])
print(s[-2:])
print(s[-3:])
#end negative
print(s[:-6])
print(s[:-5])

print(s[::-2]) 
#start neg ,stet neg
print(s[-1::-1])
print(s[:-5:-1])
 
print(s[-7::-1])  
print(s[-6:-1])  
print(s[:-5:-2])
print(s[-1:-12])
#start,end,step neagative
print(s[-1:-6:-1])
print(s[::-1])

print(s[-7::-1])  
print(s[-1:-4])  
print(s[:-5:-4])
print(s[-7:-4])
#start,end,step neagative
print(s[-4:-1])
print(s[-1:-13])
print(s[-1:-6:-2])
print(s[:-1:])













    
    
        
    
    
    
