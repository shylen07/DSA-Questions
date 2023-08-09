class Node:
    def __init__(self,data):
        self.data= data
        self.next = None

def count_nodes(head):
    count=0
    current = head
    while current is not None:
        count+=1
        current = current.next
    return count

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(5)
    head.next.next.next = Node(7)
    
    num_nodes = count_nodes(head)
    print("Number of nodes:", num_nodes)