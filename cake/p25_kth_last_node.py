class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

def kth_to_last_node(k, head):

    if k < 1:
        raise ValueError('Impossible to find less than first to last node: %s' % k)

    left_node  = head
    right_node = head

    # move right_node to the kth node
    for _ in xrange(k - 1):

        # but along the way, if a right_node doesn't have a next,
        # then k is greater than the length of the list and there
        # can't be a kth-to-last node! we'll raise an error
        if not right_node.next:
            raise ValueError('k is larger than the length of the linked list: %s' % k)

        right_node = right_node.next

    # starting with left_node on the head,
    # move left_node and right_node down the list,
    # maintaining a distance of k between them,
    # until right_node hits the end of the list
    while right_node.next:
        left_node  = left_node.next
        right_node = right_node.next

    # since left_node is k nodes behind right_node,
    # left_node is now the kth to last node!
    return left_node

print kth_to_last_node(1, a).value



# def kth_to_last_node(k, head):
#     front = head
#     for i in range(k):
#         if front is None:
#             raise ValueError("k cannot be larger than length of linked list")
#         front = front.next
#
#     back = head
#     while front is not None:
#         back = back.next
#         front = front.next
#     return back
#
#
# print kth_to_last_node(3, a).value
