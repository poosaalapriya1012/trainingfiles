#Remove Duplicates From a sorted Array
a=[1,1,2,2,2,3,3,3]
i=0
for j in range(1,len(a)):
    if a[i] !=a[j]:
        a[i+1]=a[j]
        i=i+1


print(a[:i+1])
    
