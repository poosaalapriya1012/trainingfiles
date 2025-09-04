#using classname
'''
class Emp:
    eid=1122
print(Emp.eid)


class Emp:
    eid=1122
obj=Emp()
print(obj)


class Emp:
    eid=1122
obj=Emp()
print(obj.eid)

class Emp:
    def st_dtls(self,nm,id):
        self.name=nm
        self.eid=id
    def dsply(self):
        print(self.name,self.eid)
e1=Emp()
e1.st_dtls("k v",1122)
e1.dsply()

class Emp:
    name=None
    id=None
    def st_dtls(self,nm,id):
        self.name=nm
        self.eid=id
    def dsply(self):
        print(self.name,self.eid)
e1=Emp()
e1.st_dtls("k v",1122)
e1.dsply()


class Emp:
    def __init__(self,nm,id):
        self.name=nm
        self.eid=id
    def dsply(self):
        print(self.name,self.eid)
e1=Emp("k v",1122)
e1.dsply()
e1.__init__("priya",512)
e1.dsply()

class Emp:
    k=11
    k=20
    def __init__(self,nm,id):
        self.name=nm
        self.eid=id
    def dsply(self):
        print(self.name,self.eid)
e1=Emp("k v",1122)
e1.dsply()
print(e1.k)
e1.k=10
print(e1.k)
e2=Emp("pri",512)
print(e2.k)


class circle:
    PI=3.14159
    def __init__(self,r):
        self.radius=r
        
    def dsply(self):
        print(self.radius,self.PI*(self.radius)**2)
c=circle(5)
c.dsply()

class Emp:
    def __init__(self):
        print("obj created")
    def __del__(self):
        print("destructor called")
e1=Emp()
del e1
#print(e1) error beacuse obj deleted


class Emp:
    def __init__(self,name,id_no):
        self.n=name
        self.ind=id_no
    def display(self):
        print(self.n,self.ind)
    def __len__(self):
        return len(self.n)
    
e1=Emp("k v",1122)
e1.display()
print("length" ,e1.n, "is",len(e1) )

#length of list
class class1:
    def __init__(self,list1):
        self.l=list1
    def __len__(self):
        return len(self.l)

c=class1([1,2,3,4,5])
print("length of list1:",len(c))




#convert instance to string
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
p=Point(15,25)

print(p)


class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def display(self):
        return self.x,self.y
p=Point(15,25)
q=Point(10000,9999)
print("coordinating poinsts",p.display())
print("coordinating poinsts",q.display())


#add method reflect_x to point which return a new Point which is reflection of point about
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def reflect_x(self):
        return Point(self.x,-(self.y))
    def __str__(self):
        return f"Point({self.x},{self.y})"
op=Point(3,5)
rp=op.reflect_x()
print(f"original point {op}")
print(f"reflected point {rp}")

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"({self.x},{self.y})"
    def midpoint(p1,p2):
        mx=(p1.x+p2.x)/2
        my=(p1.y+p2.y)/2
        return Point(mx,my)
    
p=Point(-2,1)  
q=Point(5,4)

r=p.midpoint(q)
print(str(r))

class Emp:
    def __init__(self):
        self.public1= "public"
        
        self.__private1= "private"
    def display(self):
        print(self.public1,self.__private1)
e1=Emp()
e1.display()
print(e1.public1)
print(e1.__private1)#error


class A:
    def method1(self):
        print("parent")
class Dog(A):
    def method2(self):
        print("child class called")

d = Dog()
d.method1()
d.method2()


#multi


class college():
    def __init__(self,name,age):
        self.nm=name
        self.age=age
    def display(self):
        print(self.nm,self.age)

class Student(college):
    pass

s1=Student("priya",12)
s1.display()

class Animal:
    def __init__(self):
        print("main Animal  constructor")
class Dog(Animal):
    def __init__(self):
        print("Dog  constructor")
    def makesound(self):
        print("barks......")
class puppy(Dog):
    def __init__(self):
        print("puppy constructor")
    def walk(self):
        print("am chld class of dog")
p=puppy()
p.makesound()
p.walk()


'''
#multiple
class Animal:
    def makesound(self):
        print("main Animal  constructor")
class Dog:
    def  bark(self):
        print("barks......")
class puppy(Dog,Animal):
    def walk(self):
        print("am chld class of dog")
p=puppy()
p.makesound()
p.walk()
p.bark()

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self,other):
        return Point(self.x+other.x,self.y+other.y)


p=Point(2,3)
q=Point(5,3)
p3=p.add(q)
print(p3.x,p3.y)



class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

for num in MyRange(1, 5):
    print(num, end=" ")



