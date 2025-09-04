class Node:
    def _init_(self, coef, exp):
        self.coef = coef
        self.exp = exp
        self.next = None
class Polynomial:
    def _init_(self):
        self.head = None
    def insert_term(self, coef, exp):
        new_node = Node(coef, exp)
        if self.head is None or self.head.exp < exp:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            while temp.next and temp.next.exp >= exp:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

    def display(self):
        if self.head is None:
            print("0")
            return 
        temp = self.head
        while temp:
            if temp.coef > 0 and temp != self.head:
                print("+", end=" ")
            print(f"{temp.coef}x^{temp.exp}", end=" ")
            temp = temp.next
        print()
poly = Polynomial()
poly.insert_term(3, 2)
poly.insert_term(5, 3)
poly.insert_term(2, 1)
poly.insert_term(4, 4)
poly.display()