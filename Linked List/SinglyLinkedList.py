class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None


class SinglyLinkList:
    
    def __init__(self):
        self.head = None

    def traverse(self):

        temp = self.head
        while(temp != None):
            print(temp.data,end = ' ')
            temp = temp.next

    def insertion_at_first(self,data):

        first = Node(data)

        first.next = sll.head
        sll.head = first

    def insertion_at_last(self,data):

        last = Node(data)

        temp = sll.head

        while (temp.next != None):
            temp = temp.next

        temp.next = last

    def insertion_at_specified_position(self,position,data):

        specified = Node(data)
        temp = sll.head
        
        for i in range(1,position-1):
            temp = temp.next
        specified.next = temp.next
        temp.next = specified

    def deletion_at_first(self):
        temp = sll.head #n1 n2
        sll.head = temp.next
        temp.next = None

    def deletion_at_last(self):
        prev = sll.head # n4
        temp = sll.head.next #n5

        while temp.next != None:
            temp = temp.next
            prev = prev.next
        prev.next = None

    def deletion_at_specified_position(self,pos):
        prev = sll.head #n2
        temp = sll.head.next #n3

        for i in range(1,pos-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None
        
n1 = Node(1)
sll = SinglyLinkList()
sll.head = n1
n2 = Node(2)
n1.next = n2
n3 = Node(3)
n2.next = n3
n4 = Node(4)
n3.next = n4
n5 = Node(5)
n4.next = n5

sll.traverse()
print('\n')

# sll.insertion_at_first(200)
# sll.traverse()
# print('\n')

# sll.insertion_at_last(200)
# sll.traverse()

# sll.insertion_at_specified_position(2,100)
# sll.traverse()

# sll.deletion_at_first()
# sll.traverse()


# sll.deletion_at_last()
# sll.traverse()

# sll.deletion_at_specified_position(3)
# sll.traverse()
