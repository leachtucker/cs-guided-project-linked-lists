"""
Given only a reference to a specific node in a linked list, delete that node from a singly-linked list.

Example:

The code below should first construct a linked list (x -> y -> z) and then delete `y` from the linked list by calling the function `delete_node`. It is your job to write the `delete_node` function.

```python
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z

delete_node(y)
```

*Note: We can do this in O(1) time and space! But be aware that our solution will have some side effects...*
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

def delete_node(delete_this_node):
    # check that we were not given the last node
    if (delete_this_node.next == None):
        print("Cannot delete last node")
        return

    # Replace this node's value with the next node's value
    delete_this_node.value = delete_this_node.next.value
    delete_this_node.next = delete_this_node.next.next

    return delete_this_node


x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z

# print_list(x)

delete_node(y)

print_list(x)

