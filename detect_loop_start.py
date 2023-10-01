class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detect_loop_start(head):
    # Step 1: Use the "tortoise and hare" approach to find the intersection point
    slow = head
    fast = head

    # Traverse the list to find the intersection point
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break  # Intersection point found

    # Step 2: Find the start of the loop
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # The node where the two pointers meet is the start of the loop
    return slow

# Example usage:
# Create a linked list with a loop
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2  # Creating a loop

start_of_loop = detect_loop_start(head)
print(start_of_loop.data)  # Output: 2
