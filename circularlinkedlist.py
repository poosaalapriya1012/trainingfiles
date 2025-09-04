class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def insert(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            newnode.next = self.head  
            return
        temp = self.head
        while temp.next != self.head:  
            temp = temp.next
        temp.next = newnode
        newnode.next = self.head  

    # Insert at the beginning
    def insertion_at_beg(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            newnode.next = self.head  
        else:
            temp = self.head
            while temp.next != self.head:  
                temp = temp.next
            temp.next = newnode
            newnode.next = self.head
            self.head = newnode

    # Delete at the beginning
    def delete_at_beg(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        if self.head.next == self.head: 
            self.head = None
            return
        temp = self.head
        while temp.next != self.head: 
            temp = temp.next
        temp.next = self.head.next  
        self.head = self.head.next
    def delete_at_end(self):
        

    # Display the list
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(Back to head)")

# Example usage
cll = CircularLinkedList()
cll.insert(10)
cll.insert(20)
cll.insert(30)
cll.insert(40)

print("Circular Linked List after inserting at end:")
cll.display()

cll.insertion_at_beg(5)
print("Circular Linked List after inserting 5 at the beginning:")
cll.display()

cll.delete_at_beg()
print("Circular Linked List after deleting the first node:")
cll.display()
