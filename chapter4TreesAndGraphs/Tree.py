class Tree():
    def __init__(self, root):
        self.root = root

class BinaryNode():
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        self.visited = False

class BinaryNodeParent():
    def __init__(self, data, left = None, right = None, parent = None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.visited = False

class Node():
    def __init__(self, data, children):
        self.data = data
        self.children = children
        self.visited = False

def visit(node):
    print node.data
    node.visited = True

def inOrderTraversal(node):
    if node is not None:
        inOrderTraversal(node.left)
        visit(node)
        inOrderTraversal(node.right)

def preOrderTraversal(node):
    if node is not None:
        visit(node)
        preOrderTraversal(node.left)
        preOrderTraversal(node.right)

def postOrderTraversal(node):
    if node is not None:
        postOrderTraversal(node)
        postOrderTraversal(node)

def dfs(root):
    if root is None:
        return None
    visit(root)
    for node in root.children:
        if not node.visited:
            dfs(node)

def bfs(root):
    if root is None:
        return None
    visit(root)
    queue = [root]
    while queue is not None:
        node = queue.pop(0)
        for child in node.children:
            if not child.visited:
                visit(node)
                queue.append(child)
