## Two-pointer technique to find intersection
arr1=[1, 2, 3, 4]
arr2=[2, 4, 6, 7, 8]
i=0
j=0
result=[]
while i<len(arr1) and j<len(arr2):
    if arr1[i] == arr2[j]:
        if not result or result[-1]!=arr1[i]:
            result.append(arr1[i])
        i=i+1
        j=j+1
    elif arr1[i] < arr2[j]:
        i=i+1
    else:
        j=j+1
            
print(result)