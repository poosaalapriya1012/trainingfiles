def fun(l,budget,packets,cost): 
    maxi=0
    
    for i in range(l):
        for j in range(i+1,l):
            totalcost=b[i]+b[j]
            totalball=a[i]+a[j]
            if totalcost<=budget:
                maxi=max(maxi,totalball)
        
    return maxi

l=int(input())
budget=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(fun(l,budget,a,b))

