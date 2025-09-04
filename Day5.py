'''s=set()
print(type(s))

s=set([34,5,6])
print(s)

s={1122,2,3,"k v",True,3.1415,1122}
v={2,3,1122,True,3.1415,1122,"k v",}
print(type(s))
print(s)
print(v)


tup1=(1,2,[0,0,1])#internal
print(tup1)
#set2={1,2,[4,5]}#raises error --imutable
#print(set2)

set3={(1122,2191.22),'k v' ,True}
print(set3)

st={1,2,3,4,}
for i in st:
    print(i,end=" ")
    

st={1,2,3,4,}
for i in enumerate(st):
    print(i,end=" ")
    
#behavior of variables and id
str1={"hi"}
str2=str1
print(id(str1))
print(id(str2))

s={11,22,33,44,55,66}
s.add(99)
print(s)
s.discard(33)
print(s)
s.discard(100)
print(s)
s.pop()
print(s)
s.remove(44)
print(s)
#s.remove(78)#raises error if element not found
print(s)

    
#tuple does not have extend property becaus of immutable
#set has update
k={11,22,33}
v={44,55}
print(k)
print(v)
k.update(v)
print(k)
print(v)


#union
s={10,20,30}
s2={50,10,40,60}
s3=s.union(s2)
print(s)
print(s3)

s={10,20,30}
s2={50,10,40,60}
s3=s | s2 #union
print(s)
print(s3)

s={10,20,30}
s2={50,10,40,60}
s3=s.intersection(s2)
print(s)
print(s3)

s={10,20,30}
s2={50,10,40,60}
s.intersection_update(s2)
print(s)

s={10,20,30}
s2={50,10,40,60}
s= s & s2
print(s)




s={10,20,30}
s2={50,10,40,60}
s3=s & s2

print(s3)



k={33,22,11,44}
v={33,66,44,55}
print(k.difference(v))
print(v.difference(k))
k.difference_update(v)
print(k)

k={33,22,11,44}
v={33,66,44,55}
v.difference_update(k)
print(v)
print(k)

k={33,22,11,44}
v={33,66,44,55}
v.symmetric_difference(k)
print(v)
print(k)

k={33,22,11,44}
v={33,66,44,55}
k.symmetric_difference_update(v)
print(v)
print(k)

k={33,22,11,44}
v={33,66,44,55}
v.symmetric_difference_update(k)
print(v)
print(k)



k={33,22,11,44}
v={33,66,44,55}
print(v.isdisjoint(k))
print(k.isdisjoint(v))


k={33,44}
v={33,66,44,55}

print(k.issubset(v))
print(v.issubset(k))

print(k.issuperset(v))
print(v.issuperset(k))

usr=[]
mvs=[{}]

while True:
    ch=int(input("Enter choice:"))
    if ch==1:
        un=input("Enter user name: ")
        usr.append(un)
        
    elif ch==2:
        username=input("Enter user name:")
        if username in usr:
            moviename=input("Enter movie name:")
            movielist=set(moviename.split())
            print(movielist)
            mvs.append(movielist)
            
        else:
            ch=1
            print("user doesnot exist .create new user")
    elif ch==3:
        print(usr)
        continue
    elif ch==4:
        username=input("Enter user name:")
        if username in usr:
            for i in range(usr:
                print(mvs[])
    
        else:
            print("user doesnot exist .create new user")
    
      
#dictionary
d1=dict()
print(type(d1))

d4={'k':11,'z':22,'k':19}
print(d4)
print(type(d4))

print(d4.items())
print(d4.keys())

d4={'k':'11','z':'22','k':11}
print(d4)

d4={'k':11,'z':22,'k':19}
print(d4)
print(d4['k'])

d2={'A':'65','z':'90','k':'v'}
d2['pi']=3.14
print(d2)
d2['z']=26
print(d2)

d2['512']="priya"
print(d2)

del (d2['z'])
print(d2)

d2.clear()
print(d2)

del(d2)

plyrs={'p1': {'nm':'Rohit','jrsy':45 },
       'p2': {'nm':'virat','jrsy':18}}
for n,j in plyrs.items():
    print(n,j)
    
keys=['d','s','p']

vls=1122
dct=dict.fromkeys(keys,vls)
print(dct)

keys=['d','s','p']
vls=1122
dct=dict.fromkeys(keys)
print(dct)



d={'k':11,'s':6}
print(d.get('k',-1))
print(d.get('y',-1))
print(d.get('B'))


d={'k':11,'s':6}
for i in d.keys():
    print(i,end=" ")


d={'k':11,'v':22}
print(d.setdefault('k',25))
print(d.setdefault('y'))
print(d.setdefault('y',25))

name=input("enter name:")
d={}
for i in name:
    if  i  not in d:
        d[i]=1
       
    else:
        d[i]=d[i]+1
      
print(d)
        
user_list=[ ]
mvs=[]


while True:
    ch=int(input("Enter choice"))
    if ch==1:
        user_name=input("Enter user name:")
        user_list.append(user_name)
    elif ch==2:
        user_name=input("Enter user name:")
        if user_name in user_list:
            mv_name=input("enter movies names")
            ml=set(mv_name.split())
            mvs.append(ml)
            print(ml)
        else:
            print("user does not exist. create a user")
        ch=1
    elif ch==3:
        print("The users list is:",set(user_list))
        continue
    elif ch==4:
        user_name=input("Enter user name")
            #choice=(input("enter choice"))
        if user_name in user_list:
            unew=input("Enter to Add the new user")
            user_list.append(unew)
            mv_names=input("enter  movies for new user")
            ml=set(mv_names.split())
            mvs.append(ml)
        else:
            print("user not found in database.")
      #print("The users in list:",user_list)      
    elif ch==5:
        for i in user_list:
            for j in range(len(user_list)):
                idx1=user_list.index(i)
            print("The  user ",i,"at",idx1,"the movies liked by this user is:",mvs[idx1])



'''
user_data = {
    "user1": "priya123",
    "user2": "sriya456",
    "user3": "pappi789"
}

username = input("Enter your username: ")
password = input("Enter your password: ")


if username in user_data and user_data[username] == password:
    print("Login successful!")
else:
    print("Invalid username or password.")




# Dictionary to store books and their statuses
library = {}

# Menu
print("Welcome to the Library Book Management System")
print("Options:")
print("1. Add a new book")
print("2. Update book status")
print("3. View all books")
print("4. Search for a book")
print("5. Exit")

while True:
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == '1':  # Add a new book
        book = input("Enter book title: ").strip()
        if book in library:
            print(f"{book} already exists with status '{library[book]}'.")
        else:
            status = input("Enter status (available/issued): ").strip().lower()
            library[book] = status
            print(f"Added '{book}' with status '{status}'.")
    
    elif choice == '2':  # Update book status
        book = input("Enter book title to update: ").strip()
        if book in library:
            status = input("Enter new status (available/issued): ").strip().lower()
            library[book] = status
            print(f"Updated '{book}' status to '{status}'.")
        else:
            print(f"'{book}' is not in the library.")
    
    elif choice == '3':  # View all books
        if not library:
            print("Library is empty.")
        else:
            print("\nLibrary Books:")
            for book, status in library.items():
                print(f"'{book}': {status}")
    
    elif choice == '4':  # Search for a book
        book = input("Enter book title to search: ").strip()
        if book in library:
            print(f"'{book}' is in the library with status '{library[book]}'.")
        else:
            print(f"'{book}' is not in the library.")
    
    elif choice == '5':  # Exit
        print("Exiting the Library Book Management System. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")


customers = set()

while True:
    print("\nCustomer Tracking System - Options:")
    print("1. Add new customer")
    print("2. Remove customer")
    print("3. Display all unique customers")
    print("4. Remove random customer")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        customer_id = input("Enter customer ID to add: ")
        customers.add(customer_id)
        print(f"Customer ID {customer_id} added.")

    elif choice == '2':
        customer_id = input("Enter customer ID to remove: ")
        if customer_id in customers:
            customers.remove(customer_id)
            print(f"Customer ID {customer_id} removed.")
        else:
            print(f"Customer ID {customer_id} not found.")

    elif choice == '3':
        if customers:
            print("Unique Customers who visited the store:", customers)
        else:
            print("No customers in the system.")

    elif choice == '4':
        if customers:
            random_customer = customers.pop()
            print(f"Randomly removed Customer ID {random_customer}.")
        else:
            print("No customers in the system.")

    elif choice == '5':
        print("Exiting the Customer Tracking System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
