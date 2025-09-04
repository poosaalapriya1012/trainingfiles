'''def nm():
    print("Name: ----")
def rno():
    print("Roll No:----")

print(__name__)
nm()
rno()

def nm():
    print("Name: ----")
def rno():
    print("Roll No:----")
def main():
    nm()
    rno()
    
if __name__ == "__main__":
    main()

def nm():
    print("name: Raju")
def id():
    print("id no: 1122")
    
   
n=int(input("enter a numerator"))
d=int(input("enter a denomerator"))
try:
    q=n/d
    print(q)
except ZeroDivisionError:
    print("denominator cannot be zero")
    

try:
    n=int(input("enter a numerator"))
    d=int(input("enter a denomerator"))
    q=n/d
    print(q)
except ZeroDivisionError:
    print("denominator cannot be zero")
except ValueError:
    print("Invalid data type")
   
    

try:
    n=int(input("enter a numerator"))
    d=int(input("enter a denomerator"))
    q=n/d
    print(q)
except ZeroDivisionError:
    print("denominator cannot be zero")
else:
    print("Invalid ")
    
    '''
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
