class Node:
    def __init__(self,data):
        self.data =data
        self.next=None

def create_linked_list():
    head = None
    n =int(input("Number of Elements In Linked list : "))
    for _ in range(n):
        data = int(input("Enter Node Value : "))
        node = Node(data)

        if head is None:
            head = node
        else:
            current = head
            while current.next:
                current = current.next
            current.next = node
    return head

def sum_linked_list(head):
    sm = 0
    current = head
    while current is not None:
        sm+=current.data
        current = current.next
    return sm

if __name__ == "__main__":
    head = create_linked_list()

    ans = sum_linked_list(head)
    print(ans)
    
