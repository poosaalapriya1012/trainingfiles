#Day6
'''def add(n1,n2):
    sm=n1+n2
    return sm
num1=float(input("Enter number1: "))
num2=float(input("Enter number2: "))
rs=add(num1,num2)
print("sum of %.2f , %.2f is : %.2f",%(num1,num2,rs))

#with paramtrs without return
def add(n1,n2):
    sm=n1+n2
    print("sum of %.2f , %.2f is : %.2f"%(n1,n2,sm))
num1=float(input("Enter number1: "))
num2=float(input("Enter number2: "))
add(num1,num2)

#without paramtrs without return
def add():
    num1=float(input("Enter number1: "))
    num2=float(input("Enter number2: "))  
    sm=num1+num2
    print("sum of %.2f , %.2f is : %.2f"%(num1,num2,sm))

add()

#without paramtrs with return
def add():
    num1=float(input("Enter number1: "))
    num2=float(input("Enter number2: "))  
    sm=num1+num2
    return sm

print("sum: ",add())
#with paramtr with return
def nm(name):
    
    return name
def rn(roll):
    
    return roll
n=input("Enter name : ")
r=input("Enter roll: ")
nm(n)
rn(r)

#without paramtr without return
def nm():
    name=input("Enter name : ")
    print(name)
def rn():
    roll=input("Enter roll: ")
    print(roll)
nm()
rn()

#without paramtr with return
def nm():
    name=input("Enter name : ")
    return name
def rn():
    roll=input("Enter roll: ")
    return roll
print(nm())
print(rn())

#with paramtr wihout return
def nm(n):
    
    print(n)
def rn(r):
    
    print(r)

n=input("Enter name : ")
r=input("Enter roll: ")
nm(n)
rn(r)

nmbr_1=1122
def show():
    global nmbr_2
    nmbr_2=2191
    nmbr_3=22191
    print(nmbr_1)
    print(nmbr_2)
    print(nmbr_3)
show()
print(nmbr_1)
print(nmbr_2)


def details(n,r):
    print(n.upper(),r)
nm="k v"
rnk=1122
details(nm,rnk)


def details(n,r):
    print(n.upper(),r)
nm="k v"
rnk=1122
#details(rnk,nm) error
print()
def kw_ar(iv,fv,sv):
    print(iv,fv,sv)
kw_ar(fv=25.19,iv=1122,sv='python')
kw_ar(sv='python',fv=25.19,iv=1122)
kw_ar(sv='python',iv=1122,fv=25.19)
#kw_ar(s='python',i=1122,f=25.19) #error


#variable length args

def vlp_ar(*args):
    print()
    for var in args:
        print(var,end=' ')

vlp_ar(1122)
vlp_ar(1122,25.19)
vlp_ar(1122,25.19,'python')

def print_it(**kwargs):
    print()
    for name,value in kwargs.items():
        print(name,value,end=" ")
print_it(a=10)
print_it(a=10,b=3.14)
print_it(a=10,b=3.14,s='python')

#variable length args

def vlp_ar(*args):
    print()
    for var in args:
        print(var,end=' ')

vlp_ar(1122)
vlp_ar(1122,25.19)
vlp_ar(1122,25.19,'python')

def dsply(nm,crs="btech"):
   ''''''
   print(nm)
   print("course:"+crs)
dsply(nm="raju")
dsply(nm="raju",crs="MCA")
dsply(crs="MCA",nm="rani")

print(dsply.__doc__)

#passing list as paramtr
def pca(l1,l2):
    print(l1,l2)
lst1=[11,22,33]
lst2=[44,55]

pca(lst1,lst2)


#nested function
def outer_fun():
    def inner_fun():
        print("welcome")
    inner_fun()

outer_fun()

#filter
def evnchck(n):
    return n%2==0
nmbrs=range(21,30)
l2=list(filter(evnchck,nmbrs))
print(l2)

def sqr(x):
    return x**2
nmbrs=[1,2,3,4,5]
sqr_lst=list(map(sqr,nmbrs))
print(sqr_lst)

d={}

def count_alphabets_digits(s):
    for i in s:
        if i.isalpha()==True:
            if i not in d:
                d[i]=1
            else :
                d[i]=d[i]+1
        if i.isdigit()==True:
            if i not in d:
                d[i]=1
            else :
                d[i]=d[i]+1
            
count_alphabets_digits("priya12323")

print(d)

def cnt_vwls(s):
    if not s:
        return 0
    if s[0].lower() in 'aeiou':
        return 1+cnt_vwls(s[1:])
    else:
        return cnt_vwls(s[1:])


print(cnt_vwls("hello"))
            
#write recursive function to remove fun to remove any tabs present in string           
def cnt_vwls(s):
    if not s:
        return ""
    if s[0]!='\t':
        return cnt_vwls(s[1:])
    else:
        return s[0]+cnt_vwls(s[1:])


print(cnt_vwls("hello world"))
            


#without para with return
def remove_tabs():
    text = input("Enter a string: ")
    result = ""
    for char in text:
        if char not in " \t": 
            result += char
    return result

result = remove_tabs()
print("Result:", result)

#with para with return
def remove_tabs(text):
    
    result = ""
    for char in text:
        if char not in " \t": 
            result += char
    return result
text = input("Enter a string: ")
result = remove_tabs(text)
print("Result:", result)

#without para without return
def remove_tabs():
    global result
    for char in text:
        if char not in " \t": 
            result += char

text = input("Enter a string: ")
remove_tabs()
print("Result:", result)

#replace
text = input("Enter a string: ")
result = text.replace("\t", "")
print("Result:", result)


#join
text = input("Enter a string: ")
result = "".join(text.split("\t"))
print("Result:", result)

#assignment
text = input("Enter a string: ")
result = ""
for char in text:
    if char != "\t":
        result += char
print("Result:", result)

text = input("Enter a string: ")
result = "".join([char for char in text if char != "\t"])
print("Result:", result)

'''
def tabs(s):
    if not s:
        return ""
    if s[0] =='\t':
        return tabs(s[1:])
    else:
        return s[0]+tabs(s[1:])


print(tabs("hello world"))


            

