def count_frequency_elements(arr):
    mp={} #dictionary
    n=len(arr)
    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]]+=1
        else:
            mp[arr[i]]=1
 
    for x in mp:
        print(x,mp[x])
    



arr=[10,5,10,15,10,5]
count_frequency_elements(arr)

#Rearrange the array such that the first half is arranged in increasing order, and the second half is arranged in decreasing order


arr=[8,7,1,6,5,9]
n=len(arr)
arr.sort()
print(arr)
for i in range(0,n//2):
    print(arr[i] ,end=" ")
for i in range(n-1,n//2-1,-1):
    print(arr[i] ,end=" ")
    
    
    
#Sum of the Elements of the Array
arr=[1,2,3,4,5]
n=len(arr)
sum=0
for i in range(0,n):
    sum+=arr[i]
    
print(sum)
    
   
