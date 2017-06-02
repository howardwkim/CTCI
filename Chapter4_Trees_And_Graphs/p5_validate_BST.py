from Tree import Tree
from Tree import BinaryNode as Node

# def validate_BST(root):
#     prev = None
#     return validate_BST_helper(root, prev)
#
# def validate_BST_helper(root, prev):
#     if root is not None:
#         if prev is None:
#             prev = root.data
#         return validate_BST_helper(root.left, prev) and \
#                visited(root, prev) and \
#                validate_BST_helper(root.right, prev)
#
# def visited(root, prev):
#     if prev > root.data:
#         return False
#     else: #prev <= root.data
#         return True

def validate_BST(root):
    prev = None
    return validate_BST_helper(root, prev)

def validate_BST_helper(root, prev):
    if root is None:
        return True

    if not validate_BST_helper(root.left, prev):
        return False

    if prev is not None and root.data <= prev:
        return False

    prev = root.data

    if not validate_BST_helper(root.right, prev):
        return False

    return True

def validate_BST2(root):
    return validate_BST2_helper(root, min=None, max=None)

def validate_BST2_helper(root, min, max):
    return



n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)

n5.left = n3
n5.right = n7
n3.left = n2
n3.right = n4
n7.left = n6
n7.right = n8

my_tree = Tree(n5)

print validate_BST(my_tree.root)