j={}
s={}
jewels="ab"
stones="aabbgfg"
count=0
for i in range(0,len(jewels)):
    if jewels[i] not in j:
        j[jewels[i]]=1
    else:
        j[jewels[i]]=j[jewels[i]]+1
print(j)
for i in range(0,len(stones)):
    if stones[i] not in s:
        s[stones[i]]=1
    else:
        s[stones[i]]=s[stones[i]]+1
print(s)
for i in s:
    if i in j :
        count=count+s[i]
        
print(count)