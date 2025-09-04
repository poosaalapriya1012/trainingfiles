'''#lists
lst=[11,13,"sri",True]
print(lst)

lst1=[10,20,30]
lst2=[40,50]
lst3=lst1+lst2#
print(lst3)

#repitation
lst4=lst1*2
print(lst4)

lst5=[11,13,"priya",[11,99,88],True]
print(lst5)

lst6=[10,20,30,40,50,3]
print(len(lst6))
print(max(lst6))
print(min(lst6))
print(sum(lst6))
print(any(lst6))
print(all(lst6))
del(lst6[4])
print(lst6)
print(sorted(lst6))

lst6.append(99)
print(lst6)
k=[11,2,11,6,11,11]
print(k.count(11))
print(k.count(9))

#index
print(k.index(11))
print(k.index(11,3))
print(k.index(11,1,5))

#insert
print(k)
k.insert(2,'k')
print(k)
k.insert(20,'k')
print(k)
k.insert(-9,'pri')
print(k)
k.insert(-20,'k')
print(k)

#pop
k=[11,22,'k',11,44,11,66,11,88]
print(k.pop())
print(k.pop(3))
print(k)

#sort()
v=[44,22,11,55,33]
print(v)
v.sort()
print(v)

#extend
k=[11,22]
v=[33,44]
k.extend(v)
print(k)
print(v)
#appendlist
p=[11,22]
q=[33,44]
p.append(q)
print(p)
print(q)

#remove
print(k)
k.remove(33)
print(k)

s=[11,22,33,44]
k.reverse()
print(k)


#copy
#clear
k=[]
help(k.append)

k=[11,22,33,44,55]
v=k[:]
print(id(k))
print(id(v))
print(k.pop())
print(v)
print(k)


lst=[1,2,3,4]
for i in lst:
    print(i,end=" ")
    
i=0
while i<len(lst):
    print(lst[i],end=" ")
    i=i+1

l=[-12,84,11,22,-3,0,-25]
pst=[i**2 for i in l ]
pribnt(pst)


l=[-12,84,11,22,-3,0,-25]
pst=[i for i in l if i>0 ]
print(pst)

#Reading 
lst=[]
n=int(input("Enter no of elements:"))
for i in range(n):
    ele=int(input("Enter Element:"))
    lst.append(ele)
print(lst)

lst=[]
ele=int(input("Enter element:"))
while ele!=0:
    ele=int(input("Enter Element:"))
    lst.append(ele)
print(lst)




#pgm that takes list returns list containing only unique elements from original list
lst=[10,20,20,30,40,40,50]
res=[]
for i in lst:
    if i not in res:
        res.append(i)
        
        
print(res)

lst=[1,2,3,4,5,-1,-2,-3]
even=[]
odd=[]
for i in lst:
    if i>0:
        even.append(i)
    else :
        odd.append(i)
print(even)
print(odd)


#reverse the array
l=[]
n=int(input("enter size:"))
for i in range(n):
    ele=int(input("enter ele : "))
    l.append(ele)
ans=[0]*n
for i in range(n-1,-1,-1):
    ans[n-i-1]=l[i]
    
print(ans)
    
    

lst=[1,0,3,9]
code=""
for i in lst:
    if i==0:
        code+='a'
    if i==1:
        code+='b'
    if i==2:
        code+='c'
    if i==3:
        code+='d'
    if i==4:
        code+='e'
    if i==5:
        code+='f'
    if i==6:
        code+='g'
    if i==7:
        code+='h'
    if i==8:
        code+='i'
    if i==9:
        code+='j'
print(code)
    


names=[]
accno=[]
transfer=[]
ch='y'
while ch=='y':
    ele1=input("Enter name : ")
    ele2=int(input("Enter accno : "))
    ele3=int(input("Enter transfer : "))
    
    names.append(ele1)
    accno.append(ele2)
    transfer.append(ele3)
    ch=input("Do you want to continue :press y/n. ")
    if ch=='y':
        continue
    else:
        break
    
   
print("Names\tA/C no\tTransferlimit")
print('-'*40)
for i in range(len(names)):
    print(names[i],'\t',accno[i],'\t',transfer[i])
    
    


names=[]
accno=[]
transfer=[]
ch='y'
while ch=='y':
    ele1=input("Enter name : ")
    ele2=int(input("Enter accno : "))
    ele3=int(input("Enter transfer : "))
    
    names.append(ele1)
    accno.append(ele2)
    transfer.append(ele3)
    ch=input("Do you want to continue :press y/n. ")
    if ch=='y':
        continue
    else:
        break
    
   
print("Names\tA/C no\tTransferlimit")
print('-'*40)
for i in range(len(names)):
    print(names[i],'\t',accno[i],'\t',transfer[i])
    



names=[]
accno=[]
transfer=[]
ch='y'
while ch=='y':
    nm=input("Enter name : ")
    while True:
        acno=int(input("Enter accno : "))
        cnfrmacno=int(input("Confirm A/No: "))
        if acno == cnfrmacno:
            break                         
        print("Not matched,try again")
    tl=int(input("Enter t1:"))           
    
    names.append(nm)
    accno.append(acno)
    transfer.append(tl)
    ch=input("Do you want to continue :press y/n. ")
    if ch=='y':
        continue
    else:
        break
    
   
print("Names\tA/C no\tTransferlimit")
print('-'*40)
for i in range(len(names)):
      




names=[]
accno=[]
transfer=[]
ch='y'
while ch=='y':
    nm=input("Enter name : ")
    while True:
        acno=int(input("Enter accno : "))
        cnfrmacno=int(input("Confirm A/No: "))
        if(acno!=cnfrmacno):
             print("Not matched,try again")  
             continue
        break
    tl=int(input("Enter t1:"))             
    
    names.append(nm)
    accno.append(acno)
    transfer.append(tl)
    ch=input("Do you want to continue :press y/n. ")
    if ch=='y':
        continue
    else:
        break
    
   
print("Names\tA/C no\tTransferlimit")
print('-'*40)
for i in range(len(names)):
    print(names[i],'\t',accno[i],'\t',transfer[i])
    

#tuple
tpl = (11,22,33,44,55)
for i in tpl:
    print(i,end=" ")

tpl=(11,22,33,44,55)
for i in range(len(tpl)):
    print(tpl[i],end=' ')
    
tp1=(11,22,33,44,55)
indx=0
while indx<len(tpl):
    print(tpl[indx],end=" ")
    indx=indx+1
    
tpl=(11,22,33,44,55)
for i,j in enumerate(tpl):
    print(i,j)



s=([1,2,3,4],[11,22],'python')
print(s)
print(s[0])
print(s[1])

s=([1,2,3,4],[11,22],'python')
print(s[0][0])
print(s[0][1])
'''
#unpack a tuple
'''
k=(11,22,33,44)
print(k)
s=(1,2,k,3,4)
print(s)
s=(1,2,*k,3,4)
print(s)
    
    
    
#packing into a tuple
*f,s,t=(11,22,33,44,55)
print(f)
print(s)
print(t)
print(f,s,t)

'''
item_prices = (200.75, 49.5,120.00)

print("Item Prices:", item_prices)
print("Number of items:", len(item_prices))
print("Highest price", max(item_prices))
print("Lowest price", min(item_prices))
print("Total cost", sum(item_prices))
print("Any item above 200? (any):", any(price > 200 for price in item_prices))
print("All items above 10? (all):", all(price > 10 for price in item_prices))
print("Sorted prices:", sorted(item_prices))
print("Reversed prices", tuple(reversed(item_prices)))

additional_item_price = 75.25
item_prices += (additional_item_price,)
print("Prices after appending:", item_prices)

print("Count of price 49.99:", item_prices.count(49.99))
print("Index of price 120.00:", item_prices.index(120.00))

most_expensive, *middle_prices, least_expensive = sorted(item_prices, reverse=True)
print("Most expensive item::", most_expensive)
print("Middle prices:", middle_prices)
print("Least expensive:", least_expensive)

print("Item prices using for loop:")
for price in item_prices:
    print(price, end=" ")
print("Item prices using range:")
for i in range(len(item_prices)):
    print(item_prices[i],end=" ")

print()

print("Type of item_prices variable:", type(item_prices))

index_to_insert = 3
new_item_price = 99.99

T1 = (0, 1, 2, 3)
T2 = ('butter', 'milk')
T3 = (T1, T2)
print("\nTuple with nested tuples: ")
print(T3)
p = (0, 1, 2, 3,["rice","millets"])
p[4][0]="maggi"
print(p)

items = [200.75, 49.5, 120.00]

print("Items:", items)
print("Number of items:", len(items))
print("Highest price:", max(items))
print("Lowest price:", min(items))
print("Total cost:", sum(items))
print("Any item above 200?", any(price > 200 for price in items))
print("All items above 10?", all(price > 10 for price in items))

items.append(75.25) 
print("After appending:", items)

items.insert(2, 99.99)  
print("After inserting:", items)

items.remove(120.00)  
print("After removing 120.00:", items)

print("Sorted items:", sorted(items))
print("Reversed items:", list(reversed(items)))


items = [200.75, 49.5, 120.00]

def display_menu():
    print("\nMenu:")
    print("1. Display items")
    print("2. Display number of items")
    print("3. Display highest price")
    print("4. Display lowest price")
    print("5. Display total cost")
    print("6. Check if any item is above 200")
    print("7. Check if all items are above 10")
    print("8. Add a new price")
    print("9. Insert a price at a specific position")
    print("10. Remove an item by value")
    print("11. Sort items")
    print("12. Reverse items")
    print("13. Exit")

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        print("Items:", items)
    elif choice == '2':
        print("Number of items:", len(items))
    elif choice == '3':
        print("Highest price:", max(items))
    elif choice == '4':
        print("Lowest price:", min(items))
    elif choice == '5':
        print("Total cost:", sum(items))
    elif choice == '6':
        print("Any item above 200?", any(price > 200 for price in items))
    elif choice == '7':
        print("All items above 10?", all(price > 10 for price in items))
    elif choice == '8':
        price = float(input("Enter the price to add: "))
        items.append(price)
        print("After appending:", items)
    elif choice == '9':
        price = float(input("Enter the price to insert: "))
        position = int(input("Enter the position to insert at: "))
        items.insert(position, price)
        print("After inserting:", items)
    elif choice == '10':
        price = float(input("Enter the price to remove: "))
        if price in items:
            items.remove(price)
            print("After removing:", items)
        else:
            print(f"{price} not found in items.")
    elif choice == '11':
        print("Sorted items:", sorted(items))
    elif choice == '12':
        print("Reversed items:", list(reversed(items)))
    elif choice == '13':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
