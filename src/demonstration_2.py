"""
Given a reference to the head node of a singly-linked list, write a function
that reverses the linked list in place. The function should return the new head
of the reversed list.

In order to do this in O(1) space (in-place), you cannot make a new list, you
need to use the existing nodes.

In order to do this in O(n) time, you should only have to traverse the list
once.

*Note: If you get stuck, try drawing a picture of a small linked list and
running your function by hand. Does it actually work? Also, don't forget to
consider edge cases (like a list with only 1 or 0 elements).*
"""
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

def print_list(linked_list):
    prevNode = None
    currNode = linked_list
    nextNode = currNode.next

    if currNode is not None:
        print(currNode.value)

        if nextNode is not None:
            print_list(nextNode)

    return

def reverse(head_of_list):
    # Your code here
    prevNode = None
    currNode = head_of_list
    nextNode = currNode.next

    while currNode is not None:
        # Update next node
        nextNode = currNode.next

        # Swap pointers
        currNode.next = prevNode

        # Update to move on
        prevNode =  currNode
        currNode = nextNode

# Setting up a LL
x = LinkedListNode('1')
y = LinkedListNode('2')
z = LinkedListNode('3')
a = LinkedListNode('4')


x.next = y
y.next = z
z.next = a

reverse(x)

print_list(a)