#binary search on a descending order array
def binarysearch(a,element):
    start=0
    end=len(a)-1
    while start<=end:
        mid=start + (end-start)//2
        if a[mid]==element:
            return mid
        elif element<a[mid]:
            start=mid+1
        elif element>a[mid]:
            end=mid-1
    return -1
            
a=[20,17,15,14,13,12,10,9,8,4]
element=4
result = binarysearch(a, element)
if result != -1:
    print("Found at index", result)
else:
    print("Not found")