def fun(n,arr,k):    
    totalwgts=sum(arr)
    res=[]
    for i in arr:
        impact= totalwgts-i
        res.append(min(impact,k))
    
        
        
    return res

n=int(input())
arr=list(map(int,input().split()))
k=int(input())
print(fun(n,arr,k))

