class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def has_cycle(head):
    if not head or not head.next:
        return False  # No cycle if the list is empty or has only one node

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next  # Move one step
        fast = fast.next.next  # Move two steps

        if slow == fast:
            return True  # Cycle detected

    return False  # No cycle found

# Example usage:
# Create a linked list with a cycle
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2  # Creating a cycle

print(has_cycle(head))  # Output: True
