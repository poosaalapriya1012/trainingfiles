class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 

    def insertatbegin(self, data):
        newnode = Node(data) 
        newnode.next = self.head 
        self.head = newnode
        
    def insertatend(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newnode
    def deletebefore_specific_value:
        temp=self.head
        prev=None
        

    def insert_after(self, value, data):
        newnode = Node(data)
        temp = self.head
        while temp is not None and temp.data != value:
            temp = temp.next
        if temp is None:
            print("Value not found")
            return
        newnode.next = temp.next
        temp.next = newnode

    def insert_at_specific(self, position, data):
        newnode = Node(data)
        if position < 1:
            print("Invalid position")
            return
        if position == 1:
            newnode.next = self.head
            self.head = newnode
            return
        temp = self.head
        for _ in range(position - 2):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next
        if temp is None:
            print("Position out of range")
            return
        newnode.next = temp.next
        temp.next = newnode

    def insert_before_specif(self, data1, val):
        newnode = Node(data1)
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == val:
            newnode.next = self.head
            self.head = newnode
            return
        temp = self.head
        while temp.next is not None and temp.next.data != val:
            temp = temp.next
        if temp.next is None:
            print("Value not found")
            return
        newnode.next = temp.next
        temp.next = newnode
        
    def traversal(self):
        if self.head is None:
            print("empty")
            return
        temp = self.head 
        while temp is not None:
            print(temp.data, end=' --> ')
            temp = temp.next
        print("NULL")


ll = LinkedList()
x = int(input("Enter numbers (-1 to stop): "))
while x != -1:
    ll.insertatend(x)
    x = int(input())

ll.traversal()
