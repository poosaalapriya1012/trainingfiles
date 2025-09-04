#Find all Symmetric Pairs in the array of pairs
arr = [(1, 2), (2, 1), (3, 4), (4, 5), (5, 4)]
mp={}
print("The symmetric pairs are: ");
for first,second in arr:
    if second in mp and first == mp[second]:
        print(first,second)
    else:
        mp[first]=second