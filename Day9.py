''' #method overriding
class ornaments:
    def price(self):
        print("price of ornaments")
class gold(ornaments):
    def price(self):
        print("1 lakh")
class silver(ornaments):
    def price(self):
        print("50,000")

class copper(ornaments):
    def price(self):
        print("20000")
def displayprice(ornaments):
    return ornaments.price()

g=gold()
s=silver()
c=copper()

o=ornaments()
g.price()
s.price()
c.price()
o.price()



class Addition:
    def __init__(self,number):
        self.nmbr=number
    def __add__(self,other):
        return self.nmbr+other.nmbr
n1=Addition(22)
n2=Addition(33)
print(n1+n2)
'''

n=int(input())
for i in range(1,n):
    if (i**2) < n:
        print(i**2,end =" ")

else:
    print(-1)
    

    

    