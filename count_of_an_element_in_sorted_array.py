
def count_of_element_binarysearch(a,k):
    count=0
    low=0
    high=len(a)-1
    first=-1
    last=-1
    while(low<=high):
        mid=low+(high-low)//2
        if(a[mid] == k ):
            first=mid
            high=mid-1
        elif a[mid] < k:
            low=mid+1
        else :
            high=mid-1
    low=0
    high=len(a)-1
    while(low<=high):
        mid=low+(high-low)//2
        if(a[mid] == k ):
            last=mid
            low=mid+1
        elif a[mid] < k:
            low=mid+1
        else :
            high=mid-1
    count=last-first+1
    if first==-1 or last==-1:
        return 0
    else:
        return count
    
    
        
a=[2,4,10,10,10,10]
k=10
print(count_of_element_binarysearch(a,k))
            

