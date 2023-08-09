class Node:
    def __init__(self, data):
        self.data =data
        self.next =None

def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next

if __name__=="__main__":
    head = Node(1)
    head.next = Node(3)
    head.next.next= Node(5)
    head.next.next.next = Node(7)

    print("Linked List :")
    print(print_linked_list(head))     