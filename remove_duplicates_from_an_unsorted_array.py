#Remove Duplicates From an Unsorted Array
'''def remove_duplicates(arr):
    s=set()
    res=[]
    for i in arr:
        if i not in s:
            s.add(i)
            res.append(i)
    return res


arr = [1, 2, 3, 2, 4, 5, 1]
result = remove_duplicates(arr)
print(result)
'''
a = [1, 2, 3, 4, 5]
ans=1
i=0
while(i<len(a)-1):
    if a[i] > a[i+1]:
        ans=0
        break
    i=i+1
    

'''
    
for i in range(0,len(a)-1):
    if a[i] <=a[i+1]:
            ans=1
            
    else:
            ans=0 '''
print(ans)

x = 7
y = 4
z = 10
print(not (x > 5) and y <= z or x != 7)

