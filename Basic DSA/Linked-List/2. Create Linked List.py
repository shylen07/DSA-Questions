class Node:
    def __init__(self,data):
        self.data =data
        self.next =None
def create_linked_list():
    head = None
    n= int(input("Number Of Nodes : "))
    for _ in range(n):
        data =int(input("Node Value :"))
        node = Node(data)
        if head is None:
            head = node
        else:
            current =head
            while current.next :
                current = current.next
            current.next = node
    return head
def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

if __name__ == "__main__":
    head = create_linked_list()
    
    print("Linked List:")
    print_linked_list(head)