def successor(node):
    if node.right:
        return leftmost_node(node.right)
    else:
        if node.parent.left == node:
            return node.parent
        node = node.parent
        while node:
            if node.parent.left == node:
                return node.parent
            node = node.parent
    return None

def leftmost_node(node):
    if node.left == None:
        return node
    while node.left:
        node = node.left
    return node

class Node():
    def __init__(self, data, left = None, right = None, parent = None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.visited = False


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)
n10 = Node(10)
n11 = Node(11)
n12 = Node(12)

n1.parent = n2
n2.left = n1
n2.right = n5
n2.parent = n7
n3.parent = n4
n4.left = n3
n4.parent = n5
n5.left = n4
n5.right = n6
n5.parent = n2
n6.parent = n5
n7.left = n2
n7.right = n8
n8.parent = n7
n8.right = n11
n11.parent = n8
n11.left = n10
n11.right = n12
n12.parent = n11
n10.parent = n11
n10.left = n9
n9.parent = n10

print successor(n1).data
print successor(n2).data
print successor(n3).data
print successor(n4).data
print successor(n5).data
print successor(n6).data
print successor(n7).data
print successor(n8).data
print successor(n9).data
print successor(n10).data
print successor(n11).data
