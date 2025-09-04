class Queue:
    def __init__(self,size):
        self.l=[None]*size
        self.front=-1
        self.rear=-1
        self.size=size
    def enqueue(self,value):
        if self.rear==self.size-1:
            print("queue is full")
            return
        if self.front==-1:
            self.front=0
            
        self.rear+=1
        self.l[self.rear]=value
        
    def dequeue(self):
        if self.front==-1:
            print("empty")
            return
        #if queue has one element
        if self.front==self.rear:
            item=self.l[self.front]
            self.l[self.front]=None
            self.front=-1
            self.rear=-1
            return item
        self.l[self.front]=None
        self.front+=1
    def display(self):
        if self.front==-1:
            print("empty")
            return
        print(*self.l)
    def isEmpty(self):
        return self.front==-1
    def isFull(self):
        return self.rear==self.size-1
    def getRear(self):
        return self.l[self.rear]
    def getFront(self):
        return self.l[self.front]
    
q=Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.display()
q.dequeue()
q.display()
print(q.getFront())
print(q.getRear())
            
