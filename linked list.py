class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)


temp = head
if temp is None:
    print('empty')
else:
    while temp:
        print(temp.data)
        temp = temp.next 
