def isSubTree(t1, t2):
    if t2 is None: #1
        return True
    return DFS(t1, t2)

def DFS(t1Node, t2root):
    if t1Node is None: #1
        return False
    elif t1Node.data == t2root.data and DFSMatch(t1Node, t2root): #2
        return True
    # elif t1Node.data == t2root.data:
    #     return DFSMatch(t1Node, t2root)
    return DFSMatch(t1Node.left, t2root) or DFSMatch(t1Node.right, t2root)

def DFSMatch(t1Node, t2Node):
    if t1Node is None and t2Node is None: #3
        return True
    elif t1Node is None or t2Node is None: #4
        return False
    elif t1Node.data != t2Node.data:
        return False

    return DFSMatch(t1Node.left, t2Node.left) and DFSMatch(t1Node.right, t2Node.right)

'''
1: Do not forget to consider edge case that should automatically return True or False
2: My old code is equivalent, but less pretty.
3: Consider base case carefully.
4: Think carefully about 'order of operations' in nodes/None nodes. None nodes must be
   checked prior to data within node.
'''