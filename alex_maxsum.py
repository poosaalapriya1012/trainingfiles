def fun(arr, n, l): 
    arr.sort()  
    sum1 = 0
    count = 0
    for i in range(l):
        if sum1+arr[i] <=n:
            sum1 += arr[i]
            count += 1
        else:
            break
    return count
arr=list(map(int,input().split()))
n=int(input())
l=int(input())
print(fun(arr,n,l))

