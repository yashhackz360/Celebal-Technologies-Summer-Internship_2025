class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))
    
    def delete_node(self, n):
        if not self.head:
            raise IndexError("Cannot delete from empty list")
        if n < 1:
            raise IndexError("Position must be positive integer")
        
        if n == 1:
            self.head = self.head.next
            return
        
        current = self.head
        for _ in range(n-2):
            current = current.next
            if not current:
                raise IndexError("Position out of range")
        
        if not current.next:
            raise IndexError("Position out of range")
        
        current.next = current.next.next

# Test implementation
ll = LinkedList()
for i in [1, 2, 3, 4]:
    ll.add_node(i)

print("Original list:")
ll.print_list()

ll.delete_node(2)
print("\nAfter deleting 2nd node:")
ll.print_list()

ll.delete_node(3)
print("\nAfter deleting new 3rd node:")
ll.print_list()

try:
    ll.delete_node(5)
except Exception as e:
    print(f"\nError: {e}")
