from Tree import BinaryNode as Node
from Tree import Tree

def DFS (root):
    if DFS_helper(root) == -1:
        return False
    else:
        return True

def DFS_helper(root):
    if root is None:
        return 0

    if (root.left and root.left.data == -1) or (root.right and root.right.data == -1):
        return -1

    left = 1 + DFS_helper(root.left)
    right = 1 + DFS_helper(root.right)

    if abs(left-right) > 1:
        return -1
    else:
        root.data = max(left, right)
        return root.data


n1 = Node(1)
n2 = Node(1)
n3 = Node(1)
n4 = Node(1)
n5 = Node(1)
n6 = Node(1)
n7 = Node(1)
n8 = Node(1)

my_tree_true = Tree(n1)
print DFS(my_tree_true.root)
n1.left = n2
print DFS(my_tree_true.root)
n1.right = n3
n2.left = n4
n2.right = n5

print DFS(my_tree_true.root)

n4.right = n8

print DFS(my_tree_true.root)

n3.left = n6
# n3.right = n7

print DFS(my_tree_true.root)