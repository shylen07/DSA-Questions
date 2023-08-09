class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def search_linked_list(head, value):
    current = head
    while current is not None:
        if current.data == value:
            return True
        current = current.next
    return False

# Example usage
if __name__ == "__main__":
    # Creating a linked list: 1 -> 3 -> 5 -> 7 -> None
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(5)
    head.next.next.next = Node(7)
    
    value_to_search = int(input("Enter a value to search: "))
    found = search_linked_list(head, value_to_search)
    
    if found:
        print(f"{value_to_search} exists in the linked list.")
    else:
        print(f"{value_to_search} does not exist in the linked list.")
