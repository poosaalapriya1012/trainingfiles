def ispalindrome(num):
    num=str(num)
    return num[:] == num[::-1]
def palindromearr(arr):
    for i in arr:
        if not ispalindrome(i):
            return False
    return True
        
arr=[11,22,33,556]
print(palindromearr(arr))
