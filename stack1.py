class  Stack:
    def __init__(self):
        self.stack=[]
    def isEmpty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
    def push(self,item):
        return self.stack.append(item)
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        else:
            temp=self.stack.pop()
            return temp
    def peek(self):
        return self.stack[-1]
    def display(self):
        if self.isEmpty():
            print("stack is empty")
            return
        else:
            return self.stack
ob=Stack()
ob.display()
ob.push(11)
ob.push(22)
ob.push(33)
print("stack is ",ob.display())
print("peek : " ,ob.peek())
print(ob.pop())
ob.display()
