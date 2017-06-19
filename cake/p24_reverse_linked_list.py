def reverse(head_of_list):
    current = head_of_list
    previous = None
    next = None

    # until we have 'fallen off' the end of the list
    while current:
        # copy a pointer to the next element
        # before we overwrite current.next
        next = current.next

        # reverse the 'next' pointer
        current.next = previous

        # step forward in the list
        previous = current
        current = next

    return previous


def reverse_linked_list(head):
    if head is None:
        raise Exception("Cannot reverse empty list")
    if head.next is None:
        return head

    current = head.next
    current_next = current.next
    head.next = None

    while current_next is not None:
        current.next = head
        head = current
        current = current_next
        current_next = current_next.next

    current.next = head
    return current

class Node:
    def __init__(self, value, nxt = None):
        self.value = value
        self.next = nxt

def printer(node):
    while node is not None:
        print node.value
        node = node.next

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
print reverse_linked_list(n1).value

n1.next = n2
printer(reverse_linked_list(n1))
n1.next = n2
n2.next = n3
n3.next = n4
print
printer(n1)
n1.next = n2
n2.next = n3
n3.next = n4
printer(reverse_linked_list(n1))